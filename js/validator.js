var noReload = document.getElementById("form-1");

noReload.addEventListener("submit", function(e){
    e.preventDefault();
    validation();
});
// $('#contactForm').on("submit",function(ev){
//     ev.preventDefault();
//     validation();
// })

function printError(elemId, hintMsg) {
    document.getElementById(elemId).innerHTML = hintMsg;
}
function ev(){
    return true;
}
function validation(){
    var name = document.contactForm.uname.value;
    var email = document.contactForm.email.value;
    var gender = document.contactForm.gender.value;
    var age = document.contactForm.age.value;
    var mobile = document.contactForm.mobnumber.value;
    var namErr = emailErr = genderErr = ageErr = mobileErr=true;
    //name
    if (name==""){
        printError("nameErr", "Please enter your name");
    }else{
        var regex = /^[a-zA-Z\s]+$/;
        if (regex.test(name) === false) {
            printError("nameErr", "Please enter a valid name");
        } else {
            printError("nameErr", "");
            nameErr = false;
        }
    }
    //email
    if(email==""){
        printError("emailErr", "Please enter your email address");
    } else {
        // Regular expression for basic email validation
        var regex = /^\S+@\S+\.\S+$/;
        if (regex.test(email) === false) {
            printError("emailErr", "Please enter a valid email address");
        } else {
            printError("emailErr", "");
            emailErr = false;
        }
    }
    //gender
    if (gender == "") {
        printError("genderErr", "Please select your gender");
    } else {
        printError("genderErr", "");
        genderErr = false;
    }
    //age
    if (age == "") {
        printError("dobErr", "Please select your date of birth");
    } else {
        printError("dobErr", "");
        ageErr = false;
    }
    //mobile
    if (mobile == "") {
        printError("mobileErr", "Please enter your mobile number");
    } else {
        var regex = /^[1-9]\d{9}$/;
        if (regex.test(mobile) === false) {
            printError("mobileErr", "Please enter a valid 10 digit mobile number");
        } else {
            printError("mobileErr", "");
            mobileErr = false;
        }
    }
    if (!(nameErr || emailErr || genderErr || ageErr || mobileErr )) {
        var dataPreview = "Congratulations! \nYou have successfully validated the form\n";
        var no = document.getElementById("form-1");
    }
}