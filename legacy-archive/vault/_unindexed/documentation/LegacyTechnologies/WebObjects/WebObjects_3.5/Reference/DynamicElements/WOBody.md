---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOBody.html
archived_at: '2026-07-15T07:55:21.846009Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOApplet.md)

## WOBody

### Synopsis

__WOBody__ __{src__=_aURL_ | __filename__= _imageFileName___;__ [__framework__ = _frameworkBaseName_|__"app" ;__] ... __};__

### Description

WOBody specifies the background image to display for the HTML page.

**__src__**
: URL containing the image data. Use this attribute for complete URLs; for relative URLs use __filename__ instead.

**__filename__**
: Path to the image relative to the __WebServerResources__ directory.

**__framework__**
: Framework that contains the image file. This attribute is only necessary if the image file is in a different location from the component. That is, if the component and the image file are both in the application or if the component and the image file are both in the same framework, this attribute isn't necessary. If the image file is in a framework and the component is in an application, specify the framework's name here (minus the __.framework__ extension). If the image file should be in the application but the component is in a framework, specify the __"app"__ keyword in place of the framework name.

### Examples

[Dynamically setting the background image](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=BodyEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOBrowser.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
