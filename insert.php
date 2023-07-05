<?php
if (isset($_POST['submit'])) {
    if (isset($_POST['uname']) && isset($_POST['mobnumber']) &&
        isset($_POST['email']) && isset($_POST['box']) && isset($_POST['gender'])) 
        {
        
        $username = $_POST['uname'];
        $mnumber = $_POST['mobnumber'];
        $email = $_POST['email'];
        $udate = $_POST['box'];
        $gen= $_POST['gender'];
        

        $host = "localhost";
        $dbUsername = "root";
        $dbPassword = "";
        $dbName = "youtube";

        $conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);

        if ($conn->connect_error) {
            die('Could not connect to the database.');
        }
        else {
            $Select = "SELECT email FROM register WHERE email = ? LIMIT 1";
            $Insert = "INSERT INTO register(name, mobnumber,email,date,gender) values(?, ?, ?,?,?)";

            $stmt = $conn->prepare($Select);
            $stmt->bind_param("s", $email);
            $stmt->execute();
            $stmt->bind_result($resultEmail);
            $stmt->store_result();
            $stmt->fetch();
            $rnum = $stmt->num_rows;

            if ($rnum == 0) {
                $stmt->close();

                $stmt = $conn->prepare($Insert);
                $stmt->bind_param("sisss",$username, $mnumber, $email,$udate,$gen);
                if ($stmt->execute()) {
                    echo "New record inserted sucessfully.";
                }
                else {
                    echo $stmt->error;
                }
            }
            else {
                echo "Someone already registers using this email.";
            }
            $stmt->close();
            $conn->close();
        }
    }
    else {
        echo "All field are required.";
        die();
    }
}
else {
    echo "Submit button is not set";
}
?>