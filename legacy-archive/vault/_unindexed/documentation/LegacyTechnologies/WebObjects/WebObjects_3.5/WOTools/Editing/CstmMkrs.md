---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/CstmMkrs.htm
archived_at: '2026-07-15T07:56:56.992743Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](StrucEle.md)[Previous
Section](StrucEle.md) 

## Custom Marker

Not all legal HTML elements can be created directly
using WebObjects Builder's buttons or menu commands. However, you can create
any type of element using the custom tag.

To create an HTML element using a custom marker:

1. Place the cursor where you want the element. 
2. Click !. 
   ! appears in the component window. You can replace
   the text "Custom Marker" with the content of the element (if any).

 3. In the Inspector, enter the tag's name in the Marker field. 
4. If the element doesn't require an end tag, uncheck "Needs end marker." 
5. If the element has attributes you want to specify, click New Attribute,
   then enter the attribute's name and value. 
!
For example, if you want to create a <DL> element,
you would create a custom marker and enter DL for its name in the Inspector's
Marker text field. Because "Needs end marker" is checked, the </DL>
end tag is inserted for you.

You can also enter source editing mode and
type the marker and its text directly.

__Tip:__ To save a custom element so you
can use it again, save it on a palette. See ["Palettes"](Pallette.md#apple-geytcnjv).

## Removing Elements or Text From a Container

You can remove an element or text from a containing
element. For example, if you've typed some text inside a form, but you
decide you want the text to be _outside_ the form:

1. Select the text. 
2. Click ! or choose Elements !Promote
   Selection. 

This causes the text to be removed from the form.

[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](WrkTabls.md)[Next
Section](WrkTabls.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
