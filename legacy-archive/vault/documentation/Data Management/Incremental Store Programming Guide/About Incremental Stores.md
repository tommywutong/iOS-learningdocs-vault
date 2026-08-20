---
title: Incremental Store Programming Guide
apple_id: TP40010706
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Introduction/Introduction.html
archived_at: '2026-07-15T07:24:01.206286Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Implementation%20Strategy.md)

# About Incremental Stores

An incremental store is a persistent store in Core Data that allows you to access its content little by little. You can bring into memory just the data your program needs to operate, rather than the entire contents of the store. Similarly, an incremental store writes just the data that changed, rather than overwriting the entire backing data store. Core Data also supports atomic persistent stores (see _[Atomic Store Programming Topics](../../Cocoa/Atomic%20Store%20Programming%20Topics/Introduction%20to%20Atomic%20Store%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrr)_), which read the entire data store into memory and write the entire store to disk.

Incremental stores work well for apps that use large amounts of data, where storing the entirety in memory is not feasible. In contrast, atomic stores work well for apps that use small amounts of data.

The Core Data framework is responsible for all of the managed objects in memory, leaving only the implementation of the persistence mechanism to your incremental store. Your incremental store must perform the following tasks:

- Validate and load the metadata that the persistent store coordinator uses to identify and keep track of your store
- Fulfill fetch and save requests sent by a managed object context
- Realize value and relationship faults fired by a managed object

### Use Cases

Use incremental stores when:

- Your data is too large to load into memory all at once
- Retrieving your data is an expensive or time-consuming operation
- Access to your data is dependent on device conditions (network connectivity, resource availability, and so on)

For example, you might use a custom incremental store to query an unsupported database format, interface with legacy code, or bridge with cross-platform code bases. Implement your own custom incremental store when one of these situations applies and the built-in store types do not meet your needs.

### Alternatives

Core Data is an object graph and data persistence framework that provides functionality to perform complex operations like relational mapping, storage, undo management, and schema migration. Core Data is divided into several layers; each layer abstracts out a specific set of functionality: Managed object contexts hold in-memory representations of the backing data, persistent stores act as adaptors to backing data stores, and persistent store coordinators bridge contexts with persistent stores. This guide focuses on the persistent store layer. See _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ for more information on using the Core Data framework.

Core Data includes several built-in persistent stores to support atomic and incremental object persistence:

Atomic:

- In-Memory Store (`NSInMemoryStoreType`)
- XML Store (`NSXMLStoreType`)
- Binary Store (`NSBinaryStoreType`)

Incremental:

- SQLite Store (`NSSQLiteStoreType`)

Use this guide as a reference and as an implementation strategy when implementing your own incremental store. Follow the strategies and best practices presented in this guide to create incrementally runnable, testable code and to avoid common pitfalls.

You should be comfortable with the Core Data framework before implementing a custom incremental store. To learn about the basic features of Core Data, read Technology Overview in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.

You’ll find other excellent resources in Apple’s developer libraries. Here are a few whose topics are related to the content in this book.

- _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_
- _[Atomic Store Programming Topics](../../Cocoa/Atomic%20Store%20Programming%20Topics/Introduction%20to%20Atomic%20Store%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrr)_
- _[Predicate Programming Guide](../../Cocoa/Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_
[Next](Implementation%20Strategy.md)

