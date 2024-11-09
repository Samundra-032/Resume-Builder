document.addEventListener("DOMContentLoaded", function() {
    // Confirm before deleting an inline form
    document.querySelectorAll(".delete-button").forEach(function(button) {
        button.addEventListener("click", function(event) {
            const confirmed = confirm("Are you sure you want to delete this entry?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // Animate collapsible fieldsets
    document.querySelectorAll(".collapse").forEach(function(fieldset) {
        fieldset.style.cursor = "pointer";
        fieldset.addEventListener("click", function() {
            const content = this.nextElementSibling;
            if (content.style.display === "none" || content.style.display === "") {
                content.style.display = "block";
                this.style.color = "#007bff";
            } else {
                content.style.display = "none";
                this.style.color = "#555";
            }
        });
    });

    // Alert user when adding a new inline form
    document.querySelectorAll(".add-row a").forEach(function(button) {
        button.addEventListener("click", function() {
            setTimeout(function() {
                alert("A new entry has been added. Please fill out the details.");
            }, 100);
        });
    });
});
