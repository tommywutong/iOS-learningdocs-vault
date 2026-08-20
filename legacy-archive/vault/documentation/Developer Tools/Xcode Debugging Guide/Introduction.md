---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/000-Introduction/Introduction.html
archived_at: '2026-07-15T07:27:49.602972Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Debugging%20Essentials.md)

# Introduction

Finding and eliminating bugs in your code is a critical phase of the development process. Xcode provides advanced debugging facilities, which include debugging from the text editor so that you don’t stray far from your code, and using the mini debugger, which provides a graphical debugging experience that is less intrusive on the running application than other methods. You can also use a more traditional, specialized graphical debugger, or the debugger console.

This document describes the Xcode debugging environments and explains how to trace your program’s execution and view its data. It is intended for developers and system administrators who want to use Xcode to debug programs and analyze their behavior and performance.

The first chapter, [Debugging Essentials](Debugging%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmznknltc), provides a high-level summary of the Xcode debugging environments.

The next five chapters describe the debugging environments and show how to customize your debugging experience:

- [Debugging in the Debugger](Debugging%20in%20the%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnrnknltc) describes the main debugging environment.
- [Debugging in the Text Editor](Debugging%20in%20the%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnbnknltc) describes the text-editor–based debugging environment.
- [Debugging in the Mini Debugger](Debugging%20in%20the%20Mini%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnjnknltg) explains how to use the mini debugger to debug programs unobtrusively.
- [Debugging in the Console](Debugging%20in%20the%20Console.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnznknltc) discusses the GDB Console window.
- [Debugging Preferences](Debugging%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjtfvjvomi) describes the Debugging preferences pane.

The remaining chapters describe general debugging features and capabilities:

- [Managing Program Execution](Managing%20Program%20Execution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqobnknlts) describes the mechanisms used to control and monitor the execution of programs.
- [Viewing Variables and Memory](Viewing%20Variables%20and%20Memory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqojnknltk) discusses the various ways in which you can view the values of variables as you debug your programs.
- [Modifying Running Code](Modifying%20Running%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjqfvjvony) shows how you can modify your executable while it is running.
- [Debugging Programs Remotely](Debugging%20Programs%20Remotely.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjrfvjvomi) describes how to debug a program running on another computer.
- [Mac OS X Low-Level Debugging](Mac%20OS%20X%20Low-Level%20Debugging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjsfvjvomy) describes the Mac OS X debugging facilities that can help you in your debugging tasks.
- [Debug Information Format](Debug%20Information%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjufvjvomi) talks about the storage and usage of debug information in binaries.

[Next](Debugging%20Essentials.md)

