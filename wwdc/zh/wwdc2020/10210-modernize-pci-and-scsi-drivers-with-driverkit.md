---
title: 使用 DriverKit 现代化 PCI 和 SCSI 驱动程序
session_id: 10210
collection: wwdc2020
year: 2020
duration: '36:53'
topics: [System Services]
group: I · 系统服务、进程与安全底层
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10210/'
content_hash: 'sha256:77e536683d0d170a'
translated: true
---

# 使用 DriverKit 现代化 PCI 和 SCSI 驱动程序

<sub>WWDC2020 · 36:53 · System Services</sub>

借助 DriverKit 将代码移出内核，使用配件时为客户提供更安全、更可靠的体验。了解如何……

> [!note] 归档理由
> DriverKit 驱动移植

## 相关资源

- [系统扩展与 DriverKit](https://developer.apple.com/system-extensions/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10210/3/CD65DE89-E747-4A3E-A078-13ACD36B9B72/wwdc2020_10210_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10210/3/CD65DE89-E747-4A3E-A078-13ACD36B9B72/wwdc2020_10210_sd.mp4?dl=1)
- [使用 DriverKit 将驱动程序带到 iPad](https://developer.apple.com/videos/play/wwdc2022/110373)
- [使用 DriverKit 创建音频驱动程序](https://developer.apple.com/videos/play/wwdc2021/10190)
- [系统扩展与 DriverKit](https://developer.apple.com/videos/play/wwdc2019/702)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。我是 Kevin，稍后我的同事 Madhu 会加入我。今天我们将介绍 DriverKit 的新特性。首先我会简要回顾一下 System Extensions 与 DriverKit。然后介绍新的 PCIDriverKit 框架。接着我会把时间交给 Madhu，她将深入讲解如何使用 PCIDriverKit 和新的 SCSIControllerDriverKit 框架编写 SCSI 控制器驱动程序。

然后她会演示这些新框架的实际运行效果。

最后，我会总结今天所讲的全部内容。去年我们推出了 DriverKit，作为 IOKit 设备驱动程序的替代方案。DriverKit 带来了一种扩展操作系统的全新方式，更加可靠、更加安全，也更易于开发。驱动程序扩展允许开发者打造强大而创新的 App，而无需承担编写运行在内核中的代码所伴随的风险。有关 DriverKit 及其工作原理的深入介绍，请参阅 Apple 开发者网站上去年的视频《System Extensions and DriverKit》。DriverKit 系统扩展运行在用户空间，而非内核空间。和其他 App 一样，它们必须遵守系统安全策略的规则。不同的是，系统扩展被授予特殊权限来完成特殊任务。例如，它们可以直接控制特定的硬件设备，或使用特殊 API 直接与内核交互。由于 DriverKit 驱动程序运行在用户空间，其访问权限受到限制，资源也与系统其余部分的资源相互隔离。当一个驱动程序扩展崩溃时，内核和系统的其余部分仍会继续运行。开发周期也快得多。我们可以在一台机器上构建、测试和调试，而内核扩展则会带来安全问题——kext 中的一个 bug 可能危及整个内核。kext 可以访问计算机的所有资源，而不仅仅是某个特定的硬件或资源。当内核扩展崩溃时，内核会 panic，并拖垮整台机器。调试和开发可能很慢，需要多台机器，并且每次崩溃后都要重启。驱动程序扩展的另一个巨大优势是安装更加简单。你的驱动程序扩展保留在 App bundle 中。你不应该把驱动程序扩展直接复制到任何系统文件夹。要安装 App，你需要使用 SystemExtensions 框架并创建一个 activationRequest，请求扩展可供系统使用。系统管理员需要批准这个请求。大多数 App 应该在 App 启动时创建 activationRequest，以便扩展立即可用。不过，你也可以选择在 App 生命周期的不同阶段激活系统扩展，例如用户同意许可协议之后，或在需要系统扩展的 App 内购买完成之后。

你可以在驱动程序进入 App Store 之前就开始编写 DriverKit 驱动程序，而无需 provisioning profile。为此，你需要禁用系统完整性保护，对 dext 进行本地运行签名，并确保包含驱动程序所需的所有 entitlement。

去年 DriverKit 首次推出时，支持 USB、串行、网络接口控制器和人机接口设备。随后引入了 PCI 支持。现在又新增了 SCSI 控制器支持。

因为 DriverKit 相比内核扩展带来了如此多的改进，我们建议对可用框架立即迁移到 DriverKit。

Catalina 是最后一个完整支持 kext 而无任何妥协的版本。我们已经开始弃用能够执行与系统扩展相同功能的内核扩展，包括 DriverKit 支持的设备家族。在 macOS Big Sur 中，macOS Catalina 中已弃用的 kext 默认不会加载。我们将继续为 DriverKit 添加更多类型的系统扩展和更多设备家族。相应地，这些种类的内核扩展也将被弃用。今年我们增加了对 PCI 和 SCSI 控制器驱动程序的支持。这意味着，对于能够执行与系统扩展相同功能的内核扩展，PCI 和 SCSI 控制器设备家族的 kext 支持现已弃用。这也意味着 PCI 和 SCSI 控制器 kext 在未来的 macOS 版本中默认不会加载。

现在我们来讨论 DriverKit 中一项令人兴奋的新增内容：PCIDriverKit。我将展示 PCI 驱动程序扩展与内核扩展之间的关键差异和驱动模型。然后展示几乎所有 PCIDriverKit 驱动都需要的代码示例。PCIe 用于扩展机器的能力，仿佛这些能力内置于系统中。PCIe 带来很多优势，因为它能处理最苛刻的高性能任务。常见的 PCIe 设备包括串行、以太网和 SCSI 控制器。

用户可以通过 Thunderbolt 或 PCIe 插槽（如最新的 Mac Pro）添加 PCIe 设备。和所有驱动程序扩展一样，PCIDriverKit 需要 entitlement 来授予对 PCI 设备的访问权限。这是为了确保其他 App 或恶意软件无法访问你的 PCI 设备。新的 entitlement 使用与 Info.plist 相同的 IOPCIFamily 驱动匹配条件。不过，如果需要支持多种设备，你可以让 entitlement 更通用。在这个示例中，我有一个 entitlement，允许你访问具有指定 vendor ID 的任何设备。这里我们使用 ABCD。PCI entitlement 接收一个 PCI 匹配字典列表。你可以通过使用 IOPCIFamily 匹配类别，让匹配条件尽可能具体或通用。

这里我们做的是主要匹配，意味着我们会将设备的主 vendor ID 和 device ID 与字典中的条目进行比较。

通过使用 & 符号，我们可以设置一个掩码，使匹配字典更通用。这实际上从匹配字典中移除了 device ID，允许驱动程序扩展获得该 vendor ID 下所有设备的 entitlement。

使用 PCIDriverKit 时，你很可能需要与众多其他 DriverKit 框架之一交互。这是你想要编写自定义以太网 NIC 驱动时 entitlement 的示例。在这种情况下，你会添加网络家族 entitlement。有了这个家族 entitlement，你就可以使用 Networking DriverKit 框架与网络栈交互。在 PCIDriverKit 中，框架中唯一的类是 IOPCI device。这个类不打算被子类化。你将使用这个类作为 PCI provider，来访问所有 PCI 资源。这是我们网络接口控制器示例中驱动程序扩展可能的样子。

用户空间的 IOPCIDevice 会完成与内核之间所需的 PCI 相关通信。你的驱动程序将使用 IOPCI device 进行任何 PCI 资源访问。

然后你的驱动程序可以使用 PCI 设备资源与网络家族及其他用户客户端通信。驱动程序扩展的分层结构与内核扩展大多相同，只是几乎一切都在用户空间。虽然在内核扩展中鼓励这样做，但 PCIDriverKit 强制要求：在访问 PCI 设备之前，必须成功调用 Open。一旦 Open 成功返回，你的驱动程序就对 PCI 设备拥有独占访问权。如果你的设备有供多个客户端共享的资源，你需要以单一 PCI 资源管理器分发资源给所有客户端的方式设计驱动程序扩展。这是为了强制良好的设计，并允许系统更优雅地处理驱动程序扩展崩溃。使用完设备后，例如在驱动程序的 stop 例程中，你需要调用 Close。你不应期望设备状态在调用 Close 后保持不变。例如，PCI 栈会在 Close 成功完成后禁用总线主控和内存空间。另一个驱动程序可能在获得 entitlement 的情况下打开设备并改变其状态。PCI 内核扩展与 PCIDriverKit 的另一个区别是，PCIDriverKit 框架会为你处理所有设备映射。所有内存访问都将使用新的 API。这允许开发者利用 Apple 未来可能探索的任何优化。它消除了任何设备内存管理的需求，并允许更多的可观察性和可调试性。通过单一访问点，你现在可以使用 dtrace 之类的程序观察所有设备内存访问。这在多线程环境中调试 PCI 问题时尤其有用。API 的工作方式是传入你希望访问的内存空间的 memory index 以及偏移量。我现在将介绍 memory index 与 base address register index 之间的区别。这是 PCI 设备的 base address registers（BAR）示意图。对于 32 位 BAR，memoryIndex 和 BAR index 完全相同。例如，对于 32 位地址，如果你想访问 BAR2，你会使用 2 作为 memoryIndex，因为它在设备的 BAR 空间中是相同的索引。64 位 BAR 是 memoryIndex 和 BAR index 可能不同的地方。memoryIndex 是每个内存条目的索引。所有 memory index 都从零开始。

例如，如果 BAR0 和 BAR1 合起来是一个 64 位地址，你的 memoryIndex 为 0，因为它是第一个内存条目。然后如果 BAR2 和 BAR3 是另一个 64 位地址，它们的 memoryIndex=1，因为它是设备 BAR 表中的第二个内存条目。访问设备的配置空间大多是一对一映射，仍然以新名称相同的方式工作。PCIDriverKit 与内核扩展在配置空间上的主要区别是，你需要先有一个打开的会话，才能读取或写入任何配置空间寄存器。接下来我将介绍一些你可能需要的常见代码示例。首先是如何启用总线主控和内存空间。这些是在访问设备内存以及启用设备发出 I/O 时所需的。以前每项操作都有显式的内核 API。现在，为了达到相同的结果，你将先读取命令寄存器，然后写回时设置总线主控和内存空间位。这个示例是大多数 PCI 驱动的样子。在 Start 例程中，它们首先与 PCI provider 启动会话。然后读取 PCI 设备的命令寄存器。设置总线主控和内存启用位，然后将值写回 PCI 设备。这需要在发出任何内存读取或写入之前完成。所有这些偏移量和定义都可以在 PCIDriverKit 框架头文件中找到。要禁用总线主控，过程相同，只是不是设置位，而是将它们掩掉。在这个示例中，Close 也在 Stop 例程中被调用。这意味着我们已经完成与 PCI 设备的通信，可以关闭会话。现在我们介绍如何设置中断处理程序。首先需要在 iig 头文件中声明一个 InterruptOccured 方法。然后中断处理程序的定义将使用实现定义。在这个示例中，当我们收到中断时，处理程序会通过向设备某一个内存索引的 MMIO 空间写入寄存器来清除中断。现在我们需要进行设置，使 interruptOccurred 方法在中断触发时被调用。首先需要找出要使用的中断索引。为此，我们将遍历与 PCI 设备关联的所有中断索引。然后检查其 interruptType。在这个示例中，我们想要处理设备的 msiInterrupts。这意味着一旦找到支持 MSI 的中断索引，就跳出循环。

然后我们需要选择处理中断的 DispatchQueue。

在这个示例中，我们将保持单线程，使用默认 DispatchQueue。如果你想专门为中断处理创建新的 DispatchQueue，也支持。

接下来，我们将通过指定 PCI 设备在前面找到的中断索引处的 interrupters，以及我们的默认 DispatchQueue，来创建 dispatch source。然后我们需要为新创建的 source 创建一个 interrupt action，用于处理中断。一旦 source 启用，我们的中断处理程序将在设备触发中断时被调用。最后，我们介绍如何为 PCI 设备设置 DMA 传输。首先创建一个 buffer memory descriptor。在写入缓冲区之前，需要设置缓冲区长度。然后这里是一个如何获取我们段的虚拟地址并向其写入数据的示例。

接下来，为了给 PCI 设备访问我们的缓冲区的权限，我们需要创建一个 IODMACommand。首先设置描述硬件 DMA 能力的 DMA 规范。然后创建 IODMACommand，指定这是为我们 PCI 设备准备的。这是为了确保所有传输都使用正确的 memory mapper。

接下来，我们将使用 DMACommand 准备我们的 buffer memory descriptor，以便获得给 PCI 设备的物理地址。然后我们可以使用 physicalAddressSegment 的结果获取缓冲区的物理地址，写入我们的 PCI 设备。传输完成后，我们需要在 DMA 命令上调用 Complete，以便物理内存可以被另一个进程或设备使用。这是对新 PCIDriverKit 框架的简要介绍。现在我想把时间交给 Madhu，她将详细讲解如何使用 DriverKit 编写 SCSI 驱动程序。大家好，我是 Madhu，我将谈论 SCSIControllerDriverKit 框架。它是 DriverKit 中一个全新的框架，用于为 SCSI 控制器构建驱动程序扩展。让我们从概述开始。SCSIControllerDriverKit 框架今天已在 macOS Big Sur 中提供。它支持 SCSI kext 在过去支持的所有基于 IOKit 的设备驱动功能。这个框架将作为 IOSCSIParallelInterfaceController 实现的替代方案，后者直到现在一直用于 kext 开发。框架在构建时将性能作为最高优先级。它经过高度优化，以最小化 I/O 性能路径中用户空间与内核之间的交互。

它可以支持多种基于 SCSI 的设备，如 Fibre Channel 控制器、RAID 控制器、串行连接 SCSI 等。由于这些是基于 PCIe 的控制器，我们确保框架与 PCIDriverKit 框架完全兼容。

IOUserSCSIParallelInterfaceController 是 iig 接口文件中定义的新类。SCSI dext 必须子类化它并实现其函数。现在我们尽量保持与内核类相似的 API 结构，只是在 API 名称前加 "User" 前缀。例如，UserProcessParallelTask 是新 API，dext 需要实现它来向硬件提交 I/O 请求。确定 dext 需要覆盖哪些框架函数相当简单。只需覆盖所有标记为 pure virtual 的函数。这些函数是框架调用 dext 以获取控制器特定信息或执行特定任务的调用。例如，框架调用 UserDoesHBAPerformAutoSense 来检查 HBA 是否支持 auto-sense。它调用 UserInitializeController 来初始化控制器和 dext 数据结构。所有非 pure virtual 函数由 dext 调用以执行特定任务，如创建具有唯一 ID 的 SCSI 目标，或为特定目标设置目标属性。这些函数的实现存在于内核中。和我们已经知道的一样，在构建和加载驱动程序扩展之前需要添加 entitlement。除了通用的 DriverKit entitlement 和传输特定的 entitlement 之外，我们为 SCSI 控制器添加了新的家族 entitlement。SCSI dext 需要添加这个 entitlement 才能运行并完全访问框架。有了这些，让我们创建一个示例 SCSI dext。我将其分为四个重要阶段。在每个阶段，我将展示如何覆盖一些重要函数，讨论一些指南，并分享一些性能提示。让我们从启动和初始化开始。内核将通过大量调用来控制 dext 的启动和初始化阶段。

除了调用初始化控制器之外，它还将进行大量调用来收集控制器特定信息，如支持的最大任务数、支持的最高设备 ID 等，并相应设置所有内核数据结构。让我们看看当 SCSI 控制器设备插入时会发生什么。IOKit 匹配启动，内核中启动一个类型为 IOUserSCSIParallelInterfaceController 的 IOService 对象。IOKit 的 IOService 实现现在将开始创建启动用户空间 dext 所需的资源。

它初始化 IOUserServer IPC 层，并创建一个进程来托管 dext，其 DriverKit 类已初始化。DriverKit SCSI 设备被加载，IOUserSCSIParallelInterfaceController 首先调用其 Start 实现。然后它调用 UserInitializeController 和 UserStartController 等大量其他函数，以完成启动和初始化阶段。

让我们开始实现。我只讨论 dext 需要实现的一些重要框架函数。第一个是 UserInitializeController。我们首先将与 PCIDriverKit 打开一个新会话，就像 Kevin 之前讨论的那样。DriverKit 框架已经为我们创建了一个默认 DispatchQueue。我们将在这里创建并设置两个额外的 DispatchQueue。我们还将创建一个 InterruptDispatchSource 并注册一个处理程序来处理中断。

这让我们来到我们希望你在构建 dext 时遵循的排队模型。我们建议总共使用三个 DispatchQueue——由 DriverKit 环境为你创建的 Default Queue，另外还有 Interrupt Queue 和 Auxiliary Queue。Default Queue 运行所有源自内核的调用——例如 UserInitializeController、UserProcessParallelTask 等。有一个单独的队列来服务中断会很有帮助。由于 DriverKit dispatch queue 是串行的，中断和 I/O 不会相互竞争运行。

这也会带来巨大的性能提升。这个队列还可以用于服务 dext 的 IOTimeoutHandlers。需要设置一个单独的 Auxiliary Queue 来创建 SCSI 目标。作为创建目标的一部分，内核会进行大量调用 dext 以帮助初始化目标。

由于这些调用将在 Default Queue 上运行，dext 需要从单独的 Auxiliary Queue 创建 SCSI 目标。内核将基于控制器一次可以支持的最大未完成命令数，维护一个 IODMACommands（这里是 SCSIParallelTask）列表。

每次它创建一个新的 SCSIParallelTask 对象时，都会调用 dext 的 UserMapHBAData 实现。dext 可以利用这个机会创建其控制器特定的 taskData 结构，并维护它们的列表。这是我的示例 SCSI dext 的一些实现细节。

我为控制器特定的 taskData 结构创建了一个 idle buffer memory descriptor 对象。我还把 buffer memory descriptor 映射到 dext 的地址空间。在开始服务 I/O 之前进行任何此类预处理都很重要。在 I/O 路径中这样做会对性能产生负面影响。我将这个 task data 添加到 taskData 列表。我还为这个 task 分配一个唯一的 taskID，以便内核可以将其与对应的 SCSIParallelTask 对象关联。接下来，在我的 UserStartController 实现中，我在硬件上启用中断。然后我启用 interrupt dispatch source。从 UserStartController 返回 Success 表示内核 dext 已启动并准备好服务 I/O。

这让我们来到任何存储驱动最有趣的部分：I/O 路径。

让我们先稍微回顾一下，复习一下这在今天的内核中是如何工作的。

以前，kext 会覆盖 ProcessParallelTask 函数，并可以访问 SCSIParallelTask 对象。SCSIParallelTask 是 IODMACommand 的子类。kext 负责准备 IODMACommand 并生成用于 DMA 的物理段。它会在收到 I/O 的中断完成时调用 CompleteParallelTask。我们用 dext 大大改变了这一行为。内核现在将调用 dext 的 UserProcessParallelTask 实现来提交 I/O。

作为这个调用的一部分，它会向 dext 发送一份 SCSIUserParallelTask 对象的副本。

这个对象将包含 dext 执行此 I/O 所需的所有信息，dext 将不必再向内核发起任何调用。

就像我开头提到的，这个框架在构建时将 I/O 性能作为最高优先级。注意，dext 无法访问 SCSIParallelTask 对象。内核将完成所有准备 IODMACommand 和为 dext 生成物理段的繁重工作。

让内核处理准备 I/O 以进行 DMA 所需的所有操作，有明显的性能优势。在用户空间准备 IODMACommand 会导致向内核发起额外的 IPC 调用，我们希望在性能路径中不惜一切代价避免这一点。

I/O 提交后，每当硬件发送中断完成时，dext 的中断处理程序就会被调用。然后它必须调用 ParallelTaskCompletion，这是一个 OS action 回调，来完成这个 I/O。

这里是我们需要关心的两个主要函数。dext 需要实现 UserProcessParallelTask 函数用于 I/O 提交，并需要调用 ParallelTaskCompletion 来表示 I/O 完成。我们已经稍微讨论过 SCSIUserParallelTask。如我们所见，它包含大量关于 I/O 的信息，如 CDB、数据传输计数、数据传输方向等。

这个结构中的一个重要字段是 fBufferIOVMAddr。就像我之前提到的，内核为我们生成 DMA 物理段，fBufferIOVMAddr 将是这个段的起始物理地址。内核保证会生成一个可以容纳所有缓冲区数据的长连续段。

dext 需要在 ParallelTaskCompletion 回调中发送这个响应对象。

它需要包含特定 I/O 完成的所有相关信息，如完成状态、传输的字节数等，以及 sense data（如果有）。

让我们看看我们的示例实现。我首先从列表中获取 taskID 对应的 taskData。我在我 taskData 中设置此 I/O 的所有元数据。内核将生成一个以 fBufferIOVMAddr 为起始地址的长物理段。如果你的硬件规范要求将其拆分为多个段，可以自由准备自己的 ScatterGatherList。我保留并保存 away 完成回调对象以供后续使用。我向硬件发出请求，并向内核发送适当的响应。一旦收到中断完成，我处理中断响应并填充 SCSIUserParallelResponse 结构。

然后我调用完成回调。现在我们在示例 dext 中实现了 I/O 提交和完成逻辑。让我们进入驱动开发的下一阶段：电源管理。在 DriverKit 中支持电源状态转换就像覆盖 SetPowerState 函数并为支持的每个电源状态实现硬件特定功能一样简单。DriverKit 框架今天支持三种电源状态：关机状态、开机状态和低功耗状态。对于基于 PCIe 的设备，我们主要需要关心关和开两种状态。关状态用于设备进入睡眠状态时，例如系统睡眠期间，或执行 PCI pause 操作时。

开状态用于设备完全上电时，称为系统唤醒。在 DriverKit 中也支持延迟确认电源状态转换。让我们看一个示例。这里我覆盖了 SetPowerState，为了简洁，只展示了 PowerStateOn 转换。对于我的硬件，我将发出硬重置来将电源状态更改为 on。然后我将回调返回内核。由于我发出了硬重置，我的驱动程序在硬件上启动完整的 SCSITargetRescan。我确保所有目标都已启动，然后通过发出 SUPERDISPATCH SetPowerState 调用来确认电源状态转换。现在我的示例 dext 中实现了电源管理支持。让我们通过讨论终止来结束。DriverKit 终止相当直接。只需覆盖 Stop 方法并在其中拆解一切。我们为你简化了这一点。

dext 不负责完成任何未完成的 I/O 请求。

内核为你处理所有这些。让我们看一个示例。在我的 Stop 实现中，我首先关闭未完成的 PCI 会话。然后我取消所有 dispatch queue 和 source。我在 finalize 代码块中释放它们，该代码块在 Cancel 调用完成后由框架调用。就这样！我们现在在示例 SCSI dext 中实现了所有主要功能。

现在我知道你们都在想什么——这里我们有一个系统，文件系统下来的每一个 I/O 都通过 IPC 调用发送到运行在用户空间的 dext。中断处理程序通过内核的 IPC 调用被触发。

dext 的 I/O 完成通过 IPC 调用从用户空间发送回内核。这听起来开销很大。这会影响我的 dext 性能吗？我的 dext 能达到与 kext 相同的吞吐量吗？我还能在这些设备上运行专业工作负载吗？这些都是很好的问题。我们开始开发这个框架时也有同样的担忧。就像我已经提到过几次的，我们在设计和实现这个框架时将性能作为最高优先级。

我很高兴地报告，SCSIControllerDriverKit 可以处理与 kext 相同的工作负载。让我们在示例 SCSI dext 上运行一个真实工作负载，看看它的表现。我的设备设置包括一个四吉比特每秒的 Fibre Channel 主机总线适配器连接到 RAID 磁盘阵列。我已通过 Thunderbolt 3 将这个设置连接到这里的 MacBook Pro。

为了构建和安装我的示例 SCSI dext，我确保添加了所有必需的 entitlement，并将其打包在 System Extension app 中。我还确保我的 System Extension app 在 App 启动时创建 activation request，以便 dext 立即可用。然后我构建了 System Extension app 并对其进行了适当的代码签名。我已经在这个系统上安装了 System Extension app。

让我们窥探 I/O registry，看看我们的 dext 是否已匹配。在那里：我们的示例 SCSI dext 已成功启动并正在运行。我们的 Fibre Channel 控制器在这个例子中实际上是一个多功能 PCI 设备，所以我们看到两个独立的 ExampleSCSIDext 实例在运行。让我们打开磁盘工具，看看我们的 dext 是否提供了任何磁盘。看起来这里有一个带 Fibre Channel 接口的外部磁盘。磁盘已格式化为一个 APFS 卷，该卷已挂载，正如我们在这里桌面上所见。我们认为通过运行实际的专业工作负载来演示性能会是个好主意。我在这个外部 SCSI 磁盘上有一个 Final Cut Pro 库，让我们打开它。

视频处理和播放可能对 CPU 和磁盘都很密集。在服务 I/O 时，如果我们的 dext 的 CPU 利用率因任何原因增加，它将会显示出来。我们的 dext 进程可能从实际的视频播放中窃取 CPU 时间，从而导致掉帧。我们的目标是确保 dext 能够流式传输这个视频而没有任何掉帧。为了确保，如果发生这种情况我们会看到，我将在这里启用这个选项，以便因磁盘性能而收到掉帧警告。让我们开始播放视频。

我还要在旁边打开 Activity Monitor，以便我们查看磁盘使用情况。

我已在这里选择了 Final Cut Pro 进程。我们有这个以 Apple ProRes 格式播放的精美视频。这个视频的最大磁盘吞吐量约为每秒 350 兆字节，这相当接近我们的四吉比特每秒 Fibre Channel 控制器所能支持的最大吞吐量。我们的 dext 目前表现很好。

整个视频都是从运行在用户空间的示例 SCSI dext 流式传输的。这有多酷？而且我们没有收到任何掉帧警告，这意味着我们的 dext 能够像专业人士一样处理这个专业工作负载。就是这样。DriverKit 的所有优势，如安全性、易于开发和调试，而性能不受影响。这就是 SCSIControllerDriverKit 框架的简要概述。一个用于为 SCSI 控制器构建驱动程序扩展的全新框架。交还给你，Kevin。谢谢，Madhu。

今天我们简要介绍了 DriverKit 系统扩展，并了解了如何为设备采用新的 PCIDriverKit 和 SCSIControllerDriverKit 框架。我们深入探讨了通过 PCI 编写 SCSI 控制器驱动程序的示例，并看到了如何使用这些框架的真实演示。有了新的 SCSI 控制器和 PCIDriverKit 框架，当系统扩展能够执行相同功能时，SCSI 控制器和 PCI 内核驱动程序现已弃用。有关 DriverKit 的深入介绍，请查看开发者网站上去年的 System Extensions and DriverKit 会话。我鼓励开发者立即开始为可用的设备家族采用 DriverKit。

请下载最新的 DriverKit SDK，并通过 Feedback Assistant 告诉我们任何反馈。我们很乐意听到你的声音，并期待看到你将创造什么。
