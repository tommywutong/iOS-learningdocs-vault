---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/DynImgs.htm
archived_at: '2026-07-15T07:56:27.045467Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](GenWO.md)[Previous
Section](GenWO.md) 

## Dynamic Images

The elements WOImage and WOActiveImage are dynamic
images. At run time, WOImage is rendered as a passive image and WOActiveImage
as a mapped, active image. To create them, click !
or ! in the toolbar, respectively.

A static image element requires you to specify
its pathname directly in the HTML. With dynamic images, you bind the __filename__
attribute to specify the name of an image file in your project, or in a
framework. You can bind this attribute to a variable or method so that
the filename is dynamically generated at run time.

You can also create a WOImage by dragging an
image from the file system into your component (see ["Dragging
Elements into the Component Window"](CreateDE.md#apple-geydmnbq) for more information). An alert
appears, asking whether you want to add the image to the project (if it
is not already in the project). If you do, the file is added to the Web
Server Resources suitcase of your project.

[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](WOApplet.md)[Next
Section](WOApplet.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
