<?php
$id = $_GET['id'];
$file = "logs/downloads.txt";
$handle = fopen($file, "r"); 
if(!$handle) { 
    error_log("Unable to open could not open file " . $file); 
} else { 
    $counter =(int) fread($handle, 20);
    fclose($handle); 
    $counter++; 
    $handle = fopen($file, "w" ); 
    fwrite($handle, $counter);
    fclose ($handle);
}
$file = "logs/downloads" . $id . ".txt";
$handle = fopen($file, "r");
if(!$handle) { 
    error_log("Unable to open could not open file " . $file); 
} else { 
    $counter =(int) fread($handle, 20);
    fclose($handle); 
    $counter++; 
    $handle = fopen($file, "w" ); 
    fwrite($handle, $counter);
    fclose ($handle); 
}
header("Location: data/BBID" . $id . ".zip");
?>
