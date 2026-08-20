---
title: LLDB Debugging Guide
apple_id: TP40016717
resource_type: Guide
platform: Xcode Developer Tools
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/lldb-guide/chapters/Introduction.html
archived_at: '2026-07-15T07:34:42.758376Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Quick%20Tour%20of%20LLDB.md)

# About LLDB and Debugging

_Debugging_ refers to creating and using an analytical framework to isolate causal pathways and test hypotheses. The most important tool of debugging is the debugger, which helps you understand how your program behaves at runtime, without modifying the code.

LLDB provides the underlying debugging environment for developers on Apple platforms. You can use it from a Terminal window or an Xcode source editor to find and eliminate problems in your Swift, C, C++, and Objective-C code.

A debugger has two primary functions: _controlling execution flow_ and _accessing state_.

You primarily control the execution of a program by setting _breakpoints_ at different locations in code. Whenever a program hits a set breakpoint, the debugger temporarily stops execution of the program. While the execution is stopped, you can use the debugger to inspect or modify the current state of different variables, step over, into, or out of the next statement, and continue execution as needed.

- [WWDC 2013: Advanced Debugging with LLDB](https://developer.apple.com/videos/play/wwdc2013/413/)
- _[Debugging with Xcode](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/about_debugging_w_xcode.html#//apple_ref/doc/uid/TP40015022)_
- [The Official LLDB Website](http://lldb.llvm.org/)
[Next](Quick%20Tour%20of%20LLDB.md)

