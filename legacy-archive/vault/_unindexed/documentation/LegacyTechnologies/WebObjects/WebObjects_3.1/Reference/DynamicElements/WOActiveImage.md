---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOActiveImage.html
archived_at: '2026-07-15T07:49:34.678852Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](HowTo.md)

---

# WOActiveImage

### Synopsis

**__WOActiveImage__ __{__ __src__=_`aPath`_ | __value__=_`aMethod`___;__ __action__=_`aMethod`_ | __href__=_`aURL`___;__ [__imageMapFile__=_`aString`___;__] [__name__=_`aString`___;__] [__x__=_`aNumber`___;__ __y__=_`aNumber`___;__] [__target__=_`frameName`___;__] [__disabled__=YES|NO__;__] ... __};__**

### Description

A WOActiveImage displays an image within the HTML page. If the WOActiveImage is disabled, it simply displays its image as a passive element in the page. If enabled, the image is active, that is, clicking the image generates a request.

If located outside an HTML form, a WOActiveImage functions as a mapped, active image. When the user clicks such a WOActiveImage, the coordinates of the click are sent back to the server. Depending on where the user clicks, different actions can be invoked. An image map file associates actions with each of the defined areas of the image.

Within an HTML form, a WOActiveImage functions as a graphical submit button. You typically use WOActiveImages when you need more than one submit button within a form.

**__src__**
: Path to the file containing the image data. __src__ can be statically specified in the declarations file, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

**__value__**
: Image data in the form of a WOElement object. This data can come from a database, a file, or memory.

**__action__**
: Method to invoke when this element is clicked. If __imageMapFile__ is specified, __action__ is only invoked if the click is outside any mapped area. In other words, __action__ defines the default action of the active image.

**__href__**
: URL to direct the browser to as a default when the image is clicked and no hot zones are hit.

**__imageMapFile__**
: Name of the image map file.

**__name__**
: If __name__ is specified then the hit point is specified as __name.x__=_`value`_; __name.y__=_`value`_; in the form. This is useful when you need to use this element to submit a form to an external URL that expects the hit point to be expressed in a certain format.

**__x, y__**
: If specified, returns the coordinates of the user's click within the image.

**__target__**
: Frame in a frameset that will receive the page returned as a result of the user's click.

**__disabled__**
: If YES, a regular image element (<IMG>) is generated rather than an active image.

### The Image Map File

If __imageMapFile__ is specified, WebObjects searches for the file within the component bundle (_`Component`_.wo/). If it isn't found there, WebObjects searches the application directory (_`MyApplication`_.woa/).

Each line in the image map file has this format:

```
  shape action coordinate-list
```

**__shape__**
: Either `rect' or `circle' (polygon not yet supported). For `rect' shape, the coordinates x1,y1 specify the upper-left corner of the hot zone, and x2,y2 specify lower right corner. For `circle' shape, the x1,y1 is the origin, and x2,y2 is a point on the circle.

**__action__**
: Name of the method to invoke.

**__coordinate-list__**
: x1, y1 x2, y2 ...

Here's an example of an image map file:

```
  rect  home  0,0 135,56
```

```
  rect  buy  135,0 270,56
```

### Examples

[Image-mapped active image](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=ActiveImageEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOApplet.md)
