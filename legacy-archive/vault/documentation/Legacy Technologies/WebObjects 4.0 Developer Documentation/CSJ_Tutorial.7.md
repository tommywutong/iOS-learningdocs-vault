---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.7.html
archived_at: '2026-07-15T08:00:03.362637Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.6.md) | [Back Up One Level](CSJ_Tutorial.5.md) | [Next](CSJ_Tutorial.8.md)

###  The Distribution Layer

The distribution layer (implemented by the EODistribution package on the client and the EOJavaClient framework on the server) is responsible for synchronizing the states of the object graphs on the client and on the application server in the middle tier. The distribution layer moves properties in both directions, that is, as it fetches objects and saves changes.

The distribution layer has a server side and a client side. The classes in the server side of this layer are provided by the EOJavaClient framework (and associated "wrapped" Java classes). The classes on the client side are implemented in Java and live in the com.apple.client.eodistribution package.

####  Client Distribution Classes

The client-side distribution layer has four public classes.

__EODistributionChannel__
and __EOHTTPChannel__
. The distribution layer provides channels through which the application server and the Java clients communicate. The EOHTTPChannel class implements an HTTP channel, which is used by Java Client WebObjects applications, but you can subclass the abstract class EODistributionChannel and implement a channel that uses a different transport protocol (such as CORBA). On the client side EODistributedObjectStore handles communication over the channel; on the server side it's EODistributionContext.

__EODistributedObjectStore__
. On the client the distribution layer provides a distributed object store. It handles interaction with the distribution layer's channel (an EODistributionChannel object), incorporating knowledge of that channel so it can forward messages it receives from the server to its editing contexts and forward messages from its editing contexts to the server.

__EODistributedDataSource__
. A concrete subclass of EODataSource (which is defined in EOControl) that fetches using an EOEditingContext as its source of objects; the editing context, in turn, forwards the fetch requests to its object store (usually an instance of EODistributedObjectStore) where it is ultimately serviced by an EODatabaseContext on the server.

####  Server Distribution Classes

The EOClientJava framework has four public classes.

__EODistributionContext__
. This class encodes data to send to the client and decodes data it receives from the client over the distribution channel. It also keeps track of the state of the server-side object graph so it can communicate any changes to the client and thus synchronize the object graphs. EODistributionContext (or its delegate) also validate remote invocations originating from client objects.

__WOJavaClientApplet__
. The WebObjects component is used to download and create an applet of class com.apple.client.interface.EOApplet.

__EOClassMapper__
. Gives the corresponding class names on the client and server. The methods in this class are typically of interest to those who are implementing their own channels.

__EOReferenceRecording__
. Use to encode and decode objects in a pure Java environment. The methods in this class are typically of interest to those who are implementing their own channels.

In addition, __EOAccessAdditions.h__
contains Objective-C categories on EOEntity, EOClassDescriptions, and EOEntityClassDescription. The methods in these categories return client-specific information stored in model files.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.6.md) | [Back Up One Level](CSJ_Tutorial.5.md) | [Next](CSJ_Tutorial.8.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
