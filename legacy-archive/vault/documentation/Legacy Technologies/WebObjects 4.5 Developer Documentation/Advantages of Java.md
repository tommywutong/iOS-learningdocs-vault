---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.2.html
archived_at: '2026-07-15T08:09:00.615826Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Overview%20of%20Java%20Client.md) [!](Overview%20of%20Java%20Client.md) [!](Java%20Client%20Architecture.md)

---

# Advantages of Java

To understand the difference that Java makes in client-server architectures, it helps first to consider two of the more common types of client-server applications: the traditional desktop application and the Web application. Rated on a set of desirable characteristics, each class of application has complementary strengths and weaknesses.

| __ Characteristic__ | __ Desktop__ | __ Web__ |
| --- | --- | --- |
|   Interactive |   Yes |   No |
|   Flexible Controls |   Yes |   No |
|   Rich User-interface Paradigm |   Yes |   No |
|   Portable |   No |   Yes |
|   Easy to Administer |   No |   Yes |
|   Accessible |   No |   Yes |
|   Secure |   No |   Yes |

Desktop applications can typically draw upon user-interface frameworks that provide a varied and flexible set of controls, modal dialogs, and multiple windows. On the other hand, HTML has a limited and static set of controls, mainly forms, active images, and hyperlinks.

A Web application is, by definition, portable since it can run on any client browser that implements certain standards and protocols, regardless of the underlying system; desktop applications are usually limited to the platforms they were built for. Web applications also have high marks for accessibility because they are designed to make it easy for users to get data on networks. Finally, because sensitive data and business logic is confined to the server in Web applications, they tend to be more secure.

Java scores high on each of these characteristics because it can have a strong presence on each side of the client-server divide.The principal advantage of Java is that it runs almost anywhere. The client need only have a compatible Java virtual machine (VM), something that most operating systems and browsers now include as a standard feature. A Java application can run on the server or can be downloaded to the client as an applet. SunSoft's AWT and JFC packages provide a rich source of flexible, interactive controls for developers.

Thus the promise of Java is the best of both worlds ("promise" because the potential of Java is still being realized). So what are some distributed multi-tier Java-based architectures popular today?

Client JDBC applications use a "fat client" architecture. Custom code invokes JDBC on the client, which in turn goes through a driver to communicate with a JDBC proxy on the server; this proxy makes the necessary client-library calls on the server. The shortcomings of this type of architecture are typical of all fat-client architectures. Security is a problem because the bytecodes on the client are easily decompiled, leaving both sensitive data and business rules at risk. The server has to be open to allow all client operations without being able to control what the client is doing. In addition, such an architecture doesn't scale; it is expensive to move data over the channel to the client.

A JDBC Three-tier application (with CORBA as the transport) is a big improvement over Client JDBC. In this architecture the client can be thin since all that is required on the client side is the JFC, non-sensitive custom code (usually for managing the user interface), and CORBA stubs for communicating with the server. Sensitive business logic as well as logic related to database connection are stored on the server. In addition, the server handles all data-intensive computations.

Although JDBC Three-tier is an improvement over Client JDBC, it has its own weaknesses. First it results in too much network traffic. Because this architecture uses "proxy" business objects on the client as handles to the real objects on the server, each client request for an attribute is forwarded to the server, causing a separate round trip and precipitating a "message storm." Second, JDBC Three-tier requires developers to write much of the code themselves, from code for database access and data packaging to code for user-interface synchronization and change tracking. Finally, JDBC Three-tier does not provide much of the functionality associated with application servers, such as application monitoring and load balancing, nor does it provide HTML integration.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Overview%20of%20Java%20Client.md) [!](Overview%20of%20Java%20Client.md) [!](Java%20Client%20Architecture.md)
