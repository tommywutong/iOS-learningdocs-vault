---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.8.html
archived_at: '2026-07-15T08:09:17.910759Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Java%20Client%20Layers%20and%20Classes.md) [!](Client%20Interface%20and%20Control%20Layers.md) [!](Client%20Distribution%20Classes.md)

---

#  The Distribution Layer

The distribution layer (implemented by the EODistribution package on the client and the EOJavaClient framework on the server) is responsible for synchronizing the states of the object graphs on the client and on the application server in the middle tier. The distribution layer moves properties in both directions, that is, as it fetches objects and saves changes.

The distribution layer has a server side and a client side. The classes in the server side of this layer are provided by the EOJavaClient framework (and associated "wrapped" Java classes). The classes on the client side are implemented in Java and live in the com.apple.client.eodistribution package.

#### [Client Distribution Classes](Client%20Distribution%20Classes.md#apple-obtwmslehu4tsojqgmzq)

#### [Server Distribution Classes](Server%20Distribution%20Classes.md#apple-obtwmslehu4tsojqgm4q)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Java%20Client%20Layers%20and%20Classes.md) [!](Client%20Interface%20and%20Control%20Layers.md) [!](Client%20Distribution%20Classes.md)
