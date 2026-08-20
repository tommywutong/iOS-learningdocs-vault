---
title: 64-Bit Transition Guide
apple_id: TP40001064
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/64bitPorting/indications/indications.html
archived_at: '2026-07-15T07:23:04.099735Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Transition Guide](Introduction%20to%2064-Bit%20Transition%20Guide.md)


[Next](Major%2064-Bit%20Changes.md)[Previous](Introduction%20to%2064-Bit%20Transition%20Guide.md)

# Should You Recompile Your Software as a 64-Bit Executable?

As a general rule, in OS X v10.7 and later, the answer is probably yes. A 64-bit executable can provide many benefits to users and to programmers, depending on the nature of your program.

There are a number of factors to consider when deciding whether to make your application run in 64-bit mode. These considerations are described in the sections that follow.

Applications that target OS X v10.7 and later should take advantage of automatic reference counting (ARC). This technology frees you from having to manually retain and release objects, and in so doing, often fixes latent bugs in applications.

ARC is supported only in the new Objective-C runtime, which is supported only in 64-bit applications. For this reason, most new development should be 64-bit.

Prior to OS X v10.6, all applications that shipped with the operating system were 32-bit applications. Beginning in v10.6, applications that ship with the operating system are generally 64-bit applications.

This means that in v10.5 and previous, the first third-party 64-bit application that a user runs causes the entire 64-bit framework stack to be brought into memory, resulting in a launch performance penalty and significant memory overhead.

Similarly, in v10.6 and later, the first non-64-bit-capable application pays a performance and memory footprint penalty because OS X must bring in the entire 32-bit framework stack. Thus, if you are primarily targeting OS X v10.6 and later, you should be 64-bit if at all possible.

Because a 64-bit kernel cannot load 32-bit kernel extensions, it is imperative that all kernel extensions be compiled 64-bit. Beginning in OS X v10.6, some hardware configurations use a 64-bit kernel by default, and beginning in OS X v10.8, _all_ supported hardware configurations use a 64-bit kernel _exclusively_. This means that if your kernel extension is not 64-bit, it will not function in OS X v10.8 and later.

Even in older versions of OS X, if your application is performance critical, you might want to recompile your application as a 64-bit executable, particularly on Intel-based Macintosh computers.

Here’s why. The 64-bit Intel architecture contains additional CPU registers that are not available when compiling a 32-bit Intel executable. For example, the 64-bit architecture has 16 general-purpose integer registers instead of 8. Because of the extra register space, the first few arguments are passed in registers instead of on the stack. Thus, by compiling some applications as 64-bit, you may improve performance because the code generates fewer memory accesses on function calls. As a general rule, 64-bit Intel executables run somewhat more quickly unless the increased code and data size interact badly (performance-wise) with the CPU cache.

As with any complicated software system, it is difficult to predict the relative performance of recompiling a piece of software as a 64-bit executable. The only way to know for certain (on either architecture) is to compile for 64-bit and benchmark both versions of the application.

Here are some of the potential performance pitfalls:

- Larger code and data size can result in increased cache and translation lookaside buffer (TLB) misses.
- Larger code and data (both pointers and `long` integers) can require more memory to avoid paging.
- Multiply and divide operations are slower when performed on 64-bit quantities than 32-bit quantities. Other operations take roughly the same amount of time as their 32-bit counterparts. Thus, if your code frequently multiplies values of type `long`, you will see a performance impact. (The reverse is true for type `long long` because 64-bit applications do not have to break 64-bit operations up into multiple 32-bit operations.)
- When you use a 32-bit signed integer as an array index, if that number is not stored in a register, the CPU will spend extra time on each access to sign-extend the value.

For the most part, these potential performance impacts should be small, but if your application is performance critical, you should be aware of them.

If your application may need random access to exceptionally large (>2GB) data sets, it is easier to support these data sets in a 64-bit environment. You can support large data sets in a 32-bit application using memory mapping, but doing so requires additional code. Thus, for new applications, you should carefully evaluate whether supporting such large data sets is required in the 32-bit version of your application.

Applications that use 64-bit integer math extensively may see performance gains. In 32-bit applications, 64-bit integer math is performed by breaking the 64-bit integer into a pair of 32-bit quantities. It is possible to perform 64-bit computation in leaf functions in 32-bit applications, but this functionality generally offers only limited performance improvement.

If you are writing an application, any plug-ins used by your application must be compiled for the same processor architecture and address width as the running application. If your application needs to support 32-bit and 64-bit plug-ins simultaneously, you must do so using a helper process, such as an XPC service. To learn more, read _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

In OS X v10.7 and later, all Apple applications shipping as part of the OS are 64-bit executables. This means that users with 64-bit-capable computers will be running the 64-bit slice of key system components. And beginning in OS X v10.8 and later, built-in apps are generally 64-bit-only. This means that any plug-ins (screen savers, printer dialog extensions, and so on) that need to load in these applications _must_ be recompiled as 64-bit plug-ins.

As a special exception, the System Preferences application provides a 32-bit fallback mode. If the user selects a system preferences pane without a 64-bit slice, it relaunches itself as a 32-bit executable (after displaying a dialog box). To maximize your users’ experience, however, you should still transition these preference panes to 64-bit plug-ins as soon as possible.

A 64-bit app can consume significantly more memory than a 32-bit app. For this reason, it is tempting to continue to ship 32-bit apps. However, this is usually _not_ the right thing to do.

In OS X v10.6 and later, most built-in apps are 64-bit. The first time you run a 32-bit application, all of the 32-bit framework slices must be loaded into memory. This means that loading older, 32-bit-only applications causes significant memory pressure, particularly on computers with limited RAM. This often outweighs the additional memory impact caused by larger data structures.

This concern is described in more detail in [Performance Optimization](Performance%20Optimization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrufvbuqmrshawvgvzr), along with some tips for improving your memory usage in a 64-bit environment.

[Next](Major%2064-Bit%20Changes.md)[Previous](Introduction%20to%2064-Bit%20Transition%20Guide.md)

