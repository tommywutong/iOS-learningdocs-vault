---
title: 'The differences between Core Data and a Database | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/02/differences-between-core-data-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:9ed7124efcd9936f'
translated: false
---

> 原文：[The differences between Core Data and a Database | Cocoa with Love](https://www.cocoawithlove.com/2010/02/differences-between-core-data-and.html)　·　Cocoa with Love (Matt Gallagher)

The [Core Data Programming Guide](http://developer.apple.com/Mac/library/documentation/Cocoa/Conceptual/CoreData/index.html) clearly states that Core Data is not a database but since both Core Data and a database are ways of providing searchable, persistent storage, exactly how and why they are different may not be clear. In this post, I'll look at the way Core Data works and the reasons why its features and capabilities are different to those of common SQL databases — even though an SQL database may be used as the backing store.

## Introduction

Both Core Data and an SQL database provide a means of persistently storing structured data in a searchable store.

Since programmers are generally familiar with databases and since Core Data is actually backed by an SQLite database, it is understandable that Core Data is often treated and used as though it were a wrapper around SQLite.

It is important to realize that although you can use Core Data in this way (in fact, it works very well like this), that Core Data actually operates over a different domain to SQLite — meaning that it provides lots of services that SQLite doesn't but also that Core Data can't provide some of the services that SQLite can. Even for services that both technologies provide, there are different performance considerations.

## Primary function of a database

The somewhat narrow description of database that I will use is: persistent and searchable storage for data in table, row, column format where the primary goal is to keep the data up-to-date on disk at all times, with a secondary goal of powerful, focussed, narrow fetching and updating capabilities.

There are lots of database implementations and many provide features far beyond this description but I'm really looking at the key components of a straightforward SQLite-style database implementation with which many programmers are familiar.

Despite many databases being called "relational" (which implies that they have a degree of support for object connectivity), SQLite and many other relational databases don't handle the mechanics of connecting objects; maintaining state (like a an object relation) between columns, rows or tables is left to the user of the database. In this sense, a database is "dumb" storage — rows have few behaviors beyond "read" and "write" and extending or customizing their behavior would involve extending the database system itself. Even when triggers are available, their programmatic capabilities are limited.

## Primary function of Core Data

At its heart, Core Data is an object graph manager with lifecycle, searching and persistence features. In the case of Core Data, object graph management includes:

- You can connect object A to object B and the connection at both the A and B ends is kept perpetually in sync.
- If you change the connection at the A end, the B end will be updated and all changes trigger notifications (to which you can attach arbitrary code)
- Deletion of objects at one end of a connection can trigger cascading deletion or nullify responses.
- The other end of a connection can exist out of memory (faulted) unless the connection is actually followed at which time the connected object is loaded.

Unlike a typical database, Core Data can be used totally in-memory. While Core Data is often called a "object persistence" framework (since it is expected that you will use its persistence features), it is actually possible to use Core Data entirely in-memory without any form of persistence. Of course, once you have data, it is reasonable to want to keep that data, so persistence is treated as a major feature of the framework but it is important to know that persistence is not mandatory.

Also unlike a database, it is possible to use Core Data without any form of searching. If you allocate and connect all your objects, all you need to do is hold onto one of them and you can walk through everything without needing a fetch request. This search-less behavior is not because Core Data transparently performs a search: once data is loaded in memory, following a connection does not involve a search.

All Core Data objects are fully instantiated Objective-C objects that manage most of their own attributes, relationships and lifecycle. This also means that their properties and behaviors are implemented by methods, making them both observable and overrideable.

## Databases and object graph management are not inherently exclusive

While not available by default in SQLite, the "foreign key" of MySQL, and other SQL:2003 compliant databases, can handle keeping identifiers in different tables in sync and even cascade deletion when requested. The programmatic customization abilities of overrideable objects is not available but the basics of graph management are there.

There are other object relational frameworks that work closer to Core Data's model but which try to behave as an atomic, transactional database. To update the object graph, these frameworks must:

- load appropriate rows from a database
- instantiate objects from these rows
- make changes to the graph objects that are now in memory
- commit the changes back to the database

To be properly atomic, these steps must all be performed as a single transaction (with no other reads or write to the affected rows during the transaction). While some systems might require this, it is far too slow for a general object graph system.

Core Data does not follow this model as Core Data aims to be a more general object management system — and that means that it needs far better performance and flexibility than this model would allow.

## Operating in-memory versus an on-disk database

Without access to the source code, it's not entirely clear. We can only assume that the `NSManagedObjectContext` tracks instantiated objects in a heap or structured container of some form so that it can find them again.

This tracking structure may behave a bit like an in-memory database but it would only be for tracking the existence of instantiated objects — it is important to note that it would not itself store any data. Also note that the centralized `NSManagedObjectContext` and any structures it might maintain are not how you interact with instantiated `NSManagedObject`s — you interact with an `NSManagedObject` by sending messages to `NSManagedObject` pointers.

The reason that Core Data focuses on an in-memory representation is speed. For object graph changes that affect multiple objects, it is much faster if they are all in memory already, rather than needing to search for them again in the database.

For temporary objects (data that doesn't have to be saved to disk) Core Data can create, change and manipulate objects much faster than SQLite can since SQLite has to update indexes and update nodes in the B-tree, as well as simply allocating space and setting values. Core Data can allocate millions of objects in a few seconds, where SQLite might take a few minutes for the same number of allocations.

The tradeoff with an in-memory approach is that SQLite is still used as the backing store. Reading from disk and saving to disk involves all of SQLite's overheads plus the overhead of the Core Data to SQLite conversion process — so is invariably slower than SQLite alone.

## Common database tasks that Core Data doesn't do

I've spoken about features that Core Data has that databases do not. It is important to consider some of the features that Core Data's approach lacks with respect to a database.

### Core Data cannot operate on data without loading the data into memory

In SQL you can simply "`DROP tableName`" to delete whole tables or update every column of a table with commands like "`UPDATE tableName SET key1 = value WHERE key2 = otherValue`". These commands can efficiently update vast amounts of data because they only need to load small amounts of data into RAM at any given time.

Core Data doesn't work in this perpetually on-disk manner — it only works on objects in memory. Even if you only want to delete an object, it must be loaded and instantiated in RAM.

Of course, this is necessary because the object, and its potentially overridden behaviors must be loaded and invoked. There are also connections to be kept up to date with other objects.

However this constraint has implications: if you're trying to change huge numbers of objects (tens of thousands or more) you will need to consider keeping your memory footprint down. This can be done by periodically refaulting unchanged values (`refreshObject:mergeChanges:`) or avoiding the fetch of an object's data (`setIncludesPropertyValues:NO` on `NSFetchRequest`) or even saving the whole context and releasing all the objects you're holding.

### Core Data does not handle data logic

There are a few data-related features that SQL contains, a good example being "unique" keys, that Core Data does not include.

There are a couple of technical reasons why this might be the case. Subclasses can override the getter and setter for an attribute to the point where it is unclear whether it is or is not unique. In fact, transient Core Data attributes need not even support `isEqual:`.

However, I suspect the distinction is actually that Core Data offers no real support for attribute behaviors at all. Core Data manages the "graph" (connections) but the data attributes are all the responsibility of the business logic in the rest of the program; convenient as it may be, it falls outside Core Data's conceptual domain.

### Multi-threaded, multi-user scenarios

Core Data does not offer any amount of threading support. To be fair, `SQLite` is single threaded too but many other databases are multi-threaded and multi-user.

Core Data has been designed for single-user environments (running inside desktop and iPhone apps). Getting rid of threading and locking makes the framework much faster and simpler to work with in its standard usage scenarios.

However, there are still situations where you will want multiple threads reading your data. `NSManagedObject`s and their `NSManagedObjectContext` should be accessed from a single thread only. If you need another thread working on the same data, you need to save the file and reopen using a different `NSManagedObjectContext` in the other thread.

## Summary

| **Database** | **Core Data** |
|---|---|
| Primary function is storing and fetching data | Primary function is graph management (although reading and writing to disk is an important supporting feature) |
| Operates on data stored on disk (or minimally and incrementally loaded) | Operates on objects stored in memory (although they can be lazily loaded from disk) |
| Stores "dumb" data | Works with fully-fledged objects that self-manage a lot of their behavior and can be subclassed and customized for further behaviors |
| Can be transactional, thread-safe, multi-user | Non-transactional, single threaded, single user (unless you create an entire abstraction around Core Data which provides these things) |
| Can drop tables and edit data without loading into memory | Only operates in memory |
| Perpetually saved to disk (and often crash resilient) | Requires a save process |
| Can be slow to create millions of new rows | Can create millions of new objects in-memory very quickly (although saving these objects will be slow) |
| Offers data constraints like "unique" keys | Leaves data constraints to the business logic side of the program |
