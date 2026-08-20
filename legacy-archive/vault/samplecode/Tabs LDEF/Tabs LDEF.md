---
title: Tabs LDEF
apple_id: DTS10000621
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Tabs_LDEF/Introduction/Intro.html
archived_at: '2026-07-18T03:26:18.423959Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AppleEvents.c.md)

# Tabs LDEF

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

"Tabs LDEF" is a custom list definition which allows developers to easily create multiple columned lists using different sizes. While the List Manager does support multiple columns, a problem can occur because each column must be of the same size. We sometimes receive questions from developers asking if it's possible to work around this limitation, because they want to add extra fields to their existing single column lists. Unless you have two or more columns of text all displaying fields of very similar sizes, you can't get a useful display of the fields. Since it's common to have variably sized columns of data with most user interface designs, developers often decide not to add additional information to an existing single column list due to the amount of work involved. While working around this limitation directly within the current List Manager is not practical, there is another approach developers can take. This LDEF supports tabbed text within a single List Manager column, which allows you to add additional fields or columns to their user interfaces quickly and easily. It also demonstrates: -A list definition implementation. -A technique to help you debug stand-alone code. -An example of how to build a safe fat resource. -Use of the new accessor routines which are provided as the first step to being Copland-savvy.

[Next](AppleEvents.c.md)

