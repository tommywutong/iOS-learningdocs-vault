---
title: Unread Tabs Safari Extension
apple_id: DTS40011114
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/UnreadTabsSafariExtension/Introduction/Intro.html
archived_at: '2026-07-18T03:27:35.137026Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Unread Tabs Safari Extension

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2011-06-07 This extension keeps track of unread tabs. It includes a menu that can be used to navigate to an unread tab or close all read tabs, and a badge that displays the count of unread tabs. |
| __Build Requirements:__ | Safari v5.1 or later |
| __Runtime Requirements:__ | Safari v5.1 or later |

This extension uses the open, close, and activate events to keep track of the unread tabs in each window. When a tab is opened, it is added to a list of unread tabs. When a tab is activated or closed, it is removed from that list of unread tabs.

When the user clicks on the toolbar item which shows a badge with the number of unread tabs in its window, a menu is shown with a list of the unread tabs. The user can then select an item to go to the unread tab, or choose to close all the tabs that are already read.

[Next](ReadMe.txt.md)

