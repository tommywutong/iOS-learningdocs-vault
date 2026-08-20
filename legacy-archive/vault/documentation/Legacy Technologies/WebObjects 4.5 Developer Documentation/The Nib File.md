---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.16.html
archived_at: '2026-07-15T08:08:53.664095Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Client%20Files.md) [!](Client%20Files.md) [!](The%20Interface%20Controller.md)

---

#  The Nib File

The nib file in a Java Client application seems identical to nib files in stand-alone Yellow Box applications. You drag objects from palettes onto a window "surface" and these palettes and their objects look exactly like objects in stand-alone. However, these similarities of appearances are deceiving.

When the EOJavaClient palette has been loaded into Interface Builder and you create a user interface, the nib file contains two parallel object graphs, one populated with Yellow Box objects and the other with Swing (JFC) objects. The Swing object graph constitutes a "Java archive" that is loaded onto the client.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Client%20Files.md) [!](Client%20Files.md) [!](The%20Interface%20Controller.md)
