---
title: 分析崩溃报告
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/analyzing-a-crash-report
source_url: 'https://developer.apple.com/documentation/xcode/analyzing-a-crash-report'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/analyzing-a-crash-report.json'
content_hash: 'sha256:59bc3f1157015cdc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md)

# 分析崩溃报告

<sub>文章</sub>

识别崩溃报告中有助于诊断问题的线索。

## 概述

崩溃报告是 App 崩溃时其状态的详细日志，在你尝试修复问题之前，它是识别问题的重要资源。如果你正在调查一个无法用[识别常见崩溃的原因](identifying-the-cause-of-common-crashes.md)中讨论的技巧解决的崩溃，就需要对完整的崩溃报告进行仔细分析。

> [!important] 重要
> 请始终分析由操作系统生成的、已完全符号化的崩溃报告。请参阅[确定崩溃报告是否已完成符号化](adding-identifiable-symbol-names-to-a-crash-report.md#Determine-if-a-crash-report-is-symbolicated)来验证你的崩溃报告是否已完全符号化。

在分析崩溃报告时，请阅读所有部分中的信息。在你就崩溃原因形成假设的过程中，针对崩溃报告每个部分中的数据提出问题，以此完善或推翻该假设。有些线索由崩溃报告中的字段明确记录，但另一些线索则较为隐晦，需要你留意细微之处才能发现。对崩溃报告进行透彻分析并形成假设，需要时间和实践才能掌握，但这是让你的 App 更加健壮的关键工具。

> [!note] 注意
> 如果你向 Apple 请求帮助分析崩溃报告，例如通过错误报告、Apple Developer Forums 或 Developer Technical Support，请始终提供操作系统生成的完整崩溃报告。来自操作系统的部分崩溃报告，以及由你 App 中包含的第三方分析库生成的崩溃报告，都不包含全部必要信息。

### 从用户的角度出发

从崩溃报告的信息中找到一个切入点，从用户的角度思考这次崩溃，以完善你的假设。例如，回溯记录中的某一帧可能表明 App 的某个特定功能正在使用中，你可以据此思考崩溃报告中的其他信息与该功能之间的关系。

### 根据相似和独特的细节对多份崩溃报告进行分组

如果你有大量崩溃报告，可以尝试将它们分组，以厘清崩溃的来源。如果许多崩溃报告包含完全相同的信息，问题很可能是可以稳定重现的，崩溃报告中的共同细节有助于你锁定问题。如果你的崩溃报告表面上各不相同，但你怀疑其根本原因相同，请留意任何看起来异常的细节。把带有异常细节的崩溃报告单独归为一组。通过根据相似和不同的细节对崩溃报告分组，你有时能发现单独查看每份崩溃报告时无法察觉的、关于崩溃原因的洞见。

### 检查头部信息以确定崩溃发生的环境

如果你有多份相似的崩溃报告，可以利用头部信息来帮助理解问题的范围，并锁定你需要用来重现该问题的具体操作系统版本和设备。以下这些问题有助于完善你对崩溃的假设：

- 这次崩溃发生在你 App 的多个版本中，还是只发生在一个版本中？
- 这次崩溃发生在操作系统的多个版本中吗？
- 这次崩溃是否只发生在某一类设备上，例如只出现在 iPad 而不出现在 iPhone 上？
- 这次崩溃源自你的主 App，还是源自你的某个 App 扩展？
- 这次崩溃是否来自你 App 的某个 TestFlight beta 版本？
- 所有崩溃是否都来自同一个 App 精简变体？如果你导出该特定的 App 变体，能否重现这次崩溃？要导出特定的 App 变体，请参阅[为 beta 测试和发布分发你的 App](distributing-your-app-for-beta-testing-and-releases.md)。
- App 是在哪种设备型号上崩溃的？你在具有类似性能的设备上做过多少测试？
- 是多名用户都遇到了这次崩溃，还是只有少数几个独立用户遇到？使用 `CrashReporter Key` 或 `Beta Identifier` 字段来判断这一点。
- App 在崩溃前运行了多长时间？使用 `Date/Time` 和 `Launch Time` 字段来判断这一点。

如果你不熟悉崩溃报告这一部分中的某个具体字段或其取值，请参阅[头部](examining-the-fields-in-a-crash-report.md#Header)。

### 识别异常信息

每份崩溃报告都会记录异常信息，展示 App 进程终止的确切机制。终止始终是错误处理的最后一步，但它始于 App 或其所使用的框架中出现不可恢复的状况之时。例如，App 可能直接请求终止，比如调用 `abort()`。再举一个不同的例子，操作系统可能为了执行某项系统策略而终止该进程，例如通过确保 App 响应能力的看门狗。

异常信息缩小了你正在分析的崩溃的可能来源范围，并有助于确定你需要在崩溃报告其他部分中寻找的线索。请参阅[了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md)，了解你正在分析的崩溃报告中具体异常类型的详细信息，然后回答以下问题：

- 异常类型是什么？该异常定义了哪一类错误？
- 是哪个线程触发了崩溃？崩溃线程回溯记录中的各帧，与该异常类型所传达的信息之间有什么关系？
- 该异常类型排除了哪些类型的潜在问题？例如，`EXC_BAD_ACCESS` 异常排除了崩溃是由未捕获的语言异常引起的可能性。
- `Termination Reason` 字段中是否有附加代码？该代码是什么含义？
- 该异常类型是否表明有特定的诊断工具适合用来发现该问题？
- 该异常是否与某种特定类型的系统资源有关？

如果你不熟悉这一部分中的某个字段，请参阅[异常信息](examining-the-fields-in-a-crash-report.md#Exception-information)。

### 查找诊断消息

对于某些类型的问题，崩溃报告可能在「Exception Information」部分和「Backtraces」部分之间包含附加的诊断信息。这些信息与异常类型直接相关。

- 根据异常类型判断，这次崩溃是否由未捕获的语言异常引起？如果是，该消息中是否有关于抛出该异常的 API 的附加信息？更多信息请参阅[处理语言异常崩溃](addressing-language-exception-crashes.md)。
- 根据异常类型判断，这次崩溃是否由内存访问问题引起？请参阅[排查内存访问崩溃](investigating-memory-access-crashes.md)了解如何解读所提供的 `VM Region Info`。
- 是否存在一个 `Termination Description` 字段，表明操作系统的某个特定部分参与其中？`Termination Reason` 字段中是否有附加代码？该消息提供了哪些关于问题根源的线索？
- 是否存在一个 `Application Specific Information` 字段？该消息中是否提到了某个具体的 API？你在代码中的哪些地方使用了该 API？

如果你不熟悉这一部分中的某个字段，请参阅[诊断消息](examining-the-fields-in-a-crash-report.md#Diagnostic-messages)。

### 阅读回溯记录

崩溃报告中的回溯记录展示了崩溃发生时正在执行的确切方法——请参阅[回溯记录](examining-the-fields-in-a-crash-report.md#Backtraces)了解该部分中每一列的含义。作为切入点，先查看崩溃线程，以及（如果存在的话）`Last Exception Backtrace`。针对回溯记录回答以下问题：

- 这个线程在 App 中承担什么功能？它是主线程，还是具有特定用途的其他线程？
- 是否抛出了语言异常？`Last Exception Backtrace` 显示了什么？
- App 的哪些部分使用了这个线程，以及这个线程回溯记录中出现的这些函数？
- 回溯记录中你 App 的二进制文件与 Apple 系统框架的构成比例是怎样的？

即使回溯记录中的函数不是你直接调用的，它们也包含关键线索。例如，下面这份回溯记录除了该 App 的 `main` 函数外全部是系统框架，但这次崩溃是由某个 iPadOS App 中一个无效的弹出窗口配置引起的：

```other
Last Exception Backtrace:
0   CoreFoundation                    0x1a1801190 __exceptionPreprocess + 228
1   libobjc.A.dylib                   0x1a09d69f8 objc_exception_throw + 55
2   UIKitCore                         0x1cd5d0af0 -[UIPopoverPresentationController presentationTransitionWillBegin] + 2739
3   UIKitCore                         0x1cd5d9358 __71-[UIPresentationController _initViewHierarchyForPresentationSuperview:]_block_invoke + 2175
4   UIKitCore                         0x1cd5d6ea4 __56-[UIPresentationController runTransitionForCurrentState]_block_invoke + 463
5   UIKitCore                         0x1cdc5c0ac _runAfterCACommitDeferredBlocks + 295
6   UIKitCore                         0x1cdc4abfc _cleanUpAfterCAFlushAndRunDeferredBlocks + 351
7   UIKitCore                         0x1cdc77a6c _afterCACommitHandler + 115
8   CoreFoundation                    0x1a179250c __CFRUNLOOP_IS_CALLING_OUT_TO_AN_OBSERVER_CALLBACK_FUNCTION__ + 31
9   CoreFoundation                    0x1a178d234 __CFRunLoopDoObservers + 411
10  CoreFoundation                    0x1a178d7b0 __CFRunLoopRun + 1227
11  CoreFoundation                    0x1a178cfc4 CFRunLoopRunSpecific + 435
12  GraphicsServices                  0x1a398e79c GSEventRunModal + 103
13  UIKitCore                         0x1cdc50c38 UIApplicationMain + 211
14  MyGreatApp                        0x10079600c main (in MyGreatApp) (AppDelegate.swift:12)
15  libdyld.dylib                     0x1a124d8e0 start + 3
```

第 3 帧和第 4 帧提示这次崩溃与呈现某个视图控制器有关，第 2 帧则提示该 App 正在呈现一个弹出窗口。即使回溯记录中没有来自该 App 的代码，这些信息也能缩小你需要关注的 App 代码范围。

你通常可以根据线程回溯记录底部的帧来判断该线程的用途。App 主线程的底部帧中会有 [NSApplicationMain(_:_:)](<../appkit/nsapplicationmain(____).md>) 或 [UIApplicationMain(_:_:_:_:)](<../uikit/uiapplicationmain(________)-1yub7.md>)。通过 [Dispatch](../dispatch.md) 框架创建的线程，其底部帧中会有 `start_wqthread`。在你更仔细地查看崩溃线程的回溯记录时，请思考你的 App 所呈现的状态是否与你对其运作方式的预期一致：

- 该 App 的代码是否应该在这个特定线程上运行？
- 崩溃线程是不是一个后台线程？
- 是否有任何回溯记录显示该 App 在主线程以外的线程上操作界面元素？你是否已经启用 `Main Thread Checker` 测试过你的 App？
- 如果你的代码使用了某个接受完成处理程序的 API，该 API 是否保证了完成处理程序所使用的具体队列？你的代码是否预期使用的是那个队列？
- 如果你的代码使用了某个由你提供 [DispatchQueue](../dispatch/dispatchqueue.md) 的 API，崩溃报告是否显示你使用的正是你所预期的那个队列？

除了崩溃线程或语言异常的回溯记录之外，其他线程的回溯记录也能提供关于 App 所处状态的附加线索。这些线索比较隐晦：

- 其他任何线程是否有助于表明该 App 所处的状态？例如，如果你看到某些线程中含有来自 [Contacts](../contacts.md) 框架的帧，而你的 App 只在某一部分访问联系人，你就可以将调查重点集中到 App 的那部分。
- 其他线程的回溯记录中是否有与崩溃线程回溯记录中的帧相关的内容？这说明了 App 处于什么状态？
- 是否有许多线程呈现相似的状态，例如在等待系统资源之前，都有来自你 App 的同一组函数？

在某些类型的崩溃中，崩溃线程的回溯记录并不总是包含问题的根源。[处理看门狗终止](addressing-watchdog-terminations.md)描述了看门狗终止发生这种情况的场景，[排查内存访问崩溃](investigating-memory-access-crashes.md)则描述了内存损坏崩溃出现这种情况的场景。

### 了解崩溃线程的寄存器

分析大多数崩溃报告时都不需要考虑寄存器状态。然而，如果你正在调查一个棘手的内存访问问题，寄存器能提供崩溃报告其他地方找不到的信息。

- 这次内存访问是内存读取，还是指令读取？
- 程序计数器、链接寄存器和栈指针寄存器中是否包含你程序地址空间内的有效地址？
- 如果你使用 `atos` 对链接寄存器中的地址进行符号化，得到的是哪个函数？该函数是否通过函数指针跳转到其他代码？[使用命令行对崩溃报告进行符号化](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-with-the-command-line)描述了如何使用 `atos`。

[确定引发问题的内存访问类型](investigating-memory-access-crashes.md#Identify-the-type-of-memory-access-that-caused-the-issue)描述了如何利用这些问题来诊断内存访问崩溃。

### 验证你的框架是否出现在二进制映像中

使用崩溃报告的 Binary Images 部分，清点你 App 加载的框架。你可以通过文件路径识别出你 App 中的框架。

- 崩溃发生时，App 加载了哪些框架？你 App 提供的框架中是否有缺失的？
- 如果某个框架缺失，你原本预期系统会在 App 启动时自动加载该框架，还是你通过调用 `dlopen(_:_:)` 手动加载它？
- 有多少框架来自你的 App？如果你正在调查一次看门狗终止，App 内部框架数量过多可能会占用 App 启动时间预算中相当大的一部分。

有关这一部分中每一列的含义，请参阅[二进制映像](examining-the-fields-in-a-crash-report.md#Binary-images)。

## 另请参阅

### 崩溃报告

- [为崩溃报告添加可识别的符号名称](adding-identifiable-symbol-names-to-a-crash-report.md) — 用与你 App 代码对应的函数名和行号，替换崩溃报告中的十六进制地址。
- [识别常见崩溃的原因](identifying-the-cause-of-common-crashes.md) — 在崩溃报告中查找能够识别常见问题的规律模式，并根据该模式排查问题。
- [检查崩溃报告中的字段](examining-the-fields-in-a-crash-report.md) — 了解崩溃报告的结构，以及每个字段所包含的信息。
- [解读崩溃报告的 JSON 格式](interpreting-the-json-format-of-a-crash-report.md) — 了解系统在崩溃报告 JSON 中包含的对象的结构和属性。
- [了解崩溃报告中的异常类型](understanding-the-exception-types-in-a-crash-report.md) — 了解异常类型能告诉你哪些关于 App 崩溃原因的信息。
