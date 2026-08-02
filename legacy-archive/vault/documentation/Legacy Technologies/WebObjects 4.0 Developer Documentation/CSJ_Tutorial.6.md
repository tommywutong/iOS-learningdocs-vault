---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.6.html
archived_at: '2026-07-15T08:00:02.770129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.5.md) | [Back Up One Level](CSJ_Tutorial.5.md) | [Next](CSJ_Tutorial.7.md)

###  Client Interface and Control Layers

The EOInterface and EOControl layers on the client--implemented as the com.apple.client.interface and com.apple.client.control packages--contain classes _almost_
identical (in terms of APIs and behavior) to their counterparts on the server, which are implemented as Yellow Box frameworks.

Basically, the EOInterface layer displays, in the user interface, properties of the enterprise objects in the control layer, using display groups and associations. Changes to the object graph are automatically synchronized with the user interface and user-entered data is automatically reflected in the object graph. The primary mechanisms behind this synchronization are display groups (EODisplayGroup) and associations (EOAssociation subclasses).

As in the server, the EOControl layer's primary responsibility is the management of the object graph through an EOEditingContext. It also implements faulting (on-demand fetching) and tracks editing changes.

The differences between the client and server layers are:

- The client Java classes are written in "100% Pure Java" and do not, as the server classes do, use bridging technology to access Objective-C code.

- The EOInterface layer on the client is implemented in terms of the Java Foundation Classes (instead of using Application Kit objects).

- The object store and the data source used by the client EOControl layer are objects in the distribution layer; basically, these objects communicate changes to the object graph across the channel to the server.

- The client layers include APIs that enable remote invocations of server methods.

- The EOControl layer on the client does not implement undo or redo.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.5.md) | [Back Up One Level](CSJ_Tutorial.5.md) | [Next](CSJ_Tutorial.7.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
