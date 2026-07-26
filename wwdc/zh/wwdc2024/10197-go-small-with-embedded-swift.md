---
title: 用 Embedded Swift 做小
session_id: 10197
collection: wwdc2024
year: 2024
duration: '22:17'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10197/'
content_hash: 'sha256:2355da4617ba8bdf'
translated: true
---

# 用 Embedded Swift 做小

<sub>WWDC2024 · 22:17 · Swift</sub>

Embedded Swift 把 Swift 的安全性与表达力带到了资源受限的环境里。探索 Embedded Swift 是怎样在各种……

> [!note] 归档理由
> Embedded Swift：无 runtime 的 Swift 子集，反向理解 runtime 依赖

## 章节

- [Introduction](/videos/play/wwdc2024/10197/?time=0)
- [Agenda](/videos/play/wwdc2024/10197/?time=25)
- [Why Embedded Swift](/videos/play/wwdc2024/10197/?time=46)
- [Showcase](/videos/play/wwdc2024/10197/?time=150)
- [The plan](/videos/play/wwdc2024/10197/?time=167)
- [Getting started](/videos/play/wwdc2024/10197/?time=219)
- [Using Swift's interoperability to control the LED](/videos/play/wwdc2024/10197/?time=379)
- [Using an ergonomic LED struct](/videos/play/wwdc2024/10197/?time=432)
- [Adding the Matter protocol](/videos/play/wwdc2024/10197/?time=607)
- [在事件处理程序里使用一个 Swift 枚举](/videos/play/wwdc2024/10197/?time=823)
- [Demo summary](/videos/play/wwdc2024/10197/?time=1012)
- [How Embedded Swift differs](/videos/play/wwdc2024/10197/?time=1054)
- [Explore more](/videos/play/wwdc2024/10197/?time=1188)
- [Wrap up](/videos/play/wwdc2024/10197/?time=1292)

## 相关资源

- [Introduction](https://developer.apple.com/videos/play/wwdc2024/10197/?time=0)
- [Agenda](https://developer.apple.com/videos/play/wwdc2024/10197/?time=25)
- [Why Embedded Swift](https://developer.apple.com/videos/play/wwdc2024/10197/?time=46)
- [Showcase](https://developer.apple.com/videos/play/wwdc2024/10197/?time=150)
- [The plan](https://developer.apple.com/videos/play/wwdc2024/10197/?time=167)
- [Getting started](https://developer.apple.com/videos/play/wwdc2024/10197/?time=219)
- [Using Swift's interoperability to control the LED](https://developer.apple.com/videos/play/wwdc2024/10197/?time=379)
- [Using an ergonomic LED struct](https://developer.apple.com/videos/play/wwdc2024/10197/?time=432)
- [Adding the Matter protocol](https://developer.apple.com/videos/play/wwdc2024/10197/?time=607)
- [在事件处理程序里使用一个 Swift 枚举](https://developer.apple.com/videos/play/wwdc2024/10197/?time=823)
- [Demo summary](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1012)
- [How Embedded Swift differs](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1054)
- [Explore more](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1188)
- [Wrap up](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1292)
- [Tools used: Neovim](https://neovim.io)
- [Swift MMIO](https://github.com/apple/swift-mmio)
- [Swift Forums Embedded Discussion](https://forums.swift.org/c/development/embedded/107)
- [Swift Embedded Example Projects](https://github.com/apple/swift-embedded-examples)
- [Embedded Swift User Manual](https://github.com/apple/swift/blob/main/docs/EmbeddedSwift/UserManual.md)
- [A Vision for Embedded Swift](https://github.com/apple/swift-evolution/blob/main/visions/embedded-swift.md)
- [Swift Matter Examples](https://github.com/apple/swift-matter-examples)
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10197/4/61F8D9DD-2B91-4545-AA09-253E16642E98/downloads/wwdc2024-10197_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10197/4/61F8D9DD-2B91-4545-AA09-253E16642E98/downloads/wwdc2024-10197_sd.mp4?dl=1)
- [在你的智能家居 App 里添加对 Matter 的支持](https://developer.apple.com/videos/play/wwdc2021/10298)
- [Empty Embedded Swift application](https://developer.apple.com/videos/play/wwdc2024/10197/?time=230)
- [Turning on LED to blue color](https://developer.apple.com/videos/play/wwdc2024/10197/?time=408)
- [Using an LED object](https://developer.apple.com/videos/play/wwdc2024/10197/?time=512)
- [Matter application controlling an LED light](https://developer.apple.com/videos/play/wwdc2024/10197/?time=764)
- [Reflection example](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1083)
- [Unavailable features will produce errors](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1137)
- [Prefer generics over "any" types](https://developer.apple.com/videos/play/wwdc2024/10197/?time=1164)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎。我叫 Kuba Mracek，大家都知道，Swift 是一门强大的语言，既可以用来为 Apple 平台构建应用，也可以用在其他更多地方。今天，我们要把它带到一个全新的、令人兴奋的、但体积更小的地方——嵌入式设备。我会先介绍 Embedded Swift，然后通过一个演示给大家展示，可以怎样用它来构建一些实际的东西。接着我会讲讲 Embedded Swift 和你用来编写桌面、移动应用的 Swift 有什么不同，最后我会分享一些资源，供大家进一步探索学习。我们开始吧！今天，你可以用 Swift 构建很多不同类型的软件：可以面向移动设备、桌面电脑、服务器。

在这场演讲里，我们要聊聊在一个新的领域使用 Swift：嵌入式设备。我们日常生活中到处都被这类设备包围——智能灯、恒温器、报警器、智能风扇、音乐设备、灯带，还有很多其他常见的小玩意，都是用可编程微控制器构建的。今天，我想给大家展示，不管你是一个爱好者，还是更专业的开发者，都可以怎样用 Swift 来给这些嵌入式设备编程。为此，我们要推出 Embedded Swift——一种专门适用于资源受限嵌入式设备的新编译模式。历史上，C 和 C++ 一直是这个领域常用的语言。但现在，我们让 Swift 也能用在这些地方，这为嵌入式开发者带来了 Swift 的种种好处，比如它的人体工程学（ergonomics）、安全特性和易用性。Embedded Swift 当然适合用来给嵌入式设备里的微控制器编程，但也适合用在内核级代码，以及其他一些可能对「不引入新依赖」比较敏感的底层库代码上。Apple 设备在 Secure Enclave 处理器上就使用了 Embedded Swift，而 Swift 的内存安全性对这个平台来说是一个巨大的好处。Embedded Swift 是 Swift 的一个子集，涵盖了你所熟悉和喜爱的大部分语言特性——它是一个功能齐全的子集，支持值类型和引用类型、闭包、可选值、错误处理、泛型等等。现在，我们通过一场现场演示来看看 Embedded Swift。在开始之前先说明：Embedded Swift 目前是一项实验性特性，源码还不稳定，它正处于积极开发中，最好的使用方式是通过 swift.org 上的预览版工具链。在这场演示里，我要构建一个非常简单的 HomeKit 配件的原型：一个彩色 LED 灯。我会先准备好一个可用的 HomeKit 环境——也就是一个 WiFi 网络，以及一些已经连接到这个网络上的 Apple 设备。我要用一块可编程的嵌入式设备，具体来说是一块 ESP32C6 开发板，它有一个 RISC-V 微控制器，还带着一个彩色 LED。我会用一台 Mac 通过 USB 线连接到这个设备，然后用 Embedded Swift 写一个实现 HomeKit 配件的程序，接着把它刷写到这个设备上。这个设备随后会加入我的 WiFi 和 HomeKit 网络，就可以从任意一台 Apple 设备的「家庭」App 里控制它了。

我们开始吧。我用的是 Neovim 和 CMake，现在这只是一个模板项目，用来展示最基本的东西，让我们的 Embedded Swift 代码先跑起来。这个项目用的是我从设备供应商那里拿到的一个第三方 SDK，是用 C 写的 SDK。因为我不想改动那个 SDK，我可以直接用一个桥接头文件，把这个 SDK 的所有 API 导入到 Swift 里。

我需要一些简单的 CMake 逻辑，才能在供应商的 SDK 和他们的构建系统之上构建我的 Swift 代码，这还需要多写几个样板文件：比如那个 YAML 文件、CSV 文件，还有 "sdkconfig" 文件。

任何构建在这个 SDK 之上的项目都需要这些文件，我是照着供应商提供的现有示例把这些配置好的，然后只是在此基础上加上了 Swift。

我们回到 Swift 源代码这边。我的编辑器集成了 LSP，所以它能给我展示我用到的函数和类型的定义与文档。

它还能给我提供丰富的、带语义的自动补全。

如果我写的代码不合逻辑……

我会立刻收到错误和警告，告诉我哪里出了问题。现在我来把设备接上。

我会通过 USB 给这个设备编程，不过我的面包板上还接了一块独立的电池，所以一旦编程完成，我们就可以拔掉这个设备的 USB，仍然能用它。但首先，我们先让最基本的 Swift 应用在这个设备上跑起来。我用的这个 SDK 提供了相应的工具。

我要运行供应商提供的这个很方便的 Python 脚本，它让我可以用一条命令完成构建、刷写和监控设备。

在我运行它的时候，我们可以看到固件正在被构建，然后被上传到设备上，接着我们收到了设备返回的日志。这样，我们的第一个 Embedded Swift 应用就在一个嵌入式设备上跑起来了，有了生命的迹象。现在，我们来加一些更有用的代码。Swift 的互操作性让我们能访问供应商 SDK 里的所有 API。如果我想控制设备上的 LED，我可以为此使用 SDK 里现成的 C API。

我们用代表「蓝色」「100% 饱和度」「80% 亮度」的值来调用这些 API。

然后我们保存这个版本的代码，把它上传到设备上。

我会运行和上次一样的命令。

几秒钟之后，固件上传完成、设备重启之后，我们现在就可以控制这个 LED 的颜色和亮度了。

不过，如果只是用 Swift 来调用 C API 做所有事情，那就完全违背了初衷。能这样做当然很有用，但更好的做法是在这些 API 之上构建一些包装器和抽象，这样我们就可以用干净、直观、符合人体工程学的 Swift 代码来写应用了。在这个版本里，我准备好了一个 LED 对象。我们跳转到它的定义。

这是我之前写的一些辅助代码，它把这些 C API 包装成了一层不错的 Swift 封装。它提供了一些带有符合人体工程学类型的实用属性，比如 enabled 属性是一个布尔值，brightness 属性是一个整数。我们回到主应用逻辑所在的文件。用这个 LED 对象，我们现在就可以写出非常直白、直观的代码了。

启动时，我们把颜色设为红色。

把亮度设为 80%。

像这样的代码非常易读、非常清晰。我们再多加一点。

在一个循环里，我们会等待 1 秒，翻转 LED 的状态。如果我们要把它打开，那我们就请求一个用色相（hue）和饱和度值表示的新颜色。色相会是随机的，饱和度会是 100%。所有这些 Embedded Swift 代码，感觉真的就像在写普通的 Swift 一样，这门语言的大部分内容都是直接可用的。我再上传一次固件，看看结果是不是能正常运作。程序启动运行之后，我们的设备应该会用一个随机变化的颜色不停闪烁它的 LED。

太好了！这正是我们想要的效果。为 LED 对象构建这一层封装，正是真正赋予我们 Swift 力量的地方：高层 API 让我们能写出干净、可读的代码。到目前为止，我们已经看到了 Embedded Swift 是怎样很好地融入你的工作流程的。你可以把它和供应商提供的 SDK 一起使用，还可以让你的 IDE 或文本编辑器提供完整的自动补全、显示定义和文档。借助 Swift 的互操作性，你可以在 Swift 代码里直接调用 SDK 里现成的 C API。但通常来说，把这些 C API 包装成一层为你的核心应用逻辑提供符合人体工程学、直观 API 的封装，是很有价值的。

既然我们已经把基础的东西跑通了，我们继续来构建一个真正的 HomeKit 配件。为此，我们要用到 "Matter" 协议。Matter 是一个用于构建智能家居配件的开放标准，2021 年的一场 WWDC 演讲对它做过深入介绍，如果你想了解更多，我鼓励你去看看那场演讲。在我用的这个 SDK 里，Matter 是以 C++ API 的形式提供的，我们同样可以用 Swift 的互操作性来使用这些功能，它会免费给我们提供所有的基础设施部分，比如设备发现和入网配置（commissioning）。而且，只要我们有一个实现了 Matter 协议的设备，它就会自动在 HomeKit 里工作，因为 HomeKit 原生支持 Matter 配件。我们再从一个什么都不做的空应用开始。要和 Matter 打交道，我们需要对它的数据模型和术语有一点了解。这是我们要实现一个 Matter 设备大致需要做的高层任务清单。我们需要创建一个所谓的根节点（root node），它代表整个 Matter 配件。然后我们需要一个端点（endpoint），在我们这个例子里，它就是那个彩色 LED 灯，这也会是那个持有状态（比如颜色和亮度）、并且能接收命令（比如开灯或关灯）的对象。然后我们会把这个端点连接到这个节点上，再把这个节点连接到一个「应用」对象上。我已经围绕 C++ 的 Matter API 写好了一层简单的封装，就是这个 "Matter" 子目录里的内容。

这和我们之前为 LED 灯打造好用 API 时用的方法完全一样。用它，我们就可以轻松地填好顶层逻辑了。

首先我们创建这个根节点。

然后我们创建并配置这个端点。

这就是我们的彩色灯，值得注意的是，它有一个 eventHandler——一个闭包，每当有一个来自 HomeKit 的事件被发送给这个端点时，它就会被触发。闭包是一种非常自然的回调机制，我们不需要去处理不安全的函数指针，或者在 C 里做回调时常见的那种无类型 context 参数。接下来，我们注册这个端点。最后，设置并启动一个 Matter 应用。

目前，这段逻辑只是打印出所有的事件，但我们现在已经构建出了一个有效的 Matter 应用。我们把这个应用刷写到设备上。

启动会花一点时间。通常来说，你需要为一个新配件走一遍设置流程，我之前已经做过了，我已经把这个设备注册到了我的 HomeKit 网络里，所以它已经知道该加入哪个 WiFi 网络。一旦它完成这一步，它就会作为一个 "Matter Accessory" 出现在我 Mac 上的「家庭」App 里，以及我其他设备上。它会显示成一个智能灯，我可以直接在这里、从我 Mac 上的「家庭」App 里控制它。我可以打开和关闭这盏灯，当我这么做的时候，我们就会在设备日志里收到对应这些命令的事件。

到目前为止，我们只是在记录收到的这些事件。我们来让它们真正做点什么！我们把它们接到我们之前用过的那个 LED 对象上。在这个事件处理程序内部，我们想针对不同被设置的属性做出反应。而且因为这个 attribute 是一个 Swift 枚举，我们可以用一个 switch 语句，自动补全会告诉我们需要处理哪些 case。我们来给不同的属性填上代码。根据我们收到的事件类型，如果需要开灯或关灯，我们就设置 enabled 属性；或者我们会设置 brightness 属性，这里我们还需要对这个值做相应的缩放。非常类似地，我们可以处理颜色的变化，设置新的色相、新的饱和度，或者新的色温。这应该就是我们需要的全部内容了。我们把这个程序刷写到设备上，来测试一下！在程序启动的过程中，我想指出 Swift 枚举有多好用、多符合人体工程学。

在最简单的情况下，枚举只是表示一组选项里的一个，比如 attribute 的 .onOff case 或者 .levelControl case。

但它们也可以带关联值。比如说 .colorControl 这个 case 就带有一个负载（payload），而且多亏了 Swift 的模式匹配，我不需要再嵌套第二层 switch 语句，我可以直接把这个枚举 case 和它的负载一起匹配出来。

我还用枚举来表示颜色属性，它可以是「色相加饱和度」，也可以是「色温」。

这些 case 甚至有不同的负载类型：第一个的负载是两个整数，另一个只需要一个整数。这一切结合在一起，让 Swift 的枚举变得非常强大、非常有表达力，也让我们能写出这种简单、简洁、可读的逻辑。既然设备已经启动了，我可以拔掉 USB 线，改用电池给它供电。

我们就可以从「家庭」App 里无线控制这个设备了。我们把灯打开。

再关掉。我们来看看能不能调节亮度。

或者选一个不同的色温。

或者干脆完全自定义颜色，我们来试几种不同的颜色。

太棒了，我觉得我们这个智能灯原型运作得很好！我们已经成功地用 Embedded Swift 构建出了一个支持 HomeKit 的智能灯。如果你有兴趣，这个演示项目和设置说明都已经发布在 GitHub 上了。我们已经看到，借助 Swift 的互操作能力，我们能多快地把一个支持 HomeKit 设备的基本原型跑起来。我们完全不需要用 Swift 重新实现整个 Matter 协议，直接用 Swift 现成的实现就可以了。Swift 鼓励你写出干净、直观的代码设计和实现，比起 C 和 C++，它提升了可读性和安全性，就像我们看到的那样，比如把闭包用作回调的一种符合人体工程学的解决方案。在这场演示里，我们看到了 Embedded Swift 用起来感觉就像普通的 Swift，而且它确实包含了 Swift 语言的大部分特性，但也存在一些差异。嵌入式环境通常资源非常受限，程序需要小巧、简单的二进制文件才能装得下。内存、存储和 CPU 性能通常都非常有限。正因如此，为了满足这些要求，Embedded Swift 不允许使用某些特性。举个例子，我们来看看运行时反射是怎么工作的。要检查一个类型的子字段，需要访问这个类型对应的元数据记录，其中包括字段的名字、偏移量和类型，而这些又会引用其他的元数据记录，如此层层嵌套下去。这些记录累加起来，对嵌入式设备来说，可能会带来一个无法接受的代码体积开销。

为了避免这一点，Embedded Swift 里不允许使用 Mirror API 这种运行时反射，它只在完整版 Swift 里可用。出于同样的原因，为了避免在运行时需要用到元数据，元类型（metatype）和 "any" 类型在 Embedded Swift 里也是不允许的。但请不用担心，Swift 语言的绝大部分内容在 Embedded Swift 里都是可用的。相比完整版 Swift，Embedded Swift 严格来说是它的一个子集，而不是一个变体或方言，所以 Embedded Swift 和完整版 Swift 之间不会有任何行为上的差异。任何在 Embedded Swift 里能用的代码，在完整版 Swift 里也同样能用。

当你试图使用一个在 Embedded Swift 里不可用的特性时，编译器会告诉你。在这个例子里，我试着用了一个 any 类型。

为了避开这一点，我可以改用泛型，来代替这里对 any Countable 的使用。在这段代码片段里，只需要简单地把 any Countable 换成 some Countable，就能把这个函数变成一个泛型函数。泛型在 Embedded Swift 里是完全支持的，因为编译器可以对泛型函数做特化（specialize）。这样做的结果是，生成的代码不需要昂贵的运行时支持或类型元数据。关于 Embedded Swift，还有很多可以探索的内容。作为 Swift Evolution 流程的一部分，一份关于 Embedded Swift 的愿景文档已经发布并被采纳。这份文档描述了 Embedded Swift 的高层设计、需求和实现思路，是了解这种编译模式和语言子集的绝佳入门材料。如果你打算尝试 Embedded Swift，我建议你读一读《Embedded Swift —— 用户手册》，它介绍了该怎样入门、你应该期待什么、不应该期待什么，还有一些当你要和你供应商的 SDK、构建系统打交道时很可能需要知道的细节，比如该用哪些编译器标志、需要满足哪些依赖。

我们已经在 GitHub 上发布了一组用 Embedded Swift 写的示例项目，它们涵盖了一系列使用 ARM 或 RISC-V 微控制器的嵌入式设备，其中包括一些流行的嵌入式开发板，还有一些其他设备，比如 Playdate 游戏机。这些示例还展示了怎样使用各种构建系统和集成方式。它们能让你感受到 Embedded Swift 能做到什么，也可以作为你自己想法的模板。当你写运行在嵌入式设备上的代码时，你常常需要和底层的硬件寄存器打交道。为了帮助大家做到这一点，我们发布了 "Swift MMIO"，这是一个库，提供了用于对内存映射寄存器进行安全、结构化、符合人体工程学操作的 API。最后，Swift 论坛现在新增了一个 "Embedded" 子分类，那正是你接下来该去分享你的实验、提出问题、参与讨论的地方。

我们已经看到了怎样用这种新的编译模式——Embedded Swift——来给嵌入式设备编程。它目前是以预览版的形式提供的，配合 swift.org 上的每日构建版工具链效果最好。目前支持 32 位和 64 位的 ARM 和 RISC-V 芯片，但 Embedded Swift 其实并不是绑定于特定硬件的，把它移植到新的指令集上也相当容易。快去试试 Embedded Swift 吧，做一些很酷的电子项目，并在 Swift 论坛上分享你的体验和反馈。感谢观看，祝大家 WWDC 愉快。
