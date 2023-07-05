function getBotResponse(input) {
    // //rock paper scissors
    // if (input == "rock") {
    //     return "paper";
    // } else if (input == "paper") {
    //     return "scissors";
    // } else if (input == "scissors") {
    //     return "rock";
    // }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else if (input == "Nearby hospital please!"){
        return "Your Nearby Hospital Is KMCH Which Is Around 3kms";
    }
    else{
        return "Try asking something else!";
    }
}