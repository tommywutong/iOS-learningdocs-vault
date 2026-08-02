---
title: stdFilterHacking
apple_id: DTS10000619
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/stdFilterHacking/Introduction/Intro.html
archived_at: '2026-07-26T19:52:28.332335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](stdFilterHacking.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# stdFilterHacking

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Demonstrates problems and workarounds for/with the Standard Dialog Filter. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

For those of you who have been using the new Standard Dialog Filter in 7.0 and later (TechNote 1147 Pending Updates Perils) you may have encountered some odd behaviour when you bring up another dialog or alert in front of a dialog using the standard filter. If you have dimmed (de-hilited, disabled) the OK or Cancel button and bring up a dialog on top, when you dismiss the top dialog the dialog where the OK button was dimmed will suddenly have the OK button enabled! This is a behaviour of the standard filter. When the standard filter gets an Activate event, it will automatically enable the default and cancel buttons (set with SetDialogDefaultItem and SetDialogCancelItem), it is assuming that the only reason those buttons were disabled was because they were in a deactivated window. The filter has no state-saving routines or caches to remember what the old state of the buttons was, so it just slams them active again. This may not be what you want. If you disable an OK or Cancel button, use the standard filter, and bring another dialog or alert up on top of that dialog, you need to add a little extra code in your own filter to handle that situation. The code is included here, look in the filterIt function included in stdFilterHacking.c.

[Next](stdFilterHacking.c.md)

