---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/ConvertRGBtoHTMLColor.html
archived_at: '2026-07-15T07:45:27.965088Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Converting RGB to HTML Color

In HTML documents, colors are typically represented as hex values. The handlers in Listing 31-1 and Listing 31-2 show how to convert 8-bit or 256 color-based RGB values to hex values. Provide an RGB color represented by a list of three numbers, each with a value between `0` and `65535`.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=on%20convertRGBColorToHexValue%28theRGBValues%29%0A%20%20%20%20set%20theHexList%20to%20%7B%220%22%2C%20%221%22%2C%20%222%22%2C%20%223%22%2C%20%224%22%2C%20%225%22%2C%20%226%22%2C%20%227%22%2C%20%228%22%2C%20%229%22%2C%20%22A%22%2C%20%22B%22%2C%20%22C%22%2C%20%22D%22%2C%20%22E%22%2C%20%22F%22%7D%0A%20%20%20%20set%20theHexValue%20to%20%22%22%0A%20%20%20%20repeat%20with%20a%20from%201%20to%20count%20of%20theRGBValues%0A%20%20%20%20%20%20%20%20set%20theCurrentRGBValue%20to%20%28item%20a%20of%20theRGBValues%29%20div%20256%0A%20%20%20%20%20%20%20%20if%20theCurrentRGBValue%20is%20256%20then%20set%20theCurrentRGBValue%20to%20255%0A%20%20%20%20%20%20%20%20set%20theFirstItem%20to%20item%20%28%28theCurrentRGBValue%20div%2016%29%20%2B%201%29%20of%20theHexList%0A%20%20%20%20%20%20%20%20set%20theSecondItem%20to%20item%20%28%28%28theCurrentRGBValue%20%2F%2016%20mod%201%29%20*%2016%29%20%2B%201%29%20of%20theHexList%0A%20%20%20%20%20%20%20%20set%20theHexValue%20to%20%28theHexValue%20%26%20theFirstItem%20%26%20theSecondItem%29%20as%20string%0A%20%20%20%20end%20repeat%0A%20%20%20%20return%20%28%22%23%22%20%26%20theHexValue%29%20as%20string%0Aend%20convertRGBColorToHexValue)

__Listing 31-1__AppleScript: Handler that converts an RGB color to a hex value

1. `on convertRGBColorToHexValue(theRGBValues)`
2. `set theHexList to {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}`
3. `set theHexValue to ""`
4. `repeat with a from 1 to count of theRGBValues`
5. `set theCurrentRGBValue to (item a of theRGBValues) div 256`
6. `if theCurrentRGBValue is 256 then set theCurrentRGBValue to 255`
7. `set theFirstItem to item ((theCurrentRGBValue div 16) + 1) of theHexList`
8. `set theSecondItem to item (((theCurrentRGBValue / 16 mod 1) * 16) + 1) of theHexList`
9. `set theHexValue to (theHexValue & theFirstItem & theSecondItem) as string`
10. `end repeat`
11. `return ("#" & theHexValue) as string`
12. `end convertRGBColorToHexValue`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=function%20convertRGBColorToHexValue%28rgbValues%29%20%7B%0A%20%20%20%20var%20r%20%3D%20parseInt%28rgbValues%5B0%5D%2C%2010%29.toString%2816%29.slice%28-2%29%0A%20%20%20%20if%20%28r.length%20%3D%3D%201%29%0A%20%20%20%20%20%20%20%20r%20%3D%20%220%22%20%2B%20r%0A%20%20%20%20var%20g%20%3D%20parseInt%28rgbValues%5B1%5D%2C%2010%29.toString%2816%29.slice%28-2%29%0A%20%20%20%20if%20%28g.length%20%3D%3D%201%29%0A%20%20%20%20%20%20%20%20g%20%3D%20%220%22%20%2B%20g%0A%20%20%20%20var%20b%20%3D%20parseInt%28rgbValues%5B2%5D%2C%2010%29.toString%2816%29.slice%28-2%29%0A%20%20%20%20if%20%28b.length%20%3D%3D%201%29%0A%20%20%20%20%20%20%20%20b%20%3D%20%220%22%20%2B%20b%0A%20%20%20%20return%20%28%22%23%22%20%2B%20r%20%2B%20g%20%2B%20b%29%0A%7D)

__Listing 31-2__JavaScript: Function that converts an RGB color to a hex value

1. `function convertRGBColorToHexValue(rgbValues) {`
2. `var r = parseInt(rgbValues[0], 10).toString(16).slice(-2)`
3. `if (r.length == 1)`
4. `r = "0" + r`
5. `var g = parseInt(rgbValues[1], 10).toString(16).slice(-2)`
6. `if (g.length == 1)`
7. `g = "0" + g`
8. `var b = parseInt(rgbValues[2], 10).toString(16).slice(-2)`
9. `if (b.length == 1)`
10. `b = "0" + b`
11. `return ("#" + r + g + b)`
12. `}`

Listing 31-3 shows how to call the handlers in Listing 31-1 to convert a specified RGB color to a hex value for use in HTML.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=set%20theRGBValues%20to%20%28choose%20color%20default%20color%20%7B65535%2C%200%2C%200%7D%29%0AconvertRGBColorToHexValue%28theRGBValues%29)

__Listing 31-3__AppleScript: Calling a handler to convert an RGB color to a hex value

1. `set theRGBValues to (choose color default color {65535, 0, 0})`
2. `convertRGBColorToHexValue(theRGBValues)`
3. `--> Result: "#FF0000"`

__JAVASCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20color%20%3D%20app.chooseColor%28%7BdefaultColor%3A%20%5B1%2C%200%2C%200%5D%7D%29%0Acolor%20%3D%20%5BMath.trunc%28color%5B0%5D%20*%2065535%29%2C%20Math.trunc%28color%5B1%5D%20*%2065535%29%2C%20Math.trunc%28color%5B2%5D%20*%2065535%29%5D%0AconvertRGBColorToHexValue%28color%29)

__Listing 31-4__JavaScript: Calling a function to convert an RGB color to a hex value

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
4. `var color = app.chooseColor({defaultColor: [1, 0, 0]})`
5. `color = [Math.trunc(color[0] * 65535), Math.trunc(color[1] * 65535), Math.trunc(color[2] * 65535)]`
6. `convertRGBColorToHexValue(color)`
7. `// Result: "#FF0000"`

> [!NOTE]
> 

[Displaying Progress](DisplayProgress.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqmzxfvjvomi)

[Encoding and Decoding Text](EncodeandDecodeText.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqnjrfvjvomi)
