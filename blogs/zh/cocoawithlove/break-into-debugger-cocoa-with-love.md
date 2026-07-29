---
title: '进入调试器 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/break-into-debugger.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:0b80e1a815648571'
translated: true
---

> 原文：[进入调试器 | Cocoa with Love](https://www.cocoawithlove.com/2008/03/break-into-debugger.html)　·　Cocoa with Love (Matt Gallagher)

为了方便调试：提供一个 `DebugBreak()` 宏，可以程序化地在某行代码（而不是在子函数内部）停止调试器。其中部分代码也能在其他地方找到，但这里给出的是同时支持 PPC 和 Intel 架构、可直接运行的版本。

> **2008 年 7 月 31 日更新：** 修复了汇编语句，使其能再次正常工作。

## 为什么要程序化地停止调试器？

调试时，如果你的代码中有一致性检查，有时可以把错误信息记录到控制台。但另一些时候，你可能想直接进入调试器，亲自查看内存。也许你想探索变量的状态，找出问题出在哪里。也许所有的调试信息都会淹没在控制台输出中。

为了实现这一点，你需要一条命令，让 GDB 停在当前代码行。Microsoft 的 Visual Studio 有一个方便的 `DebugBreak()` 命令正是做这个的。在 Mac OS X 上，我们有 `Debugger()` 和 `DebugStr()`，但它们并不会停在调用它们的代码行，而是会让调试器卡在它们自身的内部深处。

## 如何真正地停下 GDB？

GDB 遇到 SIGINT（中断信号）时会停止运行。有很多方法可以发送 SIGINT——`pthread_kill()` 就是一个很好的例子——但在函数调用中执行它有一个缺点：调试器会在发送 SIGINT 的函数内部停止，而不是在你的代码中调用它的那一行。

## 内联汇编

绕过这个栈问题的方法，是直接在代码中使用内联汇编，调用 `sys_kill` 系统调用或 `int` 机器指令（具体取决于你的 CPU）。这样，栈不会增长，当你进入调试器时，你的函数仍然处于最顶层。

## 代码

> **语言说明：**  
> 本博客中的大部分代码仅限 Objective-C，但以下代码在 GCC 下的 C、Objective-C 或 C++ 中均能编译。

这是实现它的代码。把它放在某个头文件中。甚至可以把它包含在你的 `.pch`（预编译头文件）中。

```objc
#ifdef DEBUG
    #if __ppc64__ || __ppc__
        #define DebugBreak() \
            if(AmIBeingDebugged()) \
            { \
                __asm__("li r0, 20\nsc\nnop\nli r0, 37\nli r4, 2\nsc\nnop\n" \
                    : : : "memory","r0","r3","r4" ); \
            }
    #else
        #define DebugBreak() if(AmIBeingDebugged()) {__asm__("int $3\n" : : );}
    #endif

    bool AmIBeingDebugged(void);
#else
    #define DebugBreak()
#endif
```

你还需要从 [Apple 的技术问答 QA1361：检测调试器](http://developer.apple.com/qa/qa2004/qa1361.html) 复制 `AmIBeingDebugged()`，并将其放在某个源文件（而不是头文件）中。最好也用 `#ifdef DEBUG` 和 `#endif` 把那段代码包起来。

如果你还没有定义 `DEBUG` 预处理器宏（你确实应该定义），那么还需要设置一下。

1. 右键点击你的 target（通常与项目或可执行文件同名，但它位于 XCode 树状视图的 "Targets" 标题下）。
2. 从弹出的上下文菜单中选择 "Get Info"。
3. 转到 "Build" 选项卡。
4. 确保 "Configuration" 设置为 "Debug"。
5. 在 "GCC 4.0 - Preprocessing" 下的 "Preprocessor Macros" 旁边的字段中输入 `DEBUG`。

## 代码做了什么？

首先：在 `DEBUG` 之外它什么也不做，这很重要。然后它调用 `AmIBeingDebugged()` 来检查 GDB 是否实际在运行（即使你使用的是 Debug 构建配置，也不意味着 GDB 就在运行）。接着是汇编代码。

在 Intel 机器上，很简单：`"int $3"`（向当前进程发送一个 SIGINT 中断）。

在 PPC 平台上，要做的事就更多了（RISC 比 CISC 更冗长）。相关的 PPC 汇编信息：

- `"li"` – 加载整数，将第二个参数放入第一个参数指定的位置
- `"sc"` – 系统调用，调用由寄存器 0 中的整数指示的 UNIX 系统调用，其他参数从寄存器 3 开始。
- `"nop"` – 空操作。用于等待某些操作完成。

因此，PPC 汇编代码的作用如下：

1. 将 `20` 加载到寄存器 0
2. 发起一个系统调用，即调用 "20"（`sys_getpid`），将当前进程的进程 ID 返回到寄存器 3
3. 等待 `"sc"` 完成
4. 将 `37` 加载到寄存器 0
5. 将 `2` 加载到寄存器 4
6. 发起一个系统调用，即调用 "37"（`sys_kill`），将寄存器 4 中的整数标识的信号（2 = SIGINT）发送给寄存器 3 指定的进程 ID（即从上一个系统调用返回的我们自己的 PID）。

如果你想知道 `: : : "memory","r0","r3","r4"` 这部分是什么意思，它只是告诉编译器，这个汇编块可能会改变 "memory" 以及寄存器 0、3 和 4 的内容。
