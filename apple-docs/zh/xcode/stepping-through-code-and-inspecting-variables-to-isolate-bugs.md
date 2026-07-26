---
title: 单步执行代码并检查变量以定位 bug
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/stepping-through-code-and-inspecting-variables-to-isolate-bugs
source_url: 'https://developer.apple.com/documentation/xcode/stepping-through-code-and-inspecting-variables-to-isolate-bugs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/stepping-through-code-and-inspecting-variables-to-isolate-bugs.json'
content_hash: 'sha256:0da92d252dd7bd3e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md)

# 单步执行代码并检查变量以定位 bug

<sub>文章</sub>

在调试器中逐行执行你的源代码时，通过观察变量的变化来找出 bug 的成因。

## 概述

如果在查看源代码时无法立即看出 bug 的根本原因，那么在逐行执行代码时观察变量的变化，有助于你定位 bug 发生的位置，从而调查它可能的成因。

Xcode 调试器提供了几种逐行执行代码并检查变量的方法。你可以从一个断点开始精确控制代码的执行，按需进入或退出所调用的函数，以确定 bug 发生的位置。你可以在逐行执行代码的同时监视变量，也可以暂停执行以更仔细地检查它们。

在 bug 发生之前、App 处于已知良好状态的某一点设置断点开始调查，选在你认为 bug 可能即将发生的位置。

### 在调试器中逐行执行代码

当你运行 App 时，调试器会在遇到的第一个断点处暂停，并且默认会更新显示，展示 Debug navigator、源代码编辑器、调试栏、变量查看器和控制台。

![](../../../attachments/0599792a0f39a1675e2fc12a06197687/stepping-through-code-and-inspecting-variables-to-isolate-bugs-1@2x.png)

<sub>Xcode 在某个 App 的断点处暂停，展示了调试导航栏、高亮断点的源代码编辑器、变量查看器和调试器控制台。</sub>

你可以通过依次选择 Xcode \> Settings \> Behaviors，并在 Running 下选择相应选项，来自定 Xcode 在调试器中运行你的 App 时所显示的内容。

使用调试栏中的按钮来控制 App 的执行。

![](../../../attachments/870c41e7250ac061a333c1ec9977c41a/stepping-through-code-and-inspecting-variables-to-isolate-bugs-2@2x.png)

<sub>Xcode 调试器工具栏，展示了显示/隐藏调试区域按钮、启用/停用所有断点按钮、继续按钮、单步进入按钮、单步跳出按钮、调试视图层级结构按钮、调试内存图按钮、环境覆盖按钮、模拟位置按钮，以及栈帧选择区域。</sub>

- 使用 Continue 按钮，从暂停的位置继续正常执行，直到 App 停在下一个断点处。
- 使用 Pause 按钮，在不设置断点的情况下暂停 App。App 运行时，Continue 按钮会切换为 Pause 按钮。
- 使用 Step Over 按钮，执行同一函数中的下一条指令。
- 使用 Step Into 按钮执行下一条指令。如果下一条指令位于另一个方法或函数内部，调试器会跳转到该函数，并在你每次点击 Step Into 按钮时继续执行它。
- 在使用 Step Into 之后，点击 Step Out 按钮以跳过该函数的剩余部分，返回到调用函数或方法中的下一条指令。

在逐行执行 App 的过程中，检查与你的 bug 相关的变量，留意意外的值。

### 在代码和变量查看器中查看变量值

当你的 App 在断点处暂停时，将鼠标悬停在源代码中的某个变量上，即可查看其当前值。如果该变量是图像或其他无法以文本表示的类型，请点击右上角的 Quick Look 按钮，查看该变量的预览。点击 Print Description 按钮，可在控制台中打印该对象的描述。

![](../../../attachments/e08881a65188e0d8bd08796d30c057d1/stepping-through-code-and-inspecting-variables-to-isolate-bugs-3@2x.png)

<sub>Xcode 显示调试器暂停在某一行代码上，展示了 fruit 变量详情的悬停窗口。</sub>

变量查看器列出了当前执行上下文中可用的变量。通过查看器左下角的选择器，可以选择要查看的变量范围：自动、局部或全部变量，以及寄存器、全局变量和静态变量。使用过滤字段查找与某种模式匹配的变量。

![Xcode 暂停在某个断点处，展示了调试器变量查看器。](../../../attachments/e3455d146066fc12046dd758765a9830/stepping-through-code-and-inspecting-variables-to-isolate-bugs-4@2x.png)

每个变量都会显示其类型、值以及指针位置（如适用）的简要摘要。变量查看器所显示的摘要是通过 lldb 命令 `frame variable` 生成的。如果某个变量的摘要不可用，或只显示了一个内存指针，请参阅下面的[在控制台中求值表达式](stepping-through-code-and-inspecting-variables-to-isolate-bugs.md#Evaluate-expressions-in-the-console)一节，了解更多检查该变量的方法。

点击展开三角形，可以查看类和结构体的实例变量，或其他数据类型的内部内容。选择一个变量并点击 Quick Look 按钮以查看该变量的预览，或点击 Print Description 按钮在控制台中打印该对象的描述。

### 查看调用栈并浏览相关代码

当调试器在断点处暂停时，它会在 Debug navigator 中显示当前活跃的线程和当前的调用栈，并高亮该断点。调用栈表示导致当前断点的一系列函数或方法调用之间的关系。

![Xcode 在断点处暂停时，在调试导航栏中显示调用栈。](../../../attachments/ee212d72c2c37c23c220aa15178f729e/stepping-through-code-and-inspecting-variables-to-isolate-bugs-5@2x.png)

如果你怀疑 bug 出在某个调用函数中，可以选择调用栈中的某一行。调用函数可能错误地更改了某个实例变量，或是在参数中传递了错误的值。如果项目中有对应的源代码，调试器会显示该处的源代码以及变量查看器中的相关变量。否则，调试器会显示所选行的汇编代码。检查此处的变量，留意意外的值。

选择某个线程，可以展开或折叠该线程的调用栈视图。选择该线程调用栈中的某一行，即可查看源代码和变量。

### 在控制台中求值表达式

如果你想查看比变量查看器中摘要更详细的信息，或想在调试会话中途更改某个变量的值，可以使用控制台直接与调试器交互。

使用 `frame variable`（或其缩写别名 `v`）打印当前栈帧中某个变量的值。

```other
(lldb) v self.fruitList.title
(String) self.fruitList.title = "Healthy Fruit”
(lldb) v self.listData[0]
(String) [0] = “Banana"
```

frame variable 命令只返回当前内存中的内容，不会求值表达式，所以如果你试图打印更复杂的内容，它会返回一个错误。例如，它不会打印函数或方法调用、`@Published` 变量或计算变量。

```other
(lldb) v fruitList.fruit(at: indexPath)
error: no variable named 'fruitList' found in this frame
error: no variable named 'indexPath)' found in this frame
(lldb) v self.fruitList.calculatedFruitCount
error: "calculatedFruitCount" is not a member of "(Debugger_Demo.FruitList) self.fruitList”
```

使用 `expression` 命令（或别名 `expr`、`p`）对表达式求值并在控制台中打印结果。

```other
(lldb) p self.fruitList.calculatedFruitCount
(Int) $R18 = 9
(lldb) p fruitList.fruit(at: indexPath)
(Debugger_Demo.FruitItem) $R20 = 0x00006000013dcc90 (fruitName = "Strawberry", fruitDescription = "Small red berry with seeds on the outside.”)
(lldb) expr fruit.fruitName
(String) $R14 = "Strawberry"
(lldb) p fruit.fruitName == "Peach"
(Bool) $R16 = false
```

`p` 命令会编译代码来对表达式求值，因此它能够处理函数调用和计算变量。可以把 `p` 提供的引用作为其他表达式的组成部分来使用。

```other
(lldb) p fruit.fruitName
(String) $R2 = "Banana"
(lldb) p fruit.fruitName
(String) $R6 = "Strawberry"
(lldb) p $R2 + ", " + $R6
(String) $R8 = "Banana, Strawberry"
```

对于某些类，使用 `p` 可能只会显示一个内存指针位置，或是显示该类所有属性的完整展开视图，其中可能包含大量不必要的信息。在这些情况下，可以使用 `po`，它是 `expression —object-description` 的别名。这个版本同样会编译代码来对表达式求值，但它会为结果打印一个对象描述，你可以为自己的对象自定这个描述。

```other
(lldb) po cell
<Debugger_Demo.ListTableViewCell: 0x7fca3450e520; baseClass = UITableViewCell; frame = (0 28; 414 43.5); clipsToBounds = YES; layer = <CALayer: 0x600001d3ed40>>
(lldb) po fruitList
Yummy Fruit: 9 items starting with Banana
```

> [!tip] 提示
> 通过添加一个调试描述，来自定调试器为你的对象所展示的内容。在 Swift 中，为你的对象实现 `CustomDebugStringProtocol`。对于继承自 `NSObject` 的 Objective-C 对象，重写 `debugDescription`。

在调试过程中，可以使用 `p` 或 `po` 更改内存中某个变量的值。

```other
(lldb) po fruitList.title = "Tasty Fruit"
0 elements

(lldb) po fruitList
Tasty Fruit: 9 items starting with Banana
```

当你打印一个用协议声明的项目时，`p` 和 `po` 会打印错误，因为它们不会执行迭代式的动态类型解析。当 `p` 或 `po` 打印错误时，请使用 `v` 来打印变量。

```other
(lldb) po fruitItem.fruitName
error: <EXPR>:3:11: error: value of type 'FruitDisplayProtocol' has no member 'fruitName'
fruitItem.fruitName
~~~~~~~~~ ^~~~~~~~~

(lldb) v fruitItem.fruitName
(String) fruitItem.fruitName = "Apple"
```

## 另请参阅

### Breakpoints and variables

- [Setting breakpoints to pause your running app](setting-breakpoints-to-pause-your-running-app.md) — 指定 App 在运行调试器时暂停的位置，以便调查 bug。
