---
title: Customize Reader Safari Extension
apple_id: DTS40012308
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/samplecode/CustomizeReaderSafariExtension/Listings/CustomizeReader_safariextension_global_html.html
archived_at: '2026-07-18T03:05:48.417281Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Customize Reader Safari Extension](Customize%20Reader%20Safari%20Extension.md)


[Next](CustomizeReader.safariextension-helvetica.css.md)[Previous](CustomizeReader.safariextension-georgia.css.md)

# CustomizeReader.safariextension/global.html

```
<!--
    File: global.html
Abstract: Global Page HTML file.
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

Copyright (C) 2012 Apple Inc. All Rights Reserved.

-->

<!DOCTYPE html>
<script>

// Restore the user setting when Safari launches or the extension is enabled.
var initialFont = safari.extension.settings.font;
if (initialFont !== "default") {
    // Restrict the Content Style Sheet to all Reader pages by use of the whitelist.
    safari.extension.addContentStyleSheetFromURL(safari.extension.baseURI + initialFont + ".css", ["safari-reader://*/*"]);
}

// Listen for the user changing the font preference.
safari.extension.settings.addEventListener("change", handleSettingsChanged, false);
function handleSettingsChanged(event)
{
    if (!event.key === "font")
        return;

    // Stop using the old Content Style Sheet (if any) and add the new one (if needed).
    if (event.oldValue !== "default")
        safari.extension.removeContentStyleSheet(safari.extension.baseURI + event.oldValue + ".css");
    if (event.newValue !== "default") {
        // Restrict the Content Style Sheet to all Reader pages by use of the whitelist.
        safari.extension.addContentStyleSheetFromURL(safari.extension.baseURI + event.newValue + ".css", ["safari-reader://*/*"]);
    }

    // Example of dispatching a message to a Content Script injected into Reader.
    var browserWindows = safari.application.browserWindows;
    for (var i = 0; i < browserWindows.length; ++i) {
        var tabs = browserWindows[i].tabs;
        for (var j = 0; j < tabs.length; ++j) {
            var tab = tabs[j];
            if (!tab.reader.visible)
                continue;
            tab.reader.dispatchMessage("Message to the Content Scripts injected into Reader");
        }
    }
}

// Example of handling a message from a Content Script injected into Reader.
safari.application.addEventListener("message", handleMessage, false);
function handleMessage(event)
{
    // To distinguish whether a message came from a Content Script injected into Reader or a Content
    // Script injected into the web page, check if the target is a SafariReader object.
    if (event.target instanceof SafariReader)
        console.log("Received acknowledgment from a Content Script injected into Reader for " + event.target.tab.url);
}

</script>
```

[Next](CustomizeReader.safariextension-helvetica.css.md)[Previous](CustomizeReader.safariextension-georgia.css.md)

