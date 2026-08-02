---
title: Blocker Safari Extension
apple_id: DTS40010127
resource_type: Sample Code
platform: Safari
topic: User Experience
technology: null
published: '2010-06-08'
source_url: https://developer.apple.com/library/archive/samplecode/BlockerSafariExtension/Listings/Blocker_safariextension_content_js.html
archived_at: '2026-07-18T03:02:09.371914Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Blocker Safari Extension](Blocker%20Safari%20Extension.md)


[Next](Blocker.safariextension-global.html.md)[Previous](Blocker.safariextension-content.css.md)

# Blocker.safariextension/content.js

```
/*
    File: content.js
Abstract: Injected JavaScript file.
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

*/

// Register for the beforeload events. The beforeload event fires for all sub-resources
// (scripts, stylesheets, iframes, images, plug-ins, etc.)
document.addEventListener("beforeload", handleBeforeLoadEvent, true);

function loadContent(event)
{
    const element = event.target;

    // Restore the original className.
    element.className = element.className.replace(" blocked-content", "");

    // Remove the click event listener.
    element.removeEventListener("click", loadContent, true);

    // Mark the element as allowed to load. This property is used by handleBeforeLoadEvent.
    element.allowedToLoad = true;

    // Remove the element and reinsert it to trigger a load.
    var nextSibling = element.nextSibling;
    var parentNode = element.parentNode;
    parentNode.removeChild(element);
    parentNode.insertBefore(element, nextSibling);

    // Stop event propagation and prevent the default action so the click does not trigger
    // anything else in the page, like following a link.
    event.stopPropagation();
    event.preventDefault();
}

function handleBeforeLoadEvent(event)
{
    const element = event.target;

    // Return early, allowing the load to occur, if the element has the allowedToLoad property.
    // This property is set in loadContent when the element is clicked.
    if (element.allowedToLoad)
        return;

    // Call up to the global page using the special canLoad function. This sends a
    // synchronous message event, so it blocks while waiting for an answer.
    // If canLoad returns true return early, allowing the load to occur.
    if (safari.self.tab.canLoad(event, { url: event.url, nodeName: element.nodeName }))
        return;

    // Since the load should be blocked, call preventDefault on the event to block it.
    event.preventDefault();

    // Add the 'blocked-content' class so our injected style will style this element.
    element.className += " blocked-content";

    // Add a click event listener so when the user clicks the element we can load the content.
    // It is a capture event listener (true for the third argument) so we get first chance
    // to handle the click, so images inside links don't follow the link for the first click.
    element.addEventListener("click", loadContent, true);
}
```

[Next](Blocker.safariextension-global.html.md)[Previous](Blocker.safariextension-content.css.md)

