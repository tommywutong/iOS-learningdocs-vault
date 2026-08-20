---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILSeq.html
archived_at: '2026-07-18T02:20:18.681623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILMediaObject.md) [!](WOSMILPar.md)

## WOSMILSeq

This element encloses a group of elements that are rendered
in sequence; it corresponds to the `<seq>` tag.
The element's bindings are described in [Table 4-12](#apple-ijbegr2fijfeq) and [Table 4-13](#apple-ijbegrceirbuc).

__Table
4-12 Basic binding of the WOSMILSeq element__

| Binding | Description |
| `title` | Meaningful description for this element. |

__Table
4-13 Additional bindings of the WOSMILSeq
element__

| Binding | Description |
| `abstract` | Brief description of this element. |
| `author` | The author of the sequence. |
| `begin` | The start time for this element. |
| `dur` | The length of time this element is to be displayed. |
| `end` | The end time of this element. |
| `elementID` | Uniquely identifies this element within the presentation. |
| `regionID` | Added for completeness. Cannot be used in this element. |
| `repeat` | Determines the end time of this element. Value: an integer value or `"indefinite"`. |
| _system attribute_ | See ["System-Attribute Bindings"](System_Attribute_Bindings.md#apple-ijbegr2djjeui). |

[!](WOSMILMediaObject.md) [!](WOSMILPar.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
