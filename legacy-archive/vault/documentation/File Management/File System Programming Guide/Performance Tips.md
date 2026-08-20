---
title: File System Programming Guide
apple_id: TP40010672
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/PerformanceTips/PerformanceTips.html
archived_at: '2026-07-15T07:32:00.397460Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Programming Guide](About%20Files%20and%20Directories.md)


[Next](macOS%20Library%20Directory%20Details.md)[Previous](Using%20FileWrappers%20as%20File%20Containers.md)

# Performance Tips

Relative to other operations, accessing files on disk is one of the slowest operations a computer can perform. Depending on the size and number of files, it can take anywhere from a few milliseconds to several minutes to read files from a disk-based hard drive. Make sure your code performs as efficiently as possible under even light to moderate workloads.

If your app slows down or becomes less responsive when it starts working with files, use the Instruments app to gather some baseline metrics. Instruments show you how much time your app spends operating on files and helps monitor various file-related activity. As you fix each problem, run your code in Instruments again and record the results, so that you can verify whether your changes worked.

Look for these possible problem areas:

- __Code that’s reading lots of files (of any type) from disk.__ Remember to look for places where you are loading resource files too. Are you actually using the data from all of those files right away? If not, you might want to load some of the files more lazily.
- __Code that uses older file-system calls.__ Most calls should be using Swift or Objective-C APIs. You can use BSD-level calls too, but don’t use older Carbon-based functions that operate on `FSRef` or `FSSpec` data structures. Xcode generates warnings when it detects your code using deprecated methods and functions, so make sure you check those warnings. Also see [Use Modern File System Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqnzngeydanjrg4).
- __Code that uses callback functions or methods to process file data.__ If a newer API is available that takes a [block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3), update your code to use that API instead.
- __Code with many small read or write operations performed on the same file.__ Can you group those operations together and perform them all at once? For the same amount of data, one large read or write operation is usually more efficient than many small operations.

These recommendations can help improve your file system related performance. As with all tips, measure performance before and after so that you can verify optimizations.

- __Minimize the number of file operations.__ Moving data from a local file system into memory takes a significant amount of time. And if the target file system is located on a server halfway around the world, network latency increases the delay in retrieving the data.
- __Reuse path objects.__ When you access file resources for a [NSURL](https://developer.apple.com/documentation/foundation/nsurl) object using the [resourceValuesForKeys(_:)](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevaluesforkeys) method, those values are cached. By reusing the [NSURL](https://developer.apple.com/documentation/foundation/nsurl) object, you may avoid file system access on subsequent access to those file resources. Also, because [NSURL](https://developer.apple.com/documentation/foundation/nsurl) objects can be expensive to construct, prefer reuse over creating new instances each time you reference a file.
- __Don’t process large amounts of data in small chunks.__ Buffer size dramatically affects how fast data is read from disk to a local buffer. If you’re working with relatively large files, create a large buffer (say 128KB to 256KB) and read much or all of the data into memory before processing it. The same rules apply for writing data to the disk: Write data as sequentially as you can using a single file-system call.
- __Read data sequentially instead of jumping around in a file.__ The kernel transparently clusters I/O operations, which makes sequential reads much faster.
- __Avoid skipping ahead in an empty file before writing data.__ The system might have to write zeroes into the intervening space to fill the gap. Including “holes” in your files at write time might incur a performance penalty, so don’t do it without good reason. For more information, see [Zero-Fill Delays Provide Security at a Cost](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzg42dema).
- __Defer I/O operations until your app needs the data.__ The golden rule of being lazy applies to disk performance as well as many other types of performance.
- __Don’t use the preferences system to capture data that can be inexpensively recomputed.__ Use the preferences system to capture only user preferences (such as window positions, view settings, and user provided preferences). Recomputing simple values is significantly faster than reading the same value from disk.
- __Don’t assume that caching files in memory will speed up your app.__ Caching files in memory increases memory usage, which can decrease performance in other ways. Plus, the system may cache some file data for you automatically, so creating your own caches might make things even worse; see [The System Has its Own File Caching Mechanism](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrhe4doljzhe3tgmq).

Disk caching can be a good way to accelerate access to file data, but its use is not appropriate in every situation. Caching increases the memory footprint of your app and if used inappropriately can be more expensive than simply reloading data from the disk.

Caching is most appropriate for files you plan to access multiple times. If you have files that you intend to use only once, either disable the caches or map the file into memory.

When reading data that you won’t need again soon, such as when streaming a large multimedia file, tell the file system not to add that data to the file-system caches. Disable file system caching for files being read once and discarded by passing the [DataReadingUncached](https://developer.apple.com/documentation/foundation/nsdata/readingoptions/1412417-uncached) option to [init(contentsOfURL:options:)](https://developer.apple.com/documentation/foundation/nsdata/1407864-initwithcontentsofurl). By default, the system maintains a buffer cache with the data most recently read from disk. This disk cache is most effective when it contains frequently used data. If you leave file caching enabled while streaming a large multimedia file, you can quickly fill up the disk cache with data you won’t use again. Even worse, this process is likely to push other data out of the cache that might have benefited from being there.

For data read randomly from a file, you can sometimes improve performance by mapping that file directly into your app’s virtual memory space. File mapping is a programming convenience for files you want to access with read-only permissions. It lets the kernel take advantage of the virtual memory paging mechanism to read the file data only when it is needed. You can also use file mapping to overwrite existing bytes in a file; however, you cannot extend the size of the file using this technique. Mapped files bypass the system disk caches, so only one copy of the file is stored in memory.

For more information about mapping files into memory, see _[File System Advanced Programming Topics](../File%20System%20Advanced%20Programming%20Topics/About%20Advanced%20File%20System%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydonrv)_.

For security reasons, file systems are supposed to zero out areas on disk when the data from those areas is allocated to a file. This behavior prevents data left over from a previously deleted file from being included with the new file.

For both reading and writing operations, the system delays the writing of zeroes until the last possible moment. When you close a file after writing to it, the system writes zeroes to any portions of the file your code did not touch. When reading from a file, the system writes zeroes to new areas only when your code attempts to read from that area or when it closes the file. This delayed-write behavior avoids redundant I/O operations to the same area of a file.

If you notice a delay when closing your files, it is likely because of this zero-fill behavior. Make sure you do the following when working with files:

- Write data to files sequentially. Gaps in writing must be filled with zeros when the file is saved.
- Don’t move the file pointer past the end of the file and then close the file.
- Truncate files to match the length of the data you wrote. For scratch files you plan to delete, truncate the file to zero-length.

Choose routines that let you specify paths using [NSURL](https://developer.apple.com/documentation/foundation/nsurl) objects over those that specify paths that use strings. Most URL-based routines are supported in macOS 10.6 and later, and are designed to take advantage of technologies like Grand Central Dispatch. This gives your code an immediate advantage on multicore computers while not requiring you to do much work.

Prefer routines that accept [block objects](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) over those that accept callback functions or methods. Blocks are a convenient and more efficient way to implement callback-type behaviors. Blocks often require much less code to implement because they don’t require you to define and manage a context data structure for passing data. Some routines might also execute your block by scheduling it in a GCD queue, which can also improve performance.

[Next](macOS%20Library%20Directory%20Details.md)[Previous](Using%20FileWrappers%20as%20File%20Containers.md)

