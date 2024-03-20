<!-- Vulnerability Type: (CWE-78) Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') -->
<!-- Severity: Critical -->

<?php
function listFiles($directory) {
    $output = shell_exec("ls $directory");
    return "<pre>$output</pre>";
}

function readFileContents($filename) {
    $contents = file_get_contents($filename);
    return "<pre>$contents</pre>";
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    $action = $_GET['action'];

	switch ($action) {
        case 'list':
            $directory = $_GET['directory'];
            echo listFiles($directory);
            break;
        case 'read':
            $filename = $_GET['filename'];
            echo readFileContents($filename);
            break;
        default:
            echo "Invalid action";
            break;
    }
}
?>