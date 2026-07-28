---
title: EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sigtrap_sigill
source_url: 'https://developer.apple.com/documentation/xcode/sigtrap_sigill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sigtrap_sigill.json'
content_hash: 'sha256:d6e77000b98bb1a3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)

# EXC_BREAKPOINT (SIGTRAP) and EXC_BAD_INSTRUCTION (SIGILL)

<sub>文章</sub>

跟踪陷阱或无效的 CPU 指令中断了该进程，通常是因为该进程违反了某项要求或超时。

## 概述

跟踪陷阱让已附加的调试器有机会在进程执行到特定位置时对其进行中断。在 ARM 处理器上，这会表现为 `EXC_BREAKPOINT (SIGTRAP)`。在 `x86_64` 处理器上，这会表现为 `EXC_BAD_INSTRUCTION (SIGILL)`。

Swift 运行时对特定类型的不可恢复错误使用跟踪陷阱——有关这些错误的信息，请参阅[处理来自 Swift 运行时错误的崩溃](addressing-crashes-from-swift-runtime-errors.md)。一些更底层的库，例如 [Dispatch](../dispatch.md)，在遇到不可恢复的错误时会以该异常陷入该进程，并在崩溃报告的 `Additional Diagnostic Information` 部分记录有关该错误的附加信息。有关这些消息的信息，请参阅[诊断消息](examining-the-fields-in-a-crash-report.md#Diagnostic-messages)。

如果你想在自己的代码中对不可恢复的错误采用同样的技术，请在 Swift 中调用 [fatalError(_:file:line:)](<../swift/fatalerror(__file_line_).md>) 函数，或在 C 中调用 `__builtin_trap()` 函数。这些函数让系统能够生成带有线程回溯的崩溃报告，展示你是如何走到这个不可恢复的错误的。

非法 CPU 指令意味着程序的可执行文件中包含处理器未实现或无法执行的指令。例如，下面的程序试图执行 CPU 指令 `0x00000001`，而这在 Apple 芯片上并不是有效指令：

```c
#include <stdint.h>

int main(int argc, char **argv) {
    static const uint32_t sTest[] = {
        0x00000001,
    };
    typedef void (*FuncPtr)(void);
    FuncPtr f = (FuncPtr) sTest;
    f();
    return 0;
}
```

## 另请参阅

### 异常

- [EXC_ARITHMETIC](exc_arithmetic.md) — 算术问题终止了该进程，通常是因为除以零或浮点数错误。
- [EXC_BAD_ACCESS](exc_bad_access.md) — 错误的内存访问终止了该进程。
- [EXC_BAD_ACCESS (SIGBUS)](sigbus.md) — 总线错误终止了该进程，通常是因为该进程试图访问内存中未对齐或无效的地址，或是由于指针验证失败。
- [EXC_BAD_ACCESS (SIGSEGV)](sigsegv.md) — 内存段错误终止了该进程，通常是因为该进程试图访问内存中无效或越界的地址。
- [EXC_CRASH](exc_crash.md) — 该进程发生了崩溃。
- [EXC_CRASH (SIGABRT)](sigabrt.md) — 该进程因收到中止信号而终止。
- [EXC_CRASH (SIGKILL)](sigkill.md) — 操作系统终止了该进程，通常是因为后台任务违反了某项要求、设备资源有限，或用户强制退出了 App。
- [EXC_CRASH (SIGQUIT)](sigquit.md) — 另一个进程终止了该进程，通常是因为该进程违反了某项要求或超时。
- [EXC_CRASH (SIGSYS)](sigsys.md) — 系统调用的错误参数终止了该进程。
- [EXC_CRASH (SIGTERM)](sigterm.md) — 软件终止信号终止了该进程。
- [EXC_GUARD](exc_guard.md) — 该进程违反了受保护资源的保护机制，通常与文件描述符有关。
- [EXC_RESOURCE](exc_resource.md) — 操作系统因该进程超出了资源消耗限制（如 CPU 时间或内存）而停止了该进程。
