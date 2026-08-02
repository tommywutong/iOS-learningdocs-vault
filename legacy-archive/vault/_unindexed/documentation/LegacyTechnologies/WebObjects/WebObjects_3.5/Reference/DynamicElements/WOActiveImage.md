---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOActiveImage.html
archived_at: '2026-07-15T07:55:20.913346Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](HowTo.md)

## WOActiveImage

### Synopsis

**__WOActiveImage__ __{filename__= _imageFileName___;__ [__framework__ = _frameworkBaseName_|__"app" ;__] | __src__=_aURL___;__ | __value__=_aMethod___;__ __action__=_aMethod_ | __href__=_aURL___;__ [__imageMapFile__=_aString_]; [__name__=_aString___;__] [__x__=_aNumber___;__ __y__=_aNumber___;__] [__target__=_frameName___;__] [__disabled__=YES|NO__;__] ... __};__**

### Description

A WOActiveImage displays an image within the HTML page. If the WOActiveImage is disabled, it simply displays its image as a passive element in the page. If enabled, the image is active, that is, clicking the image generates a request.
WOActiveImages are intended to be used outside of an HTML form. WOActiveImage functions as a mapped, active image. When the user clicks such a WOActiveImage, the coordinates of the click are sent back to the server. Depending on where the user clicks, different actions can be invoked. An image map file associates actions with each of the defined areas of the image. If an image map file is not specified, the method specified by the __action__ attribute is performed when the image is clicked, or if the __href__ attribute is specified, the image acts as a hyperlink and takes you to that destination.
Within an HTML form, a WOActiveImage functions as a graphical submit button. However, it is better to use a WOImageButton instead of WOActiveImage to create a graphic submit button or a mapped image within a form.

**__filename__**
: Path to the image relative to the __WebServerResources__ directory.

**__framework__**
: Framework that contains the image file. This attribute is only necessary if the image file is in a different location from the component. That is, if the component and the image file are both in the application or if the component and the image file are both in the same framework, this attribute isn't necessary. If the image file is in a framework and the component is in the application, specify the framework's name here (minus the __.framework__ extension). If the image file should be in the application but the component is in a framework, specify the __"app"__ keyword in place of the framework name.

**__src__**
: URL containing the image data. Use this attribute for complete URLs; for relative URLs use __filename__ instead.

**__value__**
: Image data in the form of a WOElement object. This data can come from a database, a file, or memory.

**__action__**
: Method to invoke when this element is clicked. If __imageMapFile__ is specified, __action__ is only invoked if the click is outside any mapped area. In other words, __action__ defines the default action of the active image.

**__href__**
: URL to direct the browser to as a default when the image is clicked and no hot zones are hit.

**__imageMapFile__**
: Name of the image map file.

**__name__**
: If __name__ is specified then the hit point is specified as __name.x__=_value_; __name.y__=_value_; in the form. This is useful when you need to use this element to submit a form to an external URL that expects the hit point to be expressed in a certain format.

**__x, y__**
: If specified, returns the coordinates of the user's click within the image.

**__target__**
: Frame in a frameset that will receive the page returned as a result of the user's click.

**__disabled__**
: If YES, a regular image element (<IMG>) is generated rather than an active image.

### The Image Map File

If __imageMapFile__ is specified, WebObjects searches for the file in the component bundle (_Component___.wo__), and then in the application's __WebServerResources__ directory (or in the framework's __WebServerResources__ if there's a __framework__ attribute) If it isn't found there, WebObjects searches the application directory (_MyApplication___.woa/__).
__Note:__ The image map file must be in the same location as the image. For example, if the image is in a framework, the image map file must be in that same framework.
Each line in the image map file has this format:

```
    shape action coordinate-list
```


**_shape_**
: Either __rect__, __circle__, or __poly__. For __rect__ shape, the coordinates x1,y1 specify the upper-left corner of the hot zone, and x2,y2 specify lower-right corner. For __circle__ shape, the x1,y1 is the origin, and x2,y2 is a point on the circle. For the __poly__ shape, each coordinate is a vertex. Up to 100 vertices are supported.

**_action_**
: Name of the method to invoke.

**_coordinate-list_**
: x1, y1 x2, y2 ...

Here's an example of an image map file:

```
    rect	home	0,0 135,56
    rect	buy	135,0 270,56
```


### Examples

[Image-mapped active image](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=ActiveImageEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOApplet.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
