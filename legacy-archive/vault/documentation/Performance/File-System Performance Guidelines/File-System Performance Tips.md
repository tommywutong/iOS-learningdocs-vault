---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/Articles/FilePerformance.html
archived_at: '2026-07-18T01:48:36.972468Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File-System Performance Guidelines](Introduction%20to%20File-System%20Performance%20Guidelines.md)


[Next](Overview%20of%20OS%20X%20File%20Systems.md)[Previous](Introduction%20to%20File-System%20Performance%20Guidelines.md)

# File-System Performance Tips

Given the nature of disk-based storage, the file system can be a significant bottleneck to code. The following sections provide tips on how you can minimize this bottleneck to improve the performance of your code.

What follows are some basic recommendations for reducing the I/O activity of your program, and thus enhancing its performance. As with all recommendations, it is important to measure the performance of the code being optimized before and after optimization to ensure that it actually gets faster.

- 

  Minimize the number of file operations you perform. For more information, see [Minimize File-System Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzhe3tamq).
- 

  Group several small I/O transfers into one large transfer. A single write of eight pages is faster than eight separate single-page writes, primarily because it allows the hard disk to write the data in one pass over the disk surface. For more information, see [Choosing an Optimal Transfer Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljrge2tkojw).
- Perform sequential reads instead of seeking and reading small blocks of data. The kernel transparently clusters I/O operations, which makes sequential reads much faster.
- Avoid skipping ahead in an empty file before writing data. The system must write zeroes into the intervening space to fill the gap. For more information, see [Be Aware of Zero-Fill Delays](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzg42dema).
- 

  Reading is typically cheaper than writing data.
- 

  Defer any I/O operations until the point that your application actually needs the data.
- 

  Use the preferences system to capture only user preferences (such as window positions and view settings) and not data that can be inexpensively recomputed.
- 

  Do not assume that caching file data in memory will speed up your application. Storing file data in memory improves speed until that memory gets swapped out to disk, at which point you pay the price for accessing the disk once again. Strive to find an appropriate balance between reading from disk and caching in memory. For more information, see [Cache Files Selectively](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzhe3tgmq).

Be careful about making assumptions that a particular file operation will be fast. Something as simple as reading a preferences file might still take a long time if the file is located on a busy network server. If the server crashes, reading the file can take even longer. Always analyze your application with the available tools to find the actual performance problems.

For more information about measuring file access performance, see [Examining File-System Usage](Examining%20File-System%20Usage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4dslkdjjbeursjirca).

Moving data from a local file system into memory takes a significant amount of time. File-system access times are generally measured in milliseconds, which corresponds to several millions of clock cycles spent waiting for data to be fetched from disk. And if the target file system is located on a server halfway around the world, network latency increases the delay in retrieving the data. Because of these factors, you should strive to reduce your application’s dependence on files as much as possible.

To find out where your application is accessing the file system, use the `fs_usage` tool. This tool reports any file-system interactions and includes information about how long those interactions take. See [Examining File-System Usage](Examining%20File-System%20Usage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4dslkdjjbeursjirca) for more information.

If you are migrating legacy code to OS X, you should update your file-related code to use more modern APIs. Modern routines that use the `FSRef` data type offer much better performance than the older `FSSpec`-based routines. The reason is that modern routines were written with Unicode and a wide spectrum of file systems in mind and were thus optimized for those environments. Older routines require additional manipulation to work on non-HFS file systems and in non-Roman languages.

If your application requires the maximum possible performance from the file system, consider using BSD function calls to transfer data. For most application developers, this step is unnecessary because the performance of both the Carbon and Cocoa routines is quite acceptable for most uses. However, you might consider using the BSD routines if you are writing a file-system utility or an application that spends a lot of time interacting with the file system.

The BSD layer implements the POSIX routines to `open`, `close`, `read`, and `write` files. You can also use the `fcntl` routine to control the current file-system settings and perform other operations.

Disk caching can be a good way to accelerate access to file data, but its use is not appropriate in every situation. Caching increases the memory footprint of your application and if used inappropriately can be more expensive than simply reloading data from the disk.

Caching is most appropriate for files you plan to access multiple times. If you have files you only intend to use once, you should either disable the caches or map the file into memory.

When reading data that you are certain you won’t need again soon, such as streaming a large multimedia file, tell the file system not to add that data to the file-system caches. By default, the system maintains a buffer cache with the data most recently read from disk. This disk cache is most effective when it contains frequently used data. If you leave file caching enabled while streaming a large multimedia file, you can quickly fill up the disk cache with data you won’t use again. Even worse is that this process is likely to push other data out of the cache that might have benefited from being there.

Carbon applications can tell the File Manager not to cache data by passing the `kFSNoCacheBit` option to `FSReadFork` or similar functions. (In versions of OS X prior to 10.4, this option is specified using the `noCacheBit` flag instead.) Applications can also call the BSD `fcntl` function with the `F_NOCACHE` flag to enable or disable caching for a file.

If you intend to read data randomly from a file, you can improve performance in some situations by mapping that file directly into your application’s virtual memory space.File mapping is a programming convenience for files you want to access with read-only permissions. It lets the kernel take advantage of the virtual memory paging mechanism to read the file data only when it is needed. You can also use file mapping to overwrite existing bytes in a file; however, you cannot extend the size of file using this technique. Mapped files bypass the system disk caches, so only one copy of the file is stored in memory.

For more information about mapping files into memory, see [Mapping Files Into Memory](Mapping%20Files%20Into%20Memory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4talkdjjbeursjirca).

For security reasons, file systems are supposed to zero out areas on disk when they are allocated to a file. This behavior prevents data leftover from a previously deleted file from being included with the new file.

The OS X HFS Plus file system has always implemented this zero-fill behavior. However, in OS X version 10.1 a new technique was introduced to improve the performance of this operation. For both reading and writing operations, the system delays the writing of zeroes until the last possible moment. When you close a file after writing to it, the system writes zeroes to any portions of the file your code did not touch. When reading from a file, the system writes zeroes to new areas only when your code attempts to read from that area or when it closes the file. This delayed-write behavior avoids redundant I/O operations to the same area of a file.

If you notice a delay when closing your files, it is likely because of this zero-fill behavior. Make sure you do the following when working with files:

- 

  Write data to files sequentially. Gaps in writing must be filled with zeros when the file is saved.
- Do not move the file pointer past the end of the file and then close the file.
- Truncate files to match the length of the data you wrote. For scratch files you plan to delete, truncate the file to zero-length.

Converting pathname information from one form to another is often an expensive operation. If your code converts back and forth between pathnames, `FSSpec` structures, `FSRef` structures, or `CFURL` structures, you might want to consider caching the resulting data structures. The best time to cache is when you know you are going to need that same structure again. Reusing file-related data structures minimizes the interactions your program has with the file system.

The CFNetwork services provide modern APIs for accessing network-based services, such as those related to HTTP and Bonjour. If you are currently using Open Transport, URLAccess, or other legacy APIs to access network resources, you should move your code to these new services.

OS X version 10.4 and later implements true asynchronous I/O operations in Carbon File Manager routines. In previous versions of the Carbon File Manager, asynchronous I/O operations were offloaded to a separate thread, which queued I/O requests and performed them sequentially. Now, changes to the kernel allow those same operations to be performed in parallel.

In versions of OS X prior to 10.4, if you want to perform truly asynchronous I/O requests, you must add the `kFSAllowConcurrentAsyncIO` bit to the _positionMode_ parameter when calling `PBReadForkAsync` or `PBWriteForkAsync`.

When reading data from the disk to a local buffer, the buffer size you choose can have a dramatic effect on the speed of the operation. If you are working with relatively large files, it does not make sense to allocate a 1K buffer to read and process the data in small chunks. Instead, it is advisable to create a larger buffer (say 128K to 256K in size) and read much or all of the data into memory before processing it. The same rules apply for writing data to the disk: write data as sequentially as you can using a single file-system call.

[Next](Overview%20of%20OS%20X%20File%20Systems.md)[Previous](Introduction%20to%20File-System%20Performance%20Guidelines.md)

