const STORAGE_KEY = "finy-browser-data-v1";
const EXPENSE_CATEGORIES = [
  "Food",
  "Transportation",
  "Communication",
  "Housing",
  "Personal Care",
  "Health and Wellness",
  "Education",
  "Entertainment",
  "Debt payments",
  "Pets",
  "Others",
];
const INCOME_CATEGORIES = [
  "Earned income",
  "Investment income",
  "Passive income",
  "Others",
];

let state = loadState();
let toastTimer;

function loadState() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    if (
      saved &&
      Array.isArray(saved.accounts) &&
      Array.isArray(saved.transactions)
    )
      return saved;
  } catch (error) {
    console.warn("Finy could not read saved browser data.", error);
  }
  return { accounts: [], transactions: [] };
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (error) {
    showToast("This browser could not save your changes.");
    console.error("Finy could not save browser data.", error);
  }
}

function makeId() {
  return (
    globalThis.crypto?.randomUUID?.() ??
    `${Date.now()}-${Math.random().toString(16).slice(2)}`
  );
}

function escapeHtml(value) {
  return String(value ?? "").replace(
    /[&<>"']/g,
    (character) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
      })[character],
  );
}

function localDateString(date = new Date()) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function formatMoney(amount, currency = "NGN") {
  try {
    return new Intl.NumberFormat("en", {
      style: "currency",
      currency,
      maximumFractionDigits: 2,
    }).format(amount);
  } catch {
    return `${currency} ${Number(amount).toLocaleString("en", { maximumFractionDigits: 2 })}`;
  }
}

function formatGroupedMoney(groups) {
  const entries = [...groups.entries()].filter(([, amount]) => amount !== 0);
  if (!entries.length)
    return formatMoney(0, state.accounts[0]?.currency || "NGN");
  return entries
    .map(([currency, amount]) => formatMoney(amount, currency))
    .join(" · ");
}

function getAccount(accountId) {
  return state.accounts.find((account) => account.id === accountId);
}

function accountBalance(account) {
  return (
    Number(account.startingBalance || 0) +
    state.transactions.reduce((balance, transaction) => {
      if (transaction.accountId !== account.id) return balance;
      return (
        balance +
        (transaction.type === "income" ? 1 : -1) *
          Number(transaction.amount || 0)
      );
    }, 0)
  );
}

function monthKey(date) {
  return String(date || "").slice(0, 7);
}

function groupedBalances() {
  const groups = new Map();
  state.accounts.forEach((account) => {
    groups.set(
      account.currency,
      (groups.get(account.currency) || 0) + accountBalance(account),
    );
  });
  return groups;
}

function groupedTransactions(transactions) {
  const groups = new Map();
  transactions.forEach((transaction) => {
    const currency = getAccount(transaction.accountId)?.currency || "NGN";
    groups.set(
      currency,
      (groups.get(currency) || 0) + Number(transaction.amount || 0),
    );
  });
  return groups;
}

function monthTransactions(type) {
  const currentMonth = localDateString().slice(0, 7);
  return state.transactions.filter(
    (transaction) =>
      transaction.type === type && monthKey(transaction.date) === currentMonth,
  );
}

function sortedTransactions(transactions = state.transactions) {
  return [...transactions].sort((left, right) =>
    `${right.date}${right.id}`.localeCompare(`${left.date}${left.id}`),
  );
}

function formatDate(date) {
  if (!date) return "—";
  const parsed = new Date(`${date}T00:00:00`);
  return Number.isNaN(parsed.getTime())
    ? date
    : new Intl.DateTimeFormat("en", {
        month: "short",
        day: "numeric",
        year: "numeric",
      }).format(parsed);
}

function renderSummary() {
  document.querySelector("#total-balance").textContent =
    formatGroupedMoney(groupedBalances());
  document.querySelector("#month-income").textContent = formatGroupedMoney(
    groupedTransactions(monthTransactions("income")),
  );
  document.querySelector("#month-expenses").textContent = formatGroupedMoney(
    groupedTransactions(monthTransactions("expense")),
  );
  document.querySelector("#account-count").textContent = state.accounts.length;
}

function transactionRow(transaction) {
  const account = getAccount(transaction.accountId);
  const isIncome = transaction.type === "income";
  const category = escapeHtml(
    transaction.category || (isIncome ? "Income" : "Expense"),
  );
  const note = transaction.note
    ? `<div class="transaction-note">${escapeHtml(transaction.note)}</div>`
    : "";
  const amount = formatMoney(
    Number(transaction.amount),
    account?.currency || "NGN",
  );
  return `<tr>
    <td><div class="transaction-cell"><span class="transaction-symbol ${isIncome ? "" : "expense-symbol"}" aria-hidden="true">${isIncome ? "+" : "−"}</span><div><div class="transaction-name">${category}</div>${note}</div></div></td>
    <td>${escapeHtml(account?.name || "Account removed")}</td>
    <td>${escapeHtml(formatDate(transaction.date))}</td>
    <td class="amount ${isIncome ? "" : "expense-amount"}">${isIncome ? "+" : "−"}${escapeHtml(amount)}</td>
    <td><button class="delete-button" type="button" data-delete-transaction="${escapeHtml(transaction.id)}" aria-label="Delete ${category} transaction" title="Delete transaction">×</button></td>
  </tr>`;
}

function renderTransactionTable(element, transactions) {
  const body = document.querySelector(element);
  if (!transactions.length) {
    body.innerHTML =
      '<tr class="empty-row"><td colspan="5">No activity yet. Add a transaction to get started.</td></tr>';
    return;
  }
  body.innerHTML = transactions.map(transactionRow).join("");
}

function renderChart() {
  const chart = document.querySelector("#cashflow-chart");
  const months = [];
  const now = new Date();
  for (let offset = 5; offset >= 0; offset -= 1) {
    const date = new Date(now.getFullYear(), now.getMonth() - offset, 1);
    months.push({
      key: `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}`,
      label: new Intl.DateTimeFormat("en", { month: "short" }).format(date),
    });
  }

  const totals = months.map((month) => {
    const items = state.transactions.filter(
      (transaction) => monthKey(transaction.date) === month.key,
    );
    return {
      ...month,
      income: items
        .filter((item) => item.type === "income")
        .reduce((sum, item) => sum + Number(item.amount), 0),
      expense: items
        .filter((item) => item.type === "expense")
        .reduce((sum, item) => sum + Number(item.amount), 0),
    };
  });
  const highest = Math.max(
    1,
    ...totals.flatMap((month) => [month.income, month.expense]),
  );
  const hasActivity = totals.some((month) => month.income || month.expense);
  if (!hasActivity) {
    chart.innerHTML =
      '<p class="chart-empty">Your monthly picture will take shape here.</p>';
    return;
  }
  chart.innerHTML = totals
    .map(
      (
        month,
      ) => `<div class="chart-month" title="${escapeHtml(month.label)}: income ${month.income.toLocaleString()}, expenses ${month.expense.toLocaleString()}">
    <div class="bar-pair"><span class="bar" style="height:${Math.max(3, (month.income / highest) * 100)}%" aria-label="Income"></span><span class="bar expense" style="height:${Math.max(3, (month.expense / highest) * 100)}%" aria-label="Expenses"></span></div>
    <span class="chart-label">${escapeHtml(month.label)}</span>
  </div>`,
    )
    .join("");
}

function renderCategories() {
  const container = document.querySelector("#category-breakdown");
  const expenses = monthTransactions("expense");
  const totals = new Map();
  expenses.forEach((transaction) => {
    const category = transaction.category || "Others";
    const currency = getAccount(transaction.accountId)?.currency || "NGN";
    const key = `${category}\u0000${currency}`;
    totals.set(key, {
      category,
      currency,
      amount: (totals.get(key)?.amount || 0) + Number(transaction.amount),
    });
  });
  const categories = [...totals.values()]
    .sort((left, right) => right.amount - left.amount)
    .slice(0, 5);
  if (!categories.length) {
    container.innerHTML =
      '<div class="category-empty">Nothing spent this month yet.</div>';
    return;
  }
  const highest = categories[0].amount;
  container.innerHTML = categories
    .map(
      ({ category, currency, amount }) =>
        `<div class="category-row"><span class="category-name" title="${escapeHtml(category)} · ${escapeHtml(currency)}">${escapeHtml(category)} · ${escapeHtml(currency)}</span><span class="category-track"><span class="category-fill" style="display:block;width:${(amount / highest) * 100}%"></span></span><span class="category-amount">${escapeHtml(formatMoney(amount, currency))}</span></div>`,
    )
    .join("");
}

function renderAccounts() {
  const container = document.querySelector("#account-list");
  if (!state.accounts.length) {
    container.innerHTML = `<div class="accounts-empty"><strong>Start with one account.</strong><p>Add a cash, checking, or savings balance to see your money in one place.</p><button class="button button-primary" type="button" data-open-account><span class="button-plus" aria-hidden="true">+</span> Add account</button></div>`;
    return;
  }
  container.innerHTML = state.accounts
    .map(
      (account) => `<article class="account-card">
    <div class="account-card-top"><span class="account-chip" aria-hidden="true">▤</span><span>${escapeHtml(account.currency)} · ${escapeHtml(account.accountType)}</span></div>
    <h2 class="account-name">${escapeHtml(account.name)}</h2>
    <div class="account-balance">${escapeHtml(formatMoney(accountBalance(account), account.currency))}</div>
    <div class="account-meta">Starting balance ${escapeHtml(formatMoney(Number(account.startingBalance), account.currency))}</div>
  </article>`,
    )
    .join("");
}

function render() {
  renderSummary();
  renderChart();
  renderCategories();
  renderAccounts();
  renderTransactionTable(
    "#recent-transactions",
    sortedTransactions().slice(0, 5),
  );
  renderFilteredTransactions();
  refreshAccountOptions();
}

function renderFilteredTransactions() {
  const search = (document.querySelector("#transaction-search")?.value || "")
    .trim()
    .toLowerCase();
  const type = document.querySelector("#type-filter")?.value || "all";
  const filtered = sortedTransactions().filter((transaction) => {
    const accountName = getAccount(transaction.accountId)?.name || "";
    const matchesSearch = [
      transaction.category,
      transaction.note,
      accountName,
      transaction.date,
    ].some((value) =>
      String(value || "")
        .toLowerCase()
        .includes(search),
    );
    return matchesSearch && (type === "all" || transaction.type === type);
  });
  renderTransactionTable("#all-transactions", filtered);
}

function refreshAccountOptions() {
  const select = document.querySelector("#transaction-account");
  const previous = select.value;
  select.innerHTML = state.accounts
    .map(
      (account) =>
        `<option value="${escapeHtml(account.id)}">${escapeHtml(account.name)} · ${escapeHtml(account.currency)}</option>`,
    )
    .join("");
  if (state.accounts.some((account) => account.id === previous))
    select.value = previous;
}

function refreshCategories() {
  const type = document.querySelector('input[name="type"]:checked').value;
  const categories = type === "income" ? INCOME_CATEGORIES : EXPENSE_CATEGORIES;
  document.querySelector("#transaction-category").innerHTML = categories
    .map((category) => `<option>${escapeHtml(category)}</option>`)
    .join("");
}

function showToast(message) {
  const toast = document.querySelector("#toast");
  toast.textContent = message;
  toast.classList.add("is-visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 2600);
}

function openDialog(dialogId) {
  document.querySelector(dialogId).showModal();
}

function openTransactionDialog() {
  if (!state.accounts.length) {
    showToast("Add an account first, then log your activity.");
    openDialog("#account-dialog");
    return;
  }
  const form = document.querySelector("#transaction-form");
  form.reset();
  form.elements.date.value = localDateString();
  refreshCategories();
  refreshAccountOptions();
  openDialog("#transaction-dialog");
}

function setView(view) {
  document.querySelectorAll(".view").forEach((section) => {
    section.hidden = section.id !== `view-${view}`;
  });
  document
    .querySelectorAll("[data-view-link]")
    .forEach((button) =>
      button.classList.toggle("is-active", button.dataset.viewLink === view),
    );
  document.querySelector("#page-label").textContent =
    view.charAt(0).toUpperCase() + view.slice(1);
  if (location.hash !== `#${view}`) history.replaceState(null, "", `#${view}`);
}

document.querySelector("#today-label").textContent = new Intl.DateTimeFormat(
  "en",
  { weekday: "short", month: "short", day: "numeric" },
).format(new Date());
document
  .querySelectorAll("[data-view-link]")
  .forEach((button) =>
    button.addEventListener("click", () => setView(button.dataset.viewLink)),
  );
document
  .querySelectorAll("[data-open-transaction]")
  .forEach((button) => button.addEventListener("click", openTransactionDialog));
document
  .querySelectorAll("[data-open-account]")
  .forEach((button) =>
    button.addEventListener("click", () => openDialog("#account-dialog")),
  );
document
  .querySelectorAll("[data-close-dialog]")
  .forEach((button) =>
    button.addEventListener("click", () => button.closest("dialog").close()),
  );
document
  .querySelectorAll('input[name="type"]')
  .forEach((input) => input.addEventListener("change", refreshCategories));
document
  .querySelector("#transaction-search")
  .addEventListener("input", renderFilteredTransactions);
document
  .querySelector("#type-filter")
  .addEventListener("change", renderFilteredTransactions);

document
  .querySelector("#transaction-form")
  .addEventListener("submit", (event) => {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    const amount = Number(form.get("amount"));
    if (!Number.isFinite(amount) || amount <= 0) return;
    state.transactions.push({
      id: makeId(),
      type: form.get("type"),
      amount,
      date: form.get("date"),
      category: form.get("category"),
      accountId: form.get("accountId"),
      note: String(form.get("note") || "").trim(),
    });
    saveState();
    event.currentTarget.closest("dialog").close();
    render();
    showToast("Transaction saved.");
  });

document.querySelector("#account-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const form = new FormData(event.currentTarget);
  const startingBalance = Number(form.get("startingBalance"));
  if (!Number.isFinite(startingBalance)) return;
  state.accounts.push({
    id: makeId(),
    name: String(form.get("name") || "").trim(),
    currency: form.get("currency"),
    accountType: form.get("accountType"),
    startingBalance,
  });
  saveState();
  event.currentTarget.reset();
  event.currentTarget.closest("dialog").close();
  render();
  showToast("Account saved.");
});

document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-delete-transaction]");
  if (!button) return;
  state.transactions = state.transactions.filter(
    (transaction) => transaction.id !== button.dataset.deleteTransaction,
  );
  saveState();
  render();
  showToast("Transaction removed.");
});

document.querySelectorAll("dialog").forEach((dialog) =>
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  }),
);

render();
const initialView = ["overview", "activity", "accounts"].includes(
  location.hash.slice(1),
)
  ? location.hash.slice(1)
  : "overview";
setView(initialView);
