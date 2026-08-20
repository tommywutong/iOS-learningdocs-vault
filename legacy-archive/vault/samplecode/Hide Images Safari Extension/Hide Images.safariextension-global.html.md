---
title: Hide Images Safari Extension
apple_id: DTS40010157
resource_type: Sample Code
platform: Safari|macOS
topic: User Experience
technology: null
published: '2010-06-24'
source_url: https://developer.apple.com/library/archive/samplecode/HideImagesSafariExtension/Listings/Hide_Images_safariextension_global_html.html
archived_at: '2026-07-18T03:11:55.350318Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Hide Images Safari Extension](Hide%20Images%20Safari%20Extension.md)


[Next](Read%20Me.txt.md)[Previous](Hide%20Images.safariextension-content.js.md)

# Hide Images.safariextension/global.html

```
<!--
    File: global.html
Abstract: Global page HTML file.
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

Copyright (C) 2010 Apple Inc. All Rights Reserved.

-->
<!DOCTYPE HTML>
<script>
// Register for the contextmenu event in the application layer.
safari.application.addEventListener("contextmenu", handleContextMenu, false);
// Register for the command event to perform the context menu item's action when it is clicked.
safari.application.addEventListener("command", handleCommand, false);

function handleContextMenu(event)
{
    // The passed in event is a SafariExtensionContextMenuEvent.
    // Retrieve the userInfo associated with this context menu event.  It should be
    // set to an object that contains the right-clicked element's tag name.  Add the 
    // context menu item only if an image is right-clicked.
    if (event.userInfo && event.userInfo.tagName !== "IMG")
        return;

    event.contextMenu.appendContextMenuItem("hide-image", "Hide Image");

    // Alternately we could add "Hide Image" as a default context menu item in the Extension Builder
    // and disable it if the right-clicked element is not an image in the listener of the 
    // "validate" event.
}

function handleCommand(event)
{
    // Always check the command name.
    if (event.command !== "hide-image")
        return;

    // We expect the user info for this event to contain the timestamp property.
    if (!event.userInfo || !event.userInfo.timestamp)
        return;

    // Send a message to the content script to hide the image.
    safari.application.activeBrowserWindow.activeTab.page.dispatchMessage("hide-element", event.userInfo.timestamp);
}
</script>
```

[Next](Read%20Me.txt.md)[Previous](Hide%20Images.safariextension-content.js.md)

