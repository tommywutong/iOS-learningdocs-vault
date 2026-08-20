---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/CreateWOHyperlink.html
archived_at: '2026-07-15T07:50:24.882718Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElem.book.md)
[!Previous Section](UndoBinding.md)

Creating Dynamic Hyperlinks

# Creating Dynamic Hyperlinks

Drag a WOHyperlink from the Abstract Elements palette to the component window.

Replace the word `Hyperlink` with the text of the link.

[Bind](BindElements.md) the hyperlink to a variable or a method.

!

WebObjects Builder allows you to create either static hyperlinks or dynamic hyperlinks (which are WOHyperlink dynamic elements). Use WOHyperlink instead of a static hyperlink when:

- You want to link to a page that's returned by a component in your application. Pages in a WebObjects application don't have predictable URLs that you can specify in an HTML hyperlink.

  In this case, you can bind to WOHyperlink's __pageName__ attribute. Specify the component's name in the bindings inspector's text field. See "[Binding Elements Using the Inspector](BindInInspector.md#apple-kjcumobtha3tm)."
- You want the hyperlink to perform an action rather than return a page.

  In this case, you can bind to WOHyperlink's __action__ attribute. Specify the method that should be invoked when the link is clicked.
- You want the hyperlink's destination to be determined at run time.

  In this case, you can bind to WOHyperlink's __action__ attribute. Specify a method that determines which page should be returned when the link is clicked.

The inspector shows a complete list of the WOHyperlink attributes you might bind to, and the [WOHyperlink](../../Reference/DynamicElements/WOHyperlink.md) description in the _WebObjects Reference_ contains complete descriptions of them.

To learn how to create a static hyperlink, see "[Creating Hyperlinks](../HTMLEdit/CreateHyperlinks.md)."

[!Table of Contents](DynElem.book.md)
[!Next Section](CreateWORepetition.md)
