---
title: 处理语言异常崩溃
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/addressing-language-exception-crashes
source_url: 'https://developer.apple.com/documentation/xcode/addressing-language-exception-crashes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/addressing-language-exception-crashes.json'
content_hash: 'sha256:4fb69aa13285a2f5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)

# 处理语言异常崩溃

<sub>文章</sub>

识别语言异常的迹象，并处理未捕获语言异常导致的崩溃。

## 概述

Objective-C 异常等语言异常表示在运行时发现的编程错误，例如使用越界索引访问数组，或未实现协议的必需方法。若要确定崩溃是否由语言异常导致，请先确认崩溃报告中包含以下模式：

```other
Exception Type:  EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
```

未被捕获的语言异常所导致的崩溃，会在崩溃报告中包含 `Last Exception Backtrace`。请确认存在此回溯，以判断崩溃是由语言异常导致。

> [!note] 注意
> 对于 C++ 异常，系统不会提供指向抛出异常代码的异常回溯。

### 识别抛出异常的 API

在 `Last Exception Backtrace` 中，操作系统会记录导致异常的完整函数调用回溯。此回溯以能够明确表明抛出了语言异常的栈帧结束。在回溯中继续向下查看，可以找到有关哪个方法抛出异常、以及代码的哪个部分调用了该方法的关键信息。例如：

```other
Last Exception Backtrace:
0   CoreFoundation                    0x1bf596a48 __exceptionPreprocess + 220
1   libobjc.A.dylib                   0x1bf2bdfa4 objc_exception_throw + 55
2   CoreFoundation                    0x1bf49b0ec -[NSException raise] + 11
3   Foundation                        0x1bf879170 -[NSObject+ 205168 (NSKeyValueCoding) setValue:forKey:] + 311
4   UIKitCore                         0x1c2ffa0b4 -[UIViewController setValue:forKey:] + 99
5   UIKitCore                         0x1c32c1234 -[UIRuntimeOutletConnection connect] + 123
6   CoreFoundation                    0x1bf470f3c -[NSArray makeObjectsPerformSelector:] + 251
7   UIKitCore                         0x1c32be3a4 -[UINib instantiateWithOwner:options:] + 1967
8   UIKitCore                         0x1c3000f18 -[UIViewController _loadViewFromNibNamed:bundle:] + 363
9   UIKitCore                         0x1c30019a4 -[UIViewController loadView] + 175
10  UIKitCore                         0x1c3001c5c -[UIViewController loadViewIfRequired] + 171
11  UIKitCore                         0x1c3002360 -[UIViewController view] + 27
12  UIKitCore                         0x1c3017a98 -[UIViewController _setPresentationController:] + 107
13  UIKitCore                         0x1c30108a4 -[UIViewController _presentViewController:modalSourceViewController:presentationController:animationController:interactionController:completion:] + 1343
14  UIKitCore                         0x1c30122b8 -[UIViewController _presentViewController:withAnimationController:completion:] + 4255
15  UIKitCore                         0x1c3014794 __63-[UIViewController _presentViewController:animated:completion:]_block_invoke + 103
16  UIKitCore                         0x1c3014c90 -[UIViewController _performCoordinatedPresentOrDismiss:animated:] + 507
17  UIKitCore                         0x1c30146e4 -[UIViewController _presentViewController:animated:completion:] + 195
18  UIKitCore                         0x1c301494c -[UIViewController presentViewController:animated:completion:] + 159
19  MyCoolApp                         0x104e8b1ac MyViewController.viewDidLoad() (in MyCoolApp) (MyViewController.swift:35)
```

在此回溯示例中，操作系统在栈帧 0–2 中抛出异常。栈帧 3 引发异常，是因为它无法完成在栈帧 4–7 中载入内存的 Interface Builder 文件所定义 `@IBOutlet` 属性的连接。栈帧 8–17 显示 UIKit 正在准备呈现 Interface Builder 中定义的这个视图。栈帧 18 表明此次崩溃始于 App 调用 [present(_:animated:completion:)](<../uikit/uiviewcontroller/present(__animated_completion_).md>)，该调用来自栈帧 19 中的 [viewDidLoad()](<../uikit/uiviewcontroller/viewdidload().md>)。栈帧 19 是调查此次崩溃的关键信息；它提示你检查 `MyViewController.swift` 第 35 行附近的源代码，以确定哪个 Interface Builder 文件包含问题。

> [!important] 重要
> 如果抛出异常的 API 是 [doesNotRecognizeSelector(_:)](<../objectivec/nsobject-swift.class/doesnotrecognizeselector(__).md>):，崩溃可能由僵尸对象导致。有关其他信息，请参阅[调查僵尸对象导致的崩溃](investigating-crashes-for-zombie-objects.md)。

### 检查异常信息

操作系统提供的未捕获异常处理程序会在终止进程前将异常信息记录到控制台。如果在 Xcode 调试器已附加到 App 的情况下重现语言异常导致的崩溃，就可以看到此信息：

```other
Application Specific Information:
*** Terminating app due to uncaught exception 'NSUnknownKeyException',
    reason: '[<MyCoolApp.MyViewController 0x105510d50> setValue:forUndefinedKey:]:
    this class is not key value coding-compliant for the key refreshButton.'
```

继续[识别抛出异常的 API](addressing-language-exception-crashes.md#Identify-the-API-throwing-the-exception)中的示例，此异常信息补充了异常回溯中不可见的细节：Interface Builder 文件有一个名为 `refreshButton` 的 outlet，但 `MyViewController` 类没有声明同名的 `@IBOutlet` 属性。

对于某些错误，崩溃报告会排除异常信息，以防泄露 App 使用者的私密信息。对于 App 使用框架 API 时生成的许多常见语言异常，崩溃报告会包含异常信息。有关这些异常的更多信息，请参阅[读取异常信息](reading-an-exception-message.md)。

> [!note] 注意
> [AppKit](../appkit.md) App 具有默认异常处理程序，会捕获从其运行循环执行的代码所引发的所有语言异常。它会记录异常信息，然后允许 App 继续运行。

如果可以重现语言异常崩溃，请设置异常断点来暂停执行，并使用 Xcode 调试器检查 App 状态，具体方法请参阅[在事件发生时暂停执行](https://help.apple.com/xcode/mac/current/#/devfeaa874d0)。若要在异常断点暂停执行时自动输出异常信息，请为异常断点添加一个运行调试器命令的操作：

```other
po $arg1
```

### 处理系统语言异常导致的崩溃

识别出抛出异常的操作系统 API 后，请查阅该 API 的文档，以确定触发异常的条件。此外，请尝试在 Xcode 调试器已附加的情况下重现崩溃，以便从控制台获取异常的其他信息，并利用回溯中的栈帧定位需要测试的具体代码。

如果无法重现崩溃，请使用所有线程回溯（而不仅是异常回溯）作为线索，了解 App 崩溃时正在执行的操作，并思考这些信息反映出的 App 状态。以这些线索为起点处理崩溃。

### 处理 App 代码抛出的语言异常

64 位版本的 iOS 和 iPadOS 使用零开销异常实现，其中每个函数都包含额外数据，用于描述函数抛出异常时如何展开栈或退出每个栈帧。如果抛出的异常遇到没有展开数据的栈帧，异常处理便无法继续，进程也会停止。栈中更靠上的位置可能存在异常处理程序，但如果某个栈帧缺少展开数据，就无法从抛出异常的栈帧到达该异常处理程序。

如果发现 App 在异常处理域内抛出的异常未被捕获，请确认 App 和库的构建设置允许编译器创建展开表：

- 不要指定 `-no_compact_unwind` 标志。
- 如果包含纯 C 代码，请指定 `-funwind-tables` 标志。

## 另请参阅

### 相关文档

- [分析崩溃报告](analyzing-a-crash-report.md) — 识别崩溃报告中有助于诊断问题的线索。

### 运行时错误

- [处理 Swift 运行时错误导致的崩溃](addressing-crashes-from-swift-runtime-errors.md) — 识别 Swift 运行时错误的迹象，并处理运行时错误导致的崩溃。
- [读取异常信息](reading-an-exception-message.md) — 了解并处理 App 崩溃的常见原因。
