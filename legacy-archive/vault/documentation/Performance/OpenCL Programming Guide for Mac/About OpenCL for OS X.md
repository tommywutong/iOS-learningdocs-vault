---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/Introduction/Introduction.html
archived_at: '2026-07-18T01:48:59.908565Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Hello%20World%21.md)

# About OpenCL for OS X

OpenCL™ (Open Computing Language) is an open standard for cross-platform, programming of modern highly-parallel processor architectures. Introduced with OS X v10.6, OpenCL consists of a C99-based programming language designed for parallelism, a powerful scheduling API, and a flexible runtime that executes kernels on the CPU or GPU. OpenCL lets your application harness the computing power of these processors to improve performance and deliver new features based on compute-intensive algorithms.

In addition to support for the OpenCL 1.1 standard, OS X v10.7 adds integration between OpenCL, Grand Central Dispatch (_GCD_), and Xcode to make it even easier to use OpenCL in your application.

Using OpenCL is easier than ever as of OS X v10.7:

- OpenCL is fully supported by Xcode. The Xcode offline compiler removes a configuration step that used to have to be performed before the kernel could be run and facilitates debugging earlier in the development process. See [Hello World!](Hello%20World%21.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjqfvjvomq).
- You can write OpenCL functions in separate files and include them in your Xcode project. You can compile the kernels when your application is built, before it runs. This improves runtime performance.
- OpenCL now integrates with GCD, making it easier for you to focus on making your OpenCL kernels more efficient. See [Using Grand Central Dispatch With OpenCL](Using%20Grand%20Central%20Dispatch%20With%20OpenCL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjtfvjvomi).
- The autovectorizer compiles and accelerates performance of kernels that run on the CPU up to four times without additional effort. The autovectorizer allows you to write one kernel that runs efficiently on both a CPU and a GPU. You can invoke the autovectorizer regardless of whether you are compiling from Xcode or building the kernels at runtime. Or you can disable the autovectorizer if necessary. See [Autovectorizer](Autovectorizer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqnznknltc).

You can, of course, continue to use code you’ve already written to the OpenCL 1.1 standard. But see [Binary Compatibility Of OpenCL Kernels](Binary%20Compatibility%20Of%20OpenCL%20Kernels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrgqwvgvzr) for a note about how to handle existing binaries.

Because OpenCL C is based on C99, you are free to process your data in OpenCL C functions as you would in C with few limitations. Aside from support for recursion and function pointers, there are not many language features that C has that OpenCL C doesn’t have. In fact, OpenCL C provides several beneficial features that the C programming language does not offer natively, such as optimized image access functions. OpenCL C has built-in support for vector intrinsics and offers vector data types. The operators in OpenCL C are overloaded, and performing arithmetic between vector data types is syntactically equivalent to performing arithmetic between scalar values. Refer to the _The OpenCL Specification_ for more details on the built-in functions and facilities of the OpenCL C language.

This guide assumes that you program in C and have access to _The OpenCL Specification_. Although this guide discusses many key OpenCL API functions, it does not provide detailed information on the OpenCL API or the OpenCL C programming language.

_The OpenCL Specification_, available from the Khronos Group at [http://www.khronos.org/registry/cl/](http://www.khronos.org/registry/cl/) provides information on the OpenCL standard.

The _OpenCL Programming Guide_ by Aaftab Munshi, Benedict Gaster, Timothy G. Mattson, James Fung, and Dan Ginsburg, available from Pearson Education, Inc., is a helpful introduction to the OpenCL language and standard; these topics are not discussed in this book.

For more information about Grand Central Dispatch queues, see [Concurrency Programming Guide: Dispatch Queues](https://developer.apple.com/library/mac/#documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html#//apple_ref/doc/uid/TP40008091-CH102-SW28).

[Next](Hello%20World%21.md)

