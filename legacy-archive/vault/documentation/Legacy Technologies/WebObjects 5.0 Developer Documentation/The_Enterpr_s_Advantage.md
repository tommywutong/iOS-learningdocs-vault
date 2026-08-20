---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/EnterpriseObjects/The_Enterpr_s_Advantage.html
archived_at: '2026-07-15T08:15:05.761540Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](WebObjects__ise_Objects.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/index.html)

## The Enterprise Objects Advantage

A hallmark feature of WebObjects, especially in comparison
to other solutions, is the separation of the business logic from
the database and the user interface. In WebObjects, you put the
business logic in the enterprise objects ( [Figure 3-4](#apple-ijbussski5cem)).

__Figure
3-4 Implementing business logic in enterprise
objects__

![[image: ../Art/BusinessLogicWO.gif]](../Art/BusinessLogicWO.gif)

Another approach ( [Figure 3-5](#apple-ijbusq2bizces)) is to implement business logic in the web or desktop application.
The WebObjects approach betters this approach in the following ways:

- __It
  offers greater reuse.__ In WebObjects, you code your business
  logic once, and each application that accesses your database can
  use it. You don't have to recode your business logic into each
  screen or web page.
- __It's more maintainable.__ With WebObjects,
  you don't have to duplicate your business logic. Thus you can
  easily make substantial changes to your rules without resorting
  to finding and fixing every affected page in every affected application.
  You can also easily track changes to your schema.
- __It improves data integrity.__ In WebObjects,
  you don't need to rely on all application developers to implement
  the business rules correctly. If one application has an error, it is
  less likely to corrupt your database.
- __It scales better.__ In WebObjects, you
  can improve your application's performance without having to provide
  your users with faster systems. Instead, you can simply move some
  computation-intensive processing to fast server machines.

__Figure
3-5 Implementing business logic in the
user interface application__

![[image: ../Art/BusinessLogicApp.gif]](../Art/BusinessLogicApp.gif)

Another approach ( [Figure 3-6](#apple-ijbusq2fifaue)) is to implement your business rules in the database-with stored
procedures, rules, constraints, and triggers, for example. The WebObjects
approach betters this approach in the following ways:

- __It
  offers improved interactivity.__ If you implement your
  business rules in the database, you need to make a round trip to
  the database every time the user performs an action. Alternatively,
  you can batch up database changes, which prevents the user from receiving
  immediate feedback. In WebObjects applications, changes immediately appear
  in the user interface, but you access the database only when saving
  these changes or fetching objects.
- __It improves back-end portability.__ Database
  vendors all have different ways to implement logic. If you have
  to support more than one database and you're using WebObjects,
  you don't have to implement the logic multiple times and thus
  suffer maintenance problems.
- __Java is a good development language.__ With
  WebObjects, you program in Java, an industrial-strength language
  designed from the ground up to be object-oriented. The programmable
  variants of SQL usually have some object-oriented features but are basically
  procedural languages.

__Figure
3-6 Implementing business logic in the
database__

![[image: ../Art/BusinessLogicServer.gif]](../Art/BusinessLogicServer.gif)

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](WebObjects__ise_Objects.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
