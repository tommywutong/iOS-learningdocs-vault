---
title: 'Emerge Tools Blog | SwiftData vs Realm: Performance Comparison'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3ef2b820cb6de664'
translated: false
---

> 原文：[Emerge Tools Blog | SwiftData vs Realm: Performance Comparison](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison)　·　Emerge Tools Blog

# SwiftData vs Realm: Performance Comparison

June 19, 2024 by

Jacob Bartlett

iOSPerformanceGuest post

![SwiftData vs Realm: Performance Comparison](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.3aa53788.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Today we're refereeing a pitched battle between bitter rivals. The gruff, curmudgeonly, ubiquitous Realm database, versus the shiny young upstart, SwiftData. We'll compare the performance of both iOS persistence frameworks on three key metrics:

- Speed
- Storage
- Memory

In the spirit of scientific peer-review, you're encouraged to check out my [open-source repo](https://github.com/jacobsapps/RealmVsSwiftData) and view the [raw test results](https://docs.google.com/spreadsheets/d/1v_7Yc2UE1sqbseKn4QrOtqVApMQCvOvVUGw64SBZtWI/edit?usp=sharing).

## [Meet The Frameworks](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#meet-the-frameworks)

Before diving into the science, here's a brief primer for how each framework works:

### [Realm](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#realm)

Realm, released for iOS in 2014, has always sold itself as the high-performance choice for your apps.

There's a [ton of abstraction](https://academy.realm.io/posts/threading-deep-dive/) involved in the standard SQL wrapper: passing requests to the framework, translating into SQL statements, instantiating a DB connection, performing disk I/O, allocating memory, deserializing the binary data, and transforming it back into language-compatible objects.

The Realm DB engine was written from the ground-up in C++ to minimise this overhead. Realm skips many of these steps through its _zero copy architecture_: it stores data on-disk as virtual memory. In a query, Realm can access the offset in the database file and read it directly into memory.

Realm implements a multi-version concurrency control (MVCC) approach to avoid placing locks on the DB during long writes. This is essentially copy-on-write, where DB connections operate on a snapshot of the data, with writes verified by a two-phase commit.

### [SwiftData](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#swiftdata)

SwiftData was unveiled to much fanfare at [WWDC 2023](https://developer.apple.com/videos/play/wwdc2023/10187/). Finally, there was a fully Swift-native solution to persistence, allowing engineers to fully embrace Swift for building every part of their apps: the Swift language, SwiftUI, and now finally SwiftData.

In practice, SwiftData is a clean, Swift-y wrapper over Core Data. This is an _object graph management_ framework designed to manage object lifecycles and persists them to disk.

Core Data, by default, uses SQLite as its underlying storage mechanism (it can also use XML, binary, or in-memory). Therefore, it's not unreasonable to describe SwiftData as a wrapper over a wrapper over a wrapper. But then, you can say that SQLite is just a wrapper over B-trees, which are a wrapper over magnetic bits on a disk. [Let's not get carried away](https://xkcd.com/378/).

SwiftData (and Core Data, by default) uses a WAL (write-ahead log) to manage concurrency, where committed transactions are appended to the log while reads can be performed on the main database file separately on disk. SQLite periodically performs "checkpointing" to merge data into the main DB file.

## [The Experiment](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#the-experiment)

I'm aiming to create fair test conditions which capture common persistence scenarios encountered in an app, while also stretching the frameworks at extreme data volume:

- [Build an application utilising both Realm and SwiftData](https://github.com/jacobsapps/RealmVsSwiftData/)
- Create 2 models: one simple; one complex with some relationships
- Test performance of standard CRUD operations
- Test across orders of magnitude, from 100 to 10 million objects
- Measure the storage used by each DB file, alongside app binary size
- Measure peak memory usage for each test

The experiments are run by [some simple scripts](https://github.com/jacobsapps/RealmVsSwiftData/tree/main/RealmVsSwiftData/PerformanceTesting) which log execution time of various DB operations, alongside some manual profiling in Xcode.

Experiments are run live on an iPhone 15 Pro with `-Os` optimisation level to create a production-like environment.

I won't detail each low-level result here, but if you're interested, all performance testing results are logged [here](https://docs.google.com/spreadsheets/d/1v_7Yc2UE1sqbseKn4QrOtqVApMQCvOvVUGw64SBZtWI/edit?usp=sharing). You're welcome to peer-review the data and run the experiments yourself.

### [Data Models](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#data-models)

We had two data models, to help model both simple and complex queries. Our `User` objects had a few fields for ID, first name, surname, and age. Our `Student` objects were more complex, including several relationships. The base objects were similar to users, but also had a `School` (with a name and location), plus zero-to-many `Grades` (with a subject, letter-grade, and exam board).

### [Hardware Limitations](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#hardware-limitations)

While I wanted to run tests up to 10,000,000 objects, my hardware had other ideas. I began running into memory limits and adjusted the experiment accordingly to get within touching distance of system limits (storing 1-2 million simple objects; or ~200k complex objects).

![The system killing my test app while attempting to write 10,000,000 objects at once](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fout-of-memory.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The system killing my test app while attempting to write 10,000,000 objects at once

## [Speed](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#speed)

Realm, the database built for high performance, was _mostly_ faster, with some notable exceptions.

### [Object Instantiation](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#object-instantiation)

At the start of the performance test suite, objects were created in memory. This isn't a perfect test, since the `init()` methods perform some inefficient random generation, however the differences between each type — the Realm `Objects` and the SwiftData `@Models` — speak for themselves.

Since we're testing across several orders of magnitude, our charts use a log-log scale. These show that the SwiftData objects took around **10x longer** to instantiate.

![Measuring object instantiation performance with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Finit-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring object instantiation performance with both simple User objects and complex Student objects

Our Realm User and Student are both subclasses of `Object`, which itself subclasses [RLMObjectBase](https://github.com/realm/realm-swift/blob/master/Realm/RLMObjectBase.mm). This endows our Realm objects with signature features such as live synchronization (via key-value observation).

The SwiftData `@Model` macro adds a lot of functionality, which you can view inline by right-clicking and selecting _expand macro_. Here's the unassuming `firstName` property in its final form:

```swift
@_PersistedProperty
var firstName: String
@Transient
private var _firstName: _SwiftDataNoType
  @storageRestrictions(accesses: _$backingData, initializes: _firstName)
      init(initialValue) {
                  _$backingData.setValue(forKey: .firstName, to: initialValue)
                  _firstName = _SwiftDataNoType()
      }

  get {
                  _$observationRegistrar.access(self, keyPath: .firstName)
                  return self.getValue(forKey: .firstName)
      }

  set {
                  _$observationRegistrar.withMutation(of: self, keyPath: .firstName) {
                          self.setValue(forKey: .firstName, to: newValue)
                  }
      }
```

SwiftData's `@Model` macro creates additional properties such as` _$backingData`, `schemaMetadata`, and `_$observationRegistrar`, which provides storage for tracking and accessing data changes. Unfortunately, contrary to Realm, we can't look at the closed source code of SwiftData's `BackingData` type.

All this additional eager allocation vastly outweighs the work performed when instantiating Realm objects.

### [Write Performance](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#write-performance)

Now we've created a lot of persistence-framework compatible objects, the next natural step is writing them to disk.

In production, when writing 100,000 objects at once, we'd usually consider avoiding a massive I/O operation by batching the writes on a background thread. In this instance, a single batch fits our purposes — testing how quickly the persistence frameworks actually saves data.

Realm was a lot quicker than SwiftData in most instances, however, with smaller numbers of objects (≤1000), SwiftData won. This baseline lag wasn't observed in write, update, or delete Realm operations. It appears there is some small constant overhead incurred by Realm when writing to disk or setting up its memory mapping.

![Measuring write performance with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fwrite-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring write performance with both simple User objects and complex Student objects

For both instantiation and writing, we observe a linear `O(n)` relationship between volume and speed.

Realm topped out at writing 2,000,000 simple `User` objects before hitting an out-of-memory exception and crashing. SwiftData was only able to manage a paltry 1,000,000 objects. Realm was about **3-6x faster** beyond write volumes exceededing 1,000 objects.

### [Read Performance](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#read-performance)

When evaluating read query performance, it appears all data models are not created equal: the best framework depends on the structure of the data we stored; simple or complex.

For our dead-simple `User` objects (a few fields and no relationships), we queried for all users with the first name "Jane". Realm was much faster, its zero-copy architecture shining when reading data directly into memory. For simple SwiftData objects, read performance started off okay and degraded sharply with over 100k objects in the database.

With our more complex `Student` model, we searched for all Physics students who got the top grade. We observed the opposite effect: SwiftData was usually more than **10x faster** than Realm.

![Measuring read performance with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fread-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring read performance with both simple User objects and complex Student objects

Both queries require a full database scan to search for objects matching the given predicates. This leads to the linear `O(n)` time complexity we observed in the data, plus some overhead that caused queries under 10,000 simple objects to complete in approximately equal times.

SwiftData performs so well with these complex relationships because of its Core Data foundation, which is right at home when managing a complex object graph and filtering data across relationships.

Lookup performance is a function of the underlying data structure implementing our storage. In the cases of both Realm ([with its custom engine](https://academy.realm.io/posts/jp-simard-realm-core-database-engine/)) and SwiftData ([built on top of SQLite](https://fly.io/blog/sqlite-internals-btree/)), it's _B-trees all the way down_. This means that querying for a specific object in the database will exhibit `O(log n)` time complexity.

### [Update Performance](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#update-performance)

Our update queries involved a few steps: a query to read some data into memory, some code execution to modify this data, and then a write back to disk.

In Realm, all modifications to an `Object` must happen inside a _write transaction_. In SwiftData, we can simply make changes to our `@Model` objects and _upsert_ them back to our database.

For the simple `User` model, we fetched all the users named "Jane" and renamed them to "Wendy" (a Jane must have done something terrible). For the more complex `Student` model, the exam board discovered that all the maths students at a specific school were cheating, so all their maths exams were revised down to an `F` grade.

Similar results were observed across frameworks for each data model. SwiftData was much faster with small-to-middling volumes of data, only surpassed by Realm when modifying 100,000 objects at once.

![Measuring update performance with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fupdate-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring update performance with both simple User objects and complex Student objects

This difference in performance can be explained by the multi-step update process: We are querying our whole database — with `n` items-to find `m` objects that match our predicate, before modifying and re-saving those objects.

At low `n`, both frameworks read lightning-fast (SwiftData having a slight edge), and have to write very little.

However, as the total volume of data increases, so does `m`, representing the number of items matching our predicate — and hence the amount of writing required. Both frameworks write much more slowly than they read, with the effect much more pronounced in SwiftData at higher write volume.

### [Delete Performance](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#delete-performance)

Our delete operation wiped all the objects from the database, so there was no query overhead required. For the more complex `Student` objects, this included a cascade delete that also erased `Schools` and `Grades`.

This operation was fairly interesting, because it's tough to pin down a time complexity for each.

![Measuring delete performance with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fdelete-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring delete performance with both simple User objects and complex Student objects

SwiftData appeared to exhibit linear `O(n)` time complexity for both models, however its object graph management capabilities gave it a small speed edge when cascade-deleting the complex `Student` models.

Realm exhibited linear behaviour for complex `Student` models, but showed _better-than-linear_ speed with simple `User` objects. Deleting all objects of the same type is fast because the memory-mapped objects all have the same layout in storage, so the final offset (to delete up to) is trivial to calculate. This allows the non-cascading `User` delete operation to run in `O(log n)` time.

## [Storage](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#storage)

Storage performance across both persistence frameworks was fairly evenly matched.

### [File System](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#file-system)

Storage space used by each framework's data was fairly simple to measure using a little utility function to log the file URL.

For Realm we can use `Realm.Configuration.defaultConfiguration.fileURL`, and for SwiftData we can log `container.configurations.first?.url`. From here, we can use `FileManager` APIs to measure the storage space.

Realm's underlying data file is stored in `default.realm` in the app `/Documents` folder. It also includes a `default.realm.lock` file to help manage its multi-version concurrency control.

SwiftData files live in `/Library/Application Support` and store SQLite data in the `default.store` file. SwiftData's concurrency mechanism, the write-ahead log, is also visible here: `default.store-wal`.

![The file system in the RealmVsSwiftData app with 100,000 Student objects stored](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fapp-db-files.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The file system in the RealmVsSwiftData app with 100,000 Student objects stored

### [Storage Performance](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#storage-performance)

We observe, unsurprisingly, a linear relationship between the number of objects stored and space utilised — `O(n)` space complexity.

SwiftData seemed to have a minimum file size of 70kB, which is several times higher than the theoretical [minimum SQLite DB file size of 512 bytes](https://www.sqlite.org/fileformat.html). Realm's custom engine didn't display any such minimum size, storing 100 users in just 20kB.

![Measuring database file size with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fstorage-space.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring database file size with both simple User objects and complex Student objects

Strangely, I measured the baseline 0.07 MB of data in SwiftData all the way up until 10,000 users — The data was probably in the write-ahead log when we measured the DB file size, waiting for checkpointing and merging into the main database.

Despite Realm's zero-copy architecture storing its data in a memory-mapped format, this seems very optimized - both frameworks used very similar amounts of storage.

Overall, Realm performs a little better with tiny amounts of data, and SwiftData does a little better with very many objects stored.

### [Binary Size](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#binary-size)

Looking at the [Size Analysis](https://www.emergetools.com/product/sizeanalysis) of our sample app, we can see the majority of storage space taken up by 2.2MB of Realm libraries.

![Emerge Tools size analysis X-ray for the open-source test project RealmVsSwiftData](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fbinary-x-ray.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools size analysis X-ray for the open-source test project RealmVsSwiftData

SwiftData is a part of iOS, so doesn't take up any extra storage space in your app bundle — the framework is dynamically linked by [dyld](https://www.emergetools.com/glossary/dyld) along with the other system frameworks.

## [Memory](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#memory)

Memory performance is naturally a function of data volume we're testing — the app will use more memory when we're manipulating more objects in and out of persistence.

Realm used a little more memory usage than SwiftData at small data volume, but Realm drastically outperformed at higher volumes — exhibiting a fraction of the memory footprint when compared to SwiftData performing the same work.

### [Peak Memory Usage](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#peak-memory-usage)

I wanted to create another utility function here, but results I found from Mach process memory APIs differed wildly from what I observed from the standard Xcode debugger, so I went with good old-fashioned eye-based observation for these tests.

I measured the Xcode memory usage graph while running the same test suite used in the rest of the experiment.

![Xcode beginning to creak when saving 1,000,000 complex objects to disk](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fmemory-graph.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Xcode beginning to creak when saving 1,000,000 complex objects to disk

Due to the way our tests were designed, the large write operation at the start of the performance test was the longest-running, most memory-intensive operation.

In production, we'd normally want to implement batching and paging to avoid this kind of resource utilisation, but in this instance I was intending to push both frameworks into an out-of-memory crash to see how much they could handle.

The results showed neither framework breaking a sweat until writing 10,000 objects or more. SwiftData appeared to have a lower memory baseline, however at higher volume, Realm took up about **1/3 as much memory** as SwiftData.

![Measuring peak memory usage with both simple User objects and complex Student objects](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fmemory-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Measuring peak memory usage with both simple User objects and complex Student objects

Realm appears to use some memory to "warm up" the framework, even when writing tiny amounts of data. The SwiftData system framework on the other hand has negligible impact on memory usage at very low data volume.

At high data volume, one thing becomes clear: Realm's custom-built mobile database engine massively outperforms the high-abstraction SwiftData when it comes to memory utilization.

## [Other Considerations](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#other-considerations)

While we've run through a fairly comprehensive performance test, there is more to mobile apps than speed, storage, and memory utilisation.

Outside of a controlled experiment, there are many factors which affect your choice of a framework:

- SwiftData targets iOS 17+, so unless your dev house targets `n-1`, you aren't going to be using it in production anytime soon.
- SwiftData is quite buggy at the time of writing — I had to replace several `Grade` enums with raw strings to get the macros behaving correctly.
- Realm is open-source, meaning if you find a bug, you can work through the engine codebase, give a detailed issue report, and even suggest a fix. SwiftData is closed source, and your only recourse for issues is filing a Radar and waiting for the next release.
- Neither database is likely to go anywhere — they are supported by MongoDB and Apple respectively, massive public companies. Realm also has a large open-source community, so won't simply die if Mongo goes bust.
- SwiftData is very immature, and we can expect it to change significantly in then next few years. Realm continues to add new features (such as `@Persisted` property wrappers replacing `@objc dynamic`), but the core engine and implementation has remained stable.
- SwiftData [allow indexes yet](https://www.hackingwithswift.com/quick-start/swiftdata/how-to-index-swiftdata-properties-for-faster-searching). This is an important consideration if you need to efficiently query a large dataset.
- Bugs notwithstanding, SwiftData is much easier to get started with.

## [Conclusion](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#conclusion)

When I began working on this, I strongly expected that the mature, performance-focused incumbent, Realm, would beat SwiftData across the board.

In terms of writes, simple read queries, and memory footprint, this was entirely correct. Realm `Objects` are lightweight to create, can be quickly stored at high volume, and their memory-mapped structure allows high volumes of data to be handled quickly without hogging your system resources. Realm particularly outperformed SwiftData when dealing with large numbers of simple objects.

SwiftData proved surprising in a few places however. The excellent object graph management endowed by its Core Data roots meant queries for more complex data across relationships was drastically better than Realm. At smaller volumes (≤10,000 items, which covers the vast majority of mobile use cases), SwiftData was also a lot faster when updating existing data.

_So, which framework is better?_

As always, it depends. All apps have different use cases, different data volumes, and different resource constraints. I hope this article helps you decide what approach is the best fit for your app.

🍺

This was an Emerge Tools guest post from **Jacob Bartlett**. If you want more of his content, you can [subscribe to Jacob's Tech Tavern](https://jacobbartlett.substack.com) to receive in-depth articles about iOS, Swift, tech, and indie projects every 2 weeks; or [follow him on Twitter](https://twitter.com/jacobs_handle).
