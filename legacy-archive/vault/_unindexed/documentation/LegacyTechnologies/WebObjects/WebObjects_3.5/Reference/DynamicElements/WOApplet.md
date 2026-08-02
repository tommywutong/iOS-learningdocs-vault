---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOApplet.html
archived_at: '2026-07-15T07:55:21.402351Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOActiveImage.md)

## Java Support: WOApplet and WOParam

### Synopsis

__WOApplet__ __{ code__=_javaClassName___;__ __width__=_aWidth___;__ __height__=_aHeight___;__ [__associationClass__=_className___;__] [__codeBase__=_aPath_;] [__archive__=_jarFile1_[__,__ _jarFile2_]__;__] [__archiveNames__=_jarFile1_[__,__ _jarFile2_]__;__] [__object__=_serializedApplet___;__] [__hspace__= _aSize___;__] [__vspace__=_aSize___;__] [__align__=_aString_]... __};__
__WOParam__ __{__ __name__=_aString___;__ __value__=_aString_ | __action__=_aMethod___;__ ... __};__

### Description

WOApplet is a dynamic element that generates HTML to specify a Java applet. The applet's parameters are passed by one or more WOParam elements.

You use the WOApplet element when you want to include applets or client-side components in your page. For more information on using WOApplet to specify a client-side component, see the _[Client-Side Applet Controls Reference](../ClientSideComponents/Applets/CSControls.mif.book.md)_.

#### WOApplet:

**__code__**
: Name of the Java class.

**__width__**
: Width, in pixels, of the area to allocate for the applet.

**__height__**
: Height, in pixels, of the area to allocate for the applet.

**__associationClass__**
: Name of Java subclass of __next.wo.client.Association__ that aids in communication between client applet and the server.

**__codeBase__**
: Directory that contains the applet code. If this attribute is omitted, the applet code is assumed to be in the same directory as the template HTML file.

**__archive__**
: Comma-separated list of URLs for jar archive files containing classes and other resources that will be preloaded. (__Note:__ Currently, most browser do not support a comma-separated list, so only a single archive file may be used.) Use this attribute for archive files that you have generated outside of a WebObjects application or framework. The value for this attribute is appended to the __archiveNames__ attribute value.

**__archiveNames__**
: Comma-separated list of archive files containing classes and other resources that will be preloaded. (__Note:__ Currently, most browser do not support a comma-separated list, so only a single archive file may be used.) Use this attribute for archive files that are built as part of a WebObjects application or framework project.

**__object__**
: File containing serialized representation of the applet.

**__hspace__**
: Amount of whitespace (in pixels) to the left and right of the applet.

**__vspace__**
: Amount of whitespace (in pixels) at the top and bottom of the applet.

**__align__**
: Alignment of the applet. Possible values are __top__, __bottom__, __left__, __right__, and __middle__.

#### WOParam:

**__name__**
: Symbolic name associated with this element's value.

**__value__**
: Value of this parameter.

**__action__**
: Method that sets the parameter's value. Use this attribute instead of __value__ if you want the parameter to be a WebObjects component.

### Examples

[Blinking text](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=AppletEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOBody.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
