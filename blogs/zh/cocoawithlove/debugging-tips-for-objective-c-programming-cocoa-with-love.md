---
title: 'Objective-C 编程调试技巧 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/10/debugging-tips-for-objective-c.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:01c5f7f98ec0e911'
translated: true
---

> 原文：[Debugging tips for Objective-C programming | Cocoa with Love](https://www.cocoawithlove.com/2008/10/debugging-tips-for-objective-c.html)　·　Cocoa with Love (Matt Gallagher)

这篇文章探讨如何在运行时从程序中获取更多信息。Xcode 和 gdb 都支持各种各样的信息访问工具——但你需要知道它们的存在。以下是所有 Cocoa 程序员都应该了解的、一些面向 Objective-C 的 gdb 技巧和命令。

## 直接与 gdb 交互

调试器控制台窗口是你与 gdb 交互的途径。在 Xcode 中，从 Run 菜单显示控制台窗口（或键入 Command-Shift-R）。

![](https://www.cocoawithlove.com/assets/objc-era/consolewindow.png)

只有程序暂停时（在断点处停止），你才能向 gdb 发送命令。当出现 (gdb) 提示符后，你就可以与 gdb 对话了。

大多数[gdb 接受的命令](http://developer.apple.com/documentation/DeveloperTools/gdb/gdb/gdb_4.html)，Xcode 已经通过在调试器窗口中显示值的方式自动为你处理了。所以我将忽略其中的大部分内容。

## "po"：打印对象

打印对象命令会显示 Objective-C 对象的文本表示。

假设你想知道为什么调用这个方法：

```objc
- (id)getFirstObjectFrom:(NSDictionary *)stringDictionary
{
    return [stringDictionary objectForKey:@"FirstKey"];
}
```

会返回 nil。在该行设置断点，当调试器停在该位置时，前往调试器控制台并输入：

```objc
po stringDictionary
```

按回车键，gdb 就会给出结果。在我的例子中，结果是：

```objc
{
    firstKey = firstObject;
    secondKey = secondObject;
    thirdKey = thirdObject;
}
```

我本应使用的键名是 @"firstKey"，首字母 'f' 小写。问题解决了。

在这个例子中，gdb 在 NSDictionary 上调用了 description 方法来生成字符串。description 方法在 Cocoa 中无处不在，用于从对象生成字符串，你可以重写它来提供你自定义对象的字符串表示。

## Xcode 数据格式化器

如果调试器仍停留在同一行，并且你在 Xcode 中打开了调试器窗口，那么变量列表的「Arguments」中会包含一个 stringDictionary 条目。对于像这样 NSDictionary 对象，Xcode 会在「Summary」列中显示「3 key/value pairs」。

这些信息来自默认情况下为 NSDictionary 设置的「数据格式化器」。你可以在 Apple 的 [Xcode 调试指南：使用数据格式化器](http://developer.apple.com/library/mac/#documentation/DeveloperTools/Conceptual/XcodeDebugging/220-Viewing_Variables_and_Memory/variables_and_memory.html%23//apple_ref/doc/uid/TP40007057-CH9-SW24) 中了解它们。本质上，数据格式化器告诉 Xcode 如何获取一些数据显示在列中。

如果我们右键单击调试器窗口中的 stringDictionary 行，并从上下文菜单中选择「Print Description to Console」，可以看到一个不同的数据格式化器。

```objc
Printing description of stringDictionary:
&lt;CFDictionary 0x35edd0 [0xa0b06174]&gt;{type = immutable, count = 3, capacity = 3, pairs = (
   0 : &lt;CFString 0x2090 [0xa0b06174]&gt;{contents = "secondKey"} = &lt;CFString 0x2080 [0xa0b06174]&gt;{contents = "secondObject"}
   1 : &lt;CFString 0x20b0 [0xa0b06174]&gt;{contents = "thirdKey"} = &lt;CFString 0x20a0 [0xa0b06174]&gt;{contents = "thirdObject"}
   3 : &lt;CFString 0x2070 [0xa0b06174]&gt;{contents = "firstKey"} = &lt;CFString 0x2060 [0xa0b06174]&gt;{contents = "firstObject"}
)}
```

如果没有数据格式化器，「Print Description to Console」会输出与「po」命令相同的信息。但在这个例子中，它明显输出了字典更详细的描述，包含了完整的类型信息和索引。这个 CFDictionary 数据格式化器具体位于何处，我并不知晓（它不在 Xcode 数据格式化器的标准位置中）。

## 其他「打印」命令

gdb 中的 po 命令只显示在对象上调用 description 的结果，但更通用的 print 命令允许我们做其他事情。

我本可以使用命令：

```objc
print (char*)[[stringDictionary description] cString]
```

它会输出：

```objc
$1 = 0x360031 "{\n    firstKey = firstObject;\n    secondKey = secondObject;\n
    thirdKey = thirdObject;\n}"
```

这与 po 示例中的数据表示相同，只是少了漂亮的格式化。

我也可以使用命令：

```objc
print (int)[stringDictionary retainCount]
```

来计算 stringDictionary 的引用计数，帮助我找出内存是否被正确释放或未释放的原因。

与 po 命令和 Xcode 中的「Print Description to Console」一样，print 命令在 Xcode 中也有对应的操作。你可以从 Run->Show->Expressions 菜单打开 Expressions 窗口。

## "info symbol"：获取地址的符号名称

我要讨论的最后一个 gdb 命令是 `info symbol` _地址_，它返回与指定内存地址相关的任何变量或代码的名称。

例如，假设你对上面 stringDictionary 的「Print Description to Console」输出中显示的内存地址「0xa0b06174」感到困惑。你只需在调试器控制台中输入：

```objc
info symbol 0xa0b06174
```

gdb 就会告诉你：

```objc
__kCFAllocatorSystemDefault in section LC_SEGMENT.__DATA.__data of /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
```

它是 CoreFoundation 的系统默认内存分配器。也许这仍然意义不大，但至少我们知道了声明在该地址的对象名称。

更有用的是，当你看到像这样的异常日志时：

```objc
2008-10-26 13:25:43.381 CrashExample[41720:20b] *** -[TransitionView doesntExist]: unrecognized selector sent to instance 0xf4fbb0
2008-10-26 13:25:43.383 CrashExample[41720:20b] *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '*** -[TransitionView doesntExist]: unrecognized selector sent to instance 0xf4fbb0'
2008-10-26 13:25:43.385 CrashExample[41720:20b] Stack: (
    2528013804,
    2478503148,
    2528042920,
    2528036272,
    2528036920,
    11076,
    11880,
    816174880,
    816174880,
    816504036,
    816500960,
    816258792,
    816202128,
    816199508,
    829005520,
    829014772,
    2527564456,
    829007724,
    816173016,
    816212336,
    9888,
    9668
)
```

日志告诉我们问题是因为向一个对象发送了无法识别的选择器（selector），但我们可能不知道程序中的哪个位置发生了这个问题。

你可以查看堆栈跟踪，发现其中「较小」的地址（即很可能在你的代码中，而非默认库中）里最大的是「11076」，然后向 gdb 发送命令：

```objc
info symbol 11076
```

gdb 会告诉你：

```objc
-[CrashExampleAppDelegate performTransition] + 88 in section LC_SEGMENT.__TEXT.__text of /Users/matt/Projects/CrashExample.app/CrashExample
```

这告诉我们问题出在 performTransition 方法中。

> **更新：** 如评论中「g」所指出的，有一种更好的方法来确定此情况下地址对应的方法和代码行。`info line *11076` 会给出原始源代码文件中的行号，而不仅仅是函数起始处的字节偏移量。

如果你查看列表中 11076 以上的 5 个地址，它们都与抛出异常本身有关——令人烦恼的是 Mac OS X 10.5 的 objc_exception_throw 只返回前 5 个地址，因为这些地址通常是相同的异常抛出地址（它们对异常抛出的 _原因_ 没有任何说明）。

## 调试器之外的地址和符号

既然我提到了阅读崩溃文件和查看内存地址：如果内存地址是 _其他人_ 给你的，gdb 并不是最佳操作方式。要做到这一点，你应该拥有他们正在使用的确切构建版本中的 .dSYM 文件。

如果你不知道如何生成 .dSYM 文件，请转到 Project->Edit Project Settings->Build->Build Options->Debug Information Format，确保你拥有 dSYM 文件。你应该为你发布的每个构建版本都保留这些文件。iPhone SDK 默认会生成这些文件，但对于 Mac 构建版本，你需要手动开启。

在命令行中调用以下命令：

```objc
dwarfdump -a <em>NameOfdSYMFile</em>
```

这将告诉你文件中所有已知的地址。你只需找到离你的崩溃位置最近的前一个地址，那就是有问题的函数或方法。

然而，这是一种非常粗暴的方法。若想一次获取单个地址，将 .dSYM 和它所引用的 .app 放在同一个目录中，你可以使用 atos 命令来获取单个地址的单个符号。针对上面显示的 CrashExample 崩溃 bug，你可以像这样调用这个命令：

```objc
atos -o CrashExample.app/Contents/MacOS/CrashExample -arch ppc 11076
```

它会给出结果：

```objc
-[CrashExampleAppDelegate performTransition] (in CrashExample) (CrashExampleAppDelegate.m:94)
```

最后，如果你想从崩溃日志中获取所有地址，可以使用 [Apple 的 symbolizecrashlog 脚本](http://developer.apple.com/tools/xcode/symbolizingcrashdumps.html)。它会为 .crash.log 文件找到 .app 和 .dSYM 文件，并调用 atos 来获取其中包含的所有可能的符号。_感谢 millenomi 在评论中指出这一点。_

## 结论

调试时，能榨取的信息远比变量中的原始数值要多得多。在调试过程中能够获取这些信息，可以让你更快地追踪到 bug。
