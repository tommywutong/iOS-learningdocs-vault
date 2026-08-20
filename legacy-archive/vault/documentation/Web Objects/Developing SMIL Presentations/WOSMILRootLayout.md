---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILRootLayout.html
archived_at: '2026-07-18T02:20:18.611875Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILHeadLayout.md) [!](WOSMILRegion.md)

## WOSMILRootLayout

This element corresponds to the `<root-layout>` tag.
It provides the layout information for the presentation's window. [Table 4-5](#apple-ijbegsciifbuc) and [Table 4-6](#apple-ijbegrkijjeus) describe
its bindings.

__Table
4-5 Basic bindings of the WOSMILRootLayout
element__

| Binding | Description |
| `bgcolor` | Background color of the region. You can use hexadecimal values or names. Examples: `"FFFFFF"` or `"blue"`. |
| `height` | Determines the height of the presentation's window in pixels. |
| `skipContent` | Used for future extensibility of SMIL. Value: `"true"` or `"false"`. |
| `width` | Determines the width of the presentation's window in pixels. |

__Table
4-6 Additional bindings of the WOSMILRootLayout
element__

| Binding | Description |
| `elementID` | Name of this element. |
| `title` | Meaningful description for this element. |

[!](WOSMILHeadLayout.md) [!](WOSMILRegion.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
