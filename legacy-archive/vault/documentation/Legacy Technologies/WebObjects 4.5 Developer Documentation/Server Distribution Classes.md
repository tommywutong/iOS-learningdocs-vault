---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.a.html
archived_at: '2026-07-15T08:09:17.959844Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](The%20Distribution%20Layer.md) [!](Client%20Distribution%20Classes.md) [!](Programming%20With%20Java%20Client.md)

---

#  Server Distribution Classes

The EOClientJava framework has four public classes.

__EODistributionContext__. This class encodes data to send to the client and decodes data it receives from the client over the distribution channel. It also keeps track of the state of the server-side object graph so it can communicate any changes to the client and thus synchronize the object graphs. EODistributionContext (or its delegate) also validate remote invocations originating from client objects.

__WOJavaClientApplet__. The WebObjects component is used to download and create an applet of class com.apple.client.interface.EOApplet.

__EOClassMapper__. Gives the corresponding class names on the client and server. The methods in this class are typically of interest to those who are implementing their own channels.

__EOReferenceRecording__. Use to encode and decode objects in a pure Java environment. The methods in this class are typically of interest to those who are implementing their own channels.

In addition, __EOAccessAdditions.h__ contains Objective-C categories on EOEntity, EOClassDescriptions, and EOEntityClassDescription. The methods in these categories return client-specific information stored in model files.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](The%20Distribution%20Layer.md) [!](Client%20Distribution%20Classes.md) [!](Programming%20With%20Java%20Client.md)
