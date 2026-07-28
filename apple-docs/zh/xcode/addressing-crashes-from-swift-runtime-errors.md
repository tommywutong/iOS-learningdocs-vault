---
title: 处理 Swift 运行时错误引发的崩溃
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/addressing-crashes-from-swift-runtime-errors
source_url: 'https://developer.apple.com/documentation/xcode/addressing-crashes-from-swift-runtime-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/addressing-crashes-from-swift-runtime-errors.json'
content_hash: 'sha256:399a9e76d96bc9ab'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [识别常见崩溃的原因](identifying-the-cause-of-common-crashes.md)

# 处理 Swift 运行时错误引发的崩溃

<sub>文章</sub>

识别 Swift 运行时错误的迹象，并处理运行时错误引发的崩溃。

## 概述

Swift 使用内存安全（memory safety）技术尽早捕获编程错误。可选值（optional）要求你思考处理 `nil` 值的最佳方式。类型安全可防止将对象转换为与其实际类型不匹配的类型。

如果你使用 `!` 运算符强制解包一个值为 `nil` 的可选值，或者使用 `as!` 运算符强制向下类型转换但转换失败，Swift 运行时会捕获这些错误并有意让 App 崩溃。如果你能重现运行时错误，Xcode 会将问题相关信息记录到控制台。在 ARM 处理器上，崩溃报告中的异常信息如下所示：

```other
Exception Type:  EXC_BREAKPOINT (SIGTRAP)
...
Termination Signal: Trace/BPT trap: 5
Termination Reason: Namespace SIGNAL, Code 0x5
```

在 Intel 处理器上（包括面向 macOS、Mac Catalyst 以及 iOS、iPadOS、tvOS 和 watchOS 模拟器的 App），崩溃报告中的异常信息如下所示：

```other
Exception Type:        EXC_BAD_INSTRUCTION (SIGILL)
...
Exception Note:        EXC_CORPSE_NOTIFY

Termination Signal:    Illegal instruction: 4
Termination Reason:    Namespace SIGNAL, Code 0x4
```

### 识别错误的位置

崩溃报告会显示遇到运行时错误的线程，其中回溯记录中的一个栈帧会标明具体代码行。

```other
Thread 0 Crashed:
0   MyCoolApp                         0x0000000100a71a88 @objc ViewController.viewDidLoad() (in MyCoolApp) (ViewController.swift:18)
1   MyCoolApp                         0x0000000100a71a40 @objc ViewController.viewDidLoad() (in MyCoolApp) (ViewController.swift:18)
2   UIKitCore                         0x00000001c569e920 -[UIViewController _sendViewDidLoadWithAppearanceProxyObjectTaggingEnabled] + 100
3   UIKitCore                         0x00000001c56a3430 -[UIViewController loadViewIfRequired] + 936
4   UIKitCore                         0x00000001c56a3838 -[UIViewController view] + 28
```

在此示例中，线程 0 遇到了错误。该线程的栈帧 0 表明，运行时错误发生在 `ViewController.swift` 第 18 行的 `viewDidLoad` 方法中：

```other
0   MyCoolApp                         0x0000000100a71a88 @objc ViewController.viewDidLoad() (in MyCoolApp) (ViewController.swift:18)
```

### 修改代码

查看回溯记录中的其他栈帧，找出产生错误的确切函数调用，并确定你是否使用了强制解包或强制向下类型转换。强制解包使用 `!` 运算符。例如：

```swift
let image = UIImage(named: "aMissingIcon")!
print("Image size: \(image.size)")
```

不要强制解包，而应在 `nil` 值首次出现在代码中时使用可选绑定（optional binding）妥善处理：

```swift
if let image = UIImage(named: "aMissingIcon") {
    print("Image size: \(image.size)")
}
```

有关[可选值](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/TheBasics.html#//apple_ref/doc/uid/TP40014097-CH5-ID330)的更多信息，请参阅 Swift 文档。

对于类型转换，强制向下类型转换使用 `as!` 运算符。如果 `library` 包含 `Song` 以外的类型，以下示例会崩溃：

```swift
for item in library {
    let song = item as! Song
    print("Song: \(song.name), by \(song.artist)")
}
```

不要强制向下类型转换，而应使用条件向下类型转换，妥善处理对象类型与预期类型不匹配的情况：

```swift
for item in library {
    if let song = item as? Song {
         print("Song: \(song.name), by \(song.artist)")
    }
}
```

有关[类型转换](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/TypeCasting.html#//apple_ref/doc/uid/TP40014097-CH22)的更多信息，请参阅 Swift 文档。

## 另请参阅

### 相关文档

- [分析崩溃报告](analyzing-a-crash-report.md) — 识别崩溃报告中有助于诊断问题的线索。

### 运行时错误

- [处理语言异常引发的崩溃](addressing-language-exception-crashes.md) — 识别语言异常的迹象，并处理未捕获语言异常引发的崩溃。
- [读取异常消息](reading-an-exception-message.md) — 了解并处理 App 崩溃的常见原因。
