---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Introduction/Intro.html
archived_at: '2026-07-18T03:18:54.514806Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# PhotoSearch

|  |  |
| --- | --- |
| __Last Revision:__ | Version 3.1, 2015-12-03 Updated for 10.11 SDK, replaced deprecated APIs, improved error checking for resolving security scope bookmark search location. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojzgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X 10.11 SDK or later |
| __Runtime Requirements:__ | OS X 10.9 or later |

This sample application uses Spotlight to perform a search for images on your computer. The NSPredicateEditor is used to create a custom search query. The results are displayed in a custom NSTextFieldCell subclass that automatically adds tracking areas to perform automatic rollover highlighting effects inside the cells. A custom DateCell class is implemented that demonstrates how to properly truncate dates based on the cell size. The NSPathControl is used to display selected paths. Custom views inside a menu are shown with sample code. Finally, thread safe background thumbnail image processing is demonstrated by the data model.

PhotoSearch is App Sandboxed which offers strong defense against damage from malicious code. In doing so, it allows you to retain access to file-system resources by employing a security mechanism, known as security-scoped bookmarks, that preserves user intent between app launches. Hence, the earch location or scope becomes a security-scoped bookmark.

[Next](main.m.md)

