---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.c.html
archived_at: '2026-07-15T05:24:01.800043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.b.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.d.md)

---

#   Definition Function Mapping and Program Registration

One way the Appearance Manager coordinates the system's look and behavior is by 

mapping standard pre-Appearance Manager definition functions (the
'MBDF' 0
,
'MDEF' 0
,
'WDEF' 0
,
'WDEF' 124
,
'CDEF' 0
,
'CDEF' 1
, and
'CDEF' 63
resources) to their theme-compliant equivalents. With Appearance Manager 1.1, mapping always occurs systemwide. Prior to Appearance Manager 1.1, the user can turn off 

systemwide appearance and, therefore, systemwide mapping. Programs can ensure that their standard interface elements are mapped--with any version of the Appearance Manager--by registering with the Appearance Manager. See [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
for more details on registering your program.

[Figure 2-10](#apple-gi3teojr)
shows how the Appearance Manager determines whether mapping occurs for standard definition functions.

__Figure 2-10__  Mapping of standard definition functions

!

Some mapped definition functions have a slightly different look and behavior than if they were specified directly. For example, since a standard pre-Appearance Manager window definition function can't specify the inclusion of a horizontal zoom box, when the old resource is mapped to a new one, the resulting window still won't have a horizontal zoom box. For this reason (and to eliminate the time spent going through the mapping layer), it's recommended that you specify theme-compliant definition function IDs directly.

> ####  Note
>
> 
>
> Custom definition functions cannot be mapped automatically to theme-compliant equivalents. However, the Appearance Manager does provide functions that you can use to coordinate specific custom interface elements with themes.

The Appearance Manager provides the following functions for registering your program:

- 

  RegisterAppearanceClient
  registers your program with the Appearance Manager.
- 

  UnregisterAppearanceClient
  informs the Appearance Manager that your program is no longer its client.
- 

  IsAppearanceClient
  returns whether a given process is currently registered as a client of the Appearance Manager.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.b.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.d.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
