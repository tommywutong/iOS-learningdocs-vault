---
title: Core Data Batch Programming Guide
apple_id: TP40016086
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/featuredarticles/CoreData_Batch_Guide/Introduction/Introduction.html
archived_at: '2026-07-18T02:28:02.066098Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md)


[Next](Implementing%20Batch%20Updates.md)

# About Making Batch Changes

In certain situations, it may be necessary to make extensive alterations to the persisted data of an app. When these situations occur, it is advisable to make these changes against the data on disk rather than in memory with objects.

There are two types of batch operations: batch updates and batch deletes.

Both batch updates and batch deletes are developed in a similar manner to a [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest). Executing either a batch delete or a batch update blocks the [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) that it is being run just as occurs with a `NSFetchRequest`. However, because both batch updates and batch deletes are executed directly against the SQLite persistent store, they execute far more quickly compared to performing the same changes or deletes in memory.

Use this guide as a reference and as an implementation strategy when implementing batch updates or batch deletes. Follow the strategies and best practices presented in this guide to handle large changes to your persistent store and to avoid common pitfalls.

You should be comfortable with the Core Data framework before implementing batch updates or batch deletes. To learn about the basic features of Core Data, read Technology Overview in the _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.

You’ll find other excellent resources in Apple’s developer libraries. Here are a two whose topics are related to the content of this document.

- _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_
- _[Predicate Programming Guide](../../documentation/Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_
[Next](Implementing%20Batch%20Updates.md)

