---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/DynLinks.htm
archived_at: '2026-07-15T07:56:28.599892Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](DynString.md)[Previous
Section](DynString.md) 

## Dynamic Hyperlinks

Dynamic hyperlinks (WOHyperlink) allow you to specify
the link's destination at run time rather than at compile time. There are
several ways to do this:

- You can specify the name of a page in your application as the destination
  of the link. To do this, bind the name to the WOHyperlink's __pageName__attribute. This is useful since pages in a WebObjects application don't
  have predictable URLs that you can specify in an HTML hyperlink. 
- You can specify an action to be performed when the hyperlink is clicked
  by binding WOHyperlink's __action__ attribute to an action method in
  your code. This method can perform any sort of action, as well as returning
  a page as the destination. 
- You can also specify a URL as the destination by binding to the __href
  attribute.__

To create a dynamic hyperlink:

1. Click ! in the toolbar. 
2. Replace the word Hyperlink with the text of the link. 
3. Create the element's bindings.

To learn how to create a static hyperlink, see ["Creating
Hyperlinks"](../Editing/CreatLnk.md#apple-gu3tcoa).

[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](Reps.md)[Next
Section](Reps.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
