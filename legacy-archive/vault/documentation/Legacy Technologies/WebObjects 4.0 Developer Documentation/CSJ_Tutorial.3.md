---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.3.html
archived_at: '2026-07-15T07:59:58.501474Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.2.md) | [Back Up One Level](CSJ_Tutorial.2.md) | [Next](CSJ_Tutorial.4.md)

###  Data Synchronization Between Client and Server

In a Java Client application, when the user makes a query, the fetch specification is passed through the layers on the client (EOInterface to EOControl to EODistribution), largely through successive invocations of __objectsWithFetchSpecification__
. The distribution layer on the client forwards the fetch specification to the server's distribution layer--in the default WebObjects case, synchronously via HTTP. From there the normal mechanisms take over and a SQL call is eventually made to the database server. The database server returns the rows of requested data and, as usual, this data is converted to enterprise objects and is registered with the EOControl layer on the server. The server's distribution layer then sends _copies_
of the requested objects back to the client. When the EODistribution layer on the server receives the objects, it registers them with the editing context in the control layer and, through the interface layer's display-group and association mechanisms, the user interface is updated with the requested data.

Although requested objects are copied from the server to the client, and these objects exist in parallel object graphs on both server and client, the enterprise objects on the client usually do not exactly mirror the enterprise objects on the server. The objects on the client usually have a subset of the properties of the objects on the server (although the reverse can be true). You can partition your application's enterprise objects so that the objects that exist on the client (or the server) have a restricted set of data and behaviors.

Once the client has fetched data, this data is cached and is represented internally by the client's object graph. As users modify the data (or delete or add "rows" of data), the client's object graph is updated to reflect the new state. When users request that this data be saved, the changed objects are "pushed" to the server. If the business logic on the server validates these changes, the changes are committed to the database.

Note that Java Client automatically pushes updates from the server to the client. It also, by default, pushes changes before client-side objects remotely invoke methods on server-side objects.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.2.md) | [Back Up One Level](CSJ_Tutorial.2.md) | [Next](CSJ_Tutorial.4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
