---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/BehindSc4.html
archived_at: '2026-07-18T01:19:24.110816Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Behind%20the%20Scenes.md) [!Previous Section](Saving%20Changes.md)

# Transactions

For the most part, Enterprise Objects Framework handles transactions for you. You rarely (if ever) need to explicitly start or end a transaction yourself-it generally happens as the by-product of another operation, such as a fetch or save. However, understanding how transactions are handled in the Framework can help you to make the right decisions for your application.
How transactions are handled in the Framework depends on the locking mode you have set. There are three different possibilities:

- Optimistic locking
- Pessimistic locking
- "On-demand" locking of individual objects

For a detailed description of these locking modes, see the section["Locking and Update Strategies"](Saving%20Changes.md#apple-g4ytmnq).

The way that each of these modes affects transactions is described in the following sections.

## Transactions and Optimistic Locking

If you're using optimistic locking (the default) and you're just fetching objects, Enterprise Objects Framework never explicitly starts or stops transactions. Instead, when a SELECT is performed on a database row, opening (and subsequently closing) a transaction is typically handled by the database server itself, implicitly. Ultimately, it is the responsibility of the adaptor for each database server to ensure that the right thing happens.
Under optimistic locking, Enterprise Objects Framework explicitly starts a transaction when you perform a save operation. A save operation consists of three basic parts:

- Beginning a transaction
- Performing the specified operations (including checking snapshots)
- Committing the transaction, or rolling back if the transaction fails. In either case, the transaction is closed.

## Transactions and Pessimistic Locking

When you use pessimistic locking, Enterprise Objects Framework explicitly starts a transaction as soon as you fetch objects, and every object you fetch is locked. The transaction stays open until you commit it (using the EOEditingContext method __saveChanges__), or roll it back (using the EOEditingContext method __invalidateAllObjects__).
Consequently, using pessimistic locking is very expensive. It's not suitable for applications that have user interaction since large portions of your database could be locked down for indeterminate periods of time. A good alternative to pessimistic locking is using on-demand locking to lock individual objects.

## Transactions and On-Demand Locking

When you use on-demand locking to get a server lock on an object, Enterprise Objects Framework explicitly opens a transaction and keeps it open as long as you have a lock on the object. The transaction stays open until you commit it (using the EOEditingContext method __saveChanges__), or roll it back (using the EOEditingContext method __invalidateAllObjects__).
[!Table of Contents](Behind%20the%20Scenes.md) [!Next Section](Answers%20to%20Common%20Design%20Questions.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
