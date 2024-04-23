// document.addEventListener("DOMContentLoaded", function() {
//   const editButtons = document.getElementsByClassName('edit-expense');
  
//   for (let button of editButtons) {
//       button.addEventListener("click", (e) => {
//           console.log("Edit button clicked");
//           let expenseId = e.target.getAttribute("data-edit-id");
//           let expenseItemName = document.querySelector(`.expense-item-name[data-edit-id="${expenseId}"]`).innerText;
//           let expenseItemAmount = document.querySelector(`.expense-item-amount[data-edit-id="${expenseId}"]`).innerText;
//           let expenseItemCurrency = document.querySelector(`.expense-item-currency[data-edit-id="${expenseId}"]`).innerText;
          
//           document.getElementById("id_item").innerText = expenseItemName;
//           document.getElementById("id_amount").value = expenseItemAmount;
//           document.getElementById("id_currency").value = expenseItemCurrency;
          
//           document.getElementById("expenseForm").setAttribute("action", `/edit_expense/${expenseId}/`);
//       });
//   }
// });

document.addEventListener("DOMContentLoaded", function() {
  const editButtons = document.getElementsByClassName('edit-expense');
  
  for (let button of editButtons) {
      button.addEventListener("click", (e) => {
          let expenseId = e.target.getAttribute("data-expense-id");
          window.location.href = `/expense/edit_expense/${expenseId}/`;
      });
  }
});