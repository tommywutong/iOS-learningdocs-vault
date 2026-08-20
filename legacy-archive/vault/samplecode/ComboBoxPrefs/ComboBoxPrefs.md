---
title: ComboBoxPrefs
apple_id: DTS10003509
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/ComboBoxPrefs/Introduction/Intro.html
archived_at: '2026-07-18T03:04:05.646547Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# ComboBoxPrefs

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-10-04 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X |

ComboBoxPrefs maintains a list of recently accessed pictures within its combo box. It is a chronological list (CFArray) stored via CFPreferences. We also override the standard behavior of the combo box to make it more like an address bar seen in web browsers. When an item from the ComboBox list is double-clicked that item is loaded. ComboBoxPrefs also demonstrates how to create a CGImageRef from a URL pointing to a picture.

[Next](main.c.md)

