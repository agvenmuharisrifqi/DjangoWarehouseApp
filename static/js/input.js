const inputField = document.querySelectorAll("input:not(input[type='hidden'])");
const labelInput = document.querySelectorAll("input:not(input[type='hidden'])~label");
for (let inp = 0; inp < inputField.length; inp++) {
    inputField[inp].addEventListener("focus", () => {
        if (!labelInput[inp].classList.contains("active")) {
            labelInput[inp].classList.add("active")
        }
    })
    if (inputField[inp].value !== "" || inputField[inp].type === "date") {
        labelInput[inp].classList.add("active")
    }
    inputField[inp].addEventListener("blur", (e) => {
        if (e.target.value === "" && e.target.type !== "date") {
            labelInput[inp].classList.remove("active")
        }
    })
}
const passwordEye = document.querySelectorAll(".input-wrapper i.password-eye");
const passwordInput = document.querySelectorAll(".input-field input[type='password']")
if (passwordEye !== null && passwordInput !== null) {
    for (let pass = 0; pass < passwordEye.length; pass++) {
        passwordEye[pass].addEventListener("click", (e) => {
            if (e.target.classList.contains("fa-eye-slash") && passwordInput[pass].type === "password") {
                e.target.classList.remove("fa-eye-slash")
                e.target.classList.add("fa-eye");
                passwordInput[pass].type = "text";
            } else {
                e.target.classList.remove("fa-eye");
                e.target.classList.add("fa-eye-slash")
                passwordInput[pass].type = "password";
            }
        })
    }
}

function checkInput() {
    let status = [],
        regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
        regPassword = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/gm,
        inputs = document.querySelectorAll("input[required], select[required]"),
        warnings = document.querySelectorAll("input[required]~.error, select[required]~.error"),
        len = Math.min(inputs.length, warnings.length);
    console.log(inputs);
    console.log(warnings);
    for (let inp = 0; inp < len; inp++) {
        let inpValue = inputs[inp].value
        if (inpValue === "")
            writeWarning(warnings[inp], "block", "don't be empty")
        else if (inputs[inp].type === "email" && !inpValue.match(regEmail))
            writeWarning(warnings[inp], "block", "please enter a valid email address")
        else if (inputs[inp].id === "id_password" && !inpValue.match(regPassword))
            writeWarning(warnings[inp], "block", "password is not strong")
        else
            writeWarning(warnings[inp], "none", "")
    }

    function writeWarning(warningElem, warningDisplay, warningText) {
        let statusRes = warningDisplay === "block" ? false : true;
        warningElem.textContent = warningText;
        warningElem.style.display = warningDisplay;
        status.push(statusRes)
    }
    return status
}

function checkPassSame() {
    let pass = document.getElementById("id_password"),
        rety = document.getElementById("id_retype_password"),
        warRety = rety.nextElementSibling.nextElementSibling;
    if (pass.value === "" || rety.value === "") return false
    if (pass.value !== rety.value) {
        warRety.textContent = "retype password is not same"
        warRety.style.display = "block";
        return false
    }
    return true
}