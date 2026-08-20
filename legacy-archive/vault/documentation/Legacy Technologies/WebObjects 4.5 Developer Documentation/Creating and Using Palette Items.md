---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.3b.html
archived_at: '2026-07-15T08:10:34.846420Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Palettes.md) [!](Palettes.md) [!](Changing%20a%20Palette%20Icon.md)

---

#   Creating and Using Palette Items

To add an item from a component to a palette:

1. 

   Make the palette editable.

   If the palette's background is gray, you can't make any changes to it. To enable editing, choose Make Editable from the Palettes pull-down list. The palette's background changes to white and its title is appended with "Alt-drag to insert item."
   __Note:__

   You can't make pre-configured palettes editable.
2. 

   In the component window, select the element or elements that you want to add to the palette.
3. 

   Hold down the Alt key and drag the selection to the palette.

   The cursor changes to !
   and displays in the palette when you are done dragging. You can change the title of the item by selecting its name and typing. To change the item's icon, see [Changing a Palette Icon](Changing%20a%20Palette%20Icon.md#apple-geydgobq)
   .

You can also add any item from the file system to a palette (including such things as a component, an image, or an EOModel). To do so:

1. 

   Make the palette editable.
2. 

   Locate the item in the file system.
3. 

   Drag the item onto the palette.

   For example, to add a component to a palette, you would drag its __.wo__
   folder to the palette.

When you are done adding elements to your palette, choose Save Palette or Save Palette As from the Palettes pull-down list.

To copy an item from a palette to the component window:

1. 

   Make sure the palette is not editable (if its background is white, choose Make Uneditable from the Palettes pull-down list).

   __Note:__
   If the palette is editable, you can drag the item to the window, but it will disappear from the palette.
2. 

   Drag the item from the palette to the location in the component window where you want it to appear.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Palettes.md) [!](Palettes.md) [!](Changing%20a%20Palette%20Icon.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
