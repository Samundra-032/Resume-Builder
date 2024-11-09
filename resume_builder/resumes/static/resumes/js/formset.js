// function addForm(containerId, formClass) {
//     console.log("Add Form Triggered for:", containerId); // Debugging message

//     const container = document.getElementById(containerId);
//     if (!container) {
//         console.error("Container not found for:", containerId);
//         return;
//     }

//     const totalForms = container.querySelector(`input[name$='TOTAL_FORMS']`);
//     if (!totalForms) {
//         console.error("TOTAL_FORMS not found in container:", containerId);
//         return;
//     }

//     const formCount = parseInt(totalForms.value);
//     const formTemplate = container.querySelector(`.${formClass}`);
//     if (!formTemplate) {
//         console.error("Form template not found for class:", formClass);
//         return;
//     }

//     // Clone the form template
//     const newForm = formTemplate.cloneNode(true);
//     newForm.classList.add(`${formClass}-${formCount}`); // Adding unique class

//     // Clear the cloned form's input values
//     newForm.querySelectorAll('input, textarea, select').forEach(input => {
//         input.value = ''; // Clear all input values
//     });

//     // Update name and id attributes to use the new form index
//     newForm.querySelectorAll('[name]').forEach(input => {
//         input.name = input.name.replace(/-\d+-/, `-${formCount}-`);
//         input.id = input.id.replace(/-\d+-/, `-${formCount}-`);
//     });

//     // Append the cloned form and update the total forms count
//     container.appendChild(newForm);
//     totalForms.value = formCount + 1;
//     console.log("New form added. Updated total forms:", totalForms.value); // Debugging message
// }
function addForm(containerId, formClass) {
    console.log("Adding form to:", containerId);  // Debugging message

    const container = document.getElementById(containerId);
    const totalForms = container.querySelector(`input[name$='TOTAL_FORMS']`);
    const formCount = parseInt(totalForms.value);
    const formTemplate = container.querySelector(`.${formClass}`);

    // Clone the template form
    const newForm = formTemplate.cloneNode(true);
    newForm.classList.add(`${formClass}-${formCount}`);

    // Clear input values in the cloned form
    newForm.querySelectorAll('input, textarea, select').forEach(input => {
        input.value = '';
    });

    // Update name and id attributes in the cloned form for form indexing
    newForm.querySelectorAll('[name]').forEach(input => {
        input.name = input.name.replace(/-\d+-/, `-${formCount}-`);
        input.id = input.id.replace(/-\d+-/, `-${formCount}-`);
    });

    // Create a delete button for the cloned form
    const deleteButton = document.createElement('button');
    deleteButton.type = 'button';
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('delete-button');
    deleteButton.onclick = function() {
        deleteForm(newForm, containerId);
    };
    newForm.appendChild(deleteButton);

    // Append the cloned form to the container
    container.appendChild(newForm);

    // Increment the TOTAL_FORMS count in the management form
    totalForms.value = formCount + 1;
    console.log("Form added. Updated TOTAL_FORMS:", totalForms.value);  // Debugging message
}

function deleteForm(form, containerId) {
    const container = document.getElementById(containerId);
    container.removeChild(form);

    // Decrement TOTAL_FORMS count in the management form
    const totalForms = container.querySelector(`input[name$='TOTAL_FORMS']`);
    totalForms.value = parseInt(totalForms.value) - 1;
    console.log("Form deleted. Updated TOTAL_FORMS:", totalForms.value);  // Debugging message
}
