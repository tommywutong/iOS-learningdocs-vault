---
title: 异常编程主题
apple_id: 10000012i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Exceptions/Tasks/ControllingAppResponse.html
archived_at: '2026-07-15T07:15:39.430679Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [异常编程主题](Introduction%20to%20Exception%20Programming%20Topics%20for%20Cocoa.md)


[下一篇](Exceptions%20in%2064-Bit%20Executables.md) [上一篇](Predefined%20Exceptions.md)

# 控制程序对异常的响应

本文档介绍了一些用户默认设置以及 Exception Handling 框架的 API，可用来控制应用程序响应特定类型错误时的行为。

要在 Cocoa 项目（无论是应用程序还是非应用程序）中使用 Exception Handling 框架提供的服务，请将 `/System/Library/Frameworks` 中的 `ExceptionHandling.framework` 添加到 Xcode 项目。还需要在使用该框架的类的头文件或实现文件中插入以下导入指令：

```objc
#import <ExceptionHandling/NSExceptionHandler.h>
```


某些类型的应用程序错误通常会导致 Cocoa 应用程序突然退出。对于最常见的三类此类错误，可以使用用户默认设置 `NSExceptionHandlingMask` 控制这一行为（仅适用于基于 Application Kit 的应用程序）：

- 未捕获的 NSException；
- 系统级异常（例如无效内存访问）；
- Objective-C 运行时错误（例如向已释放对象发送消息）。

对于这些错误类型，可以设置 `NSExceptionHandlingMask` 执行以下操作之一：

- 发生此类错误时，向控制台输出描述性日志和栈跟踪。
- 处理错误，防止由此导致的突然终止。
- 同时执行以上两项操作。

通过将要记录或处理的错误类型所对应的值相加，可以构建该掩码：

__表 1__　异常处理常量与 `defaults` 值

| 操作类型 | 常量 | `defaults` 值 |
| --- | --- | --- |
| 记录未捕获的 NSException | `NSLogUncaughtExceptionMask` | 1 |
| 处理未捕获的 NSException | `NSHandleUncaughtExceptionMask` | 2 |
| 记录系统级异常 | `NSLogUncaughtSystemExceptionMask` | 4 |
| 处理系统级异常 | `NSHandleUncaughtSystemExceptionMask` | 8 |
| 记录运行时错误 | `NSLogUncaughtRuntimeErrorMask` | 16 |
| 处理运行时错误 | `NSHandleUncaughtRuntimeErrorMask` | 32 |

因此，如果在命令行（“终端”应用中）输入以下命令：

```shell
defaults write NSGlobalDomain NSExceptionHandlingMask 63
```

就会对所有应用程序中的全部未捕获异常、系统级异常和运行时错误启用上述记录与处理行为。

异常处理常量中的“处理”一词会因异常类型而具有特定含义。Exception Handling 框架通过将系统级异常和运行时错误转换为 [NSException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSException/Description.html#//apple_ref/occ/cl/NSException) 对象来处理它们。这些异常对象的 `userInfo` 字典中包含键为 `NSStackTraceKey` 的栈跟踪。该框架通过终止发生异常的线程来处理未捕获的 `NSException` 对象。Cocoa 应用程序主线程上的异常由顶层处理器捕获，这些处理器通常由 Application Kit 安装。

除了使用 `NSExceptionHandlingMask` 用户默认设置，也可以通过 Exception Handling 框架的 `setExceptionHandlingMask:` 方法获得相同的异常处理行为。对于应用程序和非应用程序 Cocoa 可执行文件，都需要链接 Exception Handling 框架并发送以下消息：

```objc
[[NSExceptionHandler defaultExceptionHandler] setExceptionHandlingMask:aMask];
```

`aMask` 参数是通过对上表所列常量执行按位“或”运算组成的位掩码。有关 NSExceptionHandler API 的更多详情，请参阅 Exception Handling 框架的头文件。

出于调试目的，还可以使用相同机制报告原本会被捕获的 NSException。为此，既可以使用 `defaults` 系统的 `NSExceptionHandlingMask` 属性，也可以使用 NSExceptionHandler 类的 `setExceptionHandlingMask:` 方法。相关常量和值如下表所示：

__表 2__　调试常量与 `defaults` 值

| 操作类型 | 常量 | `defaults` 值 |
| --- | --- | --- |
| 记录本会由 NSApplication 顶层异常处理器捕获的异常。请参阅下文说明。 | `NSLogTopLevelExceptionMask` | 64 |
| 处理本会由 NSApplication 顶层异常处理器捕获的异常 | `NSHandleTopLevelExceptionMask` | 128 |
| 记录将在较低层级被捕获的异常 | `NSLogOtherExceptionMask` | 256 |
| 处理将在较低层级被捕获的异常 | `NSHandleOtherExceptionMask` | 512 |

在这些情况下，处理异常仅意味着在其 `userInfo` 字典中以 `NSStackTraceKey` 为键添加栈跟踪。请注意，只应在调试时记录或处理已捕获的异常，正常情况下不应这样做，因为这可能产生大量输出，或改变应用程序的正常行为。

为了进行更深入的调试，可以更改 NSExceptionHandler 所处理任何状况的处理行为，让应用程序改为暂停，以便附加调试器。可以通过为 `NSExceptionHangingMask` 用户默认设置提供各值之和，或通过传给 NSExceptionHandler 类 `setExceptionHangingMask:` 的位掩码来控制该行为。下表列出了有效的常量和 `defaults` 值：

| 操作类型 | 常量 | `defaults` 值 |
| --- | --- | --- |
| 遇到未捕获异常时暂停 | `NSHangOnUncaughtExceptionMask` | 1 |
| 遇到系统级异常时暂停 | `NSHangOnUncaughtSystemExceptionMask` | 2 |
| 遇到运行时错误时暂停 | `NSHangOnUncaughtRuntimeErrorMask` | 4 |
| 遇到顶层捕获的异常时暂停 | `NSHangOnTopLevelExceptionMask` | 8 |
| 遇到其他已捕获异常时暂停 | `NSHangOnOtherExceptionMask` | 16 |

为辅助调试，可以使用 `atos` 命令行工具将数值形式的栈跟踪转换为符号形式。（有关该命令行工具的详情，请参阅 `atos(1)` 手册页。）

不必在 Xcode 和“终端”shell 之间来回切换，可以在程序中添加代码，使用 `atos` 将符号化栈跟踪输出到控制台。清单 1 展示了具体做法。`printStackTrace:` 方法从传入的 `NSException` 对象中提取数值形式的栈跟踪，然后构建表示 `atos` 命令的 [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask) 对象，并将栈跟踪作为参数。它会启动该子任务，并将生成的符号化回溯输出到标准输出（即 Xcode 中的运行日志）。

__清单 1__　输出异常符号化回溯的方法

```objc
- (BOOL)exceptionHandler:(NSExceptionHandler *)sender shouldLogException:(NSException *)exception mask:(unsigned int)mask
{
    [self printStackTrace:exception];
    return YES;
}

- (void)printStackTrace:(NSException *)e
{
    NSString *stack = [[e userInfo] objectForKey:NSStackTraceKey];
    if (stack) {
        NSTask *ls = [[NSTask alloc] init];
        NSString *pid = [[NSNumber numberWithInt:[[NSProcessInfo processInfo] processIdentifier]] stringValue];
        NSMutableArray *args = [NSMutableArray arrayWithCapacity:20];

        [args addObject:@"-p"];
        [args addObject:pid];
        [args addObjectsFromArray:[stack componentsSeparatedByString:@"  "]];
        // 注意：函数地址之间用两个空格分隔，而不是一个空格。

        [ls setLaunchPath:@"/usr/bin/atos"];
        [ls setArguments:args];
        [ls launch];
        [ls release];

    } else {
        NSLog(@"No stack trace available.");
    }
}
```

在本例中，委托在实现 [exceptionHandler:shouldLogException:mask:](https://developer.apple.com/documentation/objectivec/nsobject/1489856-exceptionhandler) 时调用 `printStackTrace:` 方法；此时异常正在处理，但尚未导致被调试的可执行文件终止。`atos` 工具的输出与 `NSExceptionHandler` 日志信息结合后，类似于清单 2。

__清单 2__　NSExceptionHandler 日志内容及 `atos` 输出

```text
2006-08-21 12:18:19.727 ExceptionHandleTest[916] NSExceptionHandler has recorded the following exception:
NSInvalidArgumentException -- *** -[NSCFString count]: selector not recognized [self = 0x2a00c]
Stack trace:  0x9275c27b  0x92782fd7  0x9280b0be  0x9272f207  0x90a51ba1  0x0002995f  0x00023f81  0x00001ca6  0x00001bcd  0x00000001
__NSRaiseError (in Foundation)
+[NSException raise:format:] (in Foundation)
-[NSObject doesNotRecognizeSelector:] (in Foundation)
-[NSObject(NSForwardInvocation) forward::] (in Foundation)
__objc_msgForward (in libobjc.A.dylib)
-[ExceptionTest testException] (in ExceptionHandleTest) (ExceptionTest.m:31)
_main (in ExceptionHandleTest) (ExceptionHandleTest.m:10)
start (in ExceptionHandleTest)
start (in ExceptionHandleTest)
0x00000001 (in ExceptionHandleTest)
```

还有其他方法可以达到相同效果。例如，可以将输出符号化栈跟踪的方法放在添加到 `NSException` 的分类中，而不是将其作为委托类的方法。

[下一篇](Exceptions%20in%2064-Bit%20Executables.md) [上一篇](Predefined%20Exceptions.md)
