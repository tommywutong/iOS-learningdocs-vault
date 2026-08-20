---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Overview/Advantages_of_Java.html
archived_at: '2026-07-15T08:14:36.604199Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Overview_of_Java_Client.md)[![Next](attachments/JavaClient/Images/next.gif)](Java_Client_Architecture.md)

## Advantages of Java

To understand the difference that Java makes in client-server
architectures, it helps first to consider two of the more common
types of client-server applications: the traditional desktop application
and the Web application. The two types have complementary strengths
and weaknesses.

__|  |  |  |
| --- | --- | --- |
| Characteristic | Desktop Application | Web Application |__| Interactive | Yes | No |
| Flexible controls | Yes | No |
| Rich user-interface paradigm | Yes | No |
| Portable | No | Yes |
| Easy to administer | No | Yes |
| Accessible | No | Yes |
| Secure | No | Yes |

Desktop applications can typically draw upon user-interface
frameworks that provide a varied and flexible set of controls, modal
dialogs, and multiple windows. On the other hand, HTML has a limited
and static set of controls; most of them are forms, active images, and
hyperlinks.

A Web application is, by definition, portable since it can
run on any client browser that implements certain standards and
protocols, regardless of the underlying system; desktop applications
are usually limited to the platforms they were built for. Web applications
also have high marks for accessibility because they are designed
to make it easy for users to get data on networks. Finally, because
sensitive data and business logic is confined to the server in Web
applications, they tend to be more secure.

Java scores high on each of these characteristics because
it can have a strong presence on each side of the client-server
divide.The principal advantage of Java is that it runs almost anywhere.
The client need only have a compatible Java virtual machine (VM),
something that most operating systems and browsers now include as
a standard feature. Java applications can be designed to run on
the server or the client. Sun's AWT and "Java 2 platform, Standard
Edition" (J2SE) packages provide a rich source of flexible, interactive controls
for developers.

Thus the promise of Java is the best of both worlds. So what
are some distributed multi-tier Java-based architectures popular
today?

Client JDBC applications use a fat-client architecture. Custom
code invokes JDBC on the client, which in turn goes through a driver
to communicate with a JDBC proxy on the server; this proxy makes
the necessary client-library calls on the server. The shortcomings of
this type of architecture are typical of all fat-client architectures.
Security is a problem because the bytecodes on the client are easily
decompiled, leaving both sensitive data and business rules at risk.
The server has to be open to allow all client operations without
being able to control what the client is doing. In addition, such
an architecture doesn't scale; it is expensive to move data over
the channel to the client.

A JDBC three-tier application (with CORBA as the transport)
is a big improvement over a client JDBC application. In this architecture
the client can be thin since all that is required on the client
side is the JFC, nonsensitive custom code (usually for managing
the user interface), and CORBA stubs for communicating with the
server. Sensitive business logic as well as logic related to database
connection are stored on the server. In addition, the server handles
all data-intensive computations.

The JDBC three-tier architecture has its own weaknesses. First
it results in too much network traffic. Because this architecture
uses proxy business objects on the client as handles to the real
objects on the server, each client request for an attribute is forwarded
to the server, causing a separate round trip and precipitating a
message storm. Second, JDBC Three-tier requires developers to write
much of the code themselves, from code for database access and data
packaging to code for user-interface synchronization and change tracking.
Finally, JDBC three-tier does not provide much of the functionality
associated with application servers, such as application monitoring
and load balancing, nor does it provide HTML integration.

[![Previous](attachments/JavaClient/Images/previous.gif)](Overview_of_Java_Client.md)[![Next](attachments/JavaClient/Images/next.gif)](Java_Client_Architecture.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
