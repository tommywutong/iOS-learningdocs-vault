---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/keepout/keepout.html
archived_at: '2026-07-15T07:23:13.763814Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Kernel%20Architecture%20Overview.md)[Previous](About%20This%20Document.md)

# Keep Out

This document assumes a broad general understanding
of kernel programming concepts. There are many good introductory
operating systems texts. This is not one of them. For more information
on basic operating systems programming, you should consider the
texts mentioned in the bibliography at the end of this document.

Many developers are justifiably cautious about programming
in the kernel. A decision to program in the kernel is not to be
taken lightly. Kernel programmers have a responsibility to users
that greatly surpasses that of programmers who write user programs.

Kernel code must be nearly perfect. A bug in the kernel could
cause random crashes, data corruption, or even render the operating
system inoperable. It is even possible for certain errant operations
to cause permanent and irreparable damage to hardware, for example, by
disabling the cooling fan and running the CPU full tilt.

Kernel programming should be avoided if
at all possible. Fortunately, kernel programming is usually unnecessary.
You can write most software entirely in user space. Even most device
drivers (FireWire and USB, for example) can be written as applications,
rather than as kernel code. A few low-level drivers must be resident
in the kernel's address space, however, and this document might
be marginally useful if you are writing drivers that fall into this
category.

Despite parts of this document being useful in driver writing,
this is _not_ a document about writing drivers.
In OS X, you write device drivers using the I/O Kit. While this document
covers the I/O Kit at a conceptual level, the details of I/O Kit
programming are beyond the scope of this document. Driver writers
are encouraged to read _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ for
detailed information about the I/O Kit.

This document covers most aspects of kernel programming _with
the exception_ of device drivers. Covered topics include
scheduling, virtual memory pagers and policies, Mach IPC, file systems,
networking protocol stacks, process and thread management, kernel security,
synchronization, and a number of more esoteric topics.

To summarize, kernel programming is an immense responsibility.
You must be exceptionally careful to ensure that your code does
not cause the system to crash, does not provide any unauthorized
user access to someone else’s files or memory, does not introduce
remote or local root exploits, and does not cause inadvertent data
loss or corruption.

[Next](Kernel%20Architecture%20Overview.md)[Previous](About%20This%20Document.md)

