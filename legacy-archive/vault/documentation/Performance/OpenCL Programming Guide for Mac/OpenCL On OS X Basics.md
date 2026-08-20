---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/TheOpenGLWorkflow/TheOpenGLWorkflow.html
archived_at: '2026-07-18T01:49:04.186783Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](Identifying%20Parallelizable%20Routines.md)[Previous](Basic%20Programming%20Sample.md)

# OpenCL On OS X Basics

Tools provided on OS X let you include OpenCL kernels as resources in Xcode projects, compile them along with the rest of your application, invoke kernels by passing them parameters just as if they were typical functions, and use Grand Central Dispatch (GCD) as the queuing API for executing OpenCL commands and kernels on the CPU and GPU.

If you need to create OpenCL programs at runtime, with source loaded as a string or from a file, or if you want API-level control over queueing, see _The OpenCL Specification_, available from the Khronos Group at [http://www.khronos.org/registry/cl/](http://www.khronos.org/registry/cl/).

In the OpenCL specification, computational processors are called _devices_. An OpenCL device has one or more _compute units_. A _workgroup_ executes on a single compute unit. A compute unit is composed of one or more processing elements and local memory.

A Mac computer always has a single CPU. It may not have any GPUs or it may have several. The CPU on a Mac has multiple compute units, which is why it is called a _multicore CPU_. The number of compute units in a CPU limits the number of workgroups that can execute concurrently.

CPUs usually contain between two and eight compute units, sometimes more. A graphics processing unit (GPU) typically contains many compute units-GPUs in current Mac systems feature tens of compute units, and future GPUs may contain hundreds. To OpenCL the number of compute units is irrelevant. OpenCL considers a CPU with eight compute units and a GPU with 100 compute units each to be a single _device_.

The OS X v10.7 implementation of the OpenCL API facilitates designing and coding _data parallel_ programs to run on both CPU and GPU devices. In a data parallel program, the same program (or _kernel_) runs concurrently on different pieces of data and each invocation is called a _work item_ and given a work item ID. The work item IDs are organized in up to three dimensions (called an _N-D range_).

A kernel is essentially a function written in the OpenCL language that enables it to be compiled for execution on any device that supports OpenCL. However, a kernel differs from a function called by another programming language because when you invoke “a” kernel, what actually happens is that many instances of the kernel execute, each of which processes a different chunk of data.

The program that calls OpenCL functions to set up the context in which kernels run and enqueue the kernels for execution is known as the _host application_. The host application is run by OS X on the CPU. The device on which the host application executes is known as the _host device_. Before it runs the kernels, the host application typically:

1. Determines what compute devices are available, if necessary.
2. Selects compute devices appropriate for the application.
3. Creates dispatch queues for selected compute devices.
4. Allocates the memory objects needed by the kernels for execution. (This step may occur earlier in the process, as convenient.)

The host application can enqueue commands to read from and write to memory objects that are also accessible by kernels. See [Memory Objects in OS X OpenCL](Memory%20Objects%20in%20OS%20X%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqgmwvgvzu). _Memory objects_ are used to manipulate device memory. There are two types of memory objects used in OpenCL: _buffer objects_ and _image objects_. Buffer objects can contain any type of data; image objects contain data organized into pixels in a given format.

Although kernels are enqueued for execution by host applications written in C, C++, or Objective-C, a kernel must be compiled separately to be customized for the device on which it is going to run. You can write your OpenCL kernel source code in a separate file or include it inline in your host application source code.

OpenCL kernels can be:

- Compiled at compile time, then run when queued by the host application.

  or
- Compiled and then run at runtime when queued by the host application.

  or
- Run from a previously-built binary.

A _work item_ is a parallel execution of a kernel on some data. It is analogous to a thread. Each kernel is executed upon hundreds of thousands of work items.

A _workgroup_ is a set of work items that execute concurrently and share data. Each workgroup is executed on a compute unit.

Workgroup _dimensions_ determine how kernels operate upon input in parallel. The application usually specifies the dimensions based on the size of the input. There are constraints; for example, there may be a maximum number of work items that can be launched for a certain kernel on a certain device.

As of OS X v10.7, the OpenCL development process includes these major steps:

__Figure 3-1__  OpenCL Development Process

!!

1. Identify the tasks to be parallelized.

   Determining how to parallelize your program effectively is often the hardest part of developing an OpenCL program. See [Identifying Parallelizable Routines](Identifying%20Parallelizable%20Routines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqojnknltc).
2. Write your kernel functions.

   - See [How the Kernel Interacts With Data in OS X OpenCL](How%20the%20Kernel%20Interacts%20With%20Data%20in%20OS%20X%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrrfvjvomi).
   - The [Basic Kernel Code Sample](Basic%20Programming%20Sample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrgiwvgvzt) shows how you can store your kernel code in a file that can be compiled using Xcode.
3. Write the host code that will call the kernel(s).

   - See [Using Grand Central Dispatch With OpenCL](Using%20Grand%20Central%20Dispatch%20With%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomi) for information about how the host can use GCD to enqueue the kernel.
   - See [Memory Objects in OS X OpenCL](Memory%20Objects%20in%20OS%20X%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqgmwvgvzu) for information about how the host passes parameters to and retrieves results from the kernel.
   - See [Sharing Data Between OpenCL and OpenGL](Sharing%20Data%20Between%20OpenCL%20and%20OpenGL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrqfvjvomi) for information about how the OpenCL host can share data with OpenGL applications.
   - See [Controlling OpenCL / OpenGL Interoperation With GCD](Controlling%20OpenCL%20-%20OpenGL%20Interoperation%20With%20GCD.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjyfvjvomi) for information about how the OpenCL host can synchronize processing with OpenGL applications using GCD.
   - See [Using IOSurfaces With OpenCL](Using%20IOSurfaces%20With%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjxfvjvomi) for information about how the OpenCL host can use IOSurfaces to exchange data with a kernel.
   - The [Basic Host Code Sample](Basic%20Programming%20Sample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrgiwvgvzv) shows how you can store your host code in a file that can be compiled with Xcode.
4. Compile using Xcode.

   See [Hello World!](Hello%20World%21.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqfvjvomq).
5. Execute.
6. Debug (if necessary).

   See [Debugging](Hello%20World%21.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqfvjvomy).
7. Improve performance (if necessary):

   - If your kernel(s) will be running on a CPU, see [Autovectorizer](Autovectorizer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqnznknltc) and, for suggestions about additional optimizations, see [Improving Performance On the CPU](Improving%20Performance%20On%20the%20CPU.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrgmwvgvzx).
   - If your kernel(s) will be running on a GPU, see [Tuning Performance On the GPU](Tuning%20Performance%20On%20the%20GPU.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrsfvjvony).

[Next](Identifying%20Parallelizable%20Routines.md)[Previous](Basic%20Programming%20Sample.md)

