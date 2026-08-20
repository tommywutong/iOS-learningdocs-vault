---
title: Memory Usage Performance Guidelines
apple_id: 10000160i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Performance
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MallocDebug.html
archived_at: '2026-07-18T01:48:53.483697Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Usage Performance Guidelines](Introduction.md)


[Next](Viewing%20Virtual%20Memory%20Usage.md)[Previous](Finding%20Memory%20Leaks.md)

# Enabling the Malloc Debugging Features

Debugging memory-related bugs can be time consuming if you do not know where to start looking. This is usually compounded by the problem that many memory bugs occur well after the memory in question was manipulated by the code. Fortunately, Xcode includes options for identifying memory problems closer to when those problems actually happen.

Guard Malloc is a special version of the malloc library that replaces the standard library during debugging. Guard Malloc uses several techniques to try and crash your application at the specific point where a memory error occurs. For example, it places separate memory allocations on different virtual memory pages and then deletes the entire page when the memory is freed. Subsequent attempts to access the deallocated memory cause an immediate memory exception rather than a blind access into memory that might now hold other data. When the crash occurs, you can then go and inspect the point of failure in the debugger to identify the problem.

To enable debugging using Guard Malloc, configure your project to run with Guard Malloc in the [Xcode Scheme Editor](http://help.apple.com/xcode)

. You can use this option for Mac apps and iOS apps running in the simulator.

For more information about the types of memory problems that Guard Malloc can help you track down, see the `libgmalloc` man page in _OS X Man Pages_.

The malloc library provides debugging features to help you track down memory smashing bugs, heap corruption, references to freed memory, and buffer overruns. You enable these debugging options through a set of environment variables. With the exception of `MallocCheckHeapStart` and `MallocCheckHeapEach`, the value for most of these environment variables is ignored. To disable a variable from Terminal, use the `unset` command. Table 1 lists some of the key environment variables and describes their basic function. For a complete list of variables, see the [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc) man page.

__Table 1__  Malloc environment variables

| Variable | Description |
| `MallocStackLogging` | If set, `malloc` remembers the function call stack at the time of each allocation. |
| `MallocStackLoggingNoCompact` | This option is similar to `MallocStackLogging` but makes sure that all allocations are logged, no matter how small or how short lived the buffer may be. |
| `MallocScribble` | If set, `free` sets each byte of every released block to the value `0x55`. |
| `MallocPreScribble` | If set, `malloc` sets each byte of a newly allocated block to the value `0xAA`. This increases the likelihood that a program making assumptions about freshly allocated memory fails. |
| `MallocGuardEdges` | If set, `malloc` adds guard pages before and after large allocations. |
| `MallocDoNotProtectPrelude` | Fine-grain control over the behavior of `MallocGuardEdges`: If set, `malloc` does not place a guard page at the head of each large block allocation. |
| `MallocDoNotProtectPostlude` | Fine-grain control over the behavior of `MallocGuardEdges`: If set, `malloc` does not place a guard page at the tail of each large block allocation. |
| `MallocCheckHeapStart` | Set this variable to the number of allocations before `malloc` will begin validating the heap. If not set, `malloc` does not validate the heap. |
| `MallocCheckHeapEach` | Set this variable to the number of allocations before `malloc` should validate the heap. If not set, `malloc` does not validate the heap. |

The following example enables stack logging and heap checking in the current shell before running an application. The value for `MallocCheckHeapStart` is set to 1 but is irrelevant and can be set to any value you want. You could also set these variables from your shell’s startup file, although if you do be sure to `export` each variable.

```shell
% MallocStackLogging=1
% MallocCheckHeapStart=1000
% MallocCheckHeapEach=100
% ./my_tool
```

If you want to run your program in `gdb`, you can set environment variables from the Xcode debugging console using the command `set env`, as shown in the following example:

```
% gdb
(gdb) set env MallocStackLogging 1
(gdb) run
```

Some of the performance tools require these options to be set in order to gather their data. For example, the `malloc_history` tool can identify the allocation site of specific blocks if the `MallocStackLogging` flag is set. This tool can also describe the blocks previously allocated at an address if the `MallocStackLoggingNoCompact` environment variable is set. The `leaks` command line tool will name the allocation site of a leaked buffer if `MallocStackLogging` is set. See the man pages for `leaks` and `malloc_history` for more details.

The malloc library reports attempts to call `free` on a buffer that has already been freed. If you have enabled the `MallocStackLoggingNoCompact` option, you can use the logged stack information to find out where in your code the second `free` call was made. You can then use this information to set up an appropriate breakpoint in the debugger and track down the problem.

The malloc library reports information to `stderr`.

To enable heap checking, assign values to the `MallocCheckHeapStart` and `MallocCheckHeapEach` environment variables. You must set both of these variables to enable heap checking. The `MallocCheckHeapStart` variable tells the malloc library how many `malloc` calls to process before initiating the first heap check. Set the second to the number of `malloc` calls to process between heap checks.

The `MallocCheckHeapStart` variable is useful when the heap corruption occurs at a predictable time. Once it hits the appropriate start point, the malloc library starts logging allocation messages to the Terminal window. You can watch the number of allocations and use that information to determine approximately where the heap is being corrupted. Adjust the values for `MallocCheckHeapStart` and `MallocCheckHeapEach` as necessary to narrow down the actual point of corruption.

To find memory smashing bugs, enable the `MallocScribble` variable. This variable writes invalid data to freed memory blocks, the execution of which causes an exception to occur. When using this variable, you should also set the `MallocStackLogging` and `MallocStackLoggingNoCompact` variables to log the location of the exception. When the exception occurs, you can then use the `malloc_history` command to track down the code that allocated the memory block. You can then use this information to track through your code and look for any lingering pointers to this block.

[Next](Viewing%20Virtual%20Memory%20Usage.md)[Previous](Finding%20Memory%20Leaks.md)

