---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/WhatsEOF1.html
archived_at: '2026-07-15T08:03:20.161506Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Previous Section](What%20Is%20Enterprise%20Objects%20Framework.md)

# The Enterprise Objects Framework Difference

Today's business applications must embody complex rules of the business, access heterogeneous corporate data in database systems from multiple vendors, and offer different front ends to meet the needs of users in all different parts of the business. This is a tall order to fill, but Enterprise Objects Framework meets all these needs. It provides database independence, transparently maps custom business objects to database tables, and binds business objects to user interfaces.

## Where Does Business Logic Go?

The biggest difference between Enterprise Objects Framework and other solutions is where you put business logic. One approach is to implement business rules in the user interface, as you do with 4GL tools. Problems with this approach include:

- _It offers limited reuse._ You have to code your business logic into each application that accesses your database. In fact, within an application, you have to code your business logic into each screen. Consequently, you wind up duplicating your code.
- _It's not maintainable._ Since you have to duplicate your business logic, even small modifications to your rules are difficult to implement. Finding and fixing every affected screen in every affected application is slow and error prone. Modifications to your database schema are equally problematic.
- _Different user interfaces require different implementations._ For example, if you have a client/server application that you want to put on the web, you have to rewrite the application and maintain both versions.
- _It provides poor data integrity._ You have to rely on all application developers to implement the business rules correctly. If any screen of any application has an error, the data in your database can be corrupted, impacting all applications.
- _It doesn't scale well._ To improve your application's performance, you have to provide your users with faster systems. Contrast this with a solution in which you can move some computation-intensive processing to fast server machines.

Another approach is to implement your business rules in the database-with stored procedures, rules, constraints, and triggers, for example. This approach also has problems:

- _It offers limited interactivity._ To provide immediate feedback to a user, you have to make a round trip to the database every time the user performs an action, which can be very slow and inefficient. On the other hand, you can batch up changes, but then the user doesn't receive immediate feedback.
- _No back-end portability._ Database vendors all have different ways to implement logic. If you have to support more than one database, you'll have to implement the logic multiple times, resulting in more maintenance problems.
- _SQL is a poor development language._

A third approach-the one that Enterprise Objects Framework takes-is to put business rules in business objects, called _enterprise objects_. By applying good object-oriented design principles, this approach provides the advantages of encapsulation, reuse, and a more natural model of the real world. For example, suppose you're writing an application for managing a video rental store. The business logic for such an application might include the rules:

- A late fee is generated automatically when a rental becomes overdue.
- A customer can't rent more videos if they have any overdue rentals.
- The total replacement value of a customer's rentals can't exceed the amount of the customer's deposit.

With Enterprise Objects Framework, you would implement these rules in enterprise objects such as Customer, VideoTape, Rental, and Fee.

## What Doesn't Go in an Enterprise Object

Deciding what code to leave out of your business objects is just as important as deciding what code you leave in. To maximize the reusability and extensibility of your objects, they shouldn't embed knowledge of the user interface or database alongside the business logic. For example, if you embed knowledge of your user interface, you can't reuse the objects because each application's user interface is different; and if you embed knowledge of your database, you have to update your objects every time you modify the database.
If not in the business objects, then where does this knowledge go? It's handled by Enterprise Objects Framework as shown in [Figure 1](#apple-gyzdqmq).

!

Figure 1. The Enterprise Objects Framework Approach

The Framework provides a database-to-objects mapping so your objects are encapsulated from the database, and it provides an
objects-to-interface mapping so they are encapsulated from the user interface. This approach enables you to create libraries of enterprise objects that can be used in as many applications as you need, with any user interface, and with any database server. You're able to concentrate on coding the logic of your business while the Framework takes care of the rest.

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Next Section](From%20Database%20to%20Objects.md)
