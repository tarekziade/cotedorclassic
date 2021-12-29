<?php

require 'vendor/autoload.php';
require 'mail-config.php';

$response = array(
    'fields' => array(
        'name' => 'error',
        'email' => 'error',
        'phone' => 'error',
        'message' => 'error'
    ),
    'sent' => 'error'
);

function stringIsValid($value)
{
    return !empty(trim($value));
}

function numberIsValid($value)
{
    return preg_match("/^[0-9\+\s]+$/", trim($value));
}

function emailIsValid($value)
{
    return filter_var(trim($value), FILTER_VALIDATE_EMAIL);
}

function sendForm($data)
{
    $sent = false;
    $body = " Vous avez recu une demande sur le site.

<b>Nom:</b><blockquote>" . utf8_decode($data['name']) . "</blockquote>
<b>Email:</b><blockquote>" . utf8_decode($data['email']) . "</blockquote>
<b>Telephone:</b><blockquote>" . utf8_decode($data['phone']) . "</blockquote>
<b>Message:</b><blockquote>" . utf8_decode($data['message']) . "</blockquote>";

    //try {
        $mail = new PHPMailer(true);
        $mail->IsSMTP();

        //$mail->SMTPDebug  = 2;
        //$mail->SMTPAuth   = true;
        //$mail->SMTPSecure = "tls";
        $mail->SMTPAutoTLS = false;
        $mail->SMTPSecure = false;
        $mail->Host       = SMTP_SERVER;
        $mail->Port       = SMTP_PORT;
        //$mail->Username   = SMTP_USER;
        //$mail->Password   = SMTP_PASS;
        $mail->AddReplyTo(SMTP_USER, SMTP_REALNAME);
        $mail->AddAddress(RECIPIENT, RECIPIENT_REALNAME);
        $mail->AddAddress(SMTP_USER, SMTP_REALNAME);
        $mail->SetFrom(SMTP_USER, SMTP_REALNAME);
        $mail->Subject = 'Demande de ' . $data['name'] . ' ' . $data['email'];
        $mail->AltBody = $body;
        $mail->MsgHTML(nl2br($body));
        $mail->Send();

        $sent = true;
    /*} catch (Exception $e) {
        $sent = false;
        }*/
    return $sent;
}

if (!empty($_POST) && (isset($_POST['lastname']) && empty($_POST['lastname']))) {
    if (stringIsValid($_POST['name'])) {
        $response['fields']['name'] = 'ok';
    }
    if (emailIsValid($_POST['email'])) {
        $response['fields']['email'] = 'ok';
    }
    if (numberIsValid($_POST['phone'])) {
        $response['fields']['phone'] = 'ok';
    }
    if (stringIsValid($_POST['message'])) {
        $response['fields']['message'] = 'ok';
    }
    if (!in_array("error", $response['fields'])) {
        if (sendForm($_POST)) {
            $response['sent'] = 'ok';
        }
    }
}

print(json_encode($response));

?>
