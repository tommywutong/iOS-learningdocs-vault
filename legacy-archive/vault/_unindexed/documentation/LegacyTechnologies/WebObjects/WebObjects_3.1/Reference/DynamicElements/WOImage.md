---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOImage.html
archived_at: '2026-07-15T07:49:41.729561Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOHyperlink.md)

---

# __WOImage__

### Synopsis

__WOImage__ __{__ __src__=_`aPath`_ | __value__=_`imageData`___;__ ... __};

### Description__

A WOImage displays an image in the HTML. It corresponds to the HTML element <IMG SRC="URL">.

**__src__**
: Path to the file containing the image data. The source can be statically specified in the declaration file or it can be an NSString, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

**__value__**
: Image data in the form of a WOElement object. This data can come from a database, a file, or memory.

### Examples

[Simple example](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=ImagesEx1)

[Daily image](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=ImagesEx2)

[Image data from a file](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=ImagesEx3)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOJavaScript.md)
