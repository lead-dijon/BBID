<?php
$file = "logs/visits.txt";
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
?>
