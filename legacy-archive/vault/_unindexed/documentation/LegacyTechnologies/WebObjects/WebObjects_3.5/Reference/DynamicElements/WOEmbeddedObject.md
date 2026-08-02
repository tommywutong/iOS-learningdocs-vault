---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOEmbeddedObject.html
archived_at: '2026-07-15T07:55:24.375578Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOConditional.md)

## WOEmbeddedObject

### Synopsis

__WOEmbeddedObject__ __{value__=_aMethod___;__ | __src__=_aURL___;__ | __filename__= _imageFileName___;__ [__framework__ = _frameworkBaseName_|__"app" ;__ ... __};__

### Description

A WOEmbeddedObject provides support for Netscape plug-ins. It corresponds to the HTML element <EMBED SRC = >. If the embedded object's content comes from outside the WebObjects application, use the __src__ attribute. If the embedded object's content is returned by a method within the WebObjects application, use the __filename__ attribute or the __value__ attribute.

**__value__**
: The content for this embedded object in the form of a WOElement object. This data can come from a database, a file, or memory.

**__src__**
: URL containing the embedded object. Use this attribute for complete URLs; for relative URLs use __filename__ instead.

**__filename__**
: Path to the embedded object relative to the __WebServerResources__ directory.

**__framework__**
: Framework that contains the embedded object. This attribute is only necessary if the object is in a different location from the component. That is, if the component and the embedded object are both in the application or if the component and the embedded object are both in the same framework, this attribute isn't necessary. If the embedded object is in a framework and the component is in an application, specify the framework's name here minus the __.framework__ extension. If the embedded object should be in the application but the component is in a framework, specify the __"app"__ keyword in place of the framework name.

### Examples

[A VRML plug-in](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=Vrml)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOForm.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
