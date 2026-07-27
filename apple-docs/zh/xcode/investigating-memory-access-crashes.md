---
title: 调查内存访问崩溃
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/investigating-memory-access-crashes
source_url: 'https://developer.apple.com/documentation/xcode/investigating-memory-access-crashes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/investigating-memory-access-crashes.json'
content_hash: 'sha256:5c08661d7c213d34'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)

# 调查内存访问崩溃

<sub>文章</sub>

识别因内存访问问题引发的崩溃，并调查崩溃原因。

## 概述

当 App 以意外方式使用内存时，就会发生内存访问问题引发的崩溃。内存访问问题有许多原因，例如解引用指向无效内存地址的指针、写入只读内存，或跳转到无效地址处的指令。在崩溃报告中，这类崩溃最常通过 `EXC_BAD_ACCESS (SIGSEGV)` 或 `EXC_BAD_ACCESS (SIGBUS)` 异常来识别：

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000000
```

在 macOS 上，错误内存访问引发的崩溃有时只能通过信号来识别，例如 `SIGSEGV`、`SEGV_MAPERR` 或 `SEGV_NOOP`：

```other
Exception Type: SIGSEGV
Exception Codes: SEGV_MAPERR at 0x41e0af0c5ab8
```

Xcode 提供了多种工具，可帮助识别内存访问问题的来源。进一步分析崩溃报告中的各个部分，可能会获得更多见解和线索，帮助你诊断问题。

### 使用 Xcode 调查崩溃

通过异常类型确定崩溃报告与内存访问问题有关后，使用 Xcode 继续调查。Xcode 包含一套调试工具，可在 App 运行时识别内存访问问题。当测试尽可能执行 App 中的更多代码分支时，这些工具最为有效：

- Address Sanitizer
- Undefined Behavior Sanitizer
- Thread Sanitizer

如果 App 包含 Objective-C、C 或 C++ 代码，请运行静态分析器，并修复它发现的所有问题。静态分析器会在构建时分析 App 的代码，识别常见编程错误，包括某些类型的内存管理问题。请参阅[分析代码中的潜在缺陷](https://help.apple.com/xcode/mac/current/#/devb7babe820)。

除崩溃报告中的异常类型外，报告的其他部分可能包含更多线索，提示你应用其他调试工具。例如，如果崩溃由僵尸对象引起，崩溃报告中会出现相应的明显迹象。有关具体线索的信息，请参阅[检查崩溃线程的回溯记录，寻找内存访问问题来源的线索](investigating-memory-access-crashes.md#Check-the-crashed-threads-backtrace-for-clues-about-the-source-of-the-memory-access-issue)。

对于难以诊断的内存访问崩溃，Guard Malloc 等 malloc 调试功能可以提供帮助。有关这些工具的信息，请参阅[启用 Malloc 调试功能](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MallocDebug.html#//apple_ref/doc/uid/20001884)。你可以通过 Xcode 方案编辑器启用这些工具，具体方式参见[使用 sanitizer、API 检查和内存管理诊断运行 App](https://help.apple.com/xcode/mac/current/#/devcef23c572)。

### 检查异常子类型，确定访问无效的原因

崩溃报告中的 `Exception Subtype` 字段包含一个 `kern_return_t` 值，用于描述错误以及被错误访问的内存地址，例如：

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000000
```

在 macOS 上，`Exception Codes` 字段包含异常子类型：

```other
Exception Type:        EXC_BAD_ACCESS (SIGBUS)
Exception Codes:       KERN_MEMORY_ERROR at 0x00000001098c1000
```

异常子类型有以下几种：

- `KERN_INVALID_ADDRESS`。崩溃线程访问了未映射的内存，可能是数据访问，也可能是指令获取。[识别导致问题的内存访问类型](investigating-memory-access-crashes.md#Identify-the-type-of-memory-access-that-caused-the-issue)介绍了如何区分这两种情况。
- `KERN_PROTECTION_FAILURE`。崩溃线程尝试使用受保护的有效内存地址。受保护内存的类型包括只读内存区域或不可执行内存区域。若要了解如何区分受保护内存的类型，请参阅[使用 VM Region Info 在 App 的地址空间中定位内存](investigating-memory-access-crashes.md#Use-VM-Region-Info-to-locate-the-memory-in-your-apps-address-space)。
- `KERN_MEMORY_ERROR`。崩溃线程尝试访问当时无法返回数据的内存，例如已变得不可用的内存映射文件。
- `EXC_ARM_DA_ALIGN`。崩溃线程尝试访问未正确对齐的内存。此异常代码很少见，因为 64 位 ARM CPU 可以处理未对齐的数据。不过，如果内存地址既未对齐、又位于未映射的内存区域中，你可能会看到此异常子类型。你可能还有其他崩溃报告，其中显示的内存访问问题具有不同的异常子类型，但它们很可能由同一个底层内存访问问题引起。

`arm64e` CPU 架构使用具有加密签名的指针认证码，检测并防范对内存中指针的意外更改。可能由指针认证（pointer authentication）失败导致的崩溃，会使用 `KERN_INVALID_ADDRESS` 异常子类型，并在末尾附加一条消息：

```other
Exception Type:  EXC_BAD_ACCESS (SIGBUS)
Exception Subtype: KERN_INVALID_ADDRESS at 0x00006f126c1a9aa0 -> 0x000000126c1a9aa0 (possible pointer authentication failure)
```

高位被错误设置的无效内存访问，看起来可能像指针认证失败，即便原因其实是 App 中的内存损坏问题。

有关指针认证的更多信息，请参阅[让 App 为使用指针认证做好准备](../security/preparing-your-app-to-work-with-pointer-authentication.md)。

### 使用 VM Region Info 在 App 的地址空间中定位内存

崩溃报告中的 `VM Region Info` 字段会显示 App 错误访问的特定内存相对于 App 地址空间中其他部分的位置。以下面的示例为例：

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000000
VM Region Info: 0 is not in any region.  Bytes before following region: 4307009536
      REGION TYPE                      START - END             [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
--->  
      __TEXT                 0000000100b7c000-0000000100b84000 [   32K] r-x/r-x SM=COW  ...pp/MyGreatApp
```

这里，对未映射内存的解引用在 `0x0000000000000000` 处触发了崩溃。这是一个无效地址，具体来说是一个 `NULL` 指针，因此异常子类型以 `KERN_INVALID_ADDRESS` 值指出这一情况。`VM Region Info` 字段显示，此无效地址位于 App 地址空间中某个有效内存区域之前 4,307,009,536 字节的位置。

再来看一个 `KERN_PROTECTION_FAILURE` 示例：

```other
Exception Type:  EXC_BAD_ACCESS (SIGBUS)
Exception Subtype: KERN_PROTECTION_FAILURE at 0x000000016c070a30
VM Region Info: 0x16c070a30 is in 0x16c070000-0x16c074000;  bytes after start: 2608  bytes before end: 13775
      REGION TYPE                      START - END             [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      Stack                  000000016bfe8000-000000016c070000 [  544K] rw-/rwx SM=COW  thread 12
--->  STACK GUARD            000000016c070000-000000016c074000 [   16K] ---/rwx SM=NUL  ...for thread 11
      Stack                  000000016c074000-000000016c0fc000 [  544K] rw-/rwx SM=COW  thread 11
```

在此示例中，被解引用的内存地址为 `0x000000016c070a30`，箭头标出了包含此内存地址的区域。该地址位于名为栈保护区（stack guard）的特殊内存区域中，这个内存区域将一个线程的栈与另一个线程的栈隔开。`PRT` 列显示内存区域的当前权限特性，其中 `r` 表示内存可读，`w` 表示内存可写，`x` 表示内存可执行。

由于栈保护区没有任何权限，对该区域的所有内存访问都无效，崩溃报告将此次内存访问识别为违反内存保护特性。栈保护区只是受保护内存的一种，其他受保护内存区域会具有不同的保护特性组合。

有关 `VM Region Info` 字段的更多信息，请参阅[解读 vmmap 的输出](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/VMPages.html#//apple_ref/doc/uid/20001985-97652)。

### 检查崩溃线程的回溯记录，寻找内存访问问题来源的线索

查看崩溃线程的回溯记录，寻找内存访问问题发生位置的线索。有些类型的内存访问问题（例如解引用 `NULL` 指针）在查看回溯记录并与源代码进行比较时很容易识别。其他内存访问问题则可以通过崩溃线程回溯记录最上方的栈帧来识别：

- 如果 [objc_msgSend](../objectivec/objc_msgsend.md)、`objc_retain` 或 `objc_release` 位于回溯记录顶部，则崩溃由僵尸对象（zombie object）引起。请参阅[调查僵尸对象导致的崩溃](investigating-crashes-for-zombie-objects.md)。
- 如果 `gpus_ReturnNotPermittedKillClient` 位于回溯记录顶部，表示进程尝试在后台使用 OpenGL ES 进行渲染，因此操作系统终止了该进程。若要解决回溯记录中包含此符号的崩溃，请将 OpenGL ES 代码迁移到 Metal。请参阅[将 OpenGL 代码迁移到 Metal](../metal/migrating-opengl-code-to-metal.md)。

在其他情况下，内存访问问题的原因不会出现在回溯记录中。当某个内存位置被意外修改时，就会发生_内存损坏（memory corruption）_。修改发生后，App 的其他部分在尝试使用该内存位置时可能会崩溃。回溯记录会显示访问已修改内存的代码，但不会显示意外修改该内存的代码。意外修改可能早在崩溃之前就已发生，因此无法从回溯记录中看到问题的来源。如果你有许多崩溃报告，都显示出内存访问问题的迹象，但回溯记录各不相同，那么可能存在内存损坏问题。[使用 Xcode 调查崩溃](investigating-memory-access-crashes.md#Investigate-the-crash-with-Xcode)中的信息可帮助识别内存损坏的来源。

### 识别导致问题的内存访问类型

内存访问问题分为两类：无效内存获取和无效指令获取。当代码解引用无效指针时，就会发生_无效内存获取（invalid memory fetch）_。当函数通过错误的函数指针跳转到另一个函数，或通过对意外对象的函数调用进行跳转时，就会发生_无效指令获取（invalid instruction fetch）_。若要确定导致崩溃的内存访问问题类型，请重点查看_程序计数器（program counter）_，它是一个包含导致内存访问异常的指令地址的寄存器。在 ARM CPU 架构上，它是 `pc` 寄存器。在 `x86_64` CPU 架构上，它是 `rip` 寄存器。

如果程序计数器寄存器与异常地址不同，崩溃是由无效内存获取所致。例如，请看以下 `x86_64` CPU 上的 macOS 崩溃报告：

```other
Exception Type:  SIGSEGV
Exception Codes: SEGV_MAPERR at 0x21474feae2c8
...
Thread 12 crashed with X86-64 Thread State:
   rip: 0x00007fff61f5739d    rbp: 0x00007000026c72c0    rsp: 0x00007000026c7248    rax: 0xe85e2965c85400b4 
   rbx: 0x00006000023ee2b0    rcx: 0x00007f9273022990    rdx: 0x00007000026c6d88    rdi: 0x00006000023ee2b0 
   rsi: 0x00007fff358aae0f     r8: 0x00000000000003ff     r9: 0x00006000023edbc0    r10: 0x000021474feae2b0 
   r11: 0x00007fff358aae0f    r12: 0x000060000237af10    r13: 0x00007fff61f57380    r14: 0x00006000023ee2b0 
   r15: 0x0000000000000006 rflags: 0x0000000000010202     cs: 0x000000000000002b     fs: 0x0000000000000000 
    gs: 0x0000000000000000 

```

程序计数器寄存器为 `0x00007fff61f5739d`，与异常地址 `0x21474feae2c8` 不同。此崩溃由无效内存获取引起。

如果程序计数器寄存器与异常地址相同，崩溃是由无效指令获取所致。例如，请看以下 `arm64` CPU 上的 iOS 崩溃报告：

```other
Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Subtype: KERN_INVALID_ADDRESS at 0x0000000000000040
...
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   ???                               0x0000000000000040 0 + 64
...
Thread 0 crashed with ARM Thread State (64-bit):
    x0: 0x0000000000000002   x1: 0x0000000000000040   x2: 0x0000000000000001   x3: 0x000000016dcfe080
    x4: 0x0000000000000010   x5: 0x000000016dcfdc8f   x6: 0x000000016dcfdd80   x7: 0x0000000000000000
    x8: 0x000000010210d3c8   x9: 0x0000000000000000  x10: 0x0000000000000014  x11: 0x0000000102835948
   x12: 0x0000000000000014  x13: 0x0000000000000000  x14: 0x0000000000000001  x15: 0x0000000000000000
   x16: 0x000000010210c0b8  x17: 0x00000001021063b0  x18: 0x0000000000000000  x19: 0x0000000102402b80
   x20: 0x0000000102402b80  x21: 0x0000000204f6b000  x22: 0x00000001f6e6f984  x23: 0x0000000000000001
   x24: 0x0000000000000001  x25: 0x00000001fc47b690  x26: 0x0000000102304040  x27: 0x0000000204eea000
   x28: 0x00000001f6e78fae   fp: 0x000000016dcfdec0   lr: 0x00000001021063c4
    sp: 0x000000016dcfdec0   pc: 0x0000000000000040 cpsr: 0x40000000
   esr: 0x82000006 (Instruction Abort) Translation fault

Binary Images:
0x102100000 - 0x102107fff MyCoolApp arm64  <87760ecf8573392ca5795f0db63a44e2> /var/containers/Bundle/Application/686CA3F1-6CC5-4F84-8126-EE22D03BC161/MyCoolApp.app/MyCoolApp

```

在此示例中，程序计数器寄存器为 `0x0000000000000040`，与 Exception Subtype 中报告的地址相同，表明此崩溃由错误的指令获取引起。由于这是一次错误的指令获取，回溯记录中的栈帧 0 不包含正在运行的函数；回溯记录中显示的是 `???` 和内存地址，而不是符号名称，这一点也说明了这种情况。不过，在正常情况下，链接寄存器 `lr` 包含函数调用后代码将返回的位置。借助链接寄存器中的值，你可以追踪跳转到错误指令指针的来源。

> [!note] 注意
> `x86_64` CPU 架构将返回地址存储在栈上，而不是链接寄存器中，因此无法在 `x86_64` CPU 上追踪错误函数指针的来源。

链接寄存器包含 `0x00000001021063c4`，这是 App 进程中所加载某个二进制文件里的指令地址。崩溃报告的 Binary Images 部分表明，此地址位于 `MyCoolApp` 二进制文件中，因为该地址处于为该二进制文件列出的 `0x102100000-0x102107fff` 范围内。有了此信息，你就可以结合该二进制文件的 `dSYM` 文件使用 `atos` 命令行工具，并识别位于 `0x00000001021063c4` 的对应代码：

```other
% atos -arch arm64 -o MyCoolApp.app.dSYM/Contents/Resources/DWARF/MyCoolApp -l 0x102100000 0x00000001021063c4
-[ViewController loadData] (in MyCoolApp) (ViewController.m:38)
```

[使用命令行对崩溃报告进行符号化](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-with-the-command-line)更详细地讨论了如何使用 `atos` 命令行工具。

## 另请参阅

### 相关文档

- [分析崩溃报告](analyzing-a-crash-report.md) — 识别崩溃报告中有助于诊断问题的线索。

### 内存访问错误

- [调查僵尸对象导致的崩溃](investigating-crashes-for-zombie-objects.md) — 识别僵尸对象的特征，并调查崩溃的原因。
