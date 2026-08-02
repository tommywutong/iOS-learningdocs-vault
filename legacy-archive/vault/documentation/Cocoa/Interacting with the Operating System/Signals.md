---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Articles/Signals.html
archived_at: '2026-07-15T07:17:34.558969Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Creating%20and%20Launching%20an%20NSTask.md)[Previous](Task%20Management.md)

# Signals

Signals are software interrupts that can be invoked on a specified process. The default signal handling behavior (provided by the system) usually terminates the process immediately on receipt of a signal. A process can override this behavior by installing a signal handler routine.

The most typical use of signals is by the kernel, which uses signals to notify a process of exceptional conditions such as invalid address errors and divide-by-zero errors. Another typical use is the command-line `kill` tool, which is capable of sending any user-specified signal to a process, though the most common use is to terminate a process with a hang-up signal (`SIGHUP`).

Because signals are complex to use effectively and they tend to behave differently (sometimes unreliably) on different operating systems, you should generally avoid installing signal handlers for your own applications. The default system handler usually provides the most appropriate response for a given signal. If you do want to handle signals in your application, see the `signal` man page for basic information about the signals that may be sent.

[Next](Creating%20and%20Launching%20an%20NSTask.md)[Previous](Task%20Management.md)

