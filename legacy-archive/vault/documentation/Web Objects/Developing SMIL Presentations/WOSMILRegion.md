---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILRegion.html
archived_at: '2026-07-18T02:20:18.556223Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILRootLayout.md) [!](WOSMILSwitch.md)

## WOSMILRegion

This element defines the position, size, and scaling of media-object
elements. It corresponds to the `<region>` tag.
Its bindings are described in [Table 4-7](#apple-ijbegskdivfek) and [Table 4-8](#apple-ijbegsckizbei).

__Table
4-7 Basic bindings of the WOSMILRegion
element__

| Binding | Description |
| `bgcolor` | Background color of the region. You can use hexadecimal values or names. Examples: `"#FFFFFF"` or `"blue"`. |
| `fit` | Determines how objects are scaled or cropped when rendered within the region. Value: `"fill"`, `"hidden"`, `"meet"`, `"scroll"`, or `"slice"`. |
| `height` | Determines the height of the region. Can be specified in pixels or a percentage of the presentation's window. Examples: `"150"` or `"50%"`. |
| `left` | Determines the left coordinate of the region within the presentation's window. Can be specified in pixels or as a percentage of the presentation window's `width`. |
| `regionID` | Name of the region. |
| `skipContent` | Used for future extensibility of SMIL. Value: `"true"` or `"false"`. |
| `top` | Determines the top coordinate of the region within the presentation's window. Can be specified in pixels or as a percentage of the presentation window's `height`. |
| `width` | Determines the width of the region. Can be specified in pixels or a percentage of the display window. |

__Table
4-8 Additional bindings of the WOSMILRegion
element__

| Binding | Description |
| `title` | Meaningful description for this element. |
| `zIndex` | Determines the layer in which the region is displayed. When regions overlap, the region with the highest `zIndex` is displayed on top of the others. |

[!](WOSMILRootLayout.md) [!](WOSMILSwitch.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
