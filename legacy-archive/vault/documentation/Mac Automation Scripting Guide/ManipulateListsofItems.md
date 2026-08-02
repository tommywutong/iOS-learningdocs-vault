---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ManipulateListsofItems.html
archived_at: '2026-07-15T07:45:49.010155Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Manipulating Lists of Items

In scripting, a list—typically referred to as an array in JavaScript—is a an ordered collection of values that’s stored in a single object. A script can loop through the items of a list in order to process the items individually. There are many other tasks scripts commonly performed with lists, such as joining and sorting, which usually require custom scripting.

> [!NOTE]
> 

### Looping through a List

Listing 21-1 and Listing 21-2 show how to incrementally loop through a list. In these examples, a variable—`a` in AppleScript and `i` in JavaScript—represents an integer value from `1` through the number of items in the list. Each loop causes this variable value to increase, and you can use the increment variable to target a specific list item.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0Arepeat%20with%20a%20from%201%20to%20length%20of%20theList%0A%20%20%20%20set%20theCurrentListItem%20to%20item%20a%20of%20theList%0A%20%20%20%20--%20Process%20the%20current%20list%20item%0A%20%20%20%20display%20dialog%20theCurrentListItem%20%26%20%22%20is%20item%20%22%20%26%20a%20%26%20%22%20in%20the%20list.%22%0Aend%20repeat)

__Listing 21-1__AppleScript: Incrementally looping through items in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `repeat with a from 1 to length of theList`
3. `set theCurrentListItem to item a of theList`
4. `-- Process the current list item`
5. `display dialog theCurrentListItem & " is item " & a & " in the list."`
6. `end repeat`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Avar%20arrayLength%20%3D%20array.length%0A%0Afor%20%28var%20i%20%3D%200%3B%20i%20%3C%20arrayLength%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20var%20currentArrayItem%20%3D%20array%5Bi%5D%0A%20%20%20%20%2F%2F%20Process%20the%20current%20array%20item%0A%20%20%20%20app.displayDialog%28%60%24%7BcurrentArrayItem%7D%20is%20item%20%24%7Bi%20%2B%201%7D%20in%20the%20array.%60%29%0A%7D)

__Listing 21-2__JavaScript: Incrementally looping through items in an array

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `var array = ["Sal", "Ben", "David", "Chris"]`
5. `var arrayLength = array.length`
7. `for (var i = 0; i < arrayLength; i++) {`
8. `var currentArrayItem = array[i]`
9. `// Process the current array item`
10. `` app.displayDialog(`${currentArrayItem} is item ${i + 1} in the array.`) ``
11. `}`

A script can also loop through a list of items more directly by dynamically assigning a list item to a variable. In Listing 21-3 and Listing 21-4, a variable—`theCurrentListItem` in AppleScript and `currentArrayItem` in JavaScript—represents the item matching the current loop.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0Arepeat%20with%20theCurrentListItem%20in%20theList%0A%20%20%20%20--%20Process%20the%20current%20list%20item%0A%20%20%20%20display%20dialog%20theCurrentListItem%20%26%20%22%20is%20an%20item%20in%20the%20list.%22%0Aend%20repeat)

__Listing 21-3__AppleScript: Directly looping through items in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `repeat with theCurrentListItem in theList`
3. `-- Process the current list item`
4. `display dialog theCurrentListItem & " is an item in the list."`
5. `end repeat`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Avar%20arrayLength%20%3D%20array.length%0Afor%20%28var%20currentArrayItem%20of%20array%29%20%7B%0A%20%20%20%20%2F%2F%20Process%20the%20current%20array%20item%0A%20%20%20%20app.displayDialog%28%60%24%7BcurrentArrayItem%7D%20is%20an%20item%20in%20the%20array.%60%29%0A%7D)

__Listing 21-4__JavaScript: Directly looping through items in an array

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `var array = ["Sal", "Ben", "David", "Chris"]`
5. `var arrayLength = array.length`
6. `for (var currentArrayItem of array) {`
7. `// Process the current array item`
8. `` app.displayDialog(`${currentArrayItem} is an item in the array.`) ``
9. `}`

> [!NOTE]
> 

### Converting a List to a String

The handler in Listing 21-5 joins a list of strings together in AppleScript, separating them by a specific delimiter.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20convertListToString%28theList%2C%20theDelimiter%29%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20theDelimiter%0A%20%20%20%20set%20theString%20to%20theList%20as%20string%0A%20%20%20%20set%20AppleScript%27s%20text%20item%20delimiters%20to%20%22%22%0A%20%20%20%20return%20theString%0Aend%20convertListToString)

__Listing 21-5__AppleScript: Handler that converts a list of strings into a single string

1. `on convertListToString(theList, theDelimiter)`
2. `set AppleScript's text item delimiters to theDelimiter`
3. `set theString to theList as string`
4. `set AppleScript's text item delimiters to ""`
5. `return theString`
6. `end convertListToString`

Listing 21-6 shows how to call the handler in Listing 21-5.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22The%22%2C%20%22quick%22%2C%20%22brown%22%2C%20%22fox%22%2C%20%22jumps%22%2C%20%22over%22%2C%20%22a%22%2C%20%22lazy%22%2C%20%22dog.%22%7D%0AconvertListToString%28theList%2C%20space%29)

__Listing 21-6__AppleScript: Calling a handler to convert a list of strings into a single string

1. `set theList to {"The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."}`
2. `convertListToString(theList, space)`
3. `--> Result: "The quick brown fox jumps over a lazy dog."`

In JavaScript, custom scripting isn’t required to perform this operation. The `Array` object has a `join()` method, which can be called to merge a list of items together, as shown in Listing 21-7.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22The%22%2C%20%22quick%22%2C%20%22brown%22%2C%20%22fox%22%2C%20%22jumps%22%2C%20%22over%22%2C%20%22a%22%2C%20%22lazy%22%2C%20%22dog.%22%5D%0Avar%20array.join%28%22%20%22%29)

__Listing 21-7__JavaScript: Calling a function to convert an array of strings into a single string

1. `var array = ["The", "quick", "brown", "fox", "jumps", "over", "a", "lazy", "dog."]`
2. `var array.join(" ")`
3. `// Result: "The quick brown fox jumps over a lazy dog."`

> [!NOTE]
> 

### Counting the Items in a List

Listing 21-10 and Listing 21-11 show how to get the number of items in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Apple%20Watch%22%2C%20%22iMac%22%2C%20%22iPhone%22%2C%20%22MacBook%20Pro%22%7D%0Alength%20of%20theList)

__Listing 21-10__AppleScript: Get the count of the items in a list

1. `set theList to {"Apple Watch", "iMac", "iPhone", "MacBook Pro"}`
2. `length of theList`
3. `--> Result: 4`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Apple%20Watch%22%2C%20%22iMac%22%2C%20%22iPhone%22%2C%20%22MacBook%20Pro%22%5D%0Aarray.length)

__Listing 21-11__JavaScript: Get the count of the items in an array

1. `var array = ["Apple Watch", "iMac", "iPhone", "MacBook Pro"]`
2. `array.length`
3. `// Result: 4`

### Counting the Occurrences of an Item in a List

The handlers in Listing 21-12 and Listing 21-13 count how many times an item appears in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20countInstancesOfItemInList%28theList%2C%20theItem%29%0A%20%20%20%20set%20theCount%20to%200%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theList%0A%20%20%20%20%20%20%20%20if%20item%20a%20of%20theList%20is%20theItem%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theCount%20to%20theCount%20%2B%201%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20theCount%0Aend%20countInstancesOfItemInList)

__Listing 21-12__AppleScript: Handler that counts the number of times an item appears in a list

1. `on countInstancesOfItemInList(theList, theItem)`
2. `set theCount to 0`
3. `repeat with a from 1 to count of theList`
4. `if item a of theList is theItem then`
5. `set theCount to theCount + 1`
6. `end if`
7. `end repeat`
8. `return theCount`
9. `end countInstancesOfItemInList`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20countInstancesOfItemInArray%28array%2C%20item%29%20%7B%0A%20%20%20%20var%20count%20%3D%200%0A%20%20%20%20for%20%28var%20element%20of%20array%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28element%20%3D%3D%3D%20item%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20count%2B%2B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20return%20count%0A%7D)

__Listing 21-13__JavaScript: Function that counts the number of times an item appears in an array

1. `function countInstancesOfItemInArray(array, item) {`
2. `var count = 0`
3. `for (var element of array) {`
4. `if (element === item) {`
5. `count++`
6. `}`
7. `}`
8. `return count`
9. `}`

Listing 21-14 and Listing 21-15 show how to call the handlers in Listing 21-12 and Listing 21-13.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Jen%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%7D%0AcountInstancesOfItemInList%28theList%2C%20%22Jen%22%29)

__Listing 21-14__AppleScript: Calling a handler to count the number of times an item appears in a list

1. `set theList to {"Sal", "Jen", "Ben", "David", "Chris", "Jen"}`
2. `countInstancesOfItemInList(theList, "Jen")`
3. `--> Result: 2`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Jen%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%5D%0AcountInstancesOfItemInArray%28array%2C%20%22Jen%22%29)

__Listing 21-15__JavaScript: Calling a function to count the number of times an item appears in an array

1. `var array = ["Sal", "Jen", "Ben", "David", "Chris", "Jen"]`
2. `countInstancesOfItemInArray(array, "Jen")`
3. `// Result: 2`

### Determining if a List Contains a Specific Item

Listing 21-16 and Listing 21-17 return a `true` or `false` value, indicating the presence of an item in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AtheList%20contains%20%22Lizzie%22)

__Listing 21-16__AppleScript: Check for the existence of an item in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `theList contains "Lizzie"`
3. `--> false`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray.includes%28%22Lizzie%22%29)

__Listing 21-17__JavaScript: Check for the existence of an item in an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array.includes("Lizzie")`
3. `// Result: false`

Listing 21-18 and Listing 21-19 demonstrate how to add an item to a list only if the list doesn’t already contain the item.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0Aif%20theList%20does%20not%20contain%20%22Jen%22%20then%0A%20%20%20%20set%20end%20of%20theList%20to%20%22Jen%22%0Aend%20if%0Areturn%20theList)

__Listing 21-18__AppleScript: Add an item to a list only if the list doesn’t contain the item

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `if theList does not contain "Jen" then`
3. `set end of theList to "Jen"`
4. `end if`
5. `return theList`
6. `--> Result: {"Sal", "Ben", "David", "Chris", "Jen"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aif%20%28!array.includes%28%22Jen%22%29%29%20%7B%0A%20%20%20%20array.push%28%22Jen%22%29%0A%7D%0Aarray)

__Listing 21-19__JavaScript: Add an item to an array only if the array doesn’t contain the item

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `if (!array.includes("Jen")) {`
3. `array.push("Jen")`
4. `}`
5. `array`
6. `// Result: ["Sal", "Ben", "David", "Chris", "Jen"]`

### Determining the Position of an Item in a List

The handler in Listing 21-20 determines the position of an item the first time it appears in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20getPositionOfItemInList%28theItem%2C%20theList%29%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theList%0A%20%20%20%20%20%20%20%20if%20item%20a%20of%20theList%20is%20theItem%20then%20return%20a%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%200%0Aend%20getPositionOfItemInList)

__Listing 21-20__AppleScript: Handler that determines the position of an item in a list

1. `on getPositionOfItemInList(theItem, theList)`
2. `repeat with a from 1 to count of theList`
3. `if item a of theList is theItem then return a`
4. `end repeat`
5. `return 0`
6. `end getPositionOfItemInList`

Listing 21-21 shows how to call the handler in Listing 21-20. In AppleScript, list item positions start at `1`—the first item in a list has a position of `1`.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%2C%20%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%7D%0AgetPositionOfItemInList%28%22Maddie%22%2C%20theList%29)

__Listing 21-21__AppleScript: Calling a handler to determine the position of an item in a list

1. `set theList to {"Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie"}`
2. `getPositionOfItemInList("Maddie", theList)`
3. `--> Result: 7`

In JavaScript, the `indexOf()` method of the `Array` object can be called to determine the position of an item in an array, as shown in Listing 21-22. In JavaScript, array item positions start at `0`—the first item in an array has an index of `0`.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%2C%20%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%5D%0Aarray.indexOf%28%22Maddie%22%29)

__Listing 21-22__JavaScript: Determine the position of an item in an array

1. `var array = ["Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie]`
2. `array.indexOf("Maddie")`
3. `// Result: 6`

The `getPositionOfItemInList()` AppleScript handler and `indexOf()` JavaScript method can be used to cross-reference data between corresponding lists. In Listing 21-23 and Listing 21-24, a person is located in a list by name. Next, the person’s phone extension is located in a corresponding list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theNames%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%2C%20%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%7D%0Aset%20theExtensions%20to%20%7B%22x1111%22%2C%20%22x2222%22%2C%20%22x3333%22%2C%20%22x4444%22%2C%20%22x5555%22%2C%20%22x6666%22%2C%20%22x7777%22%2C%20%22x8888%22%7D%7D%0Aset%20thePerson%20to%20choose%20from%20list%20theNames%20with%20prompt%20%22Choose%20a%20person%3A%22%0Aif%20thePerson%20is%20false%20then%20error%20number%20-128%0Aset%20theExtension%20to%20item%20%28getPositionOfItemInList%28%28thePerson%20as%20string%29%2C%20theNames%29%29%20of%20theExtensions%0Adisplay%20dialog%20%22The%20phone%20extension%20for%20%22%20%26%20thePerson%20%26%20%22%20is%20%22%20%26%20theExtension%20%26%20%22.%22)

__Listing 21-23__AppleScript: Using cross-referencing to locate an item in a list based on the position of an item in another list

1. `set theNames to {"Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie"}`
2. `set theExtensions to {"x1111", "x2222", "x3333", "x4444", "x5555", "x6666", "x7777", "x8888"}}`
3. `set thePerson to choose from list theNames with prompt "Choose a person:"`
4. `if thePerson is false then error number -128`
5. `set theExtension to item (getPositionOfItemInList((thePerson as string), theNames)) of theExtensions`
6. `display dialog "The phone extension for " & thePerson & " is " & theExtension & "."`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20names%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%2C%20%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%5D%0Avar%20extensions%20%3D%20%5B%22x1111%22%2C%20%22x2222%22%2C%20%22x3333%22%2C%20%22x4444%22%2C%20%22x5555%22%2C%20%22x6666%22%2C%20%22x7777%22%2C%20%22x8888%22%5D%0Avar%20people%20%3D%20app.chooseFromList%28names%2C%20%7BwithPrompt%3A%20%22Choose%20a%20person%3A%22%7D%29%0Aif%20%28!people%29%20%7B%0A%20%20%20%20throw%20new%20Error%28-128%29%0A%7D%0Avar%20person%20%3D%20people%5B0%5D%0Avar%20index%20%3D%20names.indexOf%28person%29%0Aconsole.log%28index%29%0Avar%20extension%20%3D%20extensions%5Bindex%5D%0Aapp.displayDialog%28%60The%20phone%20extension%20for%20%24%7Bperson%7D%20is%20%24%7Bextension%7D.%60%29)

__Listing 21-24__JavaScript: Using cross-referencing to locate an item in an array based on the position of an item in another array

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `var names = ["Sal", "Ben", "David", "Chris", "Jen", "Lizzie", "Maddie", "Lillie"]`
5. `var extensions = ["x1111", "x2222", "x3333", "x4444", "x5555", "x6666", "x7777", "x8888"]`
6. `var people = app.chooseFromList(names, {withPrompt: "Choose a person:"})`
7. `if (!people) {`
8. `throw new Error(-128)`
9. `}`
10. `var person = people[0]`
11. `var index = names.indexOf(person)`
12. `console.log(index)`
13. `var extension = extensions[index]`
14. `` app.displayDialog(`The phone extension for ${person} is ${extension}.`) ``

### Determining Multiple Positions of an Item in a List

The handlers in Listing 21-25 and Listing 21-26 determine every position of an item in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20getPositionsOfItemInList%28theItem%2C%20theList%2C%20listFirstPositionOnly%29%0A%20%20%20%20set%20thePositions%20to%20%7B%7D%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20length%20of%20theList%0A%20%20%20%20%20%20%20%20if%20item%20a%20of%20theList%20is%20theItem%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20listFirstPositionOnly%20%3D%20true%20then%20return%20a%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20end%20of%20thePositions%20to%20a%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%20%20%20%20if%20listFirstPositionOnly%20is%20true%20and%20thePositions%20%3D%20%7B%7D%20then%20return%200%0A%20%20%20%20return%20thePositions%0Aend%20getPositionsOfItemInList)

__Listing 21-25__AppleScript: Handler that determines every position of an item in a list

1. `on getPositionsOfItemInList(theItem, theList, listFirstPositionOnly)`
2. `set thePositions to {}`
3. `repeat with a from 1 to length of theList`
4. `if item a of theList is theItem then`
5. `if listFirstPositionOnly = true then return a`
6. `set end of thePositions to a`
7. `end if`
8. `end repeat`
9. `if listFirstPositionOnly is true and thePositions = {} then return 0`
10. `return thePositions`
11. `end getPositionsOfItemInList`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20getPositionsOfItemInArray%28item%2C%20array%2C%20firstPositionOnly%29%20%7B%0A%20%20%20%20if%20%28firstPositionOnly%29%20%7B%0A%20%20%20%20%20%20%20%20return%20array.indexOf%28item%29%0A%20%20%20%20%7D%0A%20%20%20%20var%20indexes%20%3D%20%5B%5D%0A%20%20%20%20for%20%28var%20index%20%3D%200%3B%20index%20%3C%20array.length%3B%20index%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20var%20element%20%3D%20array%5Bindex%5D%0A%20%20%20%20%20%20%20%20if%20%28element%20%3D%3D%3D%20item%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20indexes.push%28index%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20return%20indexes%0A%7D%0A)

__Listing 21-26__JavaScript: Function that determines every position of an item in an array

1. `function getPositionsOfItemInArray(item, array, firstPositionOnly) {`
2. `if (firstPositionOnly) {`
3. `return array.indexOf(item)`
4. `}`
5. `var indexes = []`
6. `for (var index = 0; index < array.length; index++) {`
7. `var element = array[index]`
8. `if (element === item) {`
9. `indexes.push(index)`
10. `}`
11. `}`
12. `return indexes`
13. `}`

Listing 21-27 and Listing 21-28 show how to call the handlers in Listing 21-25 and Listing 21-26.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22Jen%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Jen%22%2C%20%22Lillie%22%7D%0AgetPositionsOfItemInList%28%22Jen%22%2C%20theList%2C%20false%29)

__Listing 21-27__AppleScript: Calling a handler to determine every position of an item in a list

1. `set theList to {"Sal", "Ben", "Jen", "David", "Chris", "Lizzie", "Maddie", "Jen", "Lillie"}`
2. `getPositionsOfItemInList("Jen", theList, false)`
3. `--> Result: {3, 8}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22Jen%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Jen%22%2C%20%22Lillie%22%5D%0AgetPositionsOfItemInArray%28%22Jen%22%2C%20array%2C%20false%29)

__Listing 21-28__JavaScript: Calling a function to determine every position of an item in an array

1. `var array = ["Sal", "Ben", "Jen", "David", "Chris", "Lizzie", "Maddie", "Jen", "Lillie"]`
2. `getPositionsOfItemInArray("Jen", array, false)`
3. `// Result: [2, 7]`

### Finding the Highest Numeric Value in a List

The handlers in Listing 21-29 and Listing 21-30 determine the highest numeric value in a list of items. The passed list can contain non-numeric data as well as lists within lists.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20getHighestNumberInList%28theList%29%0A%20%20%20%20set%20theHighestNumber%20to%20false%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theList%0A%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20item%20a%20of%20theList%0A%20%20%20%20%20%20%20%20set%20theClass%20to%20class%20of%20theCurrentItem%0A%20%20%20%20%20%20%20%20if%20theClass%20is%20in%20%7Binteger%2C%20real%7D%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20theHighestNumber%20is%20%22%22%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theHighestNumber%20to%20theCurrentItem%0A%20%20%20%20%20%20%20%20%20%20%20%20else%20if%20theCurrentItem%20is%20greater%20than%20theHighestNumber%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theHighestNumber%20to%20item%20a%20of%20theList%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20else%20if%20theClass%20is%20list%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theHighValue%20to%20getHighestNumberInList%28theCurrentItem%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20theHighValue%20is%20greater%20than%20theHighestNumber%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theHighestNumber%20to%20theHighValue%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20theHighestNumber%0Aend%20getHighestNumberInList)

__Listing 21-29__AppleScript: Handler that determines the highest numeric value in a list of items

1. `on getHighestNumberInList(theList)`
2. `set theHighestNumber to false`
3. `repeat with a from 1 to count of theList`
4. `set theCurrentItem to item a of theList`
5. `set theClass to class of theCurrentItem`
6. `if theClass is in {integer, real} then`
7. `if theHighestNumber is "" then`
8. `set theHighestNumber to theCurrentItem`
9. `else if theCurrentItem is greater than theHighestNumber then`
10. `set theHighestNumber to item a of theList`
11. `end if`
12. `else if theClass is list then`
13. `set theHighValue to getHighestNumberInList(theCurrentItem)`
14. `if theHighValue is greater than theHighestNumber then`
15. `set theHighestNumber to theHighValue`
16. `end if`
17. `end if`
18. `end repeat`
19. `return theHighestNumber`
20. `end getHighestNumberInList`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20getHighestNumberInList%28list%29%20%7B%0A%20%20%20%20var%20highestNumber%20%3D%20undefined%0A%20%20%20%20for%20%28var%20item%20of%20list%29%20%7B%0A%20%20%20%20%20%20%20%20var%20number%20%3D%20undefined%0A%20%20%20%20%20%20%20%20if%20%28item.constructor%20%3D%3D%3D%20Number%29%20%7B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20number%20%3D%20item%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20else%20if%20%28item.constructor%20%3D%3D%3D%20Array%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20number%20%3D%20getHighestNumberInList%28item%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20if%20%28number%20!%3D%20undefined%20%26%26%20%28highestNumber%20%3D%3D%3D%20undefined%20%7C%7C%20number%20%3E%20highestNumber%29%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20highestNumber%20%3D%20number%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20return%20highestNumber%0A%7D)

__Listing 21-30__JavaScript: Function that determines the highest numeric value in a list of items

1. `function getHighestNumberInList(list) {`
2. `var highestNumber = undefined`
3. `for (var item of list) {`
4. `var number = undefined`
5. `if (item.constructor === Number) {`
7. `number = item`
8. `}`
9. `else if (item.constructor === Array) {`
10. `number = getHighestNumberInList(item)`
11. `}`
12. `if (number != undefined && (highestNumber === undefined || number > highestNumber)) {`
13. `highestNumber = number`
14. `}`
15. `}`
16. `return highestNumber`
17. `}`

Listing 21-31 and Listing 21-32 show how to call the handlers in Listing 21-29 and Listing 21-30 for a list containing a mixture of numbers and strings.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getHighestNumberInList%28%7B-3.25%2C%2023%2C%202345%2C%20%22sid%22%2C%203%2C%2067%7D%29)

__Listing 21-31__AppleScript: Calling a handler to determine the highest numeric value in a list of numbers and strings

1. `getHighestNumberInList({-3.25, 23, 2345, "sid", 3, 67})`
2. `--> Result: 2345`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getHighestNumberInList%28%5B-3.25%2C%2023%2C%202345%2C%20%22sid%22%2C%203%2C%2067%5D%29)

__Listing 21-32__JavaScript: Calling a function to determine the highest numeric value in a list of numbers and strings

1. `getHighestNumberInList([-3.25, 23, 2345, "sid", 3, 67])`
2. `// Result: 2345`

Listing 21-33 and Listing 21-34 show how to call the handlers in Listing 21-29 and Listing 21-30 for a list containing a mixture of numbers, strings, booleans, and lists.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getHighestNumberInList%28%7B-3.25%2C%2023%2C%20%7B23%2C%2078695%2C%20%22bob%22%7D%2C%202345%2C%20true%2C%20%22sid%22%2C%203%2C%2067%7D%29)

__Listing 21-33__AppleScript: Calling a handler to determine the highest numeric value in a list of different value types

1. `getHighestNumberInList({-3.25, 23, {23, 78695, "bob"}, 2345, true, "sid", 3, 67})`
2. `--> Result: 78695`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getHighestNumberInList%28%5B-3.25%2C%2023%2C%20%5B23%2C%2078695%2C%20%22bob%22%5D%2C%202345%2C%20true%2C%20%22sid%22%2C%203%2C%2067%5D%29)

__Listing 21-34__JavaScript: Calling a function to determine the highest numeric value in a list of different value types

1. `getHighestNumberInList([-3.25, 23, [23, 78695, "bob"], 2345, true, "sid", 3, 67])`
2. `// Result: 78695`

Listing 21-35 and Listing 21-36 show how to call the handlers in Listing 21-29 and Listing 21-30 for a list containing only strings.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getHighestNumberInList%28%7B%22this%22%2C%20%22list%22%2C%20%22contains%22%2C%20%22only%22%2C%20%22text%22%7D%29)

__Listing 21-35__AppleScript: Calling a handler to determine the highest numeric value in a list of strings

1. `getHighestNumberInList({"this", "list", "contains", "only", "text"})`
2. `--> Result: false`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getHighestNumberInList%28%5B%22this%22%2C%20%22list%22%2C%20%22contains%22%2C%20%22only%22%2C%20%22text%22%5D%29)

__Listing 21-36__JavaScript: Calling a function to determine the highest numeric value in a list of strings

1. `getHighestNumberInList(["this", "list", "contains", "only", "text"])`
2. `// Result: undefined`

### Finding the Lowest Numeric Value in a List

The handlers in Listing 21-37 and Listing 21-38 determines the lowest numeric value in a list of items. The passed list can contain non-numeric data as well as lists within lists.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20getLowestNumberInList%28theList%29%0A%20%20%20%20set%20theLowestNumber%20to%20false%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theList%0A%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20item%20a%20of%20theList%0A%20%20%20%20%20%20%20%20set%20theClass%20to%20class%20of%20theCurrentItem%0A%20%20%20%20%20%20%20%20if%20theClass%20is%20in%20%7Binteger%2C%20real%7D%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20theLowestNumber%20is%20%22%22%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowestNumber%20to%20theCurrentItem%0A%20%20%20%20%20%20%20%20%20%20%20%20else%20if%20theCurrentItem%20is%20less%20than%20theLowestNumber%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowestNumber%20to%20item%20a%20of%20theList%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20else%20if%20theClass%20is%20list%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowValue%20to%20getLowestNumberInList%28theCurrentItem%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20theLowValue%20is%20less%20than%20theLowestNumber%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowestNumber%20to%20theLowValue%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20theLowestNumber%0Aend%20getLowestNumberInList)

__Listing 21-37__AppleScript: Handler that determines the lowest numeric value in a list of items

1. `on getLowestNumberInList(theList)`
2. `set theLowestNumber to false`
3. `repeat with a from 1 to count of theList`
4. `set theCurrentItem to item a of theList`
5. `set theClass to class of theCurrentItem`
6. `if theClass is in {integer, real} then`
7. `if theLowestNumber is "" then`
8. `set theLowestNumber to theCurrentItem`
9. `else if theCurrentItem is less than theLowestNumber then`
10. `set theLowestNumber to item a of theList`
11. `end if`
12. `else if theClass is list then`
13. `set theLowValue to getLowestNumberInList(theCurrentItem)`
14. `if theLowValue is less than theLowestNumber then`
15. `set theLowestNumber to theLowValue`
16. `end if`
17. `end if`
18. `end repeat`
19. `return theLowestNumber`
20. `end getLowestNumberInList`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20getLowestNumberInList%28list%29%20%7B%0A%20%20%20%20var%20lowestNumber%20%3D%20undefined%0A%20%20%20%20for%20%28var%20item%20of%20list%29%20%7B%0A%20%20%20%20%20%20%20%20var%20number%20%3D%20undefined%0A%20%20%20%20%20%20%20%20if%20%28item.constructor%20%3D%3D%3D%20Number%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20number%20%3D%20item%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20else%20if%20%28item.constructor%20%3D%3D%3D%20Array%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20number%20%3D%20getLowestNumberInList%28item%29%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20if%20%28number%20!%3D%20undefined%20%26%26%20%28lowestNumber%20%3D%3D%3D%20undefined%20%7C%7C%20number%20%3C%20lowestNumber%29%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20lowestNumber%20%3D%20number%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20return%20lowestNumber%0A%7D%0A)

__Listing 21-38__JavaScript: Function that determines the lowest numeric value in a list of items

1. `function getLowestNumberInList(list) {`
2. `var lowestNumber = undefined`
3. `for (var item of list) {`
4. `var number = undefined`
5. `if (item.constructor === Number) {`
6. `number = item`
7. `}`
8. `else if (item.constructor === Array) {`
9. `number = getLowestNumberInList(item)`
10. `}`
11. `if (number != undefined && (lowestNumber === undefined || number < lowestNumber)) {`
12. `lowestNumber = number`
13. `}`
14. `}`
15. `return lowestNumber`
16. `}`

Listing 21-39 and Listing 21-40 show how to call the handlers in Listing 21-37 and Listing 21-38 for a list containing a mixture of numbers and strings.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getLowestNumberInList%28%7B-3.25%2C%2023%2C%202345%2C%20%22sid%22%2C%203%2C%2067%7D%29)

__Listing 21-39__AppleScript: Calling a handler to determine the lowest numeric value in a list of numbers and strings

1. `getLowestNumberInList({-3.25, 23, 2345, "sid", 3, 67})`
2. `--> Result: -3.25`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getLowestNumberInList%28%5B-3.25%2C%2023%2C%202345%2C%20%22sid%22%2C%203%2C%2067%5D%29)

__Listing 21-40__JavaScript: Calling a function to determine the lowest numeric value in a list of strings

1. `getLowestNumberInList([-3.25, 23, 2345, "sid", 3, 67])`
2. `// Result: -3.25`

Listing 21-41 and Listing 21-42 show how to call the handlers in Listing 21-37 and Listing 21-38 for a list containing a mixture of numbers, strings, booleans, and lists.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getLowestNumberInList%28%7B-3.25%2C%2023%2C%20%7B-22%2C%2078695%2C%20%22Sal%22%7D%2C%202345%2C%20true%2C%20%22sid%22%2C%203%2C%2067%7D%29)

__Listing 21-41__AppleScript: Calling a handler to determine the lowest numeric value in a list of different value types

1. `getLowestNumberInList({-3.25, 23, {-22, 78695, "Sal"}, 2345, true, "sid", 3, 67})`
2. `--> Result: -22`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getLowestNumberInList%28%5B-3.25%2C%2023%2C%20%5B-22%2C%2078695%2C%20%22bob%22%5D%2C%202345%2C%20true%2C%20%22sid%22%2C%203%2C%2067%5D%29)

__Listing 21-42__JavaScript: Calling a function to determine the lowest numeric value in a list of different value types

1. `getLowestNumberInList([-3.25, 23, [-22, 78695, "bob"], 2345, true, "sid", 3, 67])`
2. `// Result: -22`

Listing 21-43 and Listing 21-44 show how to call the handlers in Listing 21-37 and Listing 21-38 for a list containing only strings.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getLowestNumberInList%28%7B%22this%22%2C%20%22list%22%2C%20%22contains%22%2C%20%22only%22%2C%20%22text%22%7D%29)

__Listing 21-43__AppleScript: Calling a handler to determine the lowest numeric value in a list of strings

1. `getLowestNumberInList({"this", "list", "contains", "only", "text"})`
2. `--> Result: false`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=getLowestNumberInList%28%5B%22this%22%2C%20%22list%22%2C%20%22contains%22%2C%20%22only%22%2C%20%22text%22%5D%29)

__Listing 21-44__JavaScript: Calling a function to determine the lowest numeric value in a list of strings

1. `getLowestNumberInList(["this", "list", "contains", "only", "text"])`
2. `// Result: undefined`

### Inserting Items into a List

The handlers in Listing 21-45 and Listing 21-46 insert an item into a list. Provide the item to insert, the list, and the position where the item should be inserted. Note that position can be specified in relation to the end of the list by using a negative number.

> [!NOTE]
> 

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20insertItemInList%28theItem%2C%20theList%2C%20thePosition%29%0A%20%20%20%20set%20theListCount%20to%20length%20of%20theList%0A%20%20%20%20if%20thePosition%20is%200%20then%0A%20%20%20%20%20%20%20%20return%20false%0A%20%20%20%20else%20if%20thePosition%20is%20less%20than%200%20then%0A%20%20%20%20%20%20%20%20if%20%28thePosition%20*%20-1%29%20is%20greater%20than%20theListCount%20%2B%201%20then%20return%20false%0A%20%20%20%20else%0A%20%20%20%20%20%20%20%20if%20thePosition%20is%20greater%20than%20theListCount%20%2B%201%20then%20return%20false%0A%20%20%20%20end%20if%0A%20%20%20%20if%20thePosition%20is%20less%20than%200%20then%0A%20%20%20%20%20%20%20%20if%20%28thePosition%20*%20-1%29%20is%20theListCount%20%2B%201%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20beginning%20of%20theList%20to%20theItem%0A%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theList%20to%20reverse%20of%20theList%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20thePosition%20to%20%28thePosition%20*%20-1%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20thePosition%20is%201%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20beginning%20of%20theList%20to%20theItem%0A%20%20%20%20%20%20%20%20%20%20%20%20else%20if%20thePosition%20is%20%28theListCount%20%2B%201%29%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20end%20of%20theList%20to%20theItem%0A%20%20%20%20%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theList%20to%20%28items%201%20thru%20%28thePosition%20-%201%29%20of%20theList%29%20%26%20theItem%20%26%20%28items%20thePosition%20thru%20-1%20of%20theList%29%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theList%20to%20reverse%20of%20theList%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20else%0A%20%20%20%20%20%20%20%20if%20thePosition%20is%201%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20beginning%20of%20theList%20to%20theItem%0A%20%20%20%20%20%20%20%20else%20if%20thePosition%20is%20%28theListCount%20%2B%201%29%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20end%20of%20theList%20to%20theItem%0A%20%20%20%20%20%20%20%20else%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theList%20to%20%28items%201%20thru%20%28thePosition%20-%201%29%20of%20theList%29%20%26%20theItem%20%26%20%28items%20thePosition%20thru%20-1%20of%20theList%29%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20if%0A%20%20%20%20return%20theList%0Aend%20insertItemInList)

__Listing 21-45__AppleScript: Handler that inserts an item into a list

1. `on insertItemInList(theItem, theList, thePosition)`
2. `set theListCount to length of theList`
3. `if thePosition is 0 then`
4. `return false`
5. `else if thePosition is less than 0 then`
6. `if (thePosition * -1) is greater than theListCount + 1 then return false`
7. `else`
8. `if thePosition is greater than theListCount + 1 then return false`
9. `end if`
10. `if thePosition is less than 0 then`
11. `if (thePosition * -1) is theListCount + 1 then`
12. `set beginning of theList to theItem`
13. `else`
14. `set theList to reverse of theList`
15. `set thePosition to (thePosition * -1)`
16. `if thePosition is 1 then`
17. `set beginning of theList to theItem`
18. `else if thePosition is (theListCount + 1) then`
19. `set end of theList to theItem`
20. `else`
21. `set theList to (items 1 thru (thePosition - 1) of theList) & theItem & (items thePosition thru -1 of theList)`
22. `end if`
23. `set theList to reverse of theList`
24. `end if`
25. `else`
26. `if thePosition is 1 then`
27. `set beginning of theList to theItem`
28. `else if thePosition is (theListCount + 1) then`
29. `set end of theList to theItem`
30. `else`
31. `set theList to (items 1 thru (thePosition - 1) of theList) & theItem & (items thePosition thru -1 of theList)`
32. `end if`
33. `end if`
34. `return theList`
35. `end insertItemInList`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20insertItemInArray%28item%2C%20array%2C%20position%29%20%7B%0A%20%20%20%20var%20arrayCount%20%3D%20array.length%0A%20%20%20%20if%20%28Math.abs%28position%29%20%3E%20arrayCount%29%20%7B%0A%20%20%20%20%20%20%20%20return%20false%0A%20%20%20%20%7D%0A%20%20%20else%20if%20%28position%20%3D%3D%3D%200%29%20%7B%0A%20%20%20%20%20%20%20%20array.unshift%28item%29%0A%20%20%20%20%7D%0A%20%20%20%20else%20if%20%28position%20%3C%20arrayCount%29%20%7B%0A%20%20%20%20%20%20%20%20array.splice%28position%2C%200%2C%20item%29%0A%20%20%20%20%7D%0A%20%20%20%20else%20%7B%0A%20%20%20%20%20%20%20%20array.push%28item%29%0A%20%20%20%20%7D%0A%20%20%20%20return%20array%0A%7D)

__Listing 21-46__JavaScript: Function that inserts an item into an array

1. `function insertItemInArray(item, array, position) {`
2. `var arrayCount = array.length`
3. `if (Math.abs(position) > arrayCount) {`
4. `return false`
5. `}`
6. `else if (position === 0) {`
7. `array.unshift(item)`
8. `}`
9. `else if (position < arrayCount) {`
10. `array.splice(position, 0, item)`
11. `}`
12. `else {`
13. `array.push(item)`
14. `}`
15. `return array`
16. `}`

Listing 21-47 and Listing 21-48 show how to call the handlers in Listing 21-45 and Listing 21-46 to insert a single item into a list at a specific position.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AinsertItemInList%28%22Jen%22%2C%20theList%2C%203%29)

__Listing 21-47__AppleScript: Calling a handler to insert a single item at a specific position in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `insertItemInList("Jen", theList, 3)`
3. `--> Result: {"Sal", "Ben", "Jen", "David", "Chris"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray%20%3D%20insertItemInArray%28%22Jen%22%2C%20array%2C%202%29%0A)

__Listing 21-48__JavaScript: Calling a function to insert a single item at a specific position in an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array = insertItemInArray("Jen", array, 2)`
3. `// Result = ["Sal", "Ben", "Jen", "David", "Chris"]`

Listing 21-49 and Listing 21-50 show how to call the handlers in Listing 21-45 and Listing 21-46 to insert multiple items into a list at a specific position.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AinsertItemInList%28%7B%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%7D%2C%20theList%2C%203%29%0A)

__Listing 21-49__AppleScript: Calling a handler to insert multiple items at a specific position in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `insertItemInList({"Lizzie", "Maddie", "Lillie"}, theList, 3)`
3. `--> Result: {"Sal", "Ben", "Lizzie", "Maddie", "Lillie", "David", "Chris"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Avar%20items%20%3D%20%5B%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%5D%0Afor%20%28var%20item%20of%20items%29%20%7B%0A%20%20%20%20array%20%3D%20insertItemInArray%28item%2C%20array%2C%202%29%0A%7D)

__Listing 21-50__JavaScript: Calling a function to insert multiple items at a specific position in an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `var items = ["Lizzie", "Maddie", "Lillie"]`
3. `for (var item of items) {`
4. `array = insertItemInArray(item, array, 2)`
5. `}`
6. `// Result = ["Sal", "Ben", "Lillie", "Maddie", "Lizzie", "David", "Chris"]`

Listing 21-51 and Listing 21-52 show how to call the handlers in Listing 21-45 and Listing 21-46 to insert a list into a list at a specific position.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AinsertItemInList%28%7B%7B%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%7D%7D%2C%20theList%2C%203%29%0A)

__Listing 21-51__AppleScript: Calling a handler to insert a list at a specific position in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `insertItemInList({{"Lizzie", "Maddie", "Lillie"}}, theList, 3)`
3. `--> Result: {"Sal", "Ben", {"Lizzie", "Maddie", "Lillie"}, "David", "Chris"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray%20%3D%20insertItemInArray%28%5B%22Lizzie%22%2C%20%22Maddie%22%2C%20%22Lillie%22%5D%2C%20array%2C%202%29%0A)

__Listing 21-52__JavaScript: Calling a function to insert a list at a specific position in an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array = insertItemInArray(["Lizzie", "Maddie", "Lillie"], array, 2)`
3. `// Result = ["Sal", "Ben", ["Lizzie", "Maddie", "Lillie"], "David", "Chris"]`

Listing 21-53 and Listing 21-54 show how to call the handlers in Listing 21-45 and Listing 21-46 to insert a single item at the end of a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AinsertItemInList%28%22Jen%22%2C%20theList%2C%20-1%29%0A)

__Listing 21-53__AppleScript: Calling a handler to insert a single item at the end of a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `insertItemInList("Jen", theList, -1)`
3. `--> {"Sal", "Ben", "David", "Chris", "Jen"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray%20%3D%20insertItemInArray%28%22Jen%22%2C%20array%2C%20array.length%29%0A)

__Listing 21-54__JavaScript: Calling a function to insert a single item at the end of an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array = insertItemInArray("Jen", array, array.length)`
3. `// Result = ["Sal", "Ben", "David", "Chris", "Jen"]`

Listing 21-55 and Listing 21-56 show how to call the handlers in Listing 21-45 and Listing 21-46 to insert a single item at the second-to-last position in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AinsertItemInList%28%22Wanda%22%2C%20theList%2C%20-2%29%0A)

__Listing 21-55__AppleScript: Calling a handler to insert a single item at the second-to-last position in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `insertItemInList("Wanda", theList, -2)`
3. `--> {"Sal", "Sue", "Bob", "Wanda", "Carl"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray%20%3D%20insertItemInArray%28%22Jen%22%2C%20array%2C%20-1%29%0A)

__Listing 21-56__JavaScript: Calling a function to insert a single item at the second-to-last position of an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array = insertItemInArray("Jen", array, -1)`
3. `// Result = ["Sal", "Ben", "David", "Jen", "Chris"]`

Listing 21-57 and Listing 21-58 show how to call the handlers in Listing 21-45 and Listing 21-46 to insert a single item at a nonexistent position in a list.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AinsertItemInList%28%22Jen%22%2C%20theList%2C%2015%29%0A)

__Listing 21-57__AppleScript: Calling a handler to insert a single item at a position that doesn’t exist in a list

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `insertItemInList("Jen", theList, 15)`
3. `--> Result: false`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray%20%3D%20insertItemInArray%28%22Jen%22%2C%20array%2C%2014%29%0A)

__Listing 21-58__JavaScript: Calling a function to insert a single item at a position that doesn’t exist in an array

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array = insertItemInArray("Jen", array, 14)`
3. `// Result = false`

### Replacing Items in a List

You can replace an item in a list using the syntax shown in Listing 21-59 and Listing 21-60 if you know the position of the item you want to replace.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0Aset%20item%203%20of%20theList%20to%20%22Wanda%22%0Areturn%20theList)

__Listing 21-59__AppleScript: Replacing a specific item in a list based on position

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `set item 3 of theList to "Wanda"`
3. `return theList`
4. `--> Result: {"Sal", "Sue", "Wanda", "Carl"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray%5B2%5D%20%3D%20%22Wanda%22%0Aarray)

__Listing 21-60__JavaScript: Replacing a specific item in an array based on position

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array[2] = "Wanda"`
3. `array`
4. `// Result: ["Sal", "Ben", "Wanda", "Chris"]`

The handlers in Listing 21-61 and Listing 21-62 can be used to replace an item in a list when you don’t know its position. Provide the item you want to replace, the list, the replacement item, and specify whether to replace all instances of the item, or just the first one.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20replaceItemInList%28theItem%2C%20theList%2C%20theReplacementItem%2C%20replaceAll%29%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20the%20count%20of%20theList%0A%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20item%20a%20of%20theList%0A%20%20%20%20%20%20%20%20if%20theCurrentItem%20is%20theItem%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20item%20a%20of%20theList%20to%20theReplacementItem%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20replaceAll%20is%20false%20then%20return%20theList%0A%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20theList%0Aend%20replaceItemInList)

__Listing 21-61__AppleScript: Handler that replaces items in a list

1. `on replaceItemInList(theItem, theList, theReplacementItem, replaceAll)`
2. `repeat with a from 1 to the count of theList`
3. `set theCurrentItem to item a of theList`
4. `if theCurrentItem is theItem then`
5. `set item a of theList to theReplacementItem`
6. `if replaceAll is false then return theList`
7. `end if`
8. `end repeat`
9. `return theList`
10. `end replaceItemInList`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20replaceItemInArray%28item%2C%20array%2C%20replacementItem%2C%20replaceAll%29%20%7B%0A%20%20%20%20var%20arrayLength%20%3D%20array.length%0A%20%20%20%20for%20%28var%20i%20%3D%200%3B%20i%20%3C%20arrayLength%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20var%20currentArrayItem%20%3D%20array%5Bi%5D%0A%20%20%20%20%20%20%20%20if%20%28currentArrayItem%20%3D%3D%3D%20item%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20array.splice%28i%2C%201%2C%20replacementItem%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20%28!replaceAll%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20return%20array%0A%7D)

__Listing 21-62__JavaScript: Function that replaces items in an array

1. `function replaceItemInArray(item, array, replacementItem, replaceAll) {`
2. `var arrayLength = array.length`
3. `for (var i = 0; i < arrayLength; i++) {`
4. `var currentArrayItem = array[i]`
5. `if (currentArrayItem === item) {`
6. `array.splice(i, 1, replacementItem)`
7. `if (!replaceAll) {`
8. `break`
9. `}`
10. `}`
11. `}`
12. `return array`
13. `}`

Listing 21-63 and Listing 21-64 show how to call the handlers in Listing 21-61 and Listing 21-62.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Jen%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%7D%0AreplaceItemInList%28%22Jen%22%2C%20theList%2C%20%22Lizzie%22%2C%20true%29)

__Listing 21-63__AppleScript: Calling a handler to replace items in a list

1. `set theList to {"Sal", "Jen", "Ben", "David", "Chris", "Jen"}`
2. `replaceItemInList("Jen", theList, "Lizzie", true)`
3. `--> {"Sal", "Lizzie", "Ben", "David", "Chris", "Lizzie"}`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Jen%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%2C%20%22Jen%22%5D%0AreplaceItemInArray%28%22Jen%22%2C%20array%2C%20%22Lizzie%22%2C%20true%29%0A)

__Listing 21-64__JavaScript: Calling a function to replace items in an array

1. `var array = ["Sal", "Jen", "Ben", "David", "Chris", "Jen"]`
2. `replaceItemInArray("Jen", array, "Lizzie", true)`
3. `// Result: ["Sal", "Lizzie", "Ben", "David", "Chris", "Lizzie"]`

### Sorting a List

The handler in Listing 21-65 sorts a list of strings or numbers in AppleScript.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20sortList%28theList%29%0A%20%20%20%20set%20theIndexList%20to%20%7B%7D%0A%20%20%20%20set%20theSortedList%20to%20%7B%7D%0A%20%20%20%20repeat%20%28length%20of%20theList%29%20times%0A%20%20%20%20%20%20%20%20set%20theLowItem%20to%20%22%22%0A%20%20%20%20%20%20%20%20repeat%20with%20a%20from%201%20to%20%28length%20of%20theList%29%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20a%20is%20not%20in%20theIndexList%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theCurrentItem%20to%20item%20a%20of%20theList%20as%20text%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20theLowItem%20is%20%22%22%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowItem%20to%20theCurrentItem%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowItemIndex%20to%20a%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%20if%20theCurrentItem%20comes%20before%20theLowItem%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowItem%20to%20theCurrentItem%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theLowItemIndex%20to%20a%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20if%0A%20%20%20%20%20%20%20%20end%20repeat%0A%20%20%20%20%20%20%20%20set%20end%20of%20theSortedList%20to%20theLowItem%0A%20%20%20%20%20%20%20%20set%20end%20of%20theIndexList%20to%20theLowItemIndex%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20theSortedList%0Aend%20sortList)

__Listing 21-65__AppleScript: Handler that sorts a list of strings

1. `on sortList(theList)`
2. `set theIndexList to {}`
3. `set theSortedList to {}`
4. `repeat (length of theList) times`
5. `set theLowItem to ""`
6. `repeat with a from 1 to (length of theList)`
7. `if a is not in theIndexList then`
8. `set theCurrentItem to item a of theList as text`
9. `if theLowItem is "" then`
10. `set theLowItem to theCurrentItem`
11. `set theLowItemIndex to a`
12. `else if theCurrentItem comes before theLowItem then`
13. `set theLowItem to theCurrentItem`
14. `set theLowItemIndex to a`
15. `end if`
16. `end if`
17. `end repeat`
18. `set end of theSortedList to theLowItem`
19. `set end of theIndexList to theLowItemIndex`
20. `end repeat`
21. `return theSortedList`
22. `end sortList`

Listing 21-66 shows how to call the handler in Listing 21-65.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0AsortList%28theList%29)

__Listing 21-66__AppleScript: Calling a handler to sort a list of strings

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `sortList(theList)`
3. `--> Result: {"Ben", "Chris", "David", "Sal"}`

To perform a reverse (descending) sort, use the reverse command, as shown in Listing 21-67.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theList%20to%20%7B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%7D%0Areverse%20of%20sortList%28theList%29)

__Listing 21-67__AppleScript: Calling a handler to sort a list of strings in reverse order

1. `set theList to {"Sal", "Ben", "David", "Chris"}`
2. `reverse of sortList(theList)`
3. `--> Result: {"Sal", "David", "Chris", "Ben"}`

In JavaScript, the `Array` object has a `sort` method, which sorts the array’s items. See Listing 21-68.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray.sort%28%29%0A)

__Listing 21-68__JavaScript: Sorting an array of strings

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array.sort()`
3. `// Result: ["Ben", "Chris", "David", "Sal"]`

As in AppleScript, a sorted JavaScript array can be reversed, as shown in Listing 21-69.

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20array%20%3D%20%5B%22Sal%22%2C%20%22Ben%22%2C%20%22David%22%2C%20%22Chris%22%5D%0Aarray.sort%28%29%0Aarray.reverse%28%29%0A)

__Listing 21-69__JavaScript: Sorting an array of strings in reverse order

1. `var array = ["Sal", "Ben", "David", "Chris"]`
2. `array.sort()`
3. `array.reverse()`
4. `// Result: ["Sal", "David", "Chris", "Ben"]`

> [!NOTE]
> 

[Manipulating Numbers](ManipulateNumbers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnbxfvjvomi)

[Displaying Dialogs and Alerts](DisplayDialogsandAlerts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmjvfvjvomi)
