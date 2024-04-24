const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-expense");
const deleteForm = document.getElementById("deleteForm");
const deleteConfirmButton = document.getElementById("deleteConfirm");

// Add event listener to each delete button
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let expenseId = e.target.getAttribute("data-expense-id");
        // Set the action attribute of the delete form
        deleteForm.action = `/delete_expense/${expenseId}`;
        deleteModal.show();
    });
}
