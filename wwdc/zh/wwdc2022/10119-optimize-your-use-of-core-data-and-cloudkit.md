---
title: 优化 Core Data 和 CloudKit 的使用
session_id: 10119
collection: wwdc2022
year: 2022
duration: '26:21'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2022/10119/'
content_hash: 'sha256:cec1d19a16db8163'
translated: true
---

# 优化 Core Data 和 CloudKit 的使用

<sub>WWDC2022 · 26:21 · System Services</sub>

与我们一同探索开发周期中三个有助于优化 Core Data 和 CloudKit 实现的部分……

> [!note] 归档理由
> Core Data + CloudKit 同步优化

## 相关资源

- [将本地存储同步到云端](https://developer.apple.com/documentation/CoreData/synchronizing-a-local-store-to-the-cloud)
- [使用 CloudKit 镜像 Core Data 存储](https://developer.apple.com/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit)
- [Core Data](https://developer.apple.com/documentation/CoreData)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10119/4/8D4ACDA6-A3CE-4294-8DFE-B4CF5DE26D86/downloads/wwdc2022-10119_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10119/4/8D4ACDA6-A3CE-4294-8DFE-B4CF5DE26D86/downloads/wwdc2022-10119_sd.mp4?dl=1)
- [演进 Core Data 数据模型](https://developer.apple.com/videos/play/wwdc2022/10120)
- [问答：Core Data](https://developer.apple.com/videos/play/wwdc2022/110836)
- [问答：Core Data](https://developer.apple.com/videos/play/wwdc2022/110838)
- [构建通过 CloudKit 和 Core Data 共享数据的 App](https://developer.apple.com/videos/play/wwdc2021/10015)
- [使用 Xcode Organizer 诊断性能问题](https://developer.apple.com/videos/play/wwdc2020/10076)
- [Instruments 入门](https://developer.apple.com/videos/play/wwdc2019/411)
- [将 Core Data 与 CloudKit 配合使用](https://developer.apple.com/videos/play/wwdc2019/202)
- [定义大型数据生成器](https://developer.apple.com/videos/play/wwdc2022/10119/?time=275)
- [测试大型数据生成器](https://developer.apple.com/videos/play/wwdc2022/10119/?time=307)
- [在测试中同步生成的数据](https://developer.apple.com/videos/play/wwdc2022/10119/?time=333)
- [期望辅助方法](https://developer.apple.com/videos/play/wwdc2022/10119/?time=395)
- [在测试中导入数据模型](https://developer.apple.com/videos/play/wwdc2022/10119/?time=438)
- [数据生成器警报操作](https://developer.apple.com/videos/play/wwdc2022/10119/?time=503)
- [在数据生成器中急切生成缩略图](https://developer.apple.com/videos/play/wwdc2022/10119/?time=650)
- [在数据生成器中惰性生成缩略图](https://developer.apple.com/videos/play/wwdc2022/10119/?time=673)
- [有问题的 verifyPosts 实现](https://developer.apple.com/videos/play/wwdc2022/10119/?time=854)
- [高效的 verifyPosts 实现](https://developer.apple.com/videos/play/wwdc2022/10119/?time=889)
- [使用 `log stream` 显示日志](https://developer.apple.com/videos/play/wwdc2022/10119/?time=1241)
- [使用 `log show` 显示日志](https://developer.apple.com/videos/play/wwdc2022/10119/?time=1476)
- [为 `log show` 提供谓词](https://developer.apple.com/videos/play/wwdc2022/10119/?time=1517)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Nick Gillett，Apple Core Data 团队的工程师。在这个讲座中，我将向你展示如何使用我们的开发者工具，来更深入地了解你使用 NSPersistentCloudKitContainer 的 App。我们将首先详细探讨如何以富有成效且具启发性的方式探索 App。

然后，我们将使用我最喜欢的一些工具来分析 App 的行为。最后，我们将看看如何就你使用 NSPersistentCloudKitContainer 的经验，提供详细且可操作的反馈。

我喜欢把工程学看作是水循环。通常，我从探索某个功能所处的领域开始着手。然后，基于我学到的东西，我结合使用各种工具和测试，在一个可复现的环境中分析我的工作。

最后，我与同事和同行们一起回顾结果，并收集他们的反馈。

这个循环的目标是持久地捕捉我在工作中所学到的东西。Apple 平台提供了一系列出色的工具，比如 Xcode、Instruments 和 XCTest，我用它们来捕捉我所学到的内容。这些工具还使得收集大量诊断信息成为可能，我可以利用这些信息提供可操作的反馈。

本次讲座会引用很多往年的知识。我已在“构建通过 CloudKit 和 Core Data 共享数据的 App”和“将 Core Data 与 CloudKit 配合使用”这两个讲座中，详细讨论过 NSPersistentCloudKitContainer 以及我今天将演示的 Core Data CloudKit 示例 App。我还将演示如何使用 Xcode 和 Instruments 来运行测试，以及使用 Device Organizer 从设备捕获数据。如果需要，我建议你回顾“Instruments 入门”和“使用 Xcode Organizer 诊断性能问题”这两个讲座，以了解这两个工具链中的重要组成部分。好了，让我们开始这个循环的第一部分：探索。对我来说，探索的主要目标是学习。我想挑战和验证我对 App 将如何运作的所有假设。

我可能会问：如果我点按这个按钮会发生什么？当我把数据保存到持久化存储时，NSPersistentCloudKitContainer 会同步吗？App 在处理大数据集时会耗尽内存吗？从 Core Data 的角度来看，所有这些问题都受到 App 处理的数据的影响。例如，Core Data CloudKit 示例 App 使用这个数据模型。

它管理一组帖子，每个帖子有一些用于标题和内容的文本字段。

帖子可以与附件相关联，通常是图片，这些图片可能非常大。

因此，ImageData 通过一个 to-one 关系存储，以便可以按需加载。我将把探索重点放在这个数据集上，具体来说是当我改变这些数据的形态、结构和差异时，示例 App 会发生什么。

自发布以来，示例 App 就包含了一种内置的探索方式。“生成 1000 篇帖子”按钮的作用完全如其标签所示。

点按时，它会生成一个包含 1000 篇短标题帖子的示例数据集。帖子表格视图可以轻松处理这一级别的数据。所以我要问的下一个问题是，我如何在这个 App 中探索不同形态或大小的数据集？“生成 1000 篇帖子”按钮运行了我称之为算法数据生成器的东西。算法数据生成器遵循一组预定义的规则，比如“插入 1000 个对象”或“确保每个字段都有值，或者没有字段有值”。事实证明，我们自己也是数据生成器。我们可以手动在代码、SQL 或直接通过与 App 交互来精心制作特定的数据集，并且这些生成的数据集可以被保存下来供以后使用或分析。

为了探索更大的数据集，我可以定义一个新的数据生成器 LargeDataGenerator，并给它一个方法 generateData，用于构建我的新数据集。只需两个 for 循环，我就能生成一组 60 篇帖子，每篇帖子关联 11 个图片附件。总共 660 张图片。按每张图片平均 10-20 MB 计算，生成的数据集消耗近 10GB 的数据。有了如此简单的接口，数据生成器可以很容易地在测试中被调用，就像这个测试一样。这单行代码为此测试生成了超过 10GB 的代表性数据。

此外，我们还可以在测试中构建验证方法，以检查数据生成器的行为是否正确，比如断言每篇帖子确实有 11 个图片附件。

当然，如果不同步这些数据，那就不是关于 NSPersistentCloudKitContainer 的讨论了。所以让我们编写一个新的测试来做这件事。

我首先需要一个 NSPersistentCloudKitContainer 的实例。我创建了一个辅助方法来简化此过程。接下来，我使用 LargeDataGenerator 用所需的数据集填充容器。

最后，我等待容器完成数据导出。在这个特定的测试中，我最多等待 20 分钟，以便给大数据集足够的时间上传。

眼尖的你可能已经注意到，这个测试似乎花了大量时间等待不同类型的事件。这里，当我创建容器时，我等待容器完成设置。

而在这里，我使用自己编写的一个辅助方法来为容器的一个导出事件创建 XCTestExpectation。

我们来详细看一下。

这个方法接收一个所需的事件类型和一个 NSPersistentCloudKitContainer 实例作为参数。它为容器中的每个持久化存储创建一个 expectation，使用 XCTestCase 的 expectationForNotification 方法来观察 NSPersistentCloudKitContainer 的 eventChanged 通知。在通知处理程序 block 中，我会验证传入的事件是否正是该 expectation 所针对的特定存储的正确类型，并通过检查 endDate 不为 nil 来确认事件是否已完成。

通过使用这种技术，我们可以将测试中的控制点与 NSPersistentCloudKitContainer 的事件强关联起来。回到我的测试，我添加一个新的容器来导入刚刚导出的数据。这个技术使用了一个技巧。它创建了一个带有空存储文件的新 NSPersistentCloudKitContainer 实例。这使得测试可以利用 NSPersistentCloudKitContainer 的首次导入功能，来探索当一个设备下载所有这些数据时会发生什么。测试很棒，但有时我想感受一下数据集在 App 中的行为表现。为此，我可以将数据生成器绑定到用户界面，就像我们在示例 App 中所做的那样。

当我点按“生成大型数据”按钮时，我可以观察数据生成器填充数据集。在另一台设备上，我可以观察表格视图随着 NSPersistentCloudKitContainer 下载生成的数据而逐步填充。点按单个帖子，我可以看到附件逐步下载并显示，就像这个 App 的用户所看到的那样。这个特定的用户界面是由一个 alert controller 驱动的。

LargeDataGenerator 的简单接口使得只用这两行代码就能轻松添加一个新的 alert action。它清晰、简洁且易于理解。

在这一部分中，我们使用了数据生成器的概念来探索一个 App 的行为。

我们可以用任何选择的方式来驱动 App 中的数据生成器，无论是通过测试、自定义 UI（正如我演示的），还是通过命令行参数，或者任何其他恰好适合你特定用例的方式。现在我们知道了如何用数据填充 App，我们准备分析这会如何改变 App 的行为。在这一部分，我们将学习一些工具和技术，来分析 App 在处理大数据集时的行为表现。

具体来说，我们将使用 Instruments 分析 LargeDataGenerator 创建的数据集在时间和内存上的复杂性。

然后，我们将查看系统日志中可获取的大量信息。在那里，我们可以找到来自 NSPersistentCloudKitContainer、CloudKit、系统调度器和推送通知的活动记录。让我们从 Instruments 开始。我喜欢测试的一个原因是，Xcode 可以轻松分析测试的行为。在我的测试用例中，我可以在代码行号区域的测试展开按钮上右键单击，然后选择“Profile”。Xcode 将构建测试，然后自动启动 Instruments。

我可以双击 Time Profiler 工具来检查测试的时间消耗。

当我点按录制按钮时，Instruments 将启动 App 并执行选定的测试。这个测试似乎需要相当长的时间来运行。让我们快进，看看原因。

Instruments 已经选择了主线程，在右侧，我可以看到测试运行中最重的堆栈跟踪。

让我让它更容易阅读一些。

好了。现在，如果我滚动到底部，我可以看到 LargeDataGenerator 花费了大量时间生成缩略图。我们如何判断这是一个 bug 还是一个 feature？在 LargeDataGenerator 中，我有这行代码，它为每个附件生成一个新的缩略图。但是，我从 App 的数据模型知道，缩略图是特殊的。它们是按需从关联的 imageData 计算得出的。这意味着这行代码是不必要的，我的数据生成器在它们上面浪费了大量时间。所以我直接删除了它。让我们看看这对测试的性能有何影响。

使用更新后的数据生成器重建 App 后，我可以在 Instruments 中重新运行测试。老实说，我没有看到太大变化，但几秒钟后，测试完成了。这比之前的运行快了很多。让我们看看测试大部分时间花在了哪里。

在右侧面板中，我现在看到最重的堆栈跟踪是将图片保存到持久化存储，这正好是我对管理这么多数据的测试的预期。

这一个改动将 generateData 测试的运行时间从 A 缩短到了 B。它的执行时间缩短到了原来的十分之一。像这样分析测试并不总能发现 bug，有时我们只是更了解了 App 在处理特定数据集时的时间消耗。但无论如何，这都是有价值的学习。

这就是 Time Profiler 工具如何帮助探索 App 在处理数据集时的时间消耗。现在，由于这个数据集的大小，我也很好奇这个测试使用了多少内存。让我们使用 Allocations 工具运行一下。我将使用 Xcode 启动 Instruments 来分析我的测试。

这次不选择 Time Profiler 工具，而是双击 Allocations……

然后点按“Record”（录制）。

尽管这个测试执行得很快，但它使用了大量内存，实际上超过 10GB。这告诉我，整个数据集几乎全部保存在内存中。让我们找出原因。

我可以选择一段范围的分配来查看。在底部窗格中，我可以看到一些大型分配。

我可以通过点按这个展开按钮来深入查看，然后点按测试中分配的一个大型数据 blob。这个特定的 blob 被分配后，几乎有两秒钟没有被释放。在测试时间中，这就像是永恒。为什么它存活了这么久？我可以通过展开右侧的堆栈跟踪来探索。

根据经验，分配和释放的堆栈跟踪告诉我，该对象被 CoreData 转为惰值（faulted），然后在托管对象上下文完成其工作后被释放。这通常表明该对象被一个 fetch 操作、一个 autoreleasepool 或测试中的一个对象持有。

有问题的代码段位于我的验证器（verifier）中。我从附件加载一张图片并验证它。然而，这导致附件及其关联的图片数据仍然在托管对象上下文中注册。

我们可以尝试多种方法来解决这个问题。例如，在表格视图中，我们可以使用批量 fetch 来在表格滚动过帖子时释放图片。然而，这个测试执行得太快，这种方法效果不佳。我需要改变我的方法。我可以不通过获取帖子来验证，而是获取附件。如果我只获取 objectID，托管对象上下文将不会加载任何已获取的对象，直到我要求它这么做。

我可以使用 NSManagedObjectContext 的 objectWithID 方法来在验证过程中按需获取附件。最后，每验证 10 个附件，我就重置上下文，释放所有缓存状态和相关内存。

如果我使用这个修改重新运行测试，我可以看到它会产生一个更可预测、更可调的内存消耗水平。

实际上，验证器使用的内存甚至比 LargeDataGenerator 插入这些对象时还要少。

让我们深入分析一个具体的分配，来了解这个修复是如何工作的。

首先，我选择一段范围的分配来处理。然后，我选择一个特定的大小来检查。我需要启用“已销毁对象”（destroyed objects）来找到这段时间内被释放的对象，然后我可以选择一个具体的分配来检查。

在右侧，Instruments 显示了我的分配堆栈跟踪，但我想知道它是在哪里被释放的，所以我选择了释放事件。我碰巧知道，这个堆栈跟踪意味着 NSManagedObjectContext 正在异步释放持有这个 blob 的对象，从而释放了消耗的内存。

这种技术使我能够为测试建立一个高水位标记，使其能够在内存较少的系统上运行。

通过将测试与 Instruments 结合使用，我能够发现这个特定的测试存在一些不太理想的行为。我做了有针对性的改动来直接解决这些行为，然后验证了结果。此外，系统日志还包含了关于 App 及其依赖的系统服务（如 CloudKit、调度和推送通知）的大量信息。

我将在我的 MacBook Pro 和 iPhone 之间同步一篇帖子。当我在 Mac 上插入一篇新帖子时，给出一个短标题，让它上传到 iCloud，系统日志会捕获一系列事件。

当它同步到我的 iPhone 时，有时甚至会捕获中间状态，系统日志会捕获相应的一系列事件。在 MacBook Pro 上，NSPersistentCloudKitContainer 在 App 进程内部工作，在此例中为 CoreDataCloudKitDemo。当数据被写入持久化存储时，它会向一个名为 DASD 的系统服务询问现在是否是导出这些数据到 CloudKit 的好时机。如果是，DASD 会告诉 NSPersistentCloudKitContainer 运行一个 activity。然后 NSPersistentCloudKitContainer 会与一个名为 cloudd 的进程安排工作，将更改的对象导出到 CloudKit。我们可以使用“控制台”（Console）App 观察来自这些进程的日志。

对于 App 日志，我们只需查找 App 进程 CoreDataCloudKitDemo。这里，我选择了一个显示导出完成的日志。对于调度日志，我们需要查看来自进程 dasd 和 App 特定存储的日志。这里，我选择了 App 私有存储的导出 activity 的开始。让我们更详细地检查这个日志。

NSPersistentCloudKitContainer 与 dasd 创建的 activity 遵循特定格式。activity 标识符由一个特定前缀（NSPersistentCloudKitContainer 使用的）以及该 activity 所属存储的 store identifier 组成。dasd 日志包含有关该服务如何决定一个 activity 是否可以运行的信息。影响 App 执行工作能力的策略将与最终决定一起列在日志中。

最后，进程 cloudd 记录来自 CloudKit 的信息，我喜欢通过我正在使用的容器标识符来筛选这些日志。这里，我选择了与我之前提到的导出相对应的 modify records 操作。

当更改在接收设备上被导入时，还有一个额外的进程需要观察。进程 apsd 负责接收推送通知并将它们转发给 App。

这会导致 NSPersistentCloudKitContainer 启动一系列类似于导出过程的 activity。它向 dasd 请求时间以执行导入，然后与 cloudd 协作，从 CloudKit 获取所有更新的对象并将其导入到本地存储。

当 apsd 为 App 接收到推送通知时，它会记录日志，并且这条日志捕获了许多重要的细节。

日志消息包含这里的容器标识符，以及触发推送通知的订阅名称和区域标识符。这些都由 NSPersistentCloudKitContainer 管理，并且始终以 `com.apple.coredata.cloudkit` 开头。

控制台 App 很棒。但是当我在 Mac 上开发时，我喜欢在“终端”中使用 `log stream` 命令来在与我的 App 并排的窗口中显示这些日志。

我为以下每个谓词打开一个终端窗口或标签页：首先是 App。接下来是来自 cloudd 的日志，这样我可以看到 CloudKit 服务器正在发生什么。然后是 apsd，用于推送通知日志。最后是 dasd，这样我可以看到 NSPersistentCloudKitContainer 代表我调度的 activity 正在发生什么。这些谓词也可以用来指导你在控制台 App 中的查询。

我们使用的设备上有如此多的可用信息。真正的挑战是知道使用什么工具来查找和分析它们。仅凭 Instruments，我们就可以了解到运行时和内存性能等一系列主题。系统日志则捕获了描述 App 所做工作以及系统在幕后为其所做的事情的事件。

我开发周期的最后一个阶段是收集和提供可操作的反馈。在这一部分，我将演示如何从设备收集诊断信息。我们的目标是利用这些信息来生成与特定目标一致且可操作的反馈。这些技术可以帮助你从任何设备收集反馈，无论是你自己的设备还是客户的设备。从设备收集诊断信息有三个步骤。首先，我们需要安装 CloudKit 日志描述文件，它可以启用用于有效识别和分类问题的日志。接下来，我们从受影响的设备收集 sysdiagnose。最后，如果我们能物理访问设备，我们还可以从 Xcode 收集持久化存储文件。要安装日志描述文件，我们只需访问开发者门户网站上的“描述文件和日志”（Profile and Logs）页面。我可以搜索 CloudKit 描述文件，然后点按描述文件链接进行下载。在某些设备上，会出现一个通知来安装描述文件。然而，在 iOS 上，我们需要通过“设置”App 手动安装它。

在“设置”中，我可以导航到并点按“已下载描述文件”（Profile Downloaded）单元格。然后，我点按下载好的描述文件进行安装。按照步骤完成安装。安装描述文件后，可以重新启动设备，它将生效。

设备重启后，我们可以复现想要捕获的行为，然后进行 sysdiagnose。

通过按键组合，一系列特殊的按键，来进行 sysdiagnose。这些在描述文件的说明页面中有描述。我恰好知道，对于 iPhone，我们需要同时按住音量按钮和侧边按钮几秒钟，然后松开。稍等片刻后，即可在“设置”中找到 sysdiagnose。查找它的说明包含在描述文件的说明文件中。

在“设置”中，我导航到“隐私与安全性”（Privacy & Security）、“分析与改进”（Analytics and Improvements），然后选择“分析数据”（Analytics Data），并滚动浏览日志，直到找到 sysdiagnose。

如果我点按这个 sysdiagnose，然后点按“共享”（Share）按钮，我可以选择多种方式共享它。

例如，我倾向于通过 AirDrop 将它们发送到 Mac 进行分析。

最后，如果可能，我可以使用 Xcode 的 Device Organizer 从设备收集存储文件。

我可以从这个 iPhone 收集文件：在已安装 App 列表中点按示例 App，点按展开按钮，选择“下载容器”（Download Container），然后将其保存到我的下载目录。

完成所有这些后，系统日志和存储文件现在都可以用于分析了。我们已经讨论过 `log stream` 命令，但对于 sysdiagnose，我可以使用 `log show` 命令来从 sysdiagnose 打印出日志。这里，我复制了之前讨论的用于 apsd 日志的谓词。

`log show` 命令的最后一个参数是要使用的日志归档。如果未指定，它将显示所运行机器上的系统日志。这里，我指定了 `system_logs.logarchive`，以便它读取我从 sysdiagnose 中获取的日志。例如，我可以指定一个精确的时间范围，来关注我感兴趣的事件发生的时间。

我还可以组合我们之前讨论过的许多谓词，形成一个关于 App 所有相关活动的统一日志。首先是 App 日志，然后是 cloudd 日志、apsd 日志，最后是 dasd 日志。

这个强大的命令可以包含在反馈报告中，或与团队成员共享，以便每个人都能专注于分析特定的日志集。

在这个讲座中，我们讨论了如何通过数据生成器探索 App 行为，如何使用 Instruments 和系统日志分析 App，以及如何为使用 NSPersistentCloudKitContainer 的 App 提供或收集可操作的反馈。

我是 Nick Gillett，很荣幸为你带来这次分享。感谢观看，保持活跃，合上你的活动圆环，祝你 WWDC 愉快。
