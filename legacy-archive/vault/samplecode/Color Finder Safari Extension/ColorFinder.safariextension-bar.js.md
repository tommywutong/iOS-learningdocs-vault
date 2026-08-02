---
title: Color Finder Safari Extension
apple_id: DTS40011115
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/ColorFinderSafariExtension/Listings/ColorFinder_safariextension_bar_js.html
archived_at: '2026-07-18T03:03:55.369946Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Color Finder Safari Extension](Color%20Finder%20Safari%20Extension.md)


[Next](ColorFinder.safariextension-content.js.md)[Previous](ColorFinder.safariextension-bar.html.md)

# ColorFinder.safariextension/bar.js

```
/*
    File: bar.js
Abstract: Bar JavaScript file.
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

safari.application.addEventListener("navigate", eventHandler, true);
safari.application.addEventListener("activate", eventHandler, true);

function eventHandler(event)
{
    // An activate event is also sent for Reader. Ignore that.
    if (event.target instanceof SafariReader)
        return;

    // Update the bar for the window every time we switch to a new tab or the active tab navigates.
    var tab;
    if (event.target instanceof SafariBrowserTab) {
        // A background tab could be navigating.
        if (event.type === "navigate" && event.target != safari.application.activeBrowserWindow.activeTab)
            return;
        tab = event.target;
    } else
        tab = event.target.activeTab;

    clearColorInformation();
    tab.page.dispatchMessage("gatherColorInfo");
}

/* Callbacks from showColor.js */

function makeUIAdjustments()
{
    // Nothing to do here.
}

function innerTextForColorString(colorString, type)
{
    if (type === "text")
        return "A";
    return " ";
}
```

[Next](ColorFinder.safariextension-content.js.md)[Previous](ColorFinder.safariextension-bar.html.md)

