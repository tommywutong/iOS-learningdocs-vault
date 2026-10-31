---
title: System Extensions 与 DriverKit
session_id: 702
collection: wwdc2019
year: 2019
duration: '37:01'
topics: [System Services]
group: I · 系统服务、进程与安全底层
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2019/702/'
content_hash: 'sha256:5b04a3a14afcb24e'
translated: true
---

# System Extensions 与 DriverKit

<sub>WWDC2019 · 37:01 · System Services</sub>

macOS 现代化并提升安全与可靠性下一步之一，是为内核提供更好的架构……
> [!note] 归档理由
> System Extensions/DriverKit：用户态驱动与进程隔离

## 相关资源

- [System Extensions and DriverKit](https://developer.apple.com/system-extensions/)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2019/702vygott3n041/702/702_hd_system_extensions_and_driverkit.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2019/702vygott3n041/702/702_sd_system_extensions_and_driverkit.mp4?dl=1)
- [Presentation Slides (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2019/702vygott3n041/702/702_system_extensions_and_driverkit.pdf?dl=1)
- [Create camera extensions with Core Media IO](https://developer.apple.com/videos/play/wwdc2022/10022)
- [What’s new in Endpoint Security](https://developer.apple.com/videos/play/wwdc2022/110345)
- [Create audio drivers with DriverKit](https://developer.apple.com/videos/play/wwdc2021/10190)
- [Build an Endpoint Security app](https://developer.apple.com/videos/play/wwdc2020/10159)
- [Modernize PCI and SCSI drivers with DriverKit](https://developer.apple.com/videos/play/wwdc2020/10210)
- [Advances in macOS Security](https://developer.apple.com/videos/play/wwdc2019/701)
- [Network Extensions for the Modern Mac](https://developer.apple.com/videos/play/wwdc2019/714)
- [What's New in Clang and LLVM](https://developer.apple.com/videos/play/wwdc2019/409)
- [What’s New in AppKit for macOS](https://developer.apple.com/videos/play/wwdc2019/210)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

我是 Joe，稍后我的同事 Simon 和 Scott 会加入。我们来自 Core OS 组，想向大家介绍 macOS 10.15 Catalina 中 Kernel Extensions 的新进展。

Kernel Extensions，或 Kexts，是 macOS 从一开始就包含的技术。

使用 Kexts，你可以构建强大的创新 App，扩展操作系统的内置功能。这种扩展系统的能力是 Mac 之所以是 Mac 的重要部分。但 Kernel Extensions 有一些问题。

它们可能难以开发和调试，可能对机器的安全与隐私构成风险，也可能对系统可靠性构成风险。是升级的时候了。

macOS Catalina 引入两项新技术，称为 System Extensions 和 DriverKit。

使用它们，你的 App 可以扩展操作系统，比以往更可靠、更安全、更容易开发。今天我们要谈这些。首先，我介绍这些新技术，并展示它们如何避免 Kernel Extensions 的问题。

然后 Simon 上台展示如何使用 DriverKit 构建 Driver Extensions。

Scott 展示如何编写和调试简单的 USB 驱动。

然后我讲如何在 App 中包含 System Extensions。让我们开始。System Extensions 是我们在 macOS Catalina 中的第一项新技术。System Extension 是你 App 的一部分，以类似 Kernel Extension 的方式扩展操作系统功能，但在内核之外的用户空间运行。

在 Catalina 中你可以构建三种 System Extension。它们是 Network Extensions、Driver Extensions 和 Endpoint Security Extensions。

Network Extensions 是 Network Kernel Extensions 的替代。

它们可以过滤和重路由网络流量，或连接到 VPN。

关于 Network Extensions，周五上午有专门的场次。

Endpoint Security Extensions 是 KAUTH 接口拦截和监视安全相关事件的 Kext 替代。你可以用这种方式构建的 App 包括 Endpoint Detection and Response 和 Data Loss Prevention App。如果你对 Endpoint Security Extensions 感兴趣，请来 Security Labs。现在有一个，本场后继续，周四下午还有一个。第三种扩展是 Driver Extensions，使用 IOKit 替代 Device Driver Kexts。在 Catalina 中，你可以控制 USB、Serial、Network Interface 和 Human Interface 设备。

Driver Extensions 使用 DriverKit 构建，这是我们 Catalina 中的第二项新技术。

DriverKit 是新 SDK，包含基于 IOKit 但更新和现代化的所有新框架，专为在内核外的用户空间构建 Driver Extensions 而设计。现在我们了解了这些新技术，看看它们如何避免 Kernel Extensions 的问题。

我在两个定义中都用了短语：用户空间，内核之外。为什么这重要？内核是非常不容错且困难的编程环境。内核是机器上一切的指挥者，因此它绝不能停止运行、绝不能等待任何事发生、绝不能崩溃。

内核代码必须快、必须可预测、必须在内存等资源使用上节俭，且必须基本无 bug。

很难写出满足所有这些限制的代码。

System Extensions 在内核外的用户空间运行，这意味着它们运行在舒适、现代化的编程环境中。

这使它们比 Kexts 更容易开发，后者在内核代码中对内存分配或线程同步的时机与方式有限制。

这意味着它不能使用大多数系统框架如 Foundation，因为它们不是为该环境设计的。

Kext 开发唯一支持的语言是 C 和 C++。

另一方面，System Extensions 没有这些限制，这意味着它们可以用 macOS SDK 中的任何框架构建，可以用任何语言编写，包括 Swift。

有一个例外。Driver Extensions 因与硬件的密切关系，仍有部分限制。

它们必须使用 DriverKit 框架，并运行在隔离它们与系统其余部分的定制运行时中。Driver Extensions 必须用 C 或 C++ 编写。不过默认是 C++17。System Extensions 也比 Kernel Extensions 更容易调试。把调试器附加到内核会暂停内核和包括调试器在内的整台机器。这通常需要第二台机器，可能需要特殊电缆或网络配置来连接机器。构建、测试和调试 Kext 的周期可能很慢，因为 Kext 中任何崩溃都意味着整个系统必须重启。而且内核调试器支持有限。它不能做诸如求值表达式或打印对象值之类的事。另一方面，System Extensions 可以调试，而内核继续运行。

扩展崩溃无需重启。

你可以在一台机器上构建、测试和调试，拥有完整调试器支持。但 System Extensions 相比 Kernel Extensions 最大的改进在安全、隐私和可靠性领域。内核有很多职责，但最重要的之一是定义和执行系统安全策略的规则。内核把 App 彼此隔离开，也把它们与硬件直接访问隔离开。然后允许它们按照安全策略的规则共享数据和系统服务。当 Kernel Extension 加载时，它成为内核的一部分。

它可以访问机器上的一切。这是 Kext 力量的来源。但它也可能危险。因为 Kernel Extension 是制定安全规则的内核的一部分，它在规则之上。如果 Kext 有 bug 可被利用，它就能接管整台机器，做其开发者从未打算、用户也不想要的事。没有安全规则能约束它。

这意味着 Kext 中的任何 bug 都可能是严重的安全问题。Kext 中的任何 bug 也可能是——也可能是——怎么了？我的幻灯片呢？Kext 中的任何 bug 也可能是严重的可靠性问题。因为内核不只是崩溃，它会 panic，整台机器必须重启。如果你是 Kext 开发者，肯定经常看到这个对话框。不幸的是，太多用户也看到过。让我们看看 System Extensions 改变图景。

System Extension 在用户空间运行。像其他 App 一样，它必须遵守系统安全策略的规则。与其他 App 不同，System Extensions 被授予特殊特权来完成特殊任务。例如，它们可能直接访问关联的硬件设备，或使用特殊 API 直接与内核系统通信。

如果 System Extension 崩溃，其余系统和 App 不受影响并继续运行。基于所有这些原因，我们认为 System Extensions 是 Mac 平台的一大步。事实上，我们认为它们改进如此之大，建议你立即采用。正如 Sebastian 昨天在 State of the Union 中所说，「我们正在开始弃用 Kernel Extensions。macOS 10.15 Catalina 将是完全支持 Kernel Extensions 且无妥协的最后一个版本。」具体而言，对于 System Extensions 支持的能力和 DriverKit 支持的设备系列，使用 Kernel Extension 完成相同任务现已弃用，未来版本的 macOS 将不会加载这些种类的 Kernel Extensions。未来版本中，我们将为 DriverKit 添加更多种类的 System Extensions 和设备系列。

相应地，这些种类的 Kernel Extensions 也将弃用。

这就是 System Extensions 的简要介绍。

它们通过在用户空间运行避免内核编程的困难，让你的 App 能以更易开发和调试、保护用户数据安全与可靠性的方式扩展系统。现在我想把时间交给 Simon，他将展示如何使用新的 DriverKit 运行时构建 Driver Extensions。嗯，谢谢 Joe。如 Joe 刚才所说，Driver Extension 是新类型的 System Extension，控制硬件设备并使其服务在整个 OS 中可用。

我们称这些新的 Driver Extensions 为 Dext。

我们的目标是尽可能让从 Kernel Extension 过渡到 Driver Extension 容易。

为了展示 Driver Extensions 如何工作，以及如何构建自己的或从 Kext 迁移，我们将谈四件事。

我们将谈它们的生命周期以及如何匹配和启动。

以及它们如何与 Kext 竞争，以及如何使用新的 DriverKit SDK 构建它们。我们将讲安全特性如 entitlements。最后，我们讲兼容性问题，如何把 App 部署到 macOS Catalina 和 Mojave。

先谈 Kext 的生命周期。

看看设备出现且有 Driver Extension 时发生的过程。我们从 IOKit Matching 开始，创建表示你的服务的内核服务。这是由 Apple 编写的。然后我们启动托管你的驱动的进程，实例化你的 DriverKit 类。进程还为它使用的任何服务提供代理对象，如其 provider。

这个设备使用 USB 设备。这个设备使用 USB 设备，因此它有代理对象来调用表示内核设备。这意味着 DriverKit 驱动对 Kernel Extensions 可见，并可以在匹配中与内核驱动竞争。你可以用 IOReg 等工具在注册表中看到它们，也可以用 IOKit Framework API 与它们交互。由于 DriverKit 驱动与内核及彼此隔离，另一个设备将有自己的进程和驱动的另一个实例。在 macOS Catalina 中，Apple 已开始把若干自有驱动移至 Driver Extensions。

这里你可以看到托管 USB 网络设备的进程，它在注册表中作为正常以太网设备对 OS 其余部分可见。你还可以看到注册表中托管若干 HID 和 serial 驱动的其他进程。现在我们谈使用 DriverKit SDK 构建你的 Driver Extension。

我们希望让那些当前构建 Kext 的开发者容易过渡到构建 Driver Extensions，因此我们从你们熟悉的 IOKit C++ API 开始。

DriverKit API 是 IOKit API 到用户空间的扩展。我们把它们收集到新的 DriverKit SDK，与 macOS SDK 分离。该 SDK 有有限的 API 表面，以保证可靠性和安全性，无法直接访问文件系统、网络或 mock 消息。这允许 Apple 为运行驱动定制用户空间进程，并赋予它更高优先级和更强能力。因此让我们谈 DriverKit SDK 中的一些类。首先，IOService 类存在于 DriverKit 中，与 IOKit 类非常相似。还有 IOMemoryDescriptor 和 IOBufferMemoryDescriptor 类，同样与 IOKit 非常相似。我们还有 IOKit 中 IOWorkLoop 和 EventSource 类的替代。最后，有一个新类 OSAction，用于表示 C 函数指针。

让我们更仔细地看一些类。IOService 类有 IOKit 的生命周期 API，如 Start、Stop 和 Terminate。

为了同步，每个 IOService 都有默认 DispatchQueue，所有方法都在队列上被调用，包括中断、定时器和完成回调。

IODispatchQueue 基于预运行的 Grand Central Dispatch 代码，是为在受限 DriverKit 环境中运行而优化的特殊版本。

驱动确实可以控制其队列以及哪些方法在哪些队列上调用，以支持高级用法。事件 API 类似 IOKit 的 IOWorkLoop 模型，但现在基于 Grand Central Dispatch API，使用队列和调度源处理中断与定时器。

block API 被 command gate 替代，GCD 提供易于使用且很可能熟悉的同步参数。

还有 IOSharedDataQueueDispatchSource 类，提供共享内存环形缓冲区，用于快速、低开销的消息传递。我们谈的最后一个类是 OSAction，它封装了 IOKit API 中的回调。它们总是异步的，私有地持有回调客户端的状态。它们允许回调用任意参数定义，并在编译时和运行时进行类型检查。以上是 DriverKit 中的一些类。让我们看看如何定义这些类，这与 IOKit 有点不同。

DriverKit 接口用扩展名为 .iig 的新文件类型描述，并由名为 IIG 的工具处理。

IIG 文件是类定义，由 Clang 编译，可以导入 C 和 C++ 头文件以使用常见类型和结构。但它对类和方法定义有一些额外属性，以便用于跨地址空间调用。这里你可以看到基本类定义，大部分看起来正常，但有一些额外属性，如类上的 kernel，表示该类在内核中定义。

以及某些方法声明上的 local，表示该方法在用户驱动中实现。Catalina 开发者预览中可用的一些家族包括 NetworkingDriverKit，用于创建网络接口。

HIDDriverKit 用于创建 HID 设备，USBSerialDriverKit 使 USB 串行设备对 OS 可用，USB DriverKit 用于在驱动中使用 USB 设备提供者。

稍后 Scott 将演示 USBDriverKit 的 USB 设备支持。现在谈开发 Driver Extensions 的安全方面。你的 Driver Extension 需要获得几种 entitlements。

所有 Driver Extensions 都需要一个，还有用于接管设备的 transport entitlement，特定于设备类型。还有 family entitlement，用于把服务提供给 OS。Joe 稍后在本场中讲代码签名和获取这些 entitlements 的批准流程。现在快速谈一下在所有 macOS 版本上发布产品。

发布同时支持 macOS Catalina 和更早版本的产品，需要为旧版本安装 Kernel Extension，但在 macOS Catalina 上使用 System Extensions Framework 并提供 Driver Extension。现在 Scott 演示如何使用新的 USBDriverKit Framework。谢谢 Scott。谢谢 Simon。今天我向你展示如何使用新的 USBDriverKit Framework 构建简单的 USB 驱动，从中断端点读取数据。我们简要介绍如何在 Xcode 中使用 DriverKit 模板创建新项目。之后，我们看内核类与 DriverKit 类的对比。然后，我深入 DriverKit 的实现细节。最后，我简短演示驱动实际运行，并说明如何用 LLDB 实时调试你的 Dext。在 Xcode 中创建新的 DriverKit 项目，只需在 Xcode 新建项目工作流中选择正确模板。完成后，Xcode 会自动生成一些文件帮助你开始。生成的项目包含成功构建所需的标准文件。与 Kernel Extension 一样，项目包含 C++ 实现、entitlements 和 info.plist。

此外，Xcode 还生成了 Simon 早先提到的 IIG 文件。该文件包含你的驱动类定义。

因此，让我们看看 MyUserUSBInterfaceDriver 的类定义。你可以看到它看起来与内核驱动非常相似。例如，相同的 public IOKit 生命周期方法 start 和 stop 在 DriverKit 中会大写。

尽管如此，有一些小但重要的差异。

首先，DriverKit 类需要不同的回调，带有额外属性。该属性表示该方法符合 IOUSBHostPipe 对象定义的回调类型，并强制编译时类型检查。其次，DriverKit 类中没有声明实例变量。这是因为所有实例变量必须由驱动在初始化期间分配。因此让我们看看 MyUserUSBInterfaceDriver 如何做到这一点。

首先，你需要声明结构体来保存所有实例变量。所有原本属于内核类的实例变量都应成为该结构体的一部分。对于这个类，我们有指向与 Kext 相同 USB 内核类型的指针。如用于执行 IO 的 IOUSBHostInterface provider 和 IOUSBHostPipe 对象。还有 OSAction 对象，用于封装异步 IO 的回调。然后你只需在 INIT 例程中分配该结构体。这里是 MyUserUSBInterfaceDriver 的 INIT 例程。它像 Kext 那样调用超类的 INIT。然后分配 IVAR 结构体。

应注意，超类定义了必须用于分配结果的 IVARs 成员。所以下面我们看 Start 的实现。Start 的这部分负责调用超类并验证 provider。

这里与内核实现略有不同。

你可以看到定义被包裹在宏 IMPL 中。该宏是支持用户进程与内核代理对象之间 IPC 通信所必需的。

你还可以看到调用 super start 采用不同形式。接下来，使用 USB DriverKit API，你打开 IOUSB host interface provider，并分配 Pipe 对象。

然后分配用于 IO 的内存描述符。

这应该是相当熟悉的模式，基本与 Kext 中所做相同。

这里我们执行异步 IO，因此需要分配 OS 属性对象来封装回调。

最后，剩下的只是入队 IO。

此时，假设设置成功，异步读取会在完成时调用 ReadComplete。这个驱动的 ReadComplete 方法只打印传输的字节数和状态。如果成功，它重新入队 IO。接下来，让我们看看驱动实际运行。在这个演示中，你将看到我添加到 MyUserUSBInterfaceDriver 的一些日志，会打印一些生命周期方法。

我还添加了无限循环，我们将用 LDB 调试。然后我还引入了崩溃，我们可以看到使用新的 DriverKit Framework 如何恢复。所以如果我插入设备，你可以看到 INIT 和 start 像在 Kext 中一样运行。随着数据在设备间传输，ReadComplete 被调用。使用 PS，我们可以看到驱动正在运行。现在我们命中了我添加的无限循环，可以用 LDB 查看驱动中发生了什么。

因此，从早先我们可以看到 PID 是 2572，需要附加到该进程。

我们需要找到运行 ReadComplete 方法的线程。

你可以看到那是 thread two。

这里我们确实有无限循环。而且因为运行在用户空间，我们可以修改循环变量。

在继续之前，如果你仔细看，可以确定有空指针解引用，会崩溃驱动。你可以看到它崩溃了。

但随后立即重启，而不影响其余系统。然后在拔出时你可以看到 stop 和 free 方法会正常运行。

这就是——这就是用新的 DriverKit Framework 构建和调试新驱动有多容易。现在我把它交回 Joe，讲如何在 App 中交付 System Extensions。谢谢 Scott。

现在我们已看到如何构建 Driver Extension，我想告诉你如何在 App 中发布驱动或其他类型的 System Extension。

我们将谈扩展与 App 的关系、如何构建和打包扩展 bundle。我们将谈代码签名和 entitlements，以及如何安装、更新和卸载 System Extension。System Extension 总是 App 的一部分。这是设计的基本原则。没有独立的 System Extension。

这是因为用户以 App 为单位思考。他们购买 App、安装 App、运行 App。你的 System Extension 应该是 App 的实现细节。

App 是用户与扩展交互和控制的方式。一旦你把 System Extension 打包进 App，就可以使用 Developer ID 直接分发给用户，或通过 Mac App Store 分发，这在 Kernel Extensions 时代从未可能。

由于 App 与其扩展的密切关系，你的 System Extension 应该可被用户识别为与你的 App 相关。你应该在扩展的 info.plist 中使用 CFBundleDisplayName 键为其提供良好的本地化名称，并给它与 App 主图标相关的自定义图标。这样，如果扩展 ever 在用户界面中显示，用户会认出它作为他们使用的 App 的一部分。

你还应该在扩展的 info.plist 中包含 usage description 字符串，简单解释扩展是什么、做什么以及用户为何运行它。把这看作类似日历或摄像头访问所需的 usage strings。

对于 Driver Extensions，使用键 OSBundleUsageDescription。对于其他类型的 System Extensions，使用键 NSSystemExtensionUsage Description。

记住为 App 支持的所有语言本地化这些及所有其他字符串。System Extension 本身是 App 的单独子 bundle，有自己的可执行文件和 info.plist，嵌入在应用程序内。这里是在示例应用中查看 System Extension 位于 Contents Library System Extension's 文件夹的窥视。

Driver Extension bundles 使用 .dext 文件名后缀和包类型 DEXT。它们在 info.plist 中使用 OSBundle 键，类似 Kernel Extension bundles。

Driver Extension bundles 应该是扁平 bundle，没有 contents 文件夹，类似 iOS apps。

其他类型的 System Extension bundles 使用 .system extension 文件名后缀和 CFBundlePackageType SYSX，System X tension。在 Xcode 中，你的 System Extension 是单独 target。Xcode 内置了 Network Extensions 和 DriverKit drivers 的模板。

当你创建此类 target 时，Xcode 会问是否要把它嵌入项目中已有的应用程序。如果是，它会创建 Copy Files phase，把扩展构建产物复制到你的应用程序中。一旦构建了 System Extension，你用与签名 App 相同的证书签名它。不再需要特殊 Kext 证书、Kext 特定签名证书。

通常，用于签名 System Extension 和主 App 的 Team ID 必须匹配。这是安全措施。然而，你可能构建的是打算打包进其他开发者 App 的扩展。例如，常见 USB 串行接口芯片的 Driver Extension，包含在许多产品中。如果是这样，有一个 entitlement 可用于 System Extension，允许它被打包进不同开发者的 App。

如果你用 Developer ID 签名 System Extension，它必须先 notarize 才能在用户系统上运行。关于 notarization 的更多信息，请观看去年的场次或今天下午晚些时候来 Notarization Lab。

你的 System Extension 使用 entitlements 向操作系统描述其能力：扩展类型以及它能做什么。例如，DriverKit Drive-- Extensions 使用 Simon 展示的 Transport 和 Family entitlements。

包含 System Extensions 的 App 也应使用 com-apple-developer-system extension-install entitlement。

关于这些 entitlements 的更多信息，以及为开发团队请求使用它们，请访问 developer.apple.com /system-extensions。在 Catalina 的 Developer Seed 中，本地开发时你可以关闭 System Integrity Protection，以在测试时禁用代码签名和 entitlements 的部分检查。

请记住，测试完成后重新打开 System Integrity Protection。现在你已构建带 System Extension 的 App，扩展如何安装到用户系统？无需安装器或包。你的 System Extension 留在 App bundle 中。你的 App 使用新的 System Extensions Framework，并创建 activation request，请求使扩展可供系统使用。系统管理员将批准该请求。大多数 App 可能在 App 启动时创建 activation request，以便扩展立即可用。如果扩展先前已激活并批准，activation request 会快速返回成功。然而，你可能希望在 App 生命周期的不同点激活 System Extensions，例如用户同意许可协议或完成应用内购买后（如果你的扩展需要）。

一旦扩展被激活，系统将管理其生命周期，例如在需要时自动启动。例如，Driver Extension 会在匹配的硬件设备连接时启动。

要更新 System Extension，更新 App bundle。用户可能安装从你网站下载的新版本，自动更新器可能就地更新 App bundle，或者你在 App Store 发布新版本，它将为用户更新。下次你的 App 运行并提交 activation request 时，系统会注意到扩展版本已更改。它会要求你的 activation request delegate 按照你自己的版本号规则比较版本号。

如果你的 delegate 确定这是升级，系统会停止旧版本的 System Extension 并启动新版本。如果用户希望卸载你的应用程序，当他们把 App 移到废纸篓时，其所有扩展将自动停用。如果你想使用，有 deactivationRequest API，但无需专用卸载器。

因此，今天我们介绍了 System Extensions，Kernel Extensions 的替代，让你的 App 以更可靠、更安全、比以往更容易开发的方式扩展系统。

我们看到如何使用 DriverKit SDK 和框架，这是 IOKit 的现代化更新，来构建驱动。我们看到如何编写并随后在一台机器上调试示例 USB 驱动。

最后，我们谈了如何在 App 中包含 System Extensions。

如果你有问题，我们很乐意在 Core OS Labs 回答。今天晚些时候有一个，周四上午还有一个。

你可能还希望访问现在或周四下午的 Security Lab，或周五上午的 Networking Lab。非常感谢，享受 WWDC 的其余时光。[ Applause ]
