---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/JavaClient/Other_Architectures.html
archived_at: '2026-07-15T08:15:12.230001Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Java_Client_Architecture.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Development_s_and_Tools.md)

## Other Architectures

There are other Java-based architectures besides Java Client
that are also distributed and mutiltier. This section describes
how Java Client compares with the Client JDBC and JDBC three-tier
architectures.

### Client JDBC Architecture

Client JDBC applications use the same "fat-client" architecture
that desktop applications do. Custom code invokes JDBC on the client,
which in turn goes through a driver to communicate with a JDBC proxy
on the server; this proxy makes the necessary client-library calls
on the server. The shortcomings of this type of architecture are
typical of all fat-client architectures. Security is a problem because
the compiled Java on the client is easily decompiled, leaving both
sensitive data and business rules at risk. The server has to be
open to allow all client operations without being able to control
what the client is doing. In addition, such an architecture doesn't
scale; it is expensive to move data over the channel to the client.

Java Client has none of these problems. Sensitive data and
business rules can be confined to the server, so the server doesn't
have to allow indiscriminate access to data and operations. Additionally,
because the client part of a Java Client application contains nonsensitive
data and business logic, it doesn't make nearly as many round
trips to the server or move as much data back and forth.

### JDBC Three-Tier Architecture

A JDBC three-tier application (with CORBA as the transport)
is a big improvement over Client JDBC. In this architecture the
client can be thin because all that is required on the client side
is the JFC, non-sensitive custom code (usually for managing the
user interface), and CORBA stubs for communicating with the server.
Sensitive business logic as well as logic related to database connection
are stored on the server. In addition, the server handles all data-intensive
computations.

Although the JDBC three-tier architecture is an improvement
over Client JDBC, it has its own weaknesses.

- The JDBC
  three-tier architecture results in too much network traffic. Because
  this architecture uses "proxy" business objects on the client
  as handles to the real objects on the server, each client request
  for an attribute is forwarded to the server, causing a separate
  round trip and precipitating a "message storm."
- The JDBC three-tier architecture requires developers to write
  much of the code themselves, from code for database access and data
  packaging to code for user-interface synchronization and change
  tracking.
- The JDBC three-tier architecture does not provide much of
  the functionality associated with application servers, such as application
  monitoring and load balancing, nor does it provide HTML integration.

Java Client addresses these problems as well. First, instead
of using proxy business objects on the client, the Java Client application
makes use of "copies" of the objects. Second, WebObjects provides
all of the database access and user interface synchronization with
its enterprise objects technology. Finally, it provides application
server functionality and HTML integration.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Java_Client_Architecture.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Development_s_and_Tools.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
