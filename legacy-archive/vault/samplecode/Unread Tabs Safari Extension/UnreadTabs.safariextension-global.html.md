---
title: Unread Tabs Safari Extension
apple_id: DTS40011114
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/UnreadTabsSafariExtension/Listings/UnreadTabs_safariextension_global_html.html
archived_at: '2026-07-18T03:27:35.211899Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unread Tabs Safari Extension](Unread%20Tabs%20Safari%20Extension.md)


[Next](Document%20Revision%20History.md)[Previous](ReadMe.txt.md)

# UnreadTabs.safariextension/global.html

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

Copyright (C) 2011 Apple Inc. All Rights Reserved.

-->

<!DOCTYPE HTML>
<script>
var unreadTabs = [];

safari.application.addEventListener("open", openHandler, true);
safari.application.addEventListener("close", closeHandler, true);
safari.application.addEventListener("activate", activateHandler, true);

safari.application.addEventListener("validate", validateHandler, true);

safari.application.addEventListener("command", commandHandler, true);
safari.application.addEventListener("menu", menuHandler, true);

function openHandler(event)
{
    // Open events are sent for both windows and tabs. When a tab is opened, keep track of it in
    // the list of unread tabs until it has been read (activated) or closed.
    if (event.target instanceof SafariBrowserTab)
        unreadTabs.push(event.target);
}

function removeTabFromUnreadTabs(tab)
{
    var index = unreadTabs.indexOf(tab);
    if (index === -1)
        return;
    unreadTabs.splice(index, 1);
}

function closeHandler(event)
{
    // Close events are sent for both windows and tabs.
    if (event.target instanceof SafariBrowserTab)
        removeTabFromUnreadTabs(event.target);
}

function activateHandler(event)
{
    // Activate events are sent for both windows and tabs.
    if (event.target instanceof SafariBrowserTab) {
        // Once a tab has been activated, the user has seen its contents. Remove it from the list
        // of unread tabs.
        removeTabFromUnreadTabs(event.target);
    }
}

function validateHandler(event)
{
    // Check the command to determine if the validate event is for the toolbar item, since validate
    // events will also be sent for menu items.
    if (event.command !== "unreadTabs")
        return;

    var toolbarItem = event.target;
    var unreadTabsInWindow = 0;
    for (var i = 0; i < unreadTabs.length; ++i) {
        const tab = unreadTabs[i];
        // Count only the tabs in the window which is showing this instance of the toolbar item.
        if (tab.browserWindow === toolbarItem.browserWindow)
            ++unreadTabsInWindow;
    }

    toolbarItem.disabled = !unreadTabsInWindow;
    toolbarItem.badge = unreadTabsInWindow ? unreadTabsInWindow : null;
}

function commandHandler(event)
{
    // Handle the command event sent when the "Close all read tabs" menu item is selected.
    if (event.command === "closeAllReadTabs") {
        var readTabs = [];
        // Gather all the read tabs before closing them so that we don't accidentally activate and
        // then remove a tab the user has not read in the process of closing all read tabs.
        var currentTabs = safari.application.activeBrowserWindow.tabs;
        for (var i = 0; i < currentTabs.length; ++i) {
            var currentTab = currentTabs[i];
            if (unreadTabs.indexOf(currentTab) !== -1)
                continue;
            readTabs.push(currentTab);
        }
        for (var i = 0; i < readTabs.length; ++i)
            readTabs[i].close();
        return;
    }

    // Handle the command events sent when one of the unread tab menu items is selected.
    // In menuHandler, the identifier, and therefore the command, was set to be the index into
    // the list of unread tabs.
    if (event.command in unreadTabs)
        unreadTabs[event.command].activate();
}

function menuHandler(event)
{
    // Remove all the menu items except the one for closing all the read tabs.
    while (event.target.menuItems.length - 1)
        event.target.removeMenuItem(1);

    if (!unreadTabs.length)
        return;

    // Add a separator so that the user doesn't confuse "Close all read tabs" with just another
    // unread tab.
    event.target.appendSeparator("unreadTabsSection");

    // Add a menu item for each unread tab.
    for (var i = 0; i < unreadTabs.length; ++i) {
        const tab = unreadTabs[i];
        // Only add a menu item for the tabs in the window which is showing this instance of the
        // menu.
        if (tab.browserWindow === safari.application.activeBrowserWindow) {
            // Create a new menu item, using the index into the list of unread tabs as the
            // identifier and the title of the tab as the title of the menu item.
            var menuItem = event.target.appendMenuItem(i, tab.title);
            // Use the favicon of the site currently being displayed in the tab as the image for
            // the menu item, if there is one. This will not work for all sites, since not all
            // sites place their favicon at top level.
            menuItem.image = "http" + tab.url.match(/:\/\/(.[^/]+)/)[0] + "/favicon.ico";
        }
    }
}
</script>
```

[Next](Document%20Revision%20History.md)[Previous](ReadMe.txt.md)

