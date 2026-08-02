---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILSwitch.html
archived_at: '2026-07-18T02:20:18.764118Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILRegion.md) [!](WOSMILMediaObject.md)

## WOSMILSwitch

This element corresponds to the `<switch>` tag.
It defines a set of elements from which only one element is to be
chosen using each element's system bindings as the criteria. You should
list media elements inside a WOSMILSwitch element in order, starting
with the one that requires the highest system capabilities to the
one that requires the least. (See ["System-Attribute Bindings"](System_Attribute_Bindings.md#apple-ijbegr2djjeui) for
more information on system bindings.) Also, you should always include
a default element (one that doesn't have any system bindings)
as the last element of the list. The binding of the WOSMILSwitch
element is listed in [Table 4-9](#apple-ijbegq2jinbem).

__Table
4-9 Basic binding of the WOSMILSwitch element__

| Binding | Description |
| `title` | Meaningful description for this element. |

[!](WOSMILRegion.md) [!](WOSMILMediaObject.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
