
# reads data from the "sample" file and does the thing
function FindFirstDigit {
    param($FName)
    $fileContent = Get-Content -Path "$PWD\$FName"

    foreach ($line in $fileContent) {
        foreach ($char in $line.ToCharArray()) {
            if ([char]::IsDigit($char)) {
                Write-Output $char
                break
            }
        }
    }
}

function ReverseString {
    param($ToReverse)
    $result = -join ($ToReverse.ToCharArray() | [Array]::Reverse())
    return $result
}

# just for the sake of organization
function Main {
    # for testing
    FindFirstDigit -FName "sample"

    $yap = ReverseString -ToReverse YPAPPING
    Write-Output $yap

    # for actual run
    # FindFirstDigit -FName "input"
}

# calls the main func
Main
