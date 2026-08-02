---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.16.html
archived_at: '2026-07-15T05:23:56.492542Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.15.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.17.md)

---

#    Obtaining Device Color and Depth Information

To be truly theme-compliant, your program should use the QuickDraw function
DeviceLoop
with all of its drawing.
DeviceLoop
automatically supplies your application with the color and depth information that you need to supply to many Appearance Manager functions.

If your program is not drawing via
DeviceLoop
, your program should obtain the color and depth information itself. You typically do this by calling the QuickDraw function
GetGDevice
. Your program then examines the
GDevice
structure for the current device's color and depth information, as shown in [Listing 3-2](#apple-gmytgmrv)
. Note that the example shown may not produce optimal results when you are drawing across multiple monitors with different bit depths.

__Listing 3-2__  

Obtaining color and depth information for the current device

`

// Is the current device a color device?
static pascal Boolean MyGraphicDeviceIsColor (GDHandle gdh)
{
    if (!gdh) gdh = GetGDevice ( );
    return ((1 << gdDevType) & (**gdh).gdFlags) != 0;
}

// What is the bit depth of the current device?
static pascal short MyGetGraphicDeviceDepth (GDHandle gdh)
{
    if (!gdh) gdh = GetGDevice ( );
    return (**((**gdh).gdPMap)).pixelSize;
}`

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.15.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.17.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
