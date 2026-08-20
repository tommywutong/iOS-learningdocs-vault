---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ManipulateNumbers.html
archived_at: '2026-07-15T07:45:49.496271Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Manipulating Numbers

Working with and manipulating numbers is an important and regular occurrence in scripting. Basic mathematic operations—such as addition, subtraction, multiplication, and division—are language-level features, but some other commonly performed operations require custom scripting.

> [!NOTE]
> 

### Converting a Number to a String

Scripts often need to convert numbers to string format to display information to the user or populate a document. In AppleScript, this conversion can be accomplished most of the time simply by using the coercion operator `as`, as shown in Listing 20-1.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=12%20as%20string)

__Listing 20-1__AppleScript: Coercing a number to a string

1. `12 as string`
2. `--> Result: "12"`

In JavaScript, the same conversion can be accomplished by calling the `toString()` method, as shown in Listing 20-2.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=num%20%3D%2012%0Anum.toString%28%29)

__Listing 20-2__JavaScript: Coercing a number to a string

1. `num = 12`
2. `num.toString()`
3. `// Result: "12"`

### Converting a Long Number to a String

In AppleScript, long numeric values are displayed in scientific notation. For example, `1234000000` is displayed by a script as `1.234E+9`. When this value is coerced to a string, it becomes: `"1.234E+9"`. The handler in Listing 20-3 converts a number, regardless of length, to a string of numeric characters instead of a numeric string in scientific notation.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20convertNumberToString%28theNumber%29%0A%20%20%20%20set%20theNumberString%20to%20theNumber%20as%20string%0A%20%20%20%20set%20theOffset%20to%20offset%20of%20%22E%22%20in%20theNumberString%0A%20%20%20%20if%20theOffset%20%3D%200%20then%20return%20theNumberString%0A%20%20%20%20set%20thePrefix%20to%20text%201%20thru%20%28theOffset%20-%201%29%20of%20theNumberString%0A%20%20%20%20set%20theConvertedNumberPrefix%20to%20%22%22%0A%20%20%20%20if%20thePrefix%20begins%20with%20%22-%22%20then%0A%20%20%20%20%20%20%20%20set%20theConvertedNumberPrefix%20to%20%22-%22%0A%20%20%20%20%20%20%20%20if%20thePrefix%20%3D%20%22-%22%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20thePrefix%20to%20%22%22%0A%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20thePrefix%20to%20text%202%20thru%20-1%20of%20thePrefix%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20if%0A%20%20%20%20set%20theDecimalAdjustment%20to%20%28text%20%28theOffset%20%2B%201%29%20thru%20-1%20of%20theNumberString%29%20as%20number%0A%20%20%20%20set%20isNegativeDecimalAdjustment%20to%20theDecimalAdjustment%20is%20less%20than%200%0A%20%20%20%20if%20isNegativeDecimalAdjustment%20then%0A%20%20%20%20%20%20%20%20set%20thePrefix%20to%20%28reverse%20of%20%28characters%20of%20thePrefix%29%29%20as%20string%0A%20%20%20%20%20%20%20%20set%20theDecimalAdjustment%20to%20-theDecimalAdjustment%0A%20%20%20%20end%20if%0A%20%20%20%20set%20theDecimalOffset%20to%20offset%20of%20%22.%22%20in%20thePrefix%0A%20%20%20%20if%20theDecimalOffset%20%3D%200%20then%0A%20%20%20%20%20%20%20%20set%20theFirstPart%20to%20%22%22%0A%20%20%20%20else%0A%20%20%20%20%20%20%20%20set%20theFirstPart%20to%20text%201%20thru%20%28theDecimalOffset%20-%201%29%20of%20thePrefix%0A%20%20%20%20end%20if%0A%20%20%20%20set%20theSecondPart%20to%20text%20%28theDecimalOffset%20%2B%201%29%20thru%20-1%20of%20thePrefix%0A%20%20%20%20set%20theConvertedNumber%20to%20theFirstPart%0A%20%20%20%20set%20theRepeatCount%20to%20theDecimalAdjustment%0A%20%20%20%20if%20%28length%20of%20theSecondPart%29%20is%20greater%20than%20theRepeatCount%20then%20set%20theRepeatCount%20to%20length%20of%20theSecondPart%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20theRepeatCount%0A%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theConvertedNumber%20to%20theConvertedNumber%20%26%20character%20a%20of%20theSecondPart%0A%20%20%20%20%20%20%20%20on%20error%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theConvertedNumber%20to%20theConvertedNumber%20%26%20%220%22%0A%20%20%20%20%20%20%20%20end%20try%0A%20%20%20%20%20%20%20%20if%20a%20%3D%20theDecimalAdjustment%20and%20a%20is%20not%20equal%20to%20%28length%20of%20theSecondPart%29%20then%20set%20theConvertedNumber%20to%20theConvertedNumber%20%26%20%22.%22%0A%20%20%20%20end%20repeat%0A%20%20%20%20if%20theConvertedNumber%20ends%20with%20%22.%22%20then%20set%20theConvertedNumber%20to%20theConvertedNumber%20%26%20%220%22%0A%20%20%20%20if%20isNegativeDecimalAdjustment%20then%20set%20theConvertedNumber%20to%20%28reverse%20of%20%28characters%20of%20theConvertedNumber%29%29%20as%20string%0A%20%20%20%20return%20theConvertedNumberPrefix%20%26%20theConvertedNumber%0Aend%20convertNumberToString)

__Listing 20-3__AppleScript: Handler that converts a number to a string, regardless of length

1. `on convertNumberToString(theNumber)`
2. `set theNumberString to theNumber as string`
3. `set theOffset to offset of "E" in theNumberString`
4. `if theOffset = 0 then return theNumberString`
5. `set thePrefix to text 1 thru (theOffset - 1) of theNumberString`
6. `set theConvertedNumberPrefix to ""`
7. `if thePrefix begins with "-" then`
8. `set theConvertedNumberPrefix to "-"`
9. `if thePrefix = "-" then`
10. `set thePrefix to ""`
11. `else`
12. `set thePrefix to text 2 thru -1 of thePrefix`
13. `end if`
14. `end if`
15. `set theDecimalAdjustment to (text (theOffset + 1) thru -1 of theNumberString) as number`
16. `set isNegativeDecimalAdjustment to theDecimalAdjustment is less than 0`
17. `if isNegativeDecimalAdjustment then`
18. `set thePrefix to (reverse of (characters of thePrefix)) as string`
19. `set theDecimalAdjustment to -theDecimalAdjustment`
20. `end if`
21. `set theDecimalOffset to offset of "." in thePrefix`
22. `if theDecimalOffset = 0 then`
23. `set theFirstPart to ""`
24. `else`
25. `set theFirstPart to text 1 thru (theDecimalOffset - 1) of thePrefix`
26. `end if`
27. `set theSecondPart to text (theDecimalOffset + 1) thru -1 of thePrefix`
28. `set theConvertedNumber to theFirstPart`
29. `set theRepeatCount to theDecimalAdjustment`
30. `if (length of theSecondPart) is greater than theRepeatCount then set theRepeatCount to length of theSecondPart`
31. `repeat with a from 1 to theRepeatCount`
32. `try`
33. `set theConvertedNumber to theConvertedNumber & character a of theSecondPart`
34. `on error`
35. `set theConvertedNumber to theConvertedNumber & "0"`
36. `end try`
37. `if a = theDecimalAdjustment and a is not equal to (length of theSecondPart) then set theConvertedNumber to theConvertedNumber & "."`
38. `end repeat if theConvertedNumber ends with "." then set theConvertedNumber to theConvertedNumber & "0"`
39. `if isNegativeDecimalAdjustment then set theConvertedNumber to (reverse of (characters of theConvertedNumber)) as string`
40. `return theConvertedNumberPrefix & theConvertedNumber`
41. `end convertNumberToString`

Listing 20-3 shows how to call the handler in Listing 20-3.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=convertNumberToString%288.72124243234E%2B11%29)

__Listing 20-4__AppleScript: Calling a handler to convert a long number to a string

1. `convertNumberToString(8.72124243234E+11)`
2. `--> Result: "872124243234"`

### Adding a Descriptive Suffix to a Number

The handlers Listing 20-5 and Listing 20-6 convert a number to a string and appends a suffix of `"st"`, `"nd"`, `"rd"`, or `"th"`, resulting in strings such as `"1st"`, `"2nd"`, `"3rd"`, and `"4th"`.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20addDescriptiveSuffixToNumber%28theNumber%29%0A%20%20%20%20--%20Determine%20the%20suffix%20to%20add%2C%20based%20on%20the%20last%20two%20digits%0A%20%20%20%20set%20theLastDigit%20to%20theNumber%20mod%2010%0A%20%20%20%20set%20theLastTwoDigits%20to%20theNumber%20mod%20100%0A%20%20%20%20set%20theSuffix%20to%20%22th%22%0A%20%20%20%20if%20%7B1%2C%20-1%7D%20contains%20theLastDigit%20and%20%7B11%2C%20-11%7D%20does%20not%20contain%20theLastTwoDigits%20then%0A%20%20%20%20%20%20%20%20set%20theSuffix%20to%20%22st%22%0A%20%20%20%20else%20if%20%7B2%2C%20-2%7D%20contains%20theLastDigit%20and%20%7B12%2C%20-12%7D%20does%20not%20contain%20theLastTwoDigits%20then%0A%20%20%20%20%20%20%20%20set%20theSuffix%20to%20%22nd%22%0A%20%20%20%20else%20if%20%7B3%2C%20-3%7D%20contains%20theLastDigit%20and%20%7B13%2C%20-13%7D%20does%20not%20contain%20theLastTwoDigits%20then%0A%20%20%20%20%20%20%20%20set%20theSuffix%20to%20%22rd%22%0A%20%20%20%20end%20if%0A%0A%20%20%20%20--%20Return%20the%20number%20and%20suffix%0A%20%20%20%20return%20%28theNumber%20as%20string%29%20%26%20theSuffix%0Aend%20addDescriptiveSuffixToNumber)

__Listing 20-5__AppleScript: Handler that adds a descriptive suffix to a number

1. `on addDescriptiveSuffixToNumber(theNumber)`
2. `-- Determine the suffix to add, based on the last two digits`
3. `set theLastDigit to theNumber mod 10`
4. `set theLastTwoDigits to theNumber mod 100`
5. `set theSuffix to "th"`
6. `if {1, -1} contains theLastDigit and {11, -11} does not contain theLastTwoDigits then`
7. `set theSuffix to "st"`
8. `else if {2, -2} contains theLastDigit and {12, -12} does not contain theLastTwoDigits then`
9. `set theSuffix to "nd"`
10. `else if {3, -3} contains theLastDigit and {13, -13} does not contain theLastTwoDigits then`
11. `set theSuffix to "rd"`
12. `end if`
14. `-- Return the number and suffix`
15. `return (theNumber as string) & theSuffix`
16. `end addDescriptiveSuffixToNumber`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20addDescriptiveSuffixToNumber%28num%29%20%7B%0A%20%20%20%20%2F%2F%20Convert%20the%20number%20to%20absolute%20value%0A%20%20%20%20var%20integer%20%3D%20Math.abs%28num%29%0A%0A%20%20%20%20%2F%2F%20Determine%20the%20suffix%20to%20add%2C%20based%20on%20the%20last%20two%20digits%0A%20%20%20%20var%20suffix%20%3D%20%22th%22%0A%20%20%20%20var%20lastDigit%20%3D%20integer%20%25%2010%0A%20%20%20%20var%20lastTwoDigits%20%3D%20integer%20%25%20100%0A%20%20%20%20if%20%28lastDigit%20%3D%3D%3D%201%20%26%26%20lastTwoDigits%20!%3D%3D%2011%29%20%7B%0A%20%20%20%20%20%20%20%20suffix%20%3D%20%22st%22%0A%20%20%20%20%7D%0A%20%20%20%20else%20if%20%28lastDigit%20%3D%3D%3D%202%20%26%26%20lastTwoDigits%20!%3D%3D%2012%29%20%7B%0A%20%20%20%20%20%20%20%20suffix%20%3D%20%22nd%22%0A%20%20%20%20%7D%0A%20%20%20%20else%20if%20%28lastDigit%20%3D%3D%3D%203%20%26%26%20lastTwoDigits%20!%3D%3D%2013%29%20%7B%0A%20%20%20%20%20%20%20%20suffix%20%3D%20%22rd%22%0A%20%20%20%20%7D%0A%0A%20%20%20%20%2F%2F%20Return%20the%20number%20and%20suffix%0A%20%20%20%20return%20num.toString%28%29%20%2B%20suffix%0A%7D%0A)

__Listing 20-6__JavaScript: Function that adds a descriptive suffix to a number

1. `function addDescriptiveSuffixToNumber(num) {`
2. `// Convert the number to absolute value`
3. `var integer = Math.abs(num)`
5. `// Determine the suffix to add, based on the last two digits`
6. `var suffix = "th"`
7. `var lastDigit = integer % 10`
8. `var lastTwoDigits = integer % 100`
9. `if (lastDigit === 1 && lastTwoDigits !== 11) {`
10. `suffix = "st"`
11. `}`
12. `else if (lastDigit === 2 && lastTwoDigits !== 12) {`
13. `suffix = "nd"`
14. `}`
15. `else if (lastDigit === 3 && lastTwoDigits !== 13) {`
16. `suffix = "rd"`
17. `}`
19. `// Return the number and suffix`
20. `return num.toString() + suffix`
21. `}`

Listing 20-7 and Listing 20-8 show how to test the handlers in Listing 20-5 and Listing 20-6 by looping through a range of positive and negative numbers.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theTestResults%20to%20%22%22%0Arepeat%20with%20a%20from%20-10%20to%2010%0A%20%20%20%20set%20theTestResults%20to%20theTestResults%20%26%20addDescriptiveSuffixToNumber%28a%29%0A%20%20%20%20if%20a%20is%20less%20than%2010%20then%20set%20theTestResults%20to%20theTestResults%20%26%20%22%2C%20%22%0Aend%20repeat%0AtheTestResults)

__Listing 20-7__AppleScript: Testing a handler that adds a descriptive suffix to a number

1. `set theTestResults to ""`
2. `repeat with a from -10 to 10`
3. `set theTestResults to theTestResults & addDescriptiveSuffixToNumber(a)`
4. `if a is less than 10 then set theTestResults to theTestResults & ", "`
5. `end repeat`
6. `theTestResults`
7. `--> Result: "-10th, -9th, -8th, -7th, -6th, -5th, -4th, -3rd, -2nd, -1st, 0, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20testResults%20%3D%20%22%22%0Afor%20%28var%20i%20%3D%20-10%3B%20i%20%3C%3D%2010%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20testResults%20%2B%3D%20addDescriptiveSuffixToNumber%28i%29%0A%20%20%20%20if%20%28i%20%3C%2010%29%20%7B%0A%20%20%20%20%20%20%20%20testResults%20%2B%3D%20%22%2C%20%22%0A%20%20%20%20%7D%0A%7D%0AtestResults)

__Listing 20-8__JavaScript: Testing a function that adds a descriptive suffix to a number

1. `var testResults = ""`
2. `for (var i = -10; i <= 10; i++) {`
3. `testResults += addDescriptiveSuffixToNumber(i)`
4. `if (i < 10) {`
5. `testResults += ", "`
6. `}`
7. `}`
8. `testResults`
9. `// Result: "-10th, -9th, -8th, -7th, -6th, -5th, -4th, -3rd, -2nd, -1st, 0th, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th"`

Listing 20-9 and Listing 20-10 show how to call the handlers in Listing 20-5 and Listing 20-6 to identify positions of items in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20thePersonList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22Chris%22%2C%20%22David%22%7D%0Aset%20theListLength%20to%20length%20of%20thePersonList%0Arepeat%20with%20a%20from%201%20to%20theListLength%0A%20%20%20%20set%20theSuffixedNumber%20to%20addDescriptiveSuffixToNumber%28a%29%0A%20%20%20%20set%20thePerson%20to%20item%20a%20of%20thePersonList%0A%20%20%20%20display%20dialog%20%22The%20%22%20%26%20theSuffixedNumber%20%26%20%22%20person%20in%20list%20is%20%22%20%26%20thePerson%20%26%20%22.%22%0Aend%20repeat)

__Listing 20-9__AppleScript: Example script that calls a handler to identify the descriptive numeric position of items in a list

1. `set thePersonList to {"Sal", "Ben", "Chris", "David"}`
2. `set theListLength to length of thePersonList`
3. `repeat with a from 1 to theListLength`
4. `set theSuffixedNumber to addDescriptiveSuffixToNumber(a)`
5. `set thePerson to item a of thePersonList`
6. `display dialog "The " & theSuffixedNumber & " person in list is " & thePerson & "."`
7. `end repeat`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20personList%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22Chris%22%2C%20%22David%22%5D%0Avar%20listLength%20%3D%20personList.length%0Afor%20%28var%20i%20%3D%200%3B%20i%20%3C%20listLength%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20var%20suffixedNum%20%3D%20addDescriptiveSuffixToNumber%28i%20%2B%201%29%0A%20%20%20%20var%20person%20%3D%20personList%5Bi%5D%0A%20%20%20%20app.displayDialog%28%60The%20%24%7BsuffixedNum%7D%20person%20in%20list%20is%20%24%7Bperson%7D.%60%29%0A%7D)

__Listing 20-10__JavaScript: Example script that calls a function to identify the descriptive numeric position of items in a list

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `var personList = ["Sal", "Ben", "Chris", "David"]`
5. `var listLength = personList.length`
6. `for (var i = 0; i < listLength; i++) {`
7. `var suffixedNum = addDescriptiveSuffixToNumber(i + 1)`
8. `var person = personList[i]`
9. `` app.displayDialog(`The ${suffixedNum} person in list is ${person}.`) ``
10. `}`

### Adding Leading Zeros to a Number

The handlers in Listing 20-11 and Listing 20-12 convert a number to a string and prepends it with leading zeros until it reaches a certain length. They accept two parameters—the number to add leading zeros to and the maximum number of leading zeros to add. For example, if the maximum number of leading zeros is set to `2`, the results range from `001` to `999`. If the maximum number of leading zeros is `3`, the results range from `0001` to `9999`, and so on.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20addLeadingZerosToNumber%28theNumber%2C%20theMaxLeadingZeroCount%29%0A%20%20%20%20--%20Determine%20if%20the%20number%20is%20negative%0A%20%20%20%20set%20isNegative%20to%20theNumber%20is%20less%20than%200%0A%0A%20%20%20%20--%20Determine%20when%20the%20maximum%20number%20of%20digits%20will%20be%20reached%0A%20%20%20%20set%20theThreshold%20to%20%2810%20%5E%20theMaxLeadingZeroCount%29%20as%20integer%0A%0A%20%20%20%20--%20If%20the%20number%20is%20shorter%20than%20the%20maximum%20number%20of%20digits%0A%20%20%20%20if%20theNumber%20is%20less%20than%20theThreshold%20then%0A%20%20%20%20%20%20%20%20--%20If%20the%20number%20is%20negative%2C%20convert%20it%20to%20positive%0A%20%20%20%20%20%20%20%20if%20isNegative%20%3D%20true%20then%20set%20theNumber%20to%20-theNumber%0A%0A%20%20%20%20%20%20%20%20--%20Add%20the%20zeros%20to%20the%20number%0A%20%20%20%20%20%20%20%20set%20theLeadingZeros%20to%20%22%22%0A%20%20%20%20%20%20%20%20set%20theDigitCount%20to%20length%20of%20%28%28theNumber%20div%201%29%20as%20string%29%0A%20%20%20%20%20%20%20%20set%20theCharacterCount%20to%20%28theMaxLeadingZeroCount%20%2B%201%29%20-%20theDigitCount%0A%20%20%20%20%20%20%20%20repeat%20theCharacterCount%20times%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theLeadingZeros%20to%20%28theLeadingZeros%20%26%20%220%22%29%20as%20string%0A%20%20%20%20%20%20%20%20end%20repeat%0A%0A%20%20%20%20%20%20%20%20--%20Make%20the%20number%20negative%2C%20if%20it%20was%20previously%20negative%0A%20%20%20%20%20%20%20%20if%20isNegative%20%3D%20true%20then%20set%20theLeadingZeros%20to%20%22-%22%20%26%20theLeadingZeros%0A%0A%20%20%20%20%20%20%20%20--%20Return%20the%20prefixed%20number%0A%20%20%20%20%20%20%20%20return%20%28theLeadingZeros%20%26%20%28theNumber%20as%20text%29%29%20as%20string%0A%0A%20%20%20%20%20%20--%20If%20the%20number%20is%20greater%20than%20or%20equal%20to%20the%20maximum%20number%20of%20digits%0A%20%20%20%20else%0A%20%20%20%20%20%20%20%20--%20Return%20the%20original%20number%0A%20%20%20%20%20%20%20%20return%20theNumber%20as%20text%0A%20%20%20%20end%20if%0Aend%20addLeadingZerosToNumber)

__Listing 20-11__AppleScript: Handler that adds leading zeros to a number

1. `on addLeadingZerosToNumber(theNumber, theMaxLeadingZeroCount)`
2. `-- Determine if the number is negative`
3. `set isNegative to theNumber is less than 0`
5. `-- Determine when the maximum number of digits will be reached`
6. `set theThreshold to (10 ^ theMaxLeadingZeroCount) as integer`
8. `-- If the number is shorter than the maximum number of digits`
9. `if theNumber is less than theThreshold then`
10. `-- If the number is negative, convert it to positive`
11. `if isNegative = true then set theNumber to -theNumber`
13. `-- Add the zeros to the number`
14. `set theLeadingZeros to ""`
15. `set theDigitCount to length of ((theNumber div 1) as string)`
16. `set theCharacterCount to (theMaxLeadingZeroCount + 1) - theDigitCount`
17. `repeat theCharacterCount times`
18. `set theLeadingZeros to (theLeadingZeros & "0") as string`
19. `end repeat`
21. `-- Make the number negative, if it was previously negative`
22. `if isNegative = true then set theLeadingZeros to "-" & theLeadingZeros`
24. `-- Return the prefixed number`
25. `return (theLeadingZeros & (theNumber as text)) as string`
27. `-- If the number is greater than or equal to the maximum number of digits`
28. `else`
29. `-- Return the original number`
30. `return theNumber as text`
31. `end if`
32. `end addLeadingZerosToNumber`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20addLeadingZerosToNumber%28num%2C%20maxLeadingZeroCount%29%20%7B%0A%20%20%20%20var%20leadingZeros%20%3D%20%22%22%0A%0A%20%20%20%20%2F%2F%20Convert%20the%20number%20to%20absolute%20value%0A%20%20%20%20var%20absNum%20%3D%20Math.abs%28num%29%0A%0A%20%20%20%20%2F%2F%20Determine%20when%20the%20maximum%20number%20of%20digits%20will%20be%20reached%0A%20%20%20%20var%20threshold%20%3D%20Math.pow%2810%2C%20maxLeadingZeroCount%29%0A%0A%20%20%20%20%2F%2F%20If%20the%20number%20is%20shorter%20than%20the%20maximum%20number%20of%20digits%0A%20%20%20%20if%20%28absNum%20%3C%20threshold%29%20%7B%0A%20%20%20%20%20%20%20%20%2F%2F%20Prepare%20a%20leading%20zeros%20string%0A%20%20%20%20%20%20%20%20var%20digitCount%20%3D%20Math.trunc%28absNum%29.toString%28%29.length%0A%20%20%20%20%20%20%20%20var%20charCount%20%3D%20maxLeadingZeroCount%20%2B%201%20-%20digitCount%0A%20%20%20%20%20%20%20%20for%20%28var%20i%20%3D%200%20%3B%20i%20%3C%20charCount%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20leadingZeros%20%2B%3D%20%220%22%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20%2F%2F%20Add%20the%20zeros%20to%20the%20number%0A%20%20%20%20var%20result%20%3D%20%60%24%7BleadingZeros%7D%24%7BabsNum%7D%60%0A%0A%20%20%20%20%2F%2F%20Make%20the%20number%20negative%2C%20if%20it%20was%20previously%20negative%0A%20%20%20%20if%20%28num%20%3C%200%29%20%7B%0A%20%20%20%20%20%20%20%20result%20%3D%20%60-%24%7Bresult%7D%60%0A%20%20%20%20%7D%0A%20%20%20%20%2F%2F%20Return%20the%20prefixed%20number%0A%20%20%20%20return%20result%0A%7D%0A)

__Listing 20-12__JavaScript: Function that adds leading zeros to a number

1. `function addLeadingZerosToNumber(num, maxLeadingZeroCount) {`
2. `var leadingZeros = ""`
4. `// Convert the number to absolute value`
5. `var absNum = Math.abs(num)`
7. `// Determine when the maximum number of digits will be reached`
8. `var threshold = Math.pow(10, maxLeadingZeroCount)`
10. `// If the number is shorter than the maximum number of digits`
11. `if (absNum < threshold) {`
12. `// Prepare a leading zeros string`
13. `var digitCount = Math.trunc(absNum).toString().length`
14. `var charCount = maxLeadingZeroCount + 1 - digitCount`
15. `for (var i = 0 ; i < charCount; i++) {`
16. `leadingZeros += "0"`
17. `}`
18. `}`
20. `// Add the zeros to the number`
21. `` var result = `${leadingZeros}${absNum}` ``
23. `// Make the number negative, if it was previously negative`
24. `if (num < 0) {`
25. `` result = `-${result}` ``
26. `}`
27. `// Return the prefixed number`
28. `return result`
29. `}`

Listing 20-13 and Listing 20-14 show how to call the handlers in Listing 20-11 and Listing 20-12.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=addLeadingZerosToNumber%289%2C%203%29)

__Listing 20-13__AppleScript: Calling a handler to add leading zeros to a number

1. `addLeadingZerosToNumber(9, 3)`
2. `--> Result: "0009"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=addLeadingZerosToNumber%289%2C%203%29)

__Listing 20-14__JavaScript: Calling a function to add leading zeros to a number

1. `addLeadingZerosToNumber(9, 3)`
2. `// Result: "0009"`

### Comma-Delimiting a Number

The handlers Listing 20-15 and Listing 20-16 comma-delimit a numeric value and converts it to a string.

> [!NOTE]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20convertNumberToCommaDelimitedString%28theNumber%29%0A%20%20%20%20--%20Convert%20the%20number%20to%20a%20string%0A%20%20%20%20set%20theNumber%20to%20convertNumberToString%28theNumber%29%0A%0A%20%20%20%20--%20Determine%20the%20length%20of%20the%20number%0A%20%20%20%20set%20theNumberLength%20to%20length%20of%20theNumber%0A%0A%20%20%20%20--%20Reverse%20the%20number%20so%20a%20comma%20can%20be%20added%20every%203%20digits%0A%20%20%20%20set%20theNumber%20to%20%28reverse%20of%20every%20character%20of%20theNumber%29%20as%20string%0A%0A%20%20%20%20--%20Loop%20through%20the%20number%27s%20digits%2C%20add%20commas%2C%20and%20put%20the%20numbers%20back%20in%20the%20correct%20order%0A%20%20%20%20set%20theConvertedNumber%20to%20%22%22%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20theNumberLength%0A%20%20%20%20%20%20%20%20if%20a%20is%20theNumberLength%20or%20%28a%20mod%203%29%20is%20not%200%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theConvertedNumber%20to%20%28character%20a%20of%20theNumber%20%26%20theConvertedNumber%29%20as%20string%0A%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theConvertedNumber%20to%20%28%22%2C%22%20%26%20character%20a%20of%20theNumber%20%26%20theConvertedNumber%29%20as%20string%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%0A%20%20%20%20--%20Return%20the%20comma%20delimited%20number%0A%20%20%20%20return%20theConvertedNumber%0Aend%20convertNumberToCommaDelimitedString)

__Listing 20-15__AppleScript: Handler that comma-delimits a number

1. `on convertNumberToCommaDelimitedString(theNumber)`
2. `-- Convert the number to a string`
3. `set theNumber to convertNumberToString(theNumber)`
5. `-- Determine the length of the number`
6. `set theNumberLength to length of theNumber`
8. `-- Reverse the number so a comma can be added every 3 digits`
9. `set theNumber to (reverse of every character of theNumber) as string`
11. `-- Loop through the number's digits, add commas, and put the numbers back in the correct order`
12. `set theConvertedNumber to ""`
13. `repeat with a from 1 to theNumberLength`
14. `if a is theNumberLength or (a mod 3) is not 0 then`
15. `set theConvertedNumber to (character a of theNumber & theConvertedNumber) as string`
16. `else`
17. `set theConvertedNumber to ("," & character a of theNumber & theConvertedNumber) as string`
18. `end if`
19. `end repeat`
21. `-- Return the comma delimited number`
22. `return theConvertedNumber`
23. `end convertNumberToCommaDelimitedString`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20convertNumberToCommaDelimitedString%28num%29%20%7B%0A%20%20%20%20%2F%2F%20Convert%20the%20number%20to%20a%20string%0A%20%20%20%20var%20numString%20%3D%20num.toString%28%29%0A%20%20%20%20if%20%28numString.indexOf%28%22e%22%29%20!%3D%20-%201%29%20%7B%0A%20%20%20%20%20%20%20%20numString%20%3D%20convertNumberToString%28numString%29%0A%20%20%20%20%7D%0A%0A%20%20%20%20%2F%2F%20Reverse%20the%20number%20so%20a%20comma%20can%20be%20added%20every%203%20digits%0A%20%20%20%20numString%20%3D%20numString.split%28%22%22%29.reverse%28%29.join%28%22%22%29%0A%20%20%20%20var%20numStringWithCommas%20%3D%20%22%22%0A%0A%20%20%20%20%2F%2F%20Determine%20the%20length%20of%20the%20number%0A%20%20%20%20var%20numStringLength%20%3D%20numString.length%0A%0A%20%20%20%20%2F%2F%20Loop%20through%20the%20number%27s%20digits%2C%20add%20commas%2C%20and%20put%20the%20numbers%20back%20in%20the%20correct%20order%0A%20%20%20%20for%20%28var%20i%20%3D%200%3B%20i%20%3C%20numStringLength%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20var%20toPrepend%20%3D%20numString%5Bi%5D%0A%20%20%20%20%20%20%20%20if%20%28i%20!%3D%20numStringLength%20-%201%20%26%26%20%28%28i%20%2B%201%29%20%25%203%29%20%3D%3D%200%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20toPrepend%20%3D%20%22%2C%22%20%2B%20toPrepend%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20numStringWithCommas%20%3D%20toPrepend%20%2B%20numStringWithCommas%0A%20%20%20%20%7D%0A%0A%20%20%20%20%2F%2F%20Return%20the%20comma%20delimited%20number%0A%20%20%20%20return%20numStringWithCommas%0A%7D)

__Listing 20-16__JavaScript: Function that comma-delimits a number

1. `function convertNumberToCommaDelimitedString(num) {`
2. `// Convert the number to a string`
3. `var numString = num.toString()`
4. `if (numString.indexOf("e") != - 1) {`
5. `numString = convertNumberToString(numString)`
6. `}`
8. `// Reverse the number so a comma can be added every 3 digits`
9. `numString = numString.split("").reverse().join("")`
10. `var numStringWithCommas = ""`
12. `// Determine the length of the number`
13. `var numStringLength = numString.length`
15. `// Loop through the number's digits, add commas, and put the numbers back in the correct order`
16. `for (var i = 0; i < numStringLength; i++) {`
17. `var toPrepend = numString[i]`
18. `if (i != numStringLength - 1 && ((i + 1) % 3) == 0) {`
19. `toPrepend = "," + toPrepend`
20. `}`
21. `numStringWithCommas = toPrepend + numStringWithCommas`
22. `}`
24. `// Return the comma delimited number`
25. `return numStringWithCommas`
26. `}`

Listing 20-17 and Listing 20-18 shows how to call the handlers in Listing 20-15 and Listing 20-16.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=convertNumberToCommaDelimitedString%28872124243234%29)

__Listing 20-17__AppleScript: Calling a handler to comma-delimit a number

1. `convertNumberToCommaDelimitedString(872124243234)`
2. `--> Result: "872,124,243,234"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=convertNumberToCommaDelimitedString%28872124243234%29)

__Listing 20-18__JavaScript: Calling a function to comma-delimit a number

1. `convertNumberToCommaDelimitedString(872124243234)`
2. `// Result: "872,124,243,234"`

> [!NOTE]
> 

### Determining if a Number is an Odd Number

The handlers in Listing 20-28 and Listing 20-29 determine whether a whole number is even or odd. A returned value of `false` indicates the passed number is even; a returned value of `true` indicates the passed number is odd.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20isNumberOdd%28theNumber%29%0A%20%20%20%20if%20theNumber%20mod%202%20is%20not%200%20then%0A%20%20%20%20%20%20%20%20return%20true%0A%20%20%20%20else%0A%20%20%20%20%20%20%20%20return%20false%0A%20%20%20%20end%20if%0Aend%20isNumberOdd)

__Listing 20-28__AppleScript: Handler that determines whether a number is odd

1. `on isNumberOdd(theNumber)`
2. `if theNumber mod 2 is not 0 then`
3. `return true`
4. `else`
5. `return false`
6. `end if`
7. `end isNumberOdd`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20isNumberOdd%28num%29%20%7B%0A%20%20%20%20return%20num%20%25%202%20!%3D%3D%200%0A%7D%0A)

__Listing 20-29__JavaScript: Method that determines whether a number is odd

1. `function isNumberOdd(num) {`
2. `return num % 2 !== 0`
3. `}`

Listing 20-30 and Listing 20-31 show how to call the handlers in Listing 20-28 and Listing 20-29.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=isNumberOdd%283%29)

__Listing 20-30__AppleScript: Calling a handler to determine whether a number is odd

1. `isNumberOdd(3)`
2. `--> Result: true`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=isNumberOdd%283%29)

__Listing 20-31__JavaScript: Calling a method to determine whether a number is odd

1. `isNumberOdd(3)`
2. `// Result: true`

Listing 20-32 and Listing 20-33 show how to call the handlers in Listing 20-28 and Listing 20-29 by prompting the user to enter an even number.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=repeat%0A%20%20%20%20display%20dialog%20%22Enter%20an%20even%20integer%3A%22%20default%20answer%20%22%22%0A%20%20%20%20try%0A%20%20%20%20%20%20%20%20if%20text%20returned%20of%20result%20is%20not%20%22%22%20then%20set%20theNumberProvided%20to%20text%20returned%20of%20result%20as%20integer%0A%20%20%20%20%20%20%20%20if%20isNumberOdd%28theNumberProvided%29%20is%20false%20then%20exit%20repeat%0A%20%20%20%20end%20try%0Aend%20repeat)

__Listing 20-32__AppleScript: Example script that calls a handler to determine whether a user-entered number is odd

1. `repeat`
2. `display dialog "Enter an even integer:" default answer ""`
3. `try`
4. `if text returned of result is not "" then set theNumberProvided to text returned of result as integer`
5. `if isNumberOdd(theNumberProvided) is false then exit repeat`
6. `end try`
7. `end repeat`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Awhile%20%28true%29%20%7B%0A%20%20%20%20var%20result%20%3D%20app.displayDialog%28%22Enter%20an%20even%20integer%3A%22%2C%20%7BdefaultAnswer%3A%20%22%22%7D%29%0A%20%20%20%20var%20text%20%3D%20result.textReturned%0A%20%20%20%20if%20%28text%20!%3D%3D%20%22%22%29%20%7B%0A%20%20%20%20%20%20%20%20var%20num%20%3D%20Number%28text%29%0A%20%20%20%20%20%20%20%20if%20%28!isNumberOdd%28num%29%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%7D)

__Listing 20-33__JavaScript: Example script that calls a method to determine whether a user-entered number is odd

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `while (true) {`
5. `var result = app.displayDialog("Enter an even integer:", {defaultAnswer: ""})`
6. `var text = result.textReturned`
7. `if (text !== "") {`
8. `var num = Number(text)`
9. `if (!isNumberOdd(num)) {`
10. `break`
11. `}`
12. `}`
13. `}`

### Rounding and Truncating a Number

The handlers in Listing 20-34 and Listing 20-35 round and truncate a numeric value, and convert it to a string. Provide a numeric value and indicate a number of decimal places.

> [!NOTE]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20roundAndTruncateNumber%28theNumber%2C%20numberOfDecimalPlaces%29%0A%20%20%20%20if%20numberOfDecimalPlaces%20is%200%20then%0A%20%20%20%20%20%20%20%20set%20theNumber%20to%20theNumber%20%2B%200.5%0A%20%20%20%20%20%20%20%20return%20convertNumberToString%28theNumber%20div%201%29%0A%20%20%20%20end%20if%0A%0A%20%20%20%20set%20theRoundingValue%20to%20%225%22%0A%20%20%20%20repeat%20numberOfDecimalPlaces%20times%0A%20%20%20%20%20%20%20%20set%20theRoundingValue%20to%20%220%22%20%26%20theRoundingValue%0A%20%20%20%20end%20repeat%0A%20%20%20%20set%20theRoundingValue%20to%20%28%22.%22%20%26%20theRoundingValue%29%20as%20number%0A%0A%20%20%20%20set%20theNumber%20to%20theNumber%20%2B%20theRoundingValue%0A%0A%20%20%20%20set%20theModValue%20to%20%221%22%0A%20%20%20%20repeat%20numberOfDecimalPlaces%20-%201%20times%0A%20%20%20%20%20%20%20%20set%20theModValue%20to%20%220%22%20%26%20theModValue%0A%20%20%20%20end%20repeat%0A%20%20%20%20set%20theModValue%20to%20%28%22.%22%20%26%20theModValue%29%20as%20number%0A%0A%20%20%20%20set%20theSecondPart%20to%20%28theNumber%20mod%201%29%20div%20theModValue%0A%20%20%20%20if%20length%20of%20%28theSecondPart%20as%20text%29%20is%20less%20than%20numberOfDecimalPlaces%20then%0A%20%20%20%20%20%20%20%20repeat%20numberOfDecimalPlaces%20-%20%28the%20length%20of%20%28theSecondPart%20as%20text%29%29%20times%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theSecondPart%20to%20%28%220%22%20%26%20theSecondPart%29%20as%20string%0A%20%20%20%20%20%20%20%20end%20repeat%0A%20%20%20%20end%20if%0A%0A%20%20%20%20set%20theFirstPart%20to%20theNumber%20div%201%0A%20%20%20%20set%20theFirstPart%20to%20convertNumberToString%28theFirstPart%29%0A%20%20%20%20set%20theNumber%20to%20%28theFirstPart%20%26%20%22.%22%20%26%20theSecondPart%29%0A%0A%20%20%20%20return%20theNumber%0Aend%20roundAndTruncateNumber)

__Listing 20-34__AppleScript: Handler for rounding and truncating a number

1. `on roundAndTruncateNumber(theNumber, numberOfDecimalPlaces)`
2. `if numberOfDecimalPlaces is 0 then`
3. `set theNumber to theNumber + 0.5`
4. `return convertNumberToString(theNumber div 1)`
5. `end if`
7. `set theRoundingValue to "5"`
8. `repeat numberOfDecimalPlaces times`
9. `set theRoundingValue to "0" & theRoundingValue`
10. `end repeat`
11. `set theRoundingValue to ("." & theRoundingValue) as number`
13. `set theNumber to theNumber + theRoundingValue`
15. `set theModValue to "1"`
16. `repeat numberOfDecimalPlaces - 1 times`
17. `set theModValue to "0" & theModValue`
18. `end repeat`
19. `set theModValue to ("." & theModValue) as number`
21. `set theSecondPart to (theNumber mod 1) div theModValue`
22. `if length of (theSecondPart as text) is less than numberOfDecimalPlaces then`
23. `repeat numberOfDecimalPlaces - (the length of (theSecondPart as text)) times`
24. `set theSecondPart to ("0" & theSecondPart) as string`
25. `end repeat`
26. `end if`
28. `set theFirstPart to theNumber div 1`
29. `set theFirstPart to convertNumberToString(theFirstPart)`
30. `set theNumber to (theFirstPart & "." & theSecondPart)`
32. `return theNumber`
33. `end roundAndTruncateNumber`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20roundAndTruncateNumber%28num%2C%20numDecimalPlaces%29%20%7B%0A%20%20%20%20if%20%28numDecimalPlaces%20%3D%3D%3D%200%29%20%7B%0A%20%20%20%20%20%20%20%20num%20%3D%20num%20%2B%200.5%0A%20%20%20%20%20%20%20%20return%20convertNumberToString%28num%20%2F%201%29%0A%20%20%20%20%7D%0A%0A%20%20%20%20var%20roundingValue%20%3D%20%225%22%0A%20%20%20%20for%20%28var%20i%20%3D%200%3B%20i%20%3C%20numDecimalPlaces%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20roundingValue%20%3D%20%220%22%20%2B%20roundingValue%0A%20%20%20%20%7D%0A%0A%20%20%20%20roundingValue%20%3D%20Number%28%220.%22%20%2B%20roundingValue%29%0A%20%20%20%20num%20%2B%3D%20roundingValue%0A%0A%20%20%20%20var%20modValue%20%3D%20%221%22%0A%0A%20%20%20%20for%20%28var%20i%20%3D%200%3B%20i%20%3C%20numDecimalPlaces%20-%201%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20modValue%20%3D%20%220%22%20%2B%20modValue%0A%20%20%20%20%7D%0A%0A%20%20%20%20modValue%20%3D%20Number%28%220.%22%20%2B%20modValue%29%0A%0A%20%20%20%20var%20secondPart%20%3D%20Math.floor%28%28num%20%25%201%29%20%2F%20modValue%29%0A%20%20%20%20var%20secondPartStringLength%20%3D%20secondPart.toString%28%29.length%0A%0A%20%20%20%20if%20%28secondPartStringLength%20%3C%20numDecimalPlaces%29%20%7B%0A%0A%20%20%20%20%20%20%20%20var%20count%20%3D%20numDecimalPlaces%20-%20secondPartStringLength%0A%0A%20%20%20%20%20%20%20%20for%20%28var%20i%20%3D%200%3B%20i%20%3C%20count%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20secondPart%20%3D%20%220%22%20%2B%20secondPart%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%0A%20%20%20%20var%20firstPart%20%3D%20Math.floor%28num%29%0A%20%20%20%20firstPart%20%3D%20convertNumberToString%28firstPart%29%0A%0A%20%20%20%20return%20%60%24%7BfirstPart%7D.%24%7BsecondPart%7D%60%0A%7D)

__Listing 20-35__JavaScript: Function for rounding and truncating a number

1. `function roundAndTruncateNumber(num, numDecimalPlaces) {`
2. `if (numDecimalPlaces === 0) {`
3. `num = num + 0.5`
4. `return convertNumberToString(num / 1)`
5. `}`
7. `var roundingValue = "5"`
8. `for (var i = 0; i < numDecimalPlaces; i++) {`
9. `roundingValue = "0" + roundingValue`
10. `}`
12. `roundingValue = Number("0." + roundingValue)`
13. `num += roundingValue`
15. `var modValue = "1"`
17. `for (var i = 0; i < numDecimalPlaces - 1; i++) {`
18. `modValue = "0" + modValue`
19. `}`
21. `modValue = Number("0." + modValue)`
23. `var secondPart = Math.floor((num % 1) / modValue)`
24. `var secondPartStringLength = secondPart.toString().length`
26. `if (secondPartStringLength < numDecimalPlaces) {`
28. `var count = numDecimalPlaces - secondPartStringLength`
30. `for (var i = 0; i < count; i++) {`
31. `secondPart = "0" + secondPart`
32. `}`
33. `}`
35. `var firstPart = Math.floor(num)`
36. `firstPart = convertNumberToString(firstPart)`
38. `` return `${firstPart}.${secondPart}` ``
39. `}`

Listing 20-36 shows how to call the handler in Listing 20-34.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=roundAndTruncateNumber%281.04575%2C%203%29)

__Listing 20-36__AppleScript: Calling a handler to round and truncate a number

1. `roundAndTruncateNumber(1.04575, 3)`
2. `--> Result: "1.046"`

[Manipulating Text](ManipulateText.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmztfvjvomi)

[Manipulating Lists of Items](ManipulateListsofItems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnbyfvjvomi)
