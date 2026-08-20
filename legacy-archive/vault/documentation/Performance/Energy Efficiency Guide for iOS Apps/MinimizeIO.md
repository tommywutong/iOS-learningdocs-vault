---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/MinimizeIO.html
archived_at: '2026-07-18T01:47:56.753810Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Minimize I/O

Every time your app performs I/O-related tasks, such as writing file data, it brings the system out of an idle state. By writing data less, aggregating writes together, using caching wisely, scheduling network transactions, and minimizing overall I/O, you can boost the energy efficiency and performance of your app.

### Optimize File Access

Here are some guidelines for optimizing file access in your app:

- Minimize data writes. Write to files only when their content has changed, and aggregate changes into a single write whenever possible. Avoid writing out an entire file if only a few bytes have changed. If you frequently change small portions of large files, consider using a database to store the data instead.
- Avoid accessing memory too frequently. If your app saves state information, make it do so only when that state information changes. Batch changes whenever possible to avoid writing small changes at frequent intervals.
- Read and write data sequentially whenever possible. Jumping around within a file takes extra time to seek to the new location.
- Read and write larger blocks of data from files whenever possible, keeping in mind that reading too much data at once might cause other problems. For example, reading the entire contents of a 32 MB file might trigger paging of those contents before the operation is complete.
- For reading or writing significant amounts of data, consider using `dispatch_io`, which provides a GCD-based asynchronous API for doing file I/O. Using `dispatch_io` lets you specify your data needs at a high level, so the system can optimize your access. See _Grand Central Dispatch (GCD) Reference_.
- If your data consists of structured content that is randomly accessed, store it in a database and access it using, for example, SQLite or Core Data. Using a database is especially important if the amount of data you are manipulating could grow to more than a few megabytes. See [SQLite Software Library](http://www.sqlite.org/) and _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.
- Understand how the system caches file data and know how to optimize the use of those caches. Avoid caching data yourself unless you plan to refer to it more than once. See [The System Has Its Own File Caching Mechanism](../File-System%20Performance%20Guidelines/File-System%20Performance%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzhe3tgmq) in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

> [!NOTE]
> 

[Minimize Timer Use](MinimizeTimerUse.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqnbrfvjvomi)

[React to Low Power Mode on iPhones](LowPowerMode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzrfvjvomi)
