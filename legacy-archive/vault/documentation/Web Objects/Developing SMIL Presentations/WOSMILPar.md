---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILPar.html
archived_at: '2026-07-18T02:20:18.490962Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILSeq.md) [!](WOSMILActiveLink.md)

## WOSMILPar

This element encloses a group of elements whose display can
overlap in time; it corresponds to the `<par>` tag. [Table 4-14](#apple-ijbegr2kifceq) and [Table 4-15](#apple-ijbegqseivcee) list
its bindings.

__Table
4-14 Basic bindings of the WOSMILPar element__

| Binding | Description |
| `title` | Meaningful description for this element. |
| `regionID` | Added for completeness. Cannot be used in this element. |

__Table
4-15 Additional bindings of the WOSMILPar
element__

| Binding | Description |
| `abstract` | Brief description of this element. |
| `author` | The author of this element. |
| `begin` | The start time for this element. |
| `copyright` | Copyright notice for this element's content. |
| `dur` | The length of time this element is to be displayed. |
| `end` | The end time of this element. |
| `endsync` | Determines when each object within the element ends. Values: `"last"`, `"first"`, `"id(`_elementID_`)"`. |
| `elementID` | Uniquely identifies this element within the presentation. |
| `repeat` | Determines the end time of this element. Value: an integer value or `"indefinite"`. |
| _system attribute_ | See ["System-Attribute Bindings"](System_Attribute_Bindings.md#apple-ijbegr2djjeui). |

[!](WOSMILSeq.md) [!](WOSMILActiveLink.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
