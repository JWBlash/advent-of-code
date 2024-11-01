
# reads data from the "sample" file and does the thing
function GetTotal {
    param($fname)
    $fileContent = Get-Content -Path "$PWD\$fname"

    $sum = 0

    foreach ($line in $fileContent) {
        $first = FindFirstDigitInLine $line
        $rev = ReverseString $line
        $last = FindFirstDigitInLine -line $rev 
        $total = "{0}{1}" -f $first, $last
        $linesum = [int]$total
        $sum += $linesum
    }
    return $sum
}

function FindFirstDigitInLine {
    param ($line)
    foreach ($char in $line.ToCharArray()) {
        if ([char]::IsDigit($char)) {
            Write-Output $char
            break
        }
    }
}

function ReverseString {
    param($ToReverse)
    $result = ($ToReverse.ToCharArray())
    [Array]::Reverse($result)
    return -join $result
}

function IfStringIsDigit {
    param($str)
    switch ($str) {
        "one" { 1 }
        "two" { 2 }
        "three" { 3 }
        "four" { 4 }
        "five" { 5 }
        "six" { 6 }
        "seven" { 7 }
        "eight" { 8 }
        "nine" { 9 }

    }
}

# just for the sake of organization
function Main {
    # sample output
    # $total = GetTotal sample
    $total = GetTotal input 
    Write-Output $total
}

# calls the main func
Main
