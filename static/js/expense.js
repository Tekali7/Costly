/**
 * Expense deletion script.
 * 
 * Handles the deletion of expenses in the application.
 * Creates a modal for confirming the deletion choice for better UX
 * and dynamically updates the form action URL based on the expense ID.
 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-expense");
const deleteForm = document.getElementById("deleteForm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let expenseId = e.target.getAttribute("data-expense-id");
        deleteForm.action = `/delete_expense/${expenseId}`;
        deleteModal.show();
    });
}
