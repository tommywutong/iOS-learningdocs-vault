---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILHeadMeta.html
archived_at: '2026-07-18T02:20:18.326060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILDocument.md) [!](WOSMILHeadLayout.md)

## WOSMILHeadMeta

This element provides information about the presentation.
It corresponds to the `<meta>` tag. Its
bindings are described in [Table 4-2](#apple-ijbegqsfijeuq) and [Table 4-3](#apple-ijbegrsijfees).

__Table
4-2 Basic bindings of the WOSMILHeadMeta
element__

| Binding | Description |
| `content` | The value of the property defined in this element. |
| `metaName` | Identifies the property defined in this element. |
| `skipContent` | Used for future extensibility of SMIL. Value: `"true"` or `"false"`. |
| `title` | Meaningful description for this element. |

__Table
4-3 Additional bindings of the WOSMILHeadMeta
element__

| Binding | Description |
| `base` | Determines the base URI for all relative URIs used in the presentation. |
| `picsLabel` | The rating label for the presentation. |
| `elementID` | Name of this element. |

[!](WOSMILDocument.md) [!](WOSMILHeadLayout.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
