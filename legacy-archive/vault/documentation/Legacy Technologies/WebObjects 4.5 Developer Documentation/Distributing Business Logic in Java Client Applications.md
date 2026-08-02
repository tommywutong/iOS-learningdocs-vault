---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.2f.html
archived_at: '2026-07-15T08:09:09.161011Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Writing%20Derived%20Methods.md)

---

#  Distributing Business Logic in Java Client Applications

The value of Java Client applications, of course, lies in their ability to distribute processing duties among objects on the server and objects on the client. Primarily for security and performance reasons, you can have only objects on the server performing some tasks and only objects on the client performing others.

For example, sometimes you want only objects behind the firewalls and other security mechanisms of the server to have access to sensitive information, such as account numbers. On the other hand, processing tasks such as calculation of balances should be performed by objects on the client, thereby improving application performance by eliminating the need for a cycle of the request-response loop.

There are no hard and fast rules for how to distribute object behavior. An enterprise object on the client can have the same set of methods and instance variables as its counterpart on the server, or what it has can be a subset (or superset) of the other object's methods and instance variables. The best way to distribute business logic among objects depends on the particular nature of your application.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Implementing%20Custom%20Behavior%20for%20Your%20Classes.md) [!](Writing%20Derived%20Methods.md)
