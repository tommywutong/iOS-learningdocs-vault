---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.3d.html
archived_at: '2026-07-15T08:10:35.021439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Changing%20a%20Palette%20Icon.md) [!](Attributes.md)

---

# Working With Dynamic Elements

###  Introduction to Dynamic Elements

A _dynamic element_
is an element whose exact HTML representation isn't determined until run time. Dynamic elements are represented in the HTML template by the tag

<WEBOBJECT>.

There are several types of dynamic elements that you can use in your WebObjects applications. Some of them (such as dynamic forms or images) have counterparts in standard HTML (<FORM> and <IMG>) and are always translated into those counterparts at run time. These are known as _concrete_
dynamic elements. Others (such as conditionals and repetitions) don't translate directly into HTML but control the generation of other elements. These are known as _abstract_
dynamic elements.

This chapter describes the techniques you use to add dynamic elements to your components and to bind them to variables and methods in your code. For more information on programming with dynamic elements, see 

"Dynamic Elements" in the _WebObjects Developer's Guide_
. For details about specific dynamic elements, see the _Dynamic Elements Reference_
.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Changing%20a%20Palette%20Icon.md) [!](Attributes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
