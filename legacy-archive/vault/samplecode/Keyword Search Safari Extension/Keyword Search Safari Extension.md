---
title: Keyword Search Safari Extension
apple_id: DTS40012648
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2012-06-10'
source_url: https://developer.apple.com/library/archive/samplecode/KeywordSearchSafariExtension/Introduction/Intro.html
archived_at: '2026-07-18T03:13:23.420387Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Keyword Search Safari Extension

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2012-06-10 This extension demonstrates how to handle the "beforeSearch" event. |
| __Build Requirements:__ | Safari 6.0 or later |
| __Runtime Requirements:__ | Safari 6.0 or later |

This extension handles the "beforeSearch" event to let a user search bugs.webkit.org, trac.webkit.org, and developer.apple.com via a shortcut. The shortcut is to type the first letter of the site to search, a space, then a search term. For example, if a user types "t FrameLoader" into the Safari smart search field and presses the return key, this extension will cancel the default search and instead navigate to the search results page for "FrameLoader" on trac.webkit.org.

[Next](ReadMe.txt.md)

