---
title: 'Friday Q&A 2018-06-29：使用 C-Reduce 调试'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2c16b0b77557249d'
translated: true
---

> 原文：[Friday Q&A 2018-06-29: Debugging with C-Reduce](https://www.mikeash.com/pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html)　·　mikeash.com Friday Q&A

发布于 2018-06-29 13:35 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[objc_msgSend 的新原型](https://www.mikeash.com/pyblog/objc_msgsends-new-prototype.html)  
上一篇文章：[Friday Q&A 2018-04-27：在 Swift 中使用马尔可夫链生成文本](https://www.mikeash.com/pyblog/friday-qa-2018-04-27-generating-text-with-markov-chains-in-swift.html)  
标签：[调试](https://www.mikeash.com/pyblog/?tag=debugging) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2018-06-29：使用 C-Reduce 调试

作者：[Mike Ash](https://www.mikeash.com/)

**概述**  
C-Reduce 基于两个主要思想。

首先，是缩减通道（reduction pass）的思想。这是对某些源代码执行的一种转换，它会生成该代码的缩减版本。C-Reduce 有许多不同的通道，包括删除行、将 token 重命名为更短版本等。

其次，是趣味性测试（interestingness test）的思想。缩减通道是盲目的，常常会生成不再包含 bug 或根本无法编译的程序。当你使用 C-Reduce 时，你不仅要提供一个要缩减的程序，还要提供一个小的脚本（script），用于测试缩减后的程序是否“有趣”（interesting）。究竟什么是“有趣”由你决定。如果你试图隔离一个 bug，那么“有趣”就意味着 bug 仍然存在于程序中。只要你能编写脚本，你可以将其定义为你想要的任何含义。无论你提供什么测试，C-Reduce 都会尝试提供一个仍能通过该测试的程序的缩减版本。

**安装**  
C-Reduce 有很多依赖项，安装起来可能很困难。好在 Homebrew 中有它，所以你可以让它来处理：

```
    brew install creduce
```

如果你更愿意自己动手，可以[查看 C-Reduce 的 INSTALL 文件](https://github.com/csmith-project/creduce/blob/master/INSTALL)。

**简单示例**  
为 C-Reduce 设计小型示例是很困难的，因为它的全部目的就是从大型代码开始并*生成*一个小型示例，但我们会尽力尝试。下面是一个简单的 C 程序，会产生一个有点神秘的警告：

```
    $ cat test.c
    #include <stdio.h>

    struct Stuff {
        char *name;
        int age;
    }

    main(int argc, char **argv) {
        printf("Hello, world!\n");
    }
    $ clang test.c
    test.c:3:1: warning: return type of 'main' is not 'int' [-Wmain-return-type]
    struct Stuff {
    ^
    test.c:3:1: note: change return type to 'int'
    struct Stuff {
    ^~~~~~~~~~~~
    int
    test.c:10:1: warning: control reaches end of non-void function [-Wreturn-type]
    }
    ^
    2 warnings generated.
```

不知为何，我们的 `struct` 搞乱了 `main`！怎么会这样？也许缩减它能帮助我们弄清楚。

我们需要一个趣味性测试。我们将编写一个小的 shell 脚本来编译这个程序，并检查输出中的警告。C-Reduce 急于讨好，很容易将程序缩减到远超我们实际需要的程度。为了控制它，我们将编写一个脚本，它不仅要检查警告，还要拒绝任何产生错误的程序，并要求编译器输出中某处包含 `struct Stuff`。脚本如下：

```
    #!/bin/bash

    clang test.c &> output.txt
    grep error output.txt && exit 1
    grep "warning: return type of 'main' is not 'int'" output.txt &&
    grep "struct Stuff" output.txt
```

首先，它编译程序并将编译器输出保存到 `output.txt`。如果输出包含文本 "error"，则立即以错误码 1 退出，表明此程序不有趣。否则，它会检查输出中是否同时包含警告和 `struct Stuff`。如果找到匹配项，`grep` 以代码 `0` 退出，因此结果是，如果两者都匹配，此脚本以代码 `0` 退出；如果任一失败，则以代码 `1` 退出。退出码 `0` 向 C-Reduce 表明缩减后的程序是有趣的，而代码 `1` 表明它不有趣，应丢弃。

现在我们有了运行 C-Reduce 所需的一切：

```
    $ creduce interestingness.sh test.c 
    ===< 4907 >===
    running 3 interestingness tests in parallel
    ===< pass_includes :: 0 >===
    (14.6 %, 111 bytes)

    ...lots of output...

    ===< pass_clex :: rename-toks >===
    ===< pass_clex :: delete-string >===
    ===< pass_indent :: final >===
    (78.5 %, 28 bytes)
    ===================== done ====================

    pass statistics:
      method pass_balanced :: parens-inside worked 1 times and failed 0 times
      method pass_includes :: 0 worked 1 times and failed 0 times
      method pass_blank :: 0 worked 1 times and failed 0 times
      method pass_indent :: final worked 1 times and failed 0 times
      method pass_indent :: regular worked 2 times and failed 0 times
      method pass_lines :: 3 worked 3 times and failed 30 times
      method pass_lines :: 8 worked 3 times and failed 30 times
      method pass_lines :: 10 worked 3 times and failed 30 times
      method pass_lines :: 6 worked 3 times and failed 30 times
      method pass_lines :: 2 worked 3 times and failed 30 times
      method pass_lines :: 4 worked 3 times and failed 30 times
      method pass_lines :: 0 worked 4 times and failed 20 times
      method pass_balanced :: curly-inside worked 4 times and failed 0 times
      method pass_lines :: 1 worked 6 times and failed 33 times

              ******** .../test.c ********

    struct Stuff {
    } main() {
    }
```

最后，它输出了它想出的程序缩减版本。它还将缩减后的版本保存到原始文件中。在处理真实代码时要注意这一点！请务必在代码的副本（或已检入版本控制的文件）上运行 C-Reduce，而不是在不可替代的原件上。

这个缩减版本使问题更明显：我们在 `struct Stuff` 声明的末尾忘记了分号，并且忘记了 `main` 的返回类型，这导致编译器将 `struct Stuff` 解释为 `main` 的返回类型。这很糟糕，因为 `main` 必须返回 `int`，因此产生了警告。

**Xcode 项目**  
对于我们已经缩减到单个文件的情况来说，这没问题，但如果是更复杂的项目呢？我们大多数人都有 Xcode 项目，所以如果我们想缩减其中一个呢？

这会变得棘手，因为 C-Reduce 的工作方式。它将要缩减的文件复制到一个新目录，然后在那里运行你的趣味性脚本。这允许它并行运行大量测试，但如果需要其他东西才能让它工作，这就会出问题。由于你的趣味性脚本可以运行任意命令，你可以通过将项目的其余部分复制到临时目录来解决这个问题。

我在 Xcode 中创建了一个标准的 Cocoa Objective-C App 项目，然后像这样修改了 `AppDelegate.m` 文件：

```
    #import "AppDelegate.h"

    @interface AppDelegate () {
        NSWindow *win;
    }

    @property (weak) IBOutlet NSWindow *window;
    @end

    @implementation AppDelegate

    - (void)applicationDidFinishLaunching: (NSRect)visibleRect {
        NSLog(@"Starting up");
        visibleRect = NSInsetRect(visibleRect, 10, 10);
        visibleRect.size.height *= 2.0/3.0;
        win = [[NSWindow alloc] initWithContentRect: NSMakeRect(0, 0, 100, 100) styleMask:NSWindowStyleMaskTitled backing:NSBackingStoreBuffered defer:NO];
        [win makeKeyAndOrderFront: nil];
        NSLog(@"Off we go");
    }

    @end
```

这段奇怪的代码会在启动时使 App 崩溃：

```
    * thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=EXC_I386_GPFLT)
      * frame #0: 0x00007fff3ab3bf2d CoreFoundation`__CFNOTIFICATIONCENTER_IS_CALLING_OUT_TO_AN_OBSERVER__ + 13
```

这不是一个信息量很大的回溯跟踪。我们可以尝试调试（或者直接注意到问题），但不如我们来缩减！

这里的趣味性测试需要做更多工作。让我们从一个辅助函数开始，它带有超时地运行 App。我们在寻找崩溃，如果 App *没有*崩溃，它会保持打开状态，所以我们需要在几秒钟后杀死它。我在网上到处找到了这个方便的 perl 代码片段：

```
    function timeout() { perl -e 'alarm shift; exec @ARGV' "$@"; }
```

接下来，我们需要复制 Xcode 项目：

```
    cp -a ~/Development/creduce-examples/Crasher .
```

`AppDelegate.m` 文件不会自动放到合适的位置，所以需要复制过去。（注意：如果 C-Reduce 找到了缩减，它会将文件复制回来，所以这里一定要使用 `cp` 而不是 `mv`。使用 `mv` 会导致一个神秘的致命错误。）

```
    cp AppDelegate.m Crasher/Crasher
```

然后切换到 `Crasher` 目录并构建项目，失败时退出：

```
    cd Crasher
    xcodebuild || exit 1
```

如果构建成功，使用超时运行 App。我的系统配置为 `xcodebuild` 将构建结果放在本地 `build` 目录中。你的配置可能不同，所以请先检查。请注意，如果你的配置构建到共享构建目录，你需要在调用 C-Reduce 时添加 `--n 1` 命令行参数来禁用其并行构建。

```
    timeout 5 ./build/Release/Crasher.app/Contents/MacOS/Crasher
```

如果它崩溃了，会以特殊代码 `139` 退出。将其转换为退出码 `0`，所有其他情况退出码为 `1`：

```
    if [ $? -eq 139 ]; then
        exit 0
    else
        exit 1
    fi
```

现在我们准备运行 C-Reduce：

```
    $ creduce interestingness.sh Crasher/AppDelegate.m
    ...
    (78.1 %, 151 bytes)
    ===================== done ====================

    pass statistics:
      method pass_ints :: a worked 1 times and failed 2 times
      method pass_balanced :: curly worked 1 times and failed 3 times
      method pass_clex :: rm-toks-7 worked 1 times and failed 74 times
      method pass_clex :: rename-toks worked 1 times and failed 24 times
      method pass_clex :: delete-string worked 1 times and failed 3 times
      method pass_blank :: 0 worked 1 times and failed 1 times
      method pass_comments :: 0 worked 1 times and failed 0 times
      method pass_indent :: final worked 1 times and failed 0 times
      method pass_indent :: regular worked 2 times and failed 0 times
      method pass_lines :: 8 worked 3 times and failed 43 times
      method pass_lines :: 2 worked 3 times and failed 43 times
      method pass_lines :: 6 worked 3 times and failed 43 times
      method pass_lines :: 10 worked 3 times and failed 43 times
      method pass_lines :: 4 worked 3 times and failed 43 times
      method pass_lines :: 3 worked 3 times and failed 43 times
      method pass_lines :: 0 worked 4 times and failed 23 times
      method pass_lines :: 1 worked 6 times and failed 45 times

              ******** /Users/mikeash/Development/creduce-examples/Crasher/Crasher/AppDelegate.m ********

    #import "AppDelegate.h"
    @implementation AppDelegate
    - (void)applicationDidFinishLaunching:(NSRect)a {
      a = NSInsetRect(a, 0, 10);
      NSLog(@"");
    }
    @end
```

短了很多！`NSLog` 这行看起来无害，尽管如果 C-Reduce 没有移除它，那它一定是崩溃的一部分。`a = NSInsetRect(a, 0, 10);` 是唯一另外做了一些事情的行。`a` 从哪里来，为什么向它写入会导致不好的事情？它只是 `applicationDidFinishLaunching:` 的参数，而该方法……参数并不是 `NSRect`。

```
    - (void)applicationDidFinishLaunching:(NSNotification *)notification;
```

哎呀！参数类型不匹配导致了栈损坏，从而引起了信息不明的崩溃。

C-Reduce 在这个例子上运行了很长时间，因为构建一个 Xcode 项目比编译单个文件耗时更长，而且许多测试用例在运行时命中了五秒的超时。C-Reduce 每次成功时都会将缩减后的文件复制回原始目录，所以你可以将其在文本编辑器中打开，观察它的工作。如果你认为缩减已经足够了，你可以按 ^C，你将得到部分缩减的文件。如果你决定要再运行一些，重新运行它，它会从那里继续。

**Swift**  
如果你在使用 Swift 并想要缩减一个问题呢？从名字来看，我最初以为 C-Reduce 只适用于 C（也许还有 C++，因为很多工具两者都支持）。

谢天谢地，我错了。C-Reduce 确实有一些特定于 C 的缩减通道，但它还有很多其他相对语言无关的通道。它可能效果稍差，但只要你能为你的问题编写趣味性测试，C-Reduce 可能对你使用的任何语言都适用。

让我们试试。我在 [bugs.swift.org 上发现了一个不错的编译器 bug](https://bugs.swift.org/browse/SR-7354)。它已经被修复了，但 Xcode 9.3 的 Swift 会因此而崩溃，而我正好有这个版本。下面是来自那个 bug 的示例稍作修改的版本：

```
    import Foundation

    func crash() {
        let blah = ProblematicEnum.problematicCase.problematicMethod()
        NSLog("\(blah)")
    }

    enum ProblematicEnum {
        case first, second, problematicCase

        func problematicMethod() -> SomeClass {
            let someVariable: SomeClass

            switch self {
            case .first:
                someVariable = SomeClass()
            case .second:
                someVariable = SomeClass()
            case .problematicCase:
                someVariable = SomeClass(someParameter: NSObject())
                _ = NSObject().description
                return someVariable // EXC_BAD_ACCESS (simulator: EXC_I386_GPFLT, device: code=1)
            }

            let _ = [someVariable]
            return SomeClass(someParameter: NSObject())
        }

    }

    class SomeClass: NSObject {
        override init() {}
        init(someParameter: NSObject) {}
    }

    crash()
```

让我们尝试启用优化来运行它：

```
    $ swift -O test.swift 
    <unknown>:0: error: fatal error encountered during compilation; please file a bug report with your project and the crash log
    <unknown>:0: note: Program used external function '__T04test15ProblematicEnumON' which could not be resolved!
    ...
```

这个的趣味性测试相当简单。运行那个命令并检查退出码：

```
    swift -O test.swift
    if [ $? -eq 134 ]; then
        exit 0
    else
        exit 1
    fi
```

在其上运行 C-Reduce，它产生了以下示例：

```
    enum a {
        case b, c, d
        func e() -> f {
            switch self {
            case .b:
                0
            case .c:
                0
            case .d:
                0
            }
            return f()
        }
    }
    class f{}
```

深入研究实际的编译器 bug 超出了本文的范围，但如果我们要着手修复它，这个缩减版本会非常有用。我们有了一个相当简单的测试用例来处理。我们还可以推断出 Swift 语句和类实例化之间存在某种交互，因为如果其中一个是不必要的，C-Reduce 可能已经移除了它。这会给我们一些关于编译器中可能发生什么导致此崩溃的好提示。

**结论**  
盲目缩减测试用例并不是一种非常复杂的调试技术，但自动化它的能力可以使其变得极其有用。C-Reduce 可以成为你调试工具箱中的绝佳补充。它并非适用于所有情况，但又有什么是万能的呢？对于它有用的问题，它可以提供巨大帮助。让它在多文件测试用例上工作可能有点棘手，但通过趣味性脚本的一些巧思可以解决这个问题。尽管名字如此，它对 Swift 和许多其他语言开箱即用，所以不要因为你不是在 C 中工作就放弃它。

今天就到这里。下次再来看看更多有趣的内容、游戏和代码。Friday Q&A 由读者想法驱动，所以如果你有希望下次或其他时间在这里看到的内容，请[发送过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我在销售整本整本的书籍！第 II 卷和第 III 卷现已发布！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。 [点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
