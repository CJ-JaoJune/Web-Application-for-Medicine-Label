<?php 
    date_default_timezone_set('Asia/Bangkok');
    $db_host = "localhost";
    $db_user = "root";
    $db_password = "Four2020";
    $db_name = "project_test";

    try {
        $db = new PDO("mysql:host={$db_host};dbname={$db_name}", $db_user, $db_password);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    } catch(PDOException $e) {
        $e->getMessage();
        
    }

?>