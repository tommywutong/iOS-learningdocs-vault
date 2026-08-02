---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Advanced/CreatePalette.html
archived_at: '2026-07-15T07:50:02.783858Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Advanced.book.md)
[!Previous Section](Limitations.md)

Creating a Palette

# Creating a Palette

Choose Tools->Palettes->New.

Choose a name and a location and click Open to create a new empty palette.

Add items to the palette.

- Add components to the palette by dragging them from the application window or from the file system onto the palette.
- Add other elements from the component window by [selecting them](../HTMLEdit/SelectElements.md) and then holding down the Alternate key and dragging them from the component window onto the palette.

When you're finished adding items, choose Tools->Palettes->Toggle Editing to turn off edit mode.

Save your changes by choosing Tools->Palettes->Save. Be sure to choose Save from the Palettes menu, not the File menu.

!

By creating a custom palette, you can store portions of an HTML page for later reuse. You can store any combination of elements from a page --- an individual element, several elements including text, or an entire page --- as a single palette item.

For example, you can use custom palettes to store:

- Boilerplate text, such as a header, that you add to every page
- References to all your icons and background images
- [Custom tags](../HTMLEdit/CreateCustomTags.md) that you create
- Tags that require extra set up that you use frequently (for example, if you frequently use a preformatted element, you might want to store it on the palette).
- [Reusable components](../AppSetup/ReusableComponents.md)

When storing a reusable component on a palette, you can drag it from one of three places: from the file system, from the application window, or from the parent component's window. If you drag from the parent component's window, any bindings that were made before dragging the component are preserved.

__Note:__ If you're storing a reusable component, make sure all of its exported variables are in lower-case letters. See "[Reusable Component Limitations](Limitations.md#apple-kjcumojzge4dc)"

The custom palette appears in the palette window along with the standard palettes and you use them the same way. When you first create a custom palette, it is displayed in editing mode. In this mode, you can drag items on to and off of the palette. That is, dragging an item off of a palette deletes it. When your palette is ready to use, perform the command Tools->Palettes->Toggle Editing. Editing mode is turned off, and the background becomes the same as for the other palettes. Once editing mode is turned off, dragging an element off of the palette does not remove it---it adds the element to the destination page just as you would expect. (As the command name suggests, you can use Toggle Editing to turn editing mode on again later if you wish to make changes.)

__Important:__ Images and components placed on the palette are copied into the palette. If you add an item to the palette and then wish to change the item:

1. Change the item to work the way you want.
2. Choose Tools->Palettes->Toggle Editing to turn on the palette's editing mode.
3. Drag the original version of item off of the palette.
4. Drag the new version onto the palette.

[!Table of Contents](Advanced.book.md)
[!Next Section](LoadUnloadPalettes.md)
