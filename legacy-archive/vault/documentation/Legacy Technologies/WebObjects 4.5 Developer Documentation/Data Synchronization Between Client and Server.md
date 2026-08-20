---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.4.html
archived_at: '2026-07-15T08:09:16.593103Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Java%20Client%20Architecture.md) [!](Java%20Client%20Architecture.md) [!](Java%20Client%20as%20a%20WebObjects%20Application.md)

---

#  Data Synchronization Between Client and Server

In a Java Client application, when the user makes a query, the fetch specification is passed through the layers on the client (EOInterface to EOControl to EODistribution), largely through successive invocations of __objectsWithFetchSpecification__. The distribution layer on the client forwards the fetch specification to the server's distribution layer--in the default WebObjects case, synchronously via HTTP. From there the normal mechanisms take over and a SQL call is eventually made to the database server. The database server returns the rows of requested data and, as usual, this data is converted to enterprise objects and is registered with the EOControl layer on the server. The server's distribution layer then sends _copies_ of the requested objects back to the client. When the EODistribution layer on the server receives the objects, it registers them with the editing context in the control layer and, through the interface layer's display-group and association mechanisms, the user interface is updated with the requested data.

Although requested objects are copied from the server to the client, and these objects exist in parallel object graphs on both server and client, the enterprise objects on the client usually do not exactly mirror the enterprise objects on the server. The objects on the client usually have a subset of the properties of the objects on the server (although the reverse can be true). You can partition your application's enterprise objects so that the objects that exist on the client (or the server) have a restricted set of data and behaviors.

Once the client has fetched data, this data is cached and is represented internally by the client's object graph. As users modify the data (or delete or add "rows" of data), the client's object graph is updated to reflect the new state. When users request that this data be saved, the changed objects are "pushed" to the server. If the business logic on the server validates these changes, the changes are committed to the database.

Note that Java Client automatically pushes updates from the server to the client. It also, by default, pushes changes before client-side objects remotely invoke methods on server-side objects.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Java%20Client%20Architecture.md) [!](Java%20Client%20Architecture.md) [!](Java%20Client%20as%20a%20WebObjects%20Application.md)
