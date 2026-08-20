---
title: Color Finder Safari Extension
apple_id: DTS40011115
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/ColorFinderSafariExtension/Listings/ColorFinder_safariextension_showColors_js.html
archived_at: '2026-07-18T03:03:55.965707Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Color Finder Safari Extension](Color%20Finder%20Safari%20Extension.md)


[Next](Document%20Revision%20History.md)[Previous](ColorFinder.safariextension-popover.js.md)

# ColorFinder.safariextension/showColors.js

```
/*
    File: showColors.js
Abstract: Helper JavaScript file (used by both the Bar and the Popover).
 Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Copyright (C) 2011 Apple Inc. All Rights Reserved.

*/

// Listen for the messages from the content script with the color information.
safari.application.addEventListener("message", handleMessageEvent, false);
function handleMessageEvent(event)
{
    if (event.name !== "colorInfoReport")
        return;
    showColorInformation(event.message["background-colors"], event.message["text-colors"], event.message["border-colors"]);
}

var knownBgColors = [];
var knownTextColors = [];
var knownBorderColors = [];

function showColorInformation(bgColors, textColors, borderColors)
{
    // Generate the HTML to show blocks of color for the background colors, text for the text colors,
    // and borders for the border colors.

    var bgColorsElem = document.getElementById("background-colors");
    for (var bgColorIndex = 0; bgColorIndex < bgColors.length; ++bgColorIndex) {
        var colorString = bgColors[bgColorIndex];
        var colorElem = addColor(colorString, knownBgColors, "bg", bgColorsElem);
        if (!colorElem)
            continue;
        colorElem.style.backgroundColor = colorString;
    }

    var textColorsElem = document.getElementById("text-colors");
    for (var textColorsIndex = 0; textColorsIndex < textColors.length; ++textColorsIndex) {
        var colorString = textColors[textColorsIndex];
        var colorElem = addColor(colorString, knownTextColors, "text", textColorsElem);
        if (!colorElem)
            continue;
        colorElem.style.color = colorString;
    }

    var borderColorsElem = document.getElementById("border-colors");
    for (var borderColorsIndex = 0; borderColorsIndex < borderColors.length; ++borderColorsIndex) {
        var colorString = borderColors[borderColorsIndex];
        var colorElem = addColor(colorString, knownBorderColors, "border", borderColorsElem);
        if (!colorElem)
            continue;
        colorElem.style.borderColor = colorString;
    }

    // Now that the HTML content has been generated, make any adjustments to the UI to make it
    // the content fit where it is being displayed.
    makeUIAdjustments();
}

function addColor(colorString, knownColors, type, parentElement)
{
    // Only add the color if it isn't null, inherit, or initial and isn't already known.
    if (!colorString || colorString === "inherit" || colorString.indexOf("initial") != -1 || knownColors.indexOf(colorString) != -1)
        return null;
    knownColors.push(colorString);

    var colorElem = document.createElement("div");
    colorElem.className = "color-block " + type;
    colorElem.innerText = innerTextForColorString(colorString, type);
    colorElem.title = colorString;
    parentElement.appendChild(colorElem);
    return colorElem;
}

function clearColorInformation()
{
    var colorsToClear = { "background-colors" : knownBgColors, "text-colors" : knownTextColors, "border-colors" : knownBorderColors };
    for (colorType in colorsToClear) {
        var parentElement = document.getElementById(colorType);
        while (parentElement.hasChildNodes())
            parentElement.removeChild(parentElement.firstChild);
        colorsToClear[colorType].length = 0;
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](ColorFinder.safariextension-popover.js.md)

