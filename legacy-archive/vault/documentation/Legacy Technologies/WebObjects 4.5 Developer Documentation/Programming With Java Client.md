---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.b.html
archived_at: '2026-07-15T08:09:17.985719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Overview%20of%20Java%20Client.md) [!](Server%20Distribution%20Classes.md) [!](Tutorial.md)

---

# Programming With Java Client

Generally, programming a Java Client WebObjects application requires some skills and knowledge common to both Enterprise Objects Framework and WebObjects programmers. However, it also requires a specific design technique: object partitioning.

Objects on the server and the client can be instances of custom classes or generic enterprise objects (EOGenericRecord). Objects that derive from custom subclasses can have different sets of properties on both the server and the client. Usually, client objects have the more restricted set of data and behaviors, but it is really up to you to decide based on the requirements of the application and your business. As noted earlier, the primary criteria for partitioning are performance and security.

The basic tools and techniques for creating a Java Client application are covered in the tutorial for _Creating a Java Client WebObjects Application_.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Overview%20of%20Java%20Client.md) [!](Server%20Distribution%20Classes.md) [!](Tutorial.md)
