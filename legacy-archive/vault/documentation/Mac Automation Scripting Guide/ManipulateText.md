---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ManipulateText.html
archived_at: '2026-07-15T07:45:50.007403Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Manipulating Text

Manipulating text is one of the most common tasks performed in scripts. AppleScript and JavaScript both possess some basic text manipulation functions and properties that allow you to concatenate text, get the length of a string, and more. Overall, JavaScript has a much wider-range of built-in language-level text manipulation functions. Custom scripting is usually required to manipulate text with AppleScript.

> [!NOTE]
> 

### Changing the Case of Text

The handlers in Listing 19-1 and Listing 19-2 convert text to uppercase or lowercase. To use these handlers, provide some source text and a case to apply—`upper` or `lower`.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20changeCaseOfText%28theText%2C%20theCaseToSwitchTo%29%0A%20%20%20%20if%20theCaseToSwitchTo%20contains%20%22lower%22%20then%0A%20%20%20%20%20%20%20%20set%20theComparisonCharacters%20to%20%22ABCDEFGHIJKLMNOPQRSTUVWXYZ%22%0A%20%20%20%20%20%20%20%20set%20theSourceCharacters%20to%20%22abcdefghijklmnopqrstuvwxyz%22%0A%20%20%20%20else%20if%20theCaseToSwitchTo%20contains%20%22upper%22%20then%0A%20%20%20%20%20%20%20%20set%20theComparisonCharacters%20to%20%22abcdefghijklmnopqrstuvwxyz%22%0A%20%20%20%20%20%20%20%20set%20theSourceCharacters%20to%20%22ABCDEFGHIJKLMNOPQRSTUVWXYZ%22%0A%20%20%20%20else%0A%20%20%20%20%20%20%20%20return%20theText%0A%20%20%20%20end%20if%0A%20%20%20%20set%20theAlteredText%20to%20%22%22%0A%20%20%20%20repeat%20with%20aCharacter%20in%20theText%0A%20%20%20%20%20%20%20%20set%20theOffset%20to%20offset%20of%20aCharacter%20in%20theComparisonCharacters%0A%20%20%20%20%20%20%20%20if%20theOffset%20is%20not%200%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theAlteredText%20to%20%28theAlteredText%20%26%20character%20theOffset%20of%20theSourceCharacters%29%20as%20string%0A%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theAlteredText%20to%20%28theAlteredText%20%26%20aCharacter%29%20as%20string%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20theAlteredText%0Aend%20changeCaseOfText)

__Listing 19-1__AppleScript: Handler that converts text to uppercase or lowercase

1. `on changeCaseOfText(theText, theCaseToSwitchTo)`
2. `if theCaseToSwitchTo contains "lower" then`
3. `set theComparisonCharacters to "ABCDEFGHIJKLMNOPQRSTUVWXYZ"`
4. `set theSourceCharacters to "abcdefghijklmnopqrstuvwxyz"`
5. `else if theCaseToSwitchTo contains "upper" then`
6. `set theComparisonCharacters to "abcdefghijklmnopqrstuvwxyz"`
7. `set theSourceCharacters to "ABCDEFGHIJKLMNOPQRSTUVWXYZ"`
8. `else`
9. `return theText`
10. `end if`
11. `set theAlteredText to ""`
12. `repeat with aCharacter in theText`
13. `set theOffset to offset of aCharacter in theComparisonCharacters`
14. `if theOffset is not 0 then`
15. `set theAlteredText to (theAlteredText & character theOffset of theSourceCharacters) as string`
16. `else`
17. `set theAlteredText to (theAlteredText & aCharacter) as string`
18. `end if`
19. `end repeat`
20. `return theAlteredText`
21. `end changeCaseOfText`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20changeCaseOfText%28text%2C%20caseToSwitchTo%29%20%7B%0A%20%20%20%20var%20alteredText%20%3D%20text%0A%20%20%20%20if%20%28caseToSwitchTo%20%3D%3D%3D%20%22lower%22%29%20%7B%0A%20%20%20%20%20%20%20%20alteredText%20%3D%20alteredText.toLowerCase%28%29%0A%20%20%20%20%7D%0A%20%20%20%20else%20if%20%28caseToSwitchTo%20%3D%3D%3D%20%22upper%22%29%20%7B%0A%20%20%20%20%20%20%20%20alteredText%20%3D%20alteredText.toUpperCase%28%29%0A%20%20%20%20%7D%0A%20%20%20%20return%20alteredText%0A%7D)

__Listing 19-2__JavaScript: Function that converts text to uppercase or lowercase

1. `function changeCaseOfText(text, caseToSwitchTo) {`
2. `var alteredText = text`
3. `if (caseToSwitchTo === "lower") {`
4. `alteredText = alteredText.toLowerCase()`
5. `}`
6. `else if (caseToSwitchTo === "upper") {`
7. `alteredText = alteredText.toUpperCase()`
8. `}`
9. `return alteredText`
10. `}`

Listing 19-3 and Listing 19-4 show how to call the handlers in Listing 19-1 and Listing 19-2 to convert text to uppercase.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=changeCaseOfText%28%22scripting%20is%20awesome!%22%2C%20%22upper%22%29)

__Listing 19-3__AppleScript: Calling a handler to convert text to uppercase

1. `changeCaseOfText("scripting is awesome!", "upper")`
2. `--> Result: "SCRIPTING IS AWESOME!"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=changeCaseOfText%28%22scripting%20is%20awesome!%22%2C%20%22upper%22%29)

__Listing 19-4__JavaScript: Calling a function to convert text to uppercase

1. `changeCaseOfText("scripting is awesome!", "upper")`
2. `// Result: "SCRIPTING IS AWESOME!"`

Listing 19-5 and Listing 19-6 show how to call the handlers in Listing 19-1 and Listing 19-2 to convert text to lowercase.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=changeCaseOfText%28%22DOING%20REPETITIVE%20WORK%20IS%20BORING%22%2C%20%22lower%22%29)

__Listing 19-5__AppleScript: Calling a handler to convert text to lowercase

1. `changeCaseOfText("DOING REPETITIVE WORK IS BORING", "lower")`
2. `--> Result: "doing repetitive work is boring"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=changeCaseOfText%28%22DOING%20REPETITIVE%20WORK%20IS%20BORING%22%2C%20%22lower%22%29)

__Listing 19-6__JavaScript: Calling a function to convert text to lowercase

1. `changeCaseOfText("DOING REPETITIVE WORK IS BORING", "lower")`
2. `// Result: "doing repetitive work is boring"`

> [!NOTE]
> 

### Finding and Replacing Text in a String

The handler in Listing 19-9 can be used to find and replace text in a string. To use it, provide some source text, a string to find, and a replacement string. This handler replaces any found instances of the specified search string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20findAndReplaceInText%28theText%2C%20theSearchString%2C%20theReplacementString%29%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20theSearchString%0A%20%20%20%20set%20theTextItems%20to%20every%20text%20item%20of%20theText%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20theReplacementString%0A%20%20%20%20set%20theText%20to%20theTextItems%20as%20string%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20%22%22%0A%20%20%20%20return%20theText%0Aend%20findAndReplaceInText)

__Listing 19-9__AppleScript: Handler that finds and replaces text in a string

1. `on findAndReplaceInText(theText, theSearchString, theReplacementString)`
2. `set AppleScript's text item delimiters to theSearchString`
3. `set theTextItems to every text item of theText`
4. `set AppleScript's text item delimiters to theReplacementString`
5. `set theText to theTextItems as string`
6. `set AppleScript's text item delimiters to ""`
7. `return theText`
8. `end findAndReplaceInText`

Listing 19-10 shows how to call the handler in Listing 19-9.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22On%20Tuesday%2C%20I%20told%20you%20to%20have%20the%20report%20ready%20by%20next%20Tuesday.%22%0Aset%20theText%20to%20findAndReplaceInText%28theText%2C%20%22Tuesday%22%2C%20%22Friday%22%29%0A)

__Listing 19-10__AppleScript: Calling a handler to find and replace text in a string

1. `set theText to "On Tuesday, I told you to have the report ready by next Tuesday."`
2. `set theText to findAndReplaceInText(theText, "Tuesday", "Friday")`
3. `--> Result: "On Friday, I told you to have the report ready by next Friday."`

In JavaScript, the `String` object’s `replace()` method is used to find and replace text in a string, as shown in Listing 19-11. Unlike the previous AppleScript example, this function replaces only the first occurrence of the found text.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%22On%20Tuesday%2C%20I%20told%20you%20to%20have%20the%20report%20ready%20by%20next%20Tuesday.%22%0Atext%20%3D%20text.replace%28%22Tuesday%22%2C%20%22Friday%22%29)

__Listing 19-11__JavaScript: Finding and replacing the first occurrence of text in a string

1. `var text = "On Tuesday, I told you to have the report ready by next Tuesday."`
2. `text = text.replace("Tuesday", "Friday")`
3. `// Result: "On Friday, I told you to have the report ready by next Tuesday."`

The `replace()` method can be combined with a regular expression to replace every occurrence of the found text, as shown in Listing 19-12.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%22On%20Tuesday%2C%20I%20told%20you%20to%20have%20the%20report%20ready%20by%20next%20Tuesday.%22%0Atext%20%3D%20text.replace%28%2FTuesday%2Fg%2C%20%22Friday%22%29%0A)

__Listing 19-12__JavaScript: Finding and replacing every occurrence of text in a string

1. `var text = "On Tuesday, I told you to have the report ready by next Tuesday."`
2. `text = text.replace(/Tuesday/g, "Friday")`
3. `// Result: "On Friday, I told you to have the report ready by next Friday."`

> [!NOTE]
> 

### Getting the Characters of a String

Listing 19-15 and Listing 19-16 show how to get a list of characters in a string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Acharacters%20of%20theText)

__Listing 19-15__AppleScript: Get the characters of a string

1. `set theText to "The quick brown fox jumps over a lazy dog."`
2. `characters of theText`
3. `--> Result: {"T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "s", " ", "o", "v", "e", "r", " ", "a", " ", "l", "a", "z", "y", " ", "d", "o", "g", "."}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Atext.split%28%22%22%29)

__Listing 19-16__JavaScript: Get the characters of a string

1. `var text = "The quick brown fox jumps over a lazy dog."`
2. `text.split("")`
3. `// Result: ["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "s", " ", "o", "v", "e", "r", " ", "a", " ", "l", "a", "z", "y", " ", "d", "o", "g", "."]`

### Getting the Length of String

Listing 19-17 and Listing 19-18 show how to get the length of—the number of characters in—a string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Alength%20of%20theText)

__Listing 19-17__AppleScript: Get the length of a string

1. `set theText to "The quick brown fox jumps over a lazy dog."`
2. `length of theText`
3. `--> Result: 42`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Atext.length)

__Listing 19-18__JavaScript: Get the length of a string

1. `var text = "The quick brown fox jumps over a lazy dog."`
2. `text.length`
3. `// Result: 42`

### Getting the Paragraphs of a String

Listing 19-19 and Listing 19-20 show how to get a list of paragraphs in a string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22*%20Sal%0A*%20Ben%0A*%20Chris%0A*%20David%22%0Aparagraphs%20of%20theText)

__Listing 19-19__AppleScript: Get the characters of a string

1. `set theText to "* Sal`
2. `* Ben`
3. `* Chris`
4. `* David"`
5. `paragraphs of theText`
6. `--> Result: {"* Sal", "* Ben", "* Chris", "* David"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%60*%20Sal%0A*%20Ben%0A*%20Chris%0A*%20David%60%0A%0Atext.split%28%22%5Cn%22%29)

__Listing 19-20__JavaScript: Get the characters of a string

1. `` var text = `* Sal ``
2. `* Ben`
3. `* Chris`
4. `` * David` ``
6. `text.split("\n")`
7. `// Result: ["* Sal", "* Ben", "* Chris", "* David"]`

### Getting the Position of Text in a String

To determine the position of text within a string in AppleScript, request its `offset`, as shown in Listing 19-21. This provides the character number where the first instance of the text begins.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Aoffset%20of%20%22quick%22%20in%20theText)

__Listing 19-21__AppleScript: Get the position of text in a string

1. `set theText to "The quick brown fox jumps over a lazy dog."`
2. `offset of "quick" in theText`
3. `--> Result: 5`

> [!NOTE]
> 

To determine the position of text within a string in JavaScript, call the `indexOf()` method of the text object, as shown in Listing 19-22.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Atext.indexOf%28%22quick%22%29)

__Listing 19-22__JavaScript: Get the position of text in a string

1. `var text = "The quick brown fox jumps over a lazy dog."`
2. `text.indexOf("quick")`
3. `// Result: 4`

> [!NOTE]
> 

### Splitting Text

The handler in Listing 19-23 splits text into a list, based on a specific delimiter.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20splitText%28theText%2C%20theDelimiter%29%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20theDelimiter%0A%20%20%20%20set%20theTextItems%20to%20every%20text%20item%20of%20theText%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20%22%22%0A%20%20%20%20return%20theTextItems%0Aend%20splitText)

__Listing 19-23__AppleScript: Handler that splits text

1. `on splitText(theText, theDelimiter)`
2. `set AppleScript's text item delimiters to theDelimiter`
3. `set theTextItems to every text item of theText`
4. `set AppleScript's text item delimiters to ""`
5. `return theTextItems`
6. `end splitText`

Listing 19-24 shows how to call the handler in Listing 19-23.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0AsplitText%28theText%2C%20space%29)

__Listing 19-24__AppleScript: Calling a handler to split text based on a delimiter

1. `set theText to "The quick brown fox jumps over a lazy dog."`
2. `splitText(theText, space)`
3. `--> Result: {"The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."}`

In JavaScript, the `String` object’s `split()` method is used to split text based on a delimiter, as shown in Listing 19-25.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%22The%20quick%20brown%20fox%20jumps%20over%20a%20lazy%20dog.%22%0Atext.split%28%22%20%22%29)

__Listing 19-25__JavaScript: Function that splits text

1. `var text = "The quick brown fox jumps over a lazy dog."`
2. `text.split(" ")`
3. `// Result: ["The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."]`

> [!NOTE]
> 

### Trimming Text

The handlers in Listing 19-26 and Listing 19-27 trim text from the beginning or end of a string. To use these examples, provide some source text, characters to trim, and a trim direction—`beginning` (trim from the beginning), `end` (trim from the end), or `both` (trim from both the beginning and end).

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20trimText%28theText%2C%20theCharactersToTrim%2C%20theTrimDirection%29%0A%20%20%20%20set%20theTrimLength%20to%20length%20of%20theCharactersToTrim%0A%20%20%20%20if%20theTrimDirection%20is%20in%20%7B%22beginning%22%2C%20%22both%22%7D%20then%0A%20%20%20%20%20%20%20%20repeat%20while%20theText%20begins%20with%20theCharactersToTrim%0A%20%20%20%20%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theText%20to%20characters%20%28theTrimLength%20%2B%201%29%20thru%20-1%20of%20theText%20as%20string%0A%20%20%20%20%20%20%20%20%20%20%20%20on%20error%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%20text%20contains%20nothing%20but%20trim%20characters%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%22%22%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20try%0A%20%20%20%20%20%20%20%20end%20repeat%0A%20%20%20%20end%20if%0A%20%20%20%20if%20theTrimDirection%20is%20in%20%7B%22end%22%2C%20%22both%22%7D%20then%0A%20%20%20%20%20%20%20%20repeat%20while%20theText%20ends%20with%20theCharactersToTrim%0A%20%20%20%20%20%20%20%20%20%20%20%20try%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theText%20to%20characters%201%20thru%20-%28theTrimLength%20%2B%201%29%20of%20theText%20as%20string%0A%20%20%20%20%20%20%20%20%20%20%20%20on%20error%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%20text%20contains%20nothing%20but%20trim%20characters%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%22%22%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20try%0A%20%20%20%20%20%20%20%20end%20repeat%0A%20%20%20%20end%20if%0A%20%20%20%20return%20theText%0Aend%20trimText)

__Listing 19-26__AppleScript: Handler that trims text

1. `on trimText(theText, theCharactersToTrim, theTrimDirection)`
2. `set theTrimLength to length of theCharactersToTrim`
3. `if theTrimDirection is in {"beginning", "both"} then`
4. `repeat while theText begins with theCharactersToTrim`
5. `try`
6. `set theText to characters (theTrimLength + 1) thru -1 of theText as string`
7. `on error`
8. `-- text contains nothing but trim characters`
9. `return ""`
10. `end try`
11. `end repeat`
12. `end if`
13. `if theTrimDirection is in {"end", "both"} then`
14. `repeat while theText ends with theCharactersToTrim`
15. `try`
16. `set theText to characters 1 thru -(theTrimLength + 1) of theText as string`
17. `on error`
18. `-- text contains nothing but trim characters`
19. `return ""`
20. `end try`
21. `end repeat`
22. `end if`
23. `return theText`
24. `end trimText`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20trimText%28text%2C%20charsToTrim%2C%20direction%29%20%7B%0A%20%20%20%20var%20result%20%3D%20text%0A%20%20%20%20var%20regexString%20%3D%20charsToTrim.replace%28%2F%5B%5C-%5C%5B%5C%5D%5C%2F%5C%7B%5C%7D%5C%28%5C%29%5C*%5C%2B%5C%3F%5C.%5C%5C%5C%5E%5C%24%5C%7C%5D%2Fg%2C%20%22%5C%5C%24%26%22%29%3B%0A%20%20%20%20if%20%28direction%20%3D%3D%3D%20%22beginning%22%20%7C%7C%20direction%20%3D%3D%3D%20%22both%22%29%20%7B%0A%20%20%20%20%20%20%20%20var%20regex%20%3D%20new%20RegExp%28%60%5E%28%3F%3A%24%7BregexString%7D%29*%60%29%0A%20%20%20%20%20%20%20%20result%20%3D%20result.replace%28regex%2C%20%22%22%29%0A%20%20%20%20%7D%0A%20%20%20%20if%20%28direction%20%3D%3D%3D%20%22end%22%20%7C%7C%20direction%20%3D%3D%3D%20%22both%22%29%20%7B%0A%20%20%20%20%20%20%20%20var%20regex%20%3D%20new%20RegExp%28%60%28%3F%3A%24%7BregexString%7D%29*%24%60%29%0A%20%20%20%20%20%20%20%20result%20%3D%20result.replace%28regex%2C%20%22%22%29%0A%20%20%20%20%7D%0A%20%20%20%20return%20result%0A%7D)

__Listing 19-27__JavaScript: Function that trims text

1. `function trimText(text, charsToTrim, direction) {`
2. `var result = text`
3. `var regexString = charsToTrim.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");`
4. `if (direction === "beginning" || direction === "both") {`
5. `` var regex = new RegExp(`^(?:${regexString})*`) ``
6. `result = result.replace(regex, "")`
7. `}`
8. `if (direction === "end" || direction === "both") {`
9. `` var regex = new RegExp(`(?:${regexString})*$`) ``
10. `result = result.replace(regex, "")`
11. `}`
12. `return result`
13. `}`

Listing 19-28 and Listing 19-29 show how to call the handlers in Listing 19-26 and Listing 19-27 to trim text from the beginning of a string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=trimText%28%22----1----%22%2C%20%22-%22%2C%20%22beginning%22%29)

__Listing 19-28__AppleScript: Calling a handler to trim text from the beginning of a string

1. `trimText("----1----", "-", "beginning")`
2. `--> Result: "1----"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=trimText%28%22----1----%22%2C%20%22-%22%2C%20%22beginning%22%29)

__Listing 19-29__JavaScript: Calling a function to trim text from the beginning of a string

1. `trimText("----1----", "-", "beginning")`
2. `// Result: "1----"`

Listing 19-30 and Listing 19-31 show how to call the handlers in Listing 19-26 and Listing 19-27 to trim text from the end of a string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=trimText%28%2212345.txt%22%2C%20%22.txt%22%2C%20%22end%22%29)

__Listing 19-30__AppleScript: Calling a handler to trim text from the end of a string

1. `trimText("12345.txt", ".txt", "end")`
2. `--> Result: "12345"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=trimText%28%2212345.txt%22%2C%20%22.txt%22%2C%20%22end%22%29)

__Listing 19-31__JavaScript: Calling a function to trim text from the end of a string

1. `trimText("12345.txt", ".txt", "end")`
2. `// Result: "12345"`

Listing 19-32 and Listing 19-33 show how to call the handlers in Listing 19-26 and Listing 19-27 to trim text from the beginning and end of a string.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=trimText%28%22*-*-Ben*-*-%22%2C%20%22*-%22%2C%20%22both%22%29)

__Listing 19-32__AppleScript: Calling a handler to trim text from the beginning and end of a string

1. `trimText("*-*-Ben*-*-", "*-", "both")`
2. `--> Result: "Ben"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=trimText%28%22*-*-Ben*-*-%22%2C%20%22*-%22%2C%20%22both%22%29)

__Listing 19-33__JavaScript: Calling a function to trim text from the beginning and end of a string

1. `trimText("*-*-Ben*-*-", "*-", "both")`
2. `// Result: "Ben"`

> [!NOTE]
> 

### Trimming Paragraphs of Text

The handlers in Listing 19-36 and Listing 19-37 remove unwanted characters from multiple paragraphs.

> [!NOTE]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20trimParagraphsOfText%28theText%2C%20theCharactersToTrim%2C%20theTrimDirection%29%0A%20%20%20%20set%20theParagraphs%20to%20every%20paragraph%20of%20theText%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20paragraphs%20of%20theText%0A%20%20%20%20%20%20%20%20set%20theCurrentParagraph%20to%20item%20a%20of%20theParagraphs%0A%20%20%20%20%20%20%20%20set%20item%20a%20of%20theParagraphs%20to%20trimText%28theCurrentParagraph%2C%20theCharactersToTrim%2C%20theTrimDirection%29%0A%20%20%20%20end%20repeat%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20return%0A%20%20%20%20set%20theText%20to%20theParagraphs%20as%20string%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20%22%22%0A%20%20%20%20return%20theText%0Aend%20trimParagraphsOfText)

__Listing 19-36__AppleScript: Handler that trims text on multiple paragraphs

1. `on trimParagraphsOfText(theText, theCharactersToTrim, theTrimDirection)`
2. `set theParagraphs to every paragraph of theText`
3. `repeat with a from 1 to count of paragraphs of theText`
4. `set theCurrentParagraph to item a of theParagraphs`
5. `set item a of theParagraphs to trimText(theCurrentParagraph, theCharactersToTrim, theTrimDirection)`
6. `end repeat`
7. `set AppleScript's text item delimiters to return`
8. `set theText to theParagraphs as string`
9. `set AppleScript's text item delimiters to ""`
10. `return theText`
11. `end trimParagraphsOfText`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20trimParagraphsOfText%28text%2C%20charsToTrim%2C%20direction%29%20%7B%0A%20%20%20%20var%20paragraphs%20%3D%20text.split%28%22%5Cn%22%29%0A%20%20%20%20for%20%28var%20i%20%3D%200%3B%20i%20%3C%20paragraphs.length%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20var%20currentParagraph%20%3D%20paragraphs%5Bi%5D%0A%20%20%20%20%20%20%20%20paragraphs%5Bi%5D%20%3D%20trimText%28currentParagraph%2C%20charsToTrim%2C%20direction%29%0A%20%20%20%20%7D%0A%20%20%20%20return%20paragraphs.join%28%22%5Cn%22%29%0A%7D)

__Listing 19-37__JavaScript: Function that trims text on multiple paragraphs

1. `function trimParagraphsOfText(text, charsToTrim, direction) {`
2. `var paragraphs = text.split("\n")`
3. `for (var i = 0; i < paragraphs.length; i++) {`
4. `var currentParagraph = paragraphs[i]`
5. `paragraphs[i] = trimText(currentParagraph, charsToTrim, direction)`
6. `}`
7. `return paragraphs.join("\n")`
8. `}`

Listing 19-38 and Listing 19-39 show how to call the handlers in Listing 19-36 and Listing 19-37.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theText%20to%20%22*%20Sal%0A*%20Ben%0A*%20Chris%0A*%20David%22%0AtrimParagraphsOfText%28theText%2C%20%22*%20%22%2C%20%22beginning%22%29%0A)

__Listing 19-38__AppleScript: Calling a handler to trim text from multiple paragraphs

1. `set theText to "* Sal`
2. `* Ben`
3. `* Chris`
4. `* David"`
5. `trimParagraphsOfText(theText, "* ", "beginning")`
6. `--> Result:`
7. `(*`
8. `"Sal`
9. `Ben`
10. `Chris`
11. `David"`
12. `*)`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20text%20%3D%20%60*%20Sal%0A*%20Ben%0A*%20Chris%0A*%20David%60%0AtrimParagraphsOfText%28text%2C%20%22*%20%22%2C%20%22beginning%22%29%0A)

__Listing 19-39__JavaScript: Calling a function to trim text from multiple paragraphs

1. `` var text = `* Sal ``
2. `* Ben`
3. `* Chris`
4. `` * David` ``
5. `trimParagraphsOfText(text, "* ", "beginning")`
6. `// Result: "Sal\nBen\nChris\nDavid"`

> [!NOTE]
> 

[Watching Folders](WatchFolders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmzzfvjvomi)

[Manipulating Numbers](ManipulateNumbers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnbxfvjvomi)
