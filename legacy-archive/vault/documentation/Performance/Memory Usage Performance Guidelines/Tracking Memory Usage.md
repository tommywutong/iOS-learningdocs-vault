---
title: Memory Usage Performance Guidelines
apple_id: 10000160i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Performance
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/FindingPatterns.html
archived_at: '2026-07-18T01:48:52.933385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Usage Performance Guidelines](Introduction.md)


[Next](Finding%20Memory%20Leaks.md)[Previous](Caching%20and%20Purgeable%20Memory.md)

# Tracking Memory Usage

If you suspect your code is not using memory as efficiently as it could, the first step in determining if there is a problem is to gather some baseline data. Monitoring your code using one of the Apple-provided performance tools can give you a picture of your code’s memory usage and may highlight potential problems or point to areas that need further examination. The following sections describe the tools most commonly used for memory analysis and when you might want to use them.

The Instruments application is always a good starting point for doing any sort of performance analysis. Instruments is an integrated, data-gathering environment that uses special modules (called instruments) to gather all sorts of information about a process. Instruments can operate on your application’s shipping binary file—you do not need to compile special modules into your application to use it. The library of the Instruments application contains four modules that are designed specifically for gathering memory-related data. These modules are as follows:

- The ObjectAlloc instrument records and displays a history of all memory allocations since the launch of your application.
- The Leaks instrument looks for allocated memory that is no longer referenced by your program’s code; see [Finding Leaks Using Instruments](Finding%20Memory%20Leaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dglktk4za).
- The Shared Memory instrument monitors the opening and unlinking of shared memory regions.
- The Memory Monitor instrument measures and records the system’s overall memory usage.

You can add any or all of these instruments to a single trace document and gather data for each of them simultaneously. Being able to gather the data all at once lets you correlate information from one instrument with the others. For example, the Leaks instrument is often combined with the ObjectAlloc instrument so that you can both track the allocations and find out which ones were leaked.

After gathering data for your application, you need to analyze it. The following sections provide tips on how to analyze data using several of the memory-related instruments. For information on how to use the Leaks instrument, see [Finding Leaks Using Instruments](Finding%20Memory%20Leaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dglktk4za).

You use the ObjectAlloc instrument to track the memory allocation activity for your application. This instrument tracks memory allocations from the time your application is launched until you stop recording data. The instrument shows you the allocations in terms of the number of objects created and the size (or type) of the objects that were created. In the icon viewing mode, the instrument displays a real-time histogram that lets you see changes and trends directly as they occur. It also retains a history of allocations and deallocations, giving you an opportunity to go back and see where those objects were allocated.

The information displayed by the ObjectAlloc instrument is recorded by an allocation statistics facility built into the Core Foundation framework. When this facility is active, every allocation and deallocation is recorded as it happens.

For Mac apps, the Shared Memory instrument tracks calls to any `shm_open` and `shm_unlink` functions, which are used for opening and closing regions of shared memory in the system. You can use this information to find out where your application is getting references to shared memory regions and to examine how often those calls are being made. The detail pane displays the list of each function call along with information about the calling environment at the time of the call. Specifically, the pane lists the executable that initiated the call and the function parameters. Opening the Extended Detail pane shows the stack trace associated with the call.

For Mac apps, the Memory Monitor instrument displays assorted statistics about system memory usage. You can use this instrument to view the memory usage trends in your application or on the entire system. For example, you can see how much memory is currently active, inactive, wired, and free. You can also see the amount of memory that has been paged in or out. You might use this instrument in conjunction with other instruments to track the amount of memory your application uses with respect to specific operations.

In OS X, the `malloc_history` tool displays backtrace data showing exactly where your program made calls to the `malloc` and `free` functions. If you specify an address when calling `malloc_history`, the tool tracks memory allocations occurring at that address only. If you specify the `-all_by_size` or `-all_by_count` options, the tool displays all allocations, grouping frequent allocations together.

Before using the `malloc_history` tool on your program, you must first enable the malloc library logging features by setting the `MallocStackLogging` to `1`. You may also want to set the `MallocStackLoggingNoCompact` environment variable to retain information about freed blocks. For more information on these variables, see [Enabling the Malloc Debugging Features](Enabling%20the%20Malloc%20Debugging%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha4dilkdjjbeursjirca).

The `malloc_history` tool is best used in situations where you need to find the previous owner of a block of memory. If you determine that a particular data is somehow becoming corrupted, you can put checks into your code to print the address of the block when the corruption occurs. You can then use `malloc_history` to find out who owns the block and identify any stale pointers.

The `malloc_history` tool is also suited for situations where Sampler cannot be used. For example, you might use this tool from a remote computer or in situations where you want a minimal impact on the behavior of your program.

For more information on using the `malloc_history` tool, see `malloc_history` man page.

In OS X, the `heap` command-line tool displays a snapshot of the memory allocated by the malloc library and located in the address space of a specified process. For Cocoa applications, this tool identifies Objective-C objects by name. For both memory blocks and objects, the tool organizes the information by heap, showing all items in the same heap together.

The `heap` tool provides much of the same information as the ObjectAlloc instrument, but does so in a much less intrusive manner. You can use this tool from a remote session or in situations where the use of Instruments might slow the system down enough to affect the resulting output.

For more information about using the `heap` tool, see `heap(1)` man page.

[Next](Finding%20Memory%20Leaks.md)[Previous](Caching%20and%20Purgeable%20Memory.md)

