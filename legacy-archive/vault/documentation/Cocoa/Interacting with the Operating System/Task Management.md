---
title: Interacting with the Operating System
apple_id: 10000058i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OperatingSystem/Concepts/task.html
archived_at: '2026-07-15T07:17:36.072857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interacting with the Operating System](Introduction%20to%20Interacting%20with%20the%20Operating%20System.md)


[Next](Signals.md)[Previous](Process%20Information.md)

# Task Management

Using the `NSTask` class, your program can run another program as a subprocess and can monitor that program’s execution. An `NSTask` object creates a separate executable entity; it differs from `NSThread` in that it does not share memory space with the process that creates it.

A task operates within an environment defined by the current values for several items: the current directory, standard input, standard output, standard error, and the values of any environment variables. By default, an `NSTask` object inherits its environment from the process that launches it. If there are any values that should be different for the task, for example, if the current directory should change, you must change the value before you launch the task. A task’s environment cannot be changed while it is running.

Arguments can be specified for the task you want to launch. These arguments do not undergo shell expansion, so you do not need to do special quoting, and shell variables, such as `$PWD`, are not resolved.

Your program can communicate with the task by attaching one or more `NSPipe` objects to the task’s standard input, output, or error devices before launching the task. A pipe is a one-way communications channel between related processes; one process writes data while the other process reads that data. The data that passes through the pipe is buffered; the size of the buffer is determined by the underlying operating system. An `NSPipe` object represents both ends of a pipe.

The end points of the `NSPipe` object are instances of `NSFileHandle`. You read or write data from the appropriate `NSFileHandle` object to get the output from or send input to the task. Multiple tasks can be connected together by attaching an `NSPipe` object between one task’s standard output and another task’s standard input. The output from the first task is then automatically sent as input to the second task.

The task’s standard input, output, and error devices can instead be attached to `NSFileHandle` objects directly to either provide the input data from a file or capture the output to a file.

If the task is an Objective-C Cocoa application, you can also communicate with it using the distributed objects system. For information on distributed objects, see [Distributed Objects](../Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i).

An `NSTask` object can be used to run its task only once. Subsequent attempts to run the task using the same object raise an error. While the task is running, you can send it terminate or interrupt signals (both cause termination by default). You can also suspend the task temporarily. When the task terminates, its exit status is recorded and `NSTaskDidTerminateNotification` is sent.

The `NSTask` class is available in Objective-C only. Java developers can use the `java.lang.Runtime` class to launch processes.

[Next](Signals.md)[Previous](Process%20Information.md)

