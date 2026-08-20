---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.52.html
archived_at: '2026-07-15T08:10:55.852455Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Creating%20Other%20WebObjects.md) [!](Conditionals.md) [!](Generic%20WebObjects.md)

---

#   Dynamic Images

The elements WOImage and WOActiveImage are dynamic images. At run time, WOImage is rendered as a passive image and WOActiveImage as a mapped, active image. To create them, click !
or !
in the toolbar, respectively.

A static image element requires you to specify its pathname directly in the HTML. With dynamic images, you bind the __filename__
attribute to specify the name of an image file in your project, or in a framework. You can bind this attribute to a key so that the filename is dynamically generated at run time.

You can also create a WOImage by dragging an image from the file system into your component (see [Dragging Elements into the Component Window](Dragging%20Elements%20into%20the%20Component%20Window.md#apple-gi4danbw)
for more information). An alert appears, asking whether you want to add the image to the project (if it is not already in the project). If you do, the file is added to the Web Server Resources suitcase of your project.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Creating%20Other%20WebObjects.md) [!](Conditionals.md) [!](Generic%20WebObjects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
