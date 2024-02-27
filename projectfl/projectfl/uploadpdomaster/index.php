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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index Page</title>

    <link rel="stylesheet" href="css/materialize.min.css">
    <link rel="stylesheet" href="iconfont/material-icons.css">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
<style>
    .img {
    width: 50%;
    heigh: auto;
    }
    body {
    background-color: lightblue;
    }
</style>
</head>
<body >
    
    <div class="container text-center">
        <h1>Medical labels detection </h1>
    </div>
    <div class="container w3-col l3 m6 w3-padding text-center">
        
        
        <div class="container">
            <a href="add.php" class="btn btn-success">Add Image</a>
        </div>
        
        
        <div class="container ">
            <div class="row">
                
                    <?php 
                        $select_stmt = $db->prepare('SELECT * FROM tbl_file'); 
                        $select_stmt->execute();

                        while ($row = $select_stmt->fetch(PDO::FETCH_ASSOC)) {
                            $id++;
                    ?>
                    
                        <div class="col s12 m4 l8"><br>
                            <img src="upload/<?php echo $row['image']; ?>"class="img" alt="" > 
                        
                            
                                    <table>
                                        <tr>
                                            <td ></td>
                                            <td ></td>
                                            <td>Name</td>
                                           
                                            <td><?php echo $row['name']; ?></td>
                                        </tr>
                                        <tr>  
                                            <!--<td ><a href="edit.php?update_id=<?php echo $row['id']; ?>" class="btn btn-warning">Edit</a></td>-->
                                            <td  style="width:20%;"></td>
                                            <td ></td>
                                            <td ><a href="?delete_id=<?php echo $row['id']; ?>" class="btn btn-danger">Delete</a></td> 
                                            
                                            <td ><a href="ocr.php?" class="btn btn-primary">OCR</a></td>
                                        </tr>
                                        
                                        
                                    </table>
                        </div>
                        
        </div><!-- row -->
                <?php } ?>    
    </div><!--Container--->

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>