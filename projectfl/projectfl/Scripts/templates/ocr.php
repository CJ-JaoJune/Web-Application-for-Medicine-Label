<?php 

    require_once('connection.php');

    if (isset($_REQUEST['delete_id'])) {
        $id = $_REQUEST['delete_id'];

        $select_stmt = $db->prepare('SELECT * FROM tbl_file WHERE id = :id');
        $select_stmt->bindParam(':id', $id);
        $select_stmt->execute();
        $row = $select_stmt->fetch(PDO::FETCH_ASSOC);
        unlink("upload/".$row['image']); // unlin functoin permanently remove your file

        // delete an original record from db
        $delete_stmt = $db->prepare('DELETE FROM tbl_file WHERE id = :id');
        $delete_stmt->bindParam(':id', $id);
        $delete_stmt->execute();

        header("Location: index.php");
    }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <style>
        .img {
        width: 50%;
        heigh: auto;
        }
        body {
        background-color: lightblue;
        }
        .btn {
        border: none;
        color: white;
        padding: 14px 28px;
        font-size: 16px;
        cursor: pointer;
        }

        .success {background-color: #04AA6D;} /* Green */
        .success:hover {background-color: #46a049;}

        .info {background-color: #2196F3;} /* Blue */
        .info:hover {background: #0b7dda;}

        .warning {background-color: #ff9800;} /* Orange */
        .warning:hover {background: #e68a00;}

        .danger {background-color: #f44336;} /* Red */ 
        .danger:hover {background: #da190b;}

        .default {background-color: #e7e7e7; color: black;} /* Gray */ 
        .default:hover {background: #ddd;}
        .bg{
            background-color: white;
        }
        .bg_white{
            background-color: white;
        }

    </style>
</head>
<body>
    <div class="container text-center">
    
    <br><br>
        
            <!-- <a href="index.php" class="bubbly-button">HOME</a> -->
            <a href="?delete_id=<?php echo $row['id']; ?>" class="btn btn-success">HOME</a><br><br>
           
 
         
        <div class="container"> 
            
            <div class="container">
                <div class="bg">
                <br>
                <div class="row">
                    
                    <div class="col-sm">
                        <button class="btn btn-success" style="width: 150px;heigh: 10px;">สรรพคุณ</button> 
                    </div>   
                    <div class="col-sm">
                        <h4>
                            เป็นยาที่ใช้รับประทานเพื่อทำลาย
                            เชื้อโรคในลำไส้ แก้ปวดท้อง แก้ท้องอืด
                            ท้องเฟ้อ จุกเสียด ช่วยขับลม แก้ท้องเสีย
                            กลิ่นรสหอมหวาน รับประทานง่าย
                        </h4>
                    </div>   
                    
                </div>
                <br><br>
                <div class="row">
                    <div class="col-sm">
                        <button class="btn warning"style="width: 150px;heigh: 10px;">วิธีใช้</button>
                    </div>
                    <div class="col-sm">
                        <h4> 
                            เด็ก:1-2 ช้อนชา วันละ 3 ครั้ง
                            ผู้ใหญ่:1 ช้อนโต๊ะ วันละ 3 ครั้ง
                        </h4>
                    </div>
                </div>
                <br><br>
                <div class="row">
                    <div class="col-sm">
                        <button class="btn danger"style="width: 150px;heigh: 10px;">คำเตือน</button>
                    </div>
                    <div class="col-sm">
                        <h4>
                            ยานี้มีแอลกอฮอล์ผสมอยู่0.95% w/v
                            ควรใช้ด้วยความระมัดระวัง 
                            ห้ามใช้ในผู้แพ้ยานี้ 
                        </h4>
                    </div>
                </div>
            </div>
            </div>
        <br><br>
            <h3>
                <?php
                    //exec('python OCRMed.py ',$output);
                    //echo implode("",$output);
                ?>
            </h3>

        </div>
        
    </div>
    <!--<div class="container"> 
            
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                        <button class="btn btn-success" style="width: 200px;heigh: 10px;">สรรพคุณ</button>
                    </div>    
                    <div class="col-sm">
                        <h3>
                            แก้ร้อนใน กระหายน้้า แก้ไข้ตัวร้อน
                            และเป็นยาระบายอ่อนๆ

                           
                            ในตัวยาทั้งหมด 390 กรัม
                            มีอิ่งงิ้ม   30 กรัม ขมิ้นชัน30กรัม
                            บอระเพ็ด 140 กรัม
                            ลูกกระดอม 20 กรัม และตัวยาอื่นๆ
                            น้าหนักเม็ดละ 0.3 กรัม
                            เลขทะเบียนนที่ @ 198/28
                            ยาแผนโบราณ

                            ห้างขายยาตราใบห่อ
                            75/5 ม. 3 ต.บางไผ่ อ.เมือง จ.นนทบุรี
                            ผู้ผลิต



                        </h3>
                    </div>    
                </div>
                <br><br>
                <div class="row">
                    <div class="col-sm">
                        <button class="btn warning"style="width: 200px;heigh: 10px;">วิธีใช้</button>
                    </div>
                    <div class="col-sm">
                        <h3> 
                            ทานวันละ 3 เวลา ก่อนหรือ
                            หลังอาหารผู้ใหญ่รับประทานครั้งละ4เม็ด
                            เด็กรับประทานครั้งละ 2 เม็ด
                            เมื่อท่านต้องการระบายมากๆ
                            รับประทานเพิ่มอีก 1-2 เม็ด
                        </h3>
                    </div>
                </div>
                <br><br>
                <div class="row">
                    <div class="col-sm">
                        <button class="btn danger"style="width: 200px;heigh: 10px;">คำเตือน</button>
                    </div>
                    <div class="col-sm">
                        <h3>
                            -
                        </h3>
                    </div>
                </div>
            </div>-->
            
    
   
</body>

</html>