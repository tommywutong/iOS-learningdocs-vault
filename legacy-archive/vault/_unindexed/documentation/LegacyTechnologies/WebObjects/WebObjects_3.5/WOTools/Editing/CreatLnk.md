---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/CreatLnk.htm
archived_at: '2026-07-15T07:56:54.550839Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](RowCell.md)[Previous
Section](RowCell.md) 

# Creating Hyperlinks

There are two types of hyperlinks that you can use in
a WebObjects application:

- A static hyperlink (which uses the HTML <A> tag), whose destination
  is constant. 
- A dynamic hyperlink (WOHyperlink), whose destination can be specified at
  run time. See ["Dynamic Hyperlinks"](../DynamicElements/DynLinks.md#apple-gy2dimi)for
  more information about these.

To create a static hyperlink:

1. Click ! on the toolbar. 
2. Type the text that the hyperlink should contain. As you type, the text
   is underlined. 
3. Click ! again. 

Alternatively, you can select existing text and then click !
once to convert the text to a hyperlink.

4. Use the Inspector to set the destination of the link. 
!
__Note__: While the destination of a static link
cannot change, it's possible to vary its text at run time by using a dynamic
string (see ["Dynamic Strings"](../DynamicElements/DynString.md#apple-gyztmna)) inside
the hyperlink.

[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](PgAttrib.md)[Next
Section](PgAttrib.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
