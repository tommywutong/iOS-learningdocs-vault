---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOEmbeddedObject.html
archived_at: '2026-07-15T07:49:38.178724Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOConditional.md)

---

# __WOEmbeddedObject__

### Synopsis

__WOEmbeddedObject__ __{value__=_`aMethod`___;__ | __src__=_`aURL`___;__ ... __};

### Description__

A WOEmbeddedObject provides support for Netscape plug-ins. It corresponds to the HTML element <EMBED SRC = >. If the embedded object's content comes from outside the WebObjects application, use the __src__ attribute. If the embedded object's content is returned by a method within the WebObjects application, use the __value__ attribute.

**__value__**
: Method that will supply the content for this embedded object.

**__src__**
: External source that will supply the content for this embedded object.

### Examples

[A VRML plug-in](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=Vrml)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOForm.md)
