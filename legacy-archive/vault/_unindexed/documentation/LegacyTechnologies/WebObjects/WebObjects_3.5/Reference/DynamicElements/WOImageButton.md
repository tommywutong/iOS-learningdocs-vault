---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOImageButton.html
archived_at: '2026-07-15T07:55:28.383786Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOImage.md)

## WOImageButton

### Synopsis

__WOImageButton { filename__=_anImageName___;__ [__framework__=_aFrameworkName_|__"app";__] | __src__=_aURL___;__ | __value__=_aMethod___;__ __action__=_aMethod___;__ [__imageMapFile__=_aString_]; [__name__=_aString___;__] [__x__=_aNumber___;__ __y__=_aNumber___;__] [__disabled__=YES|NO__;__] ... };

### Description

WOImageButton is a graphical submit button. Clicking the image generates a request and submits the enclosing form's values. You often use WOImageButton when you need more than one submit button within a form.

**__filename__**
: Path to the image relative to the __WebServerResources__ directory.

**__framework__**
: Framework that contains the image file. This attribute is only necessary if the image file is in a different location from the component. That is, if the component and the image file are both in the application or if the component and the image file are both in the same framework, this attribute isn't necessary. If the image file is in a framework and the component is in an application, specify the framework's name here (minus the __.framework__ extension). If the image file should be in the application but the component is in a framework, specify the __"app"__ keyword in place of the framework name.

**__src__**
: URL containing the image data. Use this attribute for complete URLs; for relative URLs use __filename__ instead.

**__value__**
: Image data in the form of a WOElement object. This data can come from a database, a file, or memory.

**__action__**
: Action method to invoke when this element is clicked.

**__imageMapFile__**
: Name of the image map file. See the [WOActiveImage](WOActiveImage.md#apple-gyydg) description for more information.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__x__, __y__**
: If specified, returns the coordinates of the user's click within the image.

**__disabled__**
: If __disabled__ evaluates to YES, the element generates a static image (<IMG>) instead of an active image.

### Examples

[An image as a button](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=ImageButtonEx)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOJavaScript.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
