document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll('[data-edit-id]');
    
    // Iterate over and add event listener to each edit button
    editButtons.forEach(button => {
        button.addEventListener("click", function() {
            // Get ID from data-edit-id
            const expenseId = this.dataset.editId;
            
            // Redirect to edit_expense with expense ID
            window.location.href = `edit_expense/${expenseId}`;
        });
    });
});
