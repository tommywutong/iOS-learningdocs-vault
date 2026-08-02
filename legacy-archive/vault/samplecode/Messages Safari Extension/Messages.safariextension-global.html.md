---
title: Messages Safari Extension
apple_id: DTS40010124
resource_type: Sample Code
platform: Safari|macOS
topic: User Experience
technology: null
published: '2010-06-08'
source_url: https://developer.apple.com/library/archive/samplecode/MessagesSafariExtension/Listings/Messages_safariextension_global_html.html
archived_at: '2026-07-18T03:14:45.364142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Messages Safari Extension](Messages%20Safari%20Extension.md)


[Next](Read%20Me.txt.md)[Previous](Messages%20Safari%20Extension.md)

# Messages.safariextension/global.html

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
// Global variable for the unread message count. Initialize from settings.
var unreadMessages = safari.extension.settings.unreadMessages;

// Set a interval to call newMessage every 20 seconds.
setInterval(newMessage, 20000);

// Register for the validate and command events.
safari.application.addEventListener("validate", performValidate, false);
safari.application.addEventListener("command", performCommand, false);

function performValidate(event)
{
    // Switch based on the command of the event. You should always check the command.
    switch (event.command) {
    case "show-messages":
        // Set the badge of the target, if the target has a badge property.
        // Some targets that send commands, like context menu items, don't have badges.
        if ("badge" in event.target)
            event.target.badge = unreadMessages;
        break;
    }
}

function performCommand(event)
{
    // Switch based on the command of the event. You should always check the command.
    switch (event.command) {
    case "show-messages":
        // Show an alert with the number of messages.
        alert("You marked " + unreadMessages + " messages as read. Have a nice day!");

        // Reset the unread messages back to 0.
        updateUnreadMessageCount(0);
        break;
    }
}

function validateToolbarItems()
{
    // Iterate over all the toolbar items and tell them to validate, so their
    // badge will be updated.
    var toolbarItems = safari.extension.toolbarItems;
    for (var i = 0; i < toolbarItems.length; ++i) {
        // Skip any toolbar item that is not the messages item. You should always
        // check the identifier, even if your extension only has one toolbar item.
        if (toolbarItems[i].identifier !== "messages")
            continue;

        // Calling validate will dispatch a validate event, which will call
        // performValidate for each toolbar item. This is the recommended method
        // of updating items instead of directly setting a badge here, so multiple
        // event listeners have a chance to validate the item.
        toolbarItems[i].validate();
    }
}

// Function to update the unread messages count and toolbar item badges.
function updateUnreadMessageCount(count)
{
    // Set the unread message count.
    unreadMessages = count;

    // Store the value in settings so it persists between launches.
    safari.extension.settings.unreadMessages = unreadMessages;

    // Make all the toolbar items validate to update their badge.
    validateToolbarItems();
}

// Function that simulates a new message coming in.
function newMessage()
{
    updateUnreadMessageCount(unreadMessages + 1);
}
</script>
```

[Next](Read%20Me.txt.md)[Previous](Messages%20Safari%20Extension.md)

