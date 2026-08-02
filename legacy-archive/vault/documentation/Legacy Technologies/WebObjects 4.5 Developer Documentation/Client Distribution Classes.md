---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.9.html
archived_at: '2026-07-15T08:09:17.935295Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](The%20Distribution%20Layer.md) [!](The%20Distribution%20Layer.md) [!](Server%20Distribution%20Classes.md)

---

#  Client Distribution Classes

The client-side distribution layer has four public classes.

__EODistributionChannel__ and __EOHTTPChannel__. The distribution layer provides channels through which the application server and the Java clients communicate. The EOHTTPChannel class implements an HTTP channel, which is used by Java Client WebObjects applications, but you can subclass the abstract class EODistributionChannel and implement a channel that uses a different transport protocol (such as CORBA). On the client side EODistributedObjectStore handles communication over the channel; on the server side it's EODistributionContext.

__EODistributedObjectStore__. On the client the distribution layer provides a distributed object store. It handles interaction with the distribution layer's channel (an EODistributionChannel object), incorporating knowledge of that channel so it can forward messages it receives from the server to its editing contexts and forward messages from its editing contexts to the server.

__EODistributedDataSource__. A concrete subclass of EODataSource (which is defined in EOControl) that fetches using an EOEditingContext as its source of objects; the editing context, in turn, forwards the fetch requests to its object store (usually an instance of EODistributedObjectStore) where it is ultimately serviced by an EODatabaseContext on the server.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](The%20Distribution%20Layer.md) [!](The%20Distribution%20Layer.md) [!](Server%20Distribution%20Classes.md)
