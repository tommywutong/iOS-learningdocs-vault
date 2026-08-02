---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/WorkwithXML.html
archived_at: '2026-07-15T07:46:30.174936Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Working with XML

The XML Suite of the System Events scripting dictionary defines several classes that make it quick and easy to read and parse XML data. The `XML file` class represents any text file containing structured XML like the example data shown in Listing 36-1.

__Listing 36-1__XML: Example XML data

1. `<books>`
2. `<book country="US">`
3. `<name>The Secret Lives of Cats</name>`
4. `<publisher>Feline Press</publisher>`
5. `</book>`
6. `</books>`

At the top level, an XML file contains an `XML data` object that’s comprised of nested `XML element` objects. Each `XML element` object has a `name` and a `value` property, and may also contain `XML attribute` objects that define additional metadata. The example code in Listing 36-2 demonstrates how to access these classes to read and parse the contents of an XML file on the Desktop that contains the XML data from Listing 36-1.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=tell%20application%20%22System%20Events%22%0A%20%20%20%20tell%20XML%20file%20%22~%2FDesktop%2FBook%20Data.xml%22%0A%20%20%20%20%20%20%20%20tell%20XML%20element%20%22books%22%0A%20%20%20%20%20%20%20%20%20%20%20%20set%20theBookElements%20to%20every%20XML%20element%20whose%20name%20%3D%20%22book%22%0A%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7BXML%20element%201%20of%20XML%20element%201%20of%20contents%20of%20XML%20file%20%22Macintosh%20HD%3AUsers%3AYourUserName%3ADesktop%3ABook%20Data.xml%22%20of%20application%20%22System%20Events%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20repeat%20with%20a%20from%201%20to%20length%20of%20theBookElements%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theCurrentBookElement%20to%20item%20a%20of%20theBookElements%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20XML%20element%201%20of%20XML%20element%201%20of%20contents%20of%20XML%20file%20%22Macintosh%20HD%3AUsers%3Abwaldie%3ADesktop%3ABook%20Data.xml%22%20of%20application%20%22System%20Events%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20tell%20theCurrentBookElement%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20name%20of%20theCurrentBookElement%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%22book%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20name%20of%20every%20XML%20element%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7B%22name%22%2C%20%22publisher%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20name%20of%20every%20XML%20attribute%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7B%22country%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20of%20every%20XML%20attribute%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%7B%22US%22%7D%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20theBookName%20to%20value%20of%20XML%20element%20%22name%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%22The%20Secret%20Lives%20of%20Cats%22%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20set%20thePublisher%20to%20value%20of%20XML%20element%20%22publisher%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20--%3E%20%22Feline%20Press%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20end%20tell%0A%20%20%20%20%20%20%20%20%20%20%20%20end%20repeat%0A%20%20%20%20%20%20%20%20end%20tell%0A%20%20%20%20end%20tell%0Aend%20tell)

__Listing 36-2__AppleScript: Using System Events to parse an XML file

1. `tell application "System Events"`
2. `tell XML file "~/Desktop/Book Data.xml"`
3. `tell XML element "books"`
4. `set theBookElements to every XML element whose name = "book"`
5. `--> {XML element 1 of XML element 1 of contents of XML file "Macintosh HD:Users:YourUserName:Desktop:Book Data.xml" of application "System Events"}`
7. `repeat with a from 1 to length of theBookElements`
8. `set theCurrentBookElement to item a of theBookElements`
9. `--> XML element 1 of XML element 1 of contents of XML file "Macintosh HD:Users:YourUserName:Desktop:Book Data.xml" of application "System Events"`
11. `tell theCurrentBookElement`
12. `name of theCurrentBookElement`
13. `--> "book"`
15. `name of every XML element`
16. `--> {"name", "publisher"}`
18. `name of every XML attribute`
19. `--> {"country"}`
21. `value of every XML attribute`
22. `--> {"US"}`
24. `set theBookName to value of XML element "name"`
25. `--> "The Secret Lives of Cats"`
27. `set thePublisher to value of XML element "publisher"`
28. `--> "Feline Press"`
29. `end tell`
30. `end repeat`
31. `end tell`
32. `end tell`
33. `end tell`

[Working with Property List Files](WorkwithPropertyListFiles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnrwfvjvomi)

[Automating the User Interface](AutomatetheUserInterface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnrzfvjvomi)
