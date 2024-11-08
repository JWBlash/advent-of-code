
# reads data from the "sample" file and does the thing
function GetTotal {
    param($fname)
    $fileContent = Get-Content -Path "$PWD\$fname"

    $sum = 0

    foreach ($line in $fileContent) {
        $fixedLine = SubFirstAndLast $line
        $first = FindFirstDigitInLine $fixedline
        $rev = ReverseString $fixedline
        $last = FindFirstDigitInLine -line $rev 
        $total = "{0}{1}" -f $first, $last
        $linesum = [int]$total
        $tmpsum = $sum
        $sum += $linesum
        Write-Host "[$line]: $tmpsum + $linesum = $sum"
    }
    return $sum
}

function SubFirstAndLast {
    param([string] $line)
    $a = ReplaceFirstWordInLine $line
    $b = ReplaceLastWordInLine $a
    return $b
}

# replace the first digit-word in the line with a proper int
function ReplaceFirstWordInLine {
    param([string] $line)

    $empty = ""
    $needReplace = $true

    foreach ($char in $line.ToCharArray()) {
        $empty += $char
        if ($empty.Contains("one") -and $needReplace) {
            $line = $line.Replace("one", "1")
            $needReplace = $false
        }
        elseif ($empty.Contains("two") -and $needReplace) {
            $line = $line.Replace("two", "2")
            $needReplace = $false
        }
        elseif ($empty.Contains("three") -and $needReplace) {
            $line = $line.Replace("three", "3")
            $needReplace = $false
        }
        elseif ($empty.Contains("four") -and $needReplace) {
            $line = $line.Replace("four", "4")
            $needReplace = $false
        }
        elseif ($empty.Contains("five") -and $needReplace) {
            $line = $line.Replace("five", "5")
            $needReplace = $false
        }
        elseif ($empty.Contains("six") -and $needReplace) {
            $line = $line.Replace("six", "6")
            $needReplace = $false
        }
        elseif ($empty.Contains("seven") -and $needReplace) {
            $line = $line.Replace("seven", "7")
            $needReplace = $false
        }
        elseif ($empty.Contains("eight") -and $needReplace) {
            $line = $line.Replace("eight", "8")
            $needReplace = $false
        }
        elseif ($empty.Contains("nine") -and $needReplace) {
            $line = $line.Replace("nine", "9")
            $needReplace = $false
        }
    }
    return $line
}

# replace the last digit-word in the line with a proper int
# this is so stupid
function ReplaceLastWordInLine {
    param($line)

    $empty = ""
    $needReplace = $true

    for ($i = $line.ToCharArray().Count; $i -ge 0; $i--) {
        $empty += $line[$i]
        if ($empty.Contains("eno") -and $needReplace) {
            $line = $line.Replace("one", "1")
            $needReplace = $false
        }
        elseif ($empty.Contains("owt") -and $needReplace) {
            $line = $line.Replace("two", "2")
            $needReplace = $false
        }
        elseif ($empty.Contains("eerht") -and $needReplace) {
            $line = $line.Replace("three", "3")
            $needReplace = $false
        }
        elseif ($empty.Contains("ruof") -and $needReplace) {
            $line = $line.Replace("four", "4")
            $needReplace = $false
        }
        elseif ($empty.Contains("evif") -and $needReplace) {
            $line = $line.Replace("five", "5")
            $needReplace = $false
        }
        elseif ($empty.Contains("xis") -and $needReplace) {
            $line = $line.Replace("six", "6")
            $needReplace = $false
        }
        elseif ($empty.Contains("neves") -and $needReplace) {
            $line = $line.Replace("seven", "7")
            $needReplace = $false
        }
        elseif ($empty.Contains("thgie") -and $needReplace) {
            $line = $line.Replace("eight", "8")
            $needReplace = $false
        }
        elseif ($empty.Contains("enin") -and $needReplace) {
            $line = $line.Replace("nine", "9")
            $needReplace = $false
        }

    }
    return $line
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

# just for the sake of organization
function Main {
    # pt1 sample 
    # $total = GetTotal sample
    # pt1 total 
    $total = GetTotal input 
    # pt2 sample
    # $total = GetTotal pt2sample 
    Write-Output $total
}

# calls the main func
Main
