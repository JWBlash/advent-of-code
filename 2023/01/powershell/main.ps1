
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

# just for practice, see if there is ANY number in the line
# this will help me figure out the logic
function FindFirstNumber {
    param($line)

    $least = 0
    $firstPartLen = 0
    $lastPartLen = 0

    # split on 'one'
    $ar = $line -split "one"
}

# just for the sake of organization
function Main {
    # pt1 sample 
    # $total = GetTotal sample
    # pt1 total 
    # $total = GetTotal input 
    # pt2 sample
    # $total = GetTotal pt2sample 
    # Write-Output $total

    $leftMin = 0
    # $rightMin = 0
    $first = ""

    $in = "7onetwo3four"
    $num = "four"
    $a = $in -split $num
    $b = "len: {0} | firstpartLen: {1} | lastpartLen: {2}" -f $in.Length, $a[0].Length, $a[1].Length
    $firstpart = ($in.Length-($in.Length-$a[0].Length))
    # since we're dealing with lengths and not indices, this can run over the buffer
    # when used as an index. just keep that in mind!
    $secondpart = $firstpart + $num.Length
    $c = "appears at {0}, in[{1}] should be the first letter of the 2nd part" -f $firstpart, $secondpart

    # "handle" the case where there are multiple in one line
    # mostly just pray this naive algo doesn't bump into that :)
    if ($a.Length -gt 2) {
        Write-Output "oh no!"
        return 
    }
    Write-Output $in[$secondpart]
    Write-Output $b
    Write-Output $c

    # this is a one-off assignment. we'll save this value
    # and check afterwards if there's any digits that appear in the
    # string before this position
    # $leftMin = $a[0].Length
    # if ($leftMin -lt )

}

# calls the main func
Main
