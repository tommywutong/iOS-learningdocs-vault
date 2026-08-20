---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/CreateAbstractElements.html
archived_at: '2026-07-15T07:50:21.385790Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElem.book.md)
[!Previous Section](ResizeElements.md)

Creating Abstract Elements

# Creating Abstract Elements

Place the cursor where you want the element.

Choose the Abstract Elements palette. (Click the palette button to bring up the [palette window](../HTMLEdit/Palettes.md).)

Drag the item from the palette onto the page.

If necessary, specify the element type in the inspector window. (Click the inspector button to bring up the [inspector window](../HTMLEdit/Inspectors.md).)

!

_Abstract elements_ are dynamic elements that don't have an HTML counterpart. You can learn more about abstract elements and other dynamic elements in the chapter "[How WebObjects Works](../../DevGuide/HowWOWorks/HowWOWorks.mif.book.md)" of the _WebObjects Developer's Guide_.

WOConditionals, WOHyperlinks, WORepetitions, and WOStrings don't need any extra setup in the inspector. To create any other type of abstract element, use the custom element and specify the element type in the inspector window. Once you have the element set up, you may want to store it on a [custom palette](../Advanced/CreatePalette.md) if you are going to use it frequently.

See "[Formatting Tips](../HTMLEdit/FormattingTips.md)" if you're having trouble editing the page.

[!Table of Contents](DynElem.book.md)
[!Next Section](CustomElement.md)
