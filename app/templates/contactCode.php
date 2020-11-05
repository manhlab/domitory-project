<?php
//database
$servername = "";
$username = "";
$password = "";
$dbname = "";
$success = false;
//email
$emailto ="";
$subject = "";
$body = "";
$headers = "";
//error
$errors = array();
$data = array();

if($_POST){
  
    if(empty($_POST["email"])){
        $errors['email'] = "Need an email address to submit enquiry.";
    }
    if(empty($_POST["subject"])){
        $errors['subject'] = "Please enter a subject for this enquiry.";
    }
    if(empty($_POST["body"])){
        $errors['body'] = 'Please tell us some details about this enquiry.';
    }
    if(!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)){
        $errors['validation'] = 'Need a valid email address to submit enquiry.';
    }
    
    else{
         $email = $_POST["email"];
         $subject = $_POST["subject"];
         $body = $_POST["body"];
         $headers = 'From: "\r\n'.'Reply-To: '.$email."\r\n".'X-Mailer: PHP/'.phpversion();
        if(mail($emailto,$subject,$body,$headers)){
           $success = true;
         } 
        }
    
   if($success){
    
       $conn = mysqli_connect($servername, $username, $password, $dbname);
       if(mysqli_error($conn)){

            die("Ërror Connecting");
        }
        
        $stmt = $conn->prepare("INSERT INTO datbase_name (date, email, subject, message) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $date, $email, $subject, $body);

        $date = date("Y/m/d");
       
        $stmt->execute();
       
        $stmt->close();
       
        mysqli_close($conn);
    }
    
    if(!empty($errors)){
        $data['succes'] = false;
        $data['errors'] = $errors;
    }
    else{
        $data['succes'] = true;
        $data['errors'] = "Success!";
    }
    
    echo json_encode($data);
}



?>