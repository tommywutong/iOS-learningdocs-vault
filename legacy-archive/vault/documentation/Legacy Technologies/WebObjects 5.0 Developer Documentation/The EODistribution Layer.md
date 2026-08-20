---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Introduction.html
archived_at: '2026-07-15T08:13:49.024951Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Art/up.gif)](EODistributionTOC.md)

# The EODistribution Layer

> **__Package:__**
> : com.webobjects.eodistribution.client (client side): com.webobjects.eodistribution (server side)

---

## Introduction

The EODistribution layer is used in Java Client applications. It consists of two parts: a framework for the server and a Java package for the client. The EODistribution (or, simply, "distribution") layer performs by-copy object distribution and synchronization. It is responsible for synchronizing the states of the object graphs on the client and on the application server. The distribution layer handles communication over a "channel" (which use transports such as HTTP or CORBA) and moves properties in both directions, that is, as objects are fetched and changes are saved. It encodes and decodes objects as they travel back and forth over the channel.

The classes in the server side of the EODistribution layer are provided by the EOJavaClient framework, and server side APIs are available in both Objective-C and Java (the Java package for the server side APIs is com.webobjects.eodistribution). The classes on the client side are implemented in pure Java and live in the com.webobjects.eodistribution package.

The following table summarizes each class in the EODistribution layer:

|  |  |  |  |
| --- | --- | --- | --- |
| __Class__ | __Client__ | __Server__ | __Description__ |
| EODistributedDataSource | X |  | Fetches data using an EOEditingContext on the client as its source of objects. |
| EODistributedObjectStore | X |  | Handles interaction with the distribution layer's channel, incorporating knowledge of that channel so it can forward messages it receives from the server to its editing contexts and forward messages from its editing contexts to the server. |
| EODistributionChannel | X |  | Abstract class for distribution channels. |
| EODistributionContext |  | X | Encodes data to send to the client and decodes data it receives from the client; also tracks and communicates any changes on the server object graph to the client. |
| EOHTTPChannel | X |  | Implements a distribution channel using HTTP as the transport. |
| WOJavaClientApplet |  | X | Used to download and create the applet on the client. |

In addition, the utility class EOAccessAdditions declares a number of methods that return client-specific information stored in model files.

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Art/up.gif)](EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
