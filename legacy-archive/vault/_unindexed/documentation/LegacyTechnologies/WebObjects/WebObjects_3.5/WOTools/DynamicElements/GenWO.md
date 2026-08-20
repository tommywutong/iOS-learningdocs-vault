---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/GenWO.htm
archived_at: '2026-07-15T07:56:31.562049Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](CustomWO.md)[Previous
Section](CustomWO.md) 

## Generic WebObjects

You can use the generic WebObject element to create
a dynamic version of any HTML element.

To create a dynamic version of a standard HTML element):

1. Create the element (say, a heading). 
2. In the Inspector, click Make Dynamic. 
!

If the element has no specific dynamic counterpart, it becomes a generic
WebObject element.

!
To create a generic WebObject corresponding to any
HTML element (even ones not supported by WebObjects Builder):

1. Click ! in the toolbar. 
2. Bring up the Inspector. 
!

A generic WebObject element has one required attribute, __elementName__,
which specifies what type of element should be generated at run time.

For example, imagine that a future version of HTML adds a container
element called <BLOB>, which you would like to generate dynamically
in your component. You would:

3. Type BLOB between the quotes in the Binding column. 

If the name isn't in quotes, WebObjects assumes it is a binding that
should be resolved at run time. You might use that technique if you wanted
to choose the type of element programmatically rather than specifying it
in advance.

4. Check "Element is container". 
5. Use the Add Attribute button to specify any additional properties of the
   element.

[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](DynImgs.md)[Next
Section](DynImgs.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
