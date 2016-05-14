<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
<?php
$servername = "localhost";
$username = "meteo";
$password = "password";
$dbname = "meteo";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM METEO_DATA_SMART_HOUSE WHERE create_date = (select MAX(create_date) from METEO_DATA_SMART_HOUSE);";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        // echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
        $dom = new DOMDocument("1.0");
        $dom->appendChild($dom->createElement("p", "Temperature: " . $row["temperature"]));
        $dom->appendChild($dom->createElement("p", "Humidity: " . $row["humidity"]));
        $dom->appendChild($dom->createElement("p", "Date: " . $row["create_date"]));
        echo $dom->saveHTML();
        // echo "Temperature: " . $row["temperature"];
        // echo "Humidity: " . $row["humidity"];
        // echo "Date: " . $row["create_date"];
    }
} else {
    echo "0 results";
}
$conn->close();
?>
</body>
</html>
