const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-expense");
const deleteForm = document.getElementById("deleteForm");
const deleteConfirmButton = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let expenseId = e.target.getAttribute("data-expense-id");
        deleteForm.action = `/delete_expense/${expenseId}`;
        deleteModal.show();
    });
}
