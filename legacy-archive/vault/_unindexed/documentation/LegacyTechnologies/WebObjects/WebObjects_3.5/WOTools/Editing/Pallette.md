---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/Pallette.htm
archived_at: '2026-07-15T07:57:13.659735Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](SetColr.md)[Previous
Section](SetColr.md)

# Palettes

A palette is a collection of resources (such as images,
static or dynamic HTML elements, and components). You can drag elements
from a palette to a component to use them. You can also drag elements from
a component to a palette to store them.

Palettes appear in WebObjects Builder's palette
window. To open the palette window, click !
on the toolbar or choose Tools !Palette.

!

The icons at the top of the palette window show the
available palettes. To select a palette, click its icon. Two pre-configured
palettes are provided: Java client-side components and components from
the WOExtensions framework.

You can create your own palettes to store frequently-used
items, such as custom forms, tables, or images, and you can load palettes
created by someone else.

To create a new palette, choose Palettes !New
Palette. A panel appears, asking you to specify a location to save the
palette. (A palette is represented on disk as a folder with the extension
__.wbpalette__.) The palette appears in the palette window with the
default palette icon !. To change the palette's
icon, see ["Changing a Palette Icon"](#apple-gy4tkny).

To add an existing palette to the palette window:

1. Choose Palettes !Open Palette. 
2. Navigate to the palette's location and click Open.

To remove a palette from the palette window:

1. Select the palette in the palette window. 
2. Choose Palettes !Close Palette.

## Creating and Using Palette Items

To add an item from a component to a palette:

1. Make the palette editable. 

If the palette's background is gray, you can't make any changes to it.
To enable editing, choose Palettes !Make Editable.
The palette's background changes to white and its title says "Alt-drag
to insert item." __Note:__ When you first create a palette, it is editable
until you save it.

2. In the component window, select the element or elements that you want to
   add to the palette. 
3. Hold down the Alt key and drag the selection to the palette. 

The cursor changes to ! and displays in the palette when you are
done dragging. You can change the title of the item by selecting its name
and typing. To change the item's icon, see ["Changing
a Palette Icon"](#apple-gy4tkny).

You can also add any item from the file system to a
palette (including such things as a component, an image, or an EOModel).
To do so:

1. Make the palette editable. 
2. Locate the item in the file system. 
3. Drag the item onto the palette. 

For example, to add a component to a palette, you would drag its __.wo__
folder to the palette.

__Note:__ On Windows NT, you can't drag an item directly to the palette,
because the palette window doesn't appear unless a WebObjects Builder window
is in the foreground. Therefore, you must drag the item to WebObjects Builder's
icon in the taskbar at the bottom of the screen and hold it until the palette
window appears. With the mouse button still down, drag the item to the
palette.

When you are done adding elements to your palette, choose
Palettes !Save Palette. The background changes
to gray, indicating that the palette is no longer editable.

To copy an item from a palette to the component
window:

1. Make sure the palette is not editable (if its background is white, choose
   Palettes !Make Editable). 

__Note:__ If the palette is editable, you can drag the item to the
window, but it will disappear from the palette.

2. Drag the item from the palette to the location in the component window
   where you want it to appear.

## Changing a Palette Icon

You can replace the icon of any palette, or any item
in a palette, with an image of your own choosing. To do so:

1. Open the palette window and select the palette whose icon you want to change. 
2. Make the palette editable. 
3. Drag an image from the file system onto the palette's icon. 

You can use any image file recognized by WebObjects Builder (such as
a __.gif__, __.tif__ or __.jpg__ file) to change the icon of a
palette or of any item in the palette.

__Note:__ The same caveat for dragging items to the palette on Windows
NT applies (see ["Creating and Using Palette
Items"](#apple-heytemi)).

4. Save the palette.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
