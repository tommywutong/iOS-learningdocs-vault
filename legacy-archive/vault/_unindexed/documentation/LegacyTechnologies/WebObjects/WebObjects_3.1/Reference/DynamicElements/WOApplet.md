---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOApplet.html
archived_at: '2026-07-15T07:49:35.717747Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOActiveImage.md)

---

# __Java Support: WOApplet and WOParam__

### Synopsis

__WOApplet__ __{ code__=_`javaClassName`___;__ __width__=_`aWidth`___;__ __height__=_`aHeight`___;__ [__associationClass__=_`className`_;] [__codeBase__=_`aPath`_;] ... __};__

__WOParam__ __{__ __name__=_`aString`___;__ __value__=_`aString`_ | __action__=_`aMethod`___;__ ... __};

### Description__

WOApplet is a dynamic element that generates HTML to specify a Java applet. The applet's parameters are passed by one or more WOParam elements.

#### __WOApplet:__

**code**
: Name of the Java class.

**__width__**
: Width, in pixels, of the area to allocate for the applet.

**__height__**
: Height, in pixels, of the area to allocate for the applet.

**__associationClass__**
: Name of Java class that aids in communication between client applet and the server.

**__codeBase__**
: Directory that contains the applet code. If this attribute is omitted, the applet code is assumed to be in the same directory as the template HTML file.

#### __WOParam:__

**name**
: Symbolic name associated with this element's value.

**__value__**
: Value of this parameter.

**__action__**
: Method that the applet will invoke.

### Examples

[Blinking text](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=AppletEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOBrowser.md)
