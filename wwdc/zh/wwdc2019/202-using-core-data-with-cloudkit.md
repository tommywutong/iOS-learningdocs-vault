---
title: 将 Core Data 与 CloudKit 配合使用
session_id: 202
collection: wwdc2019
year: 2019
duration: '31:49'
topics: ['SwiftUI & UI Frameworks', System Services]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2019/202/'
content_hash: 'sha256:cb3ef56700c77644'
translated: true
---

# 将 Core Data 与 CloudKit 配合使用

<sub>WWDC2019 · 31:49 · SwiftUI & UI Frameworks、System Services</sub>

CloudKit 提供强大的云端同步技术，而 Core Data 则提供全面的数据建模和持久化 API。了解如何…

> [!note] 归档理由
> Core Data 与 CloudKit 集成

## 相关资源

- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/202mm1h4jl4wiz1h3/202/202_hd_using_core_data_with_cloudkit.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/202mm1h4jl4wiz1h3/202/202_sd_using_core_data_with_cloudkit.mp4?dl=1)
- [演讲幻灯片（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2019/202mm1h4jl4wiz1h3/202/202_using_core_data_with_cloudkit.pdf?dl=1)
- [优化 Core Data 和 CloudKit 的使用](https://developer.apple.com/videos/play/wwdc2022/10119)
- [将 Core Data 存储与 CloudKit 公共数据库同步](https://developer.apple.com/videos/play/wwdc2020/10650)
- [使用 Core Data 构建 App](https://developer.apple.com/videos/play/wwdc2019/230)
- [优化 App 中的存储](https://developer.apple.com/videos/play/wwdc2019/419)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

早上好。我叫 Nick Gillett，是 Apple 公司 Core Data 团队的一名工程师。非常荣幸欢迎大家来参加《将 Core Data 与 CloudKit 配合使用》这场讲座。

今天，我们来谈谈我持有的一种信念：我所有的数据，无论我在世界上的哪个角落，使用哪台设备，都应该触手可及。为了将这一愿景变为现实，我们必须让开发者能更轻松地为自己的 App 添加这一功能。

我相信今天在座的许多人都是带着 iPhone 来的，家里可能还有一台 Mac。甚至，你们中的一些人可能还在背包里随身携带着 MacBook 或 MacBook Pro 来参加会议。我们在所有这些设备上产生的数据，天然就被困在其中了，对吗？如果没有某种形式的用户交互，就没有简单的方法将数据从一台设备移到另一台设备。为了解决这个问题，我们通常倾向于求助于云存储。因为它承诺，可以无缝且透明地将一台设备上的数据转移到我们所拥有的所有其他设备上。即使我们只有一台设备，云存储也有其好处，对吧？当我们的 App 在这台设备上产生数据时，数据可以备份到云端并存储起来。这样，当我们得到一台新设备时——无论是出于自愿还是意外——问我怎么知道的——在离开商店的路上，那台设备就可以恢复成我们一直熟悉和喜爱的样子。

了解到我们平台上有一些现有技术可以帮助我们解决这个问题，你可能会感到惊讶。例如，Core Data 提供了一套强大的 API，用于在 App 内部和磁盘上本地管理数据。而 CloudKit 框架提供了访问世界上最大的分布式数据库之一的途径。这两个框架都可以在我们所有的 Apple 平台上使用。正因为如此，它们使我们能够构建各种各样的 App。

事实上，这些框架实际上非常相似。它们甚至使用一套共同的模式和范式来表达自己。用对象、模型和存储的方式来构建它们的 API。

在 Core Data 中，我们称这些对象为 NSManagedObject 的实例，它们使我们的 App 能够访问存储在磁盘上的值。

CloudKit 同样暴露了一个 CKRecord，它就像一个键值存储，用于访问你存储在云端的数据。

这些对象由我们称之为模型（Model）的东西来描述。在 Core Data 中，我们称之为 NSManagedObjectModel，你可以通过代码或使用 Xcode 中的模型编辑器来创建它。

非常相似的是，CloudKit 使用一个 Schema（模式）。CloudKit 的模式可以在开发环境中通过在代码中使用 CKRecords 来动态定义，也可以使用 CloudKit 仪表盘来定义。

最后，对象会持久化到——用 Core Data 的术语来说——我们称之为存储（Store）的地方。在 Core Data 中，这些是 NSPersistentStore 的实例。但在 CloudKit 中，CKRecord 存储在 CKRecordZone 或 CKDatabase 中。

因此，正如你所看到的——事实上，多年来你们中的许多人也都向我指出过——如果能够更轻松地将这两个概念上相似的框架结合起来，那就太好了。为了向你们展示我们今年在这方面取得的巨大进步，我想带你们体验一下在 Xcode 中创建一个全新 App 的过程。这里大家可以看到，我打开了一个 Xcode 窗口。我将创建一个新的 iOS 项目，选择 Master-Detail 应用程序。我喜欢 Master-Detail 应用程序，因为它在探索 Core Data 功能时为我们提供了一个很好的用户界面来构建功能。所以，我选中它，然后点击“Next”。

然后给我的 App 取个名字。这里就叫 WWDC Demo。因为今天我们是来了解 Core Data 的，所以我勾选“Core Data”复选框。Xcode 11 新增了这个名为“Use CloudKit”的复选框。这告诉 Xcode，我们要生成一个旨在同时使用 Core Data 和 CloudKit 的 App。那么，我们勾选它，然后点击“Next”并在文件系统中为我们的 App 选择一个存放位置。

点击“Create”后，Xcode 会为我们生成 App。如果你曾经开发过 CloudKit 应用程序，你就会知道，在构建和运行之前，我们还需要为此添加一些额外的配置。它们以功能（Capabilities）的形式出现，我们通过“Signing & Capabilities”标签页来添加。我们需要添加两项。第一项是 iCloud 功能。所以我点击功能旁边的加号（+），输入 iCloud，然后按回车来添加它。

当我这样做时，我可以勾选 CloudKit 复选框，你会看到这也为我添加了推送通知。Xcode 还自动为我的 App 创建了一个 iCloud 容器标识符。接下来，我们要添加一个后台模式（Background Mode）功能。为此，我再次点击加号（+），输入 Background，然后按回车。我们这样做的原因是为了启用远程通知（Remote Notifications），这允许我们的 App 在未运行时也能接收推送通知。

那么，让我们运行这个 App，看看 Xcode 为我们创建了什么。

这里你可以看到，我们有一个非常简单的 App，包含两个视图控制器（view controller）。左边是一个表格视图（table view），右边是一个详情视图控制器。

我可以使用右上角的加号（+）按钮向这个 App 添加一些数据。默认情况下，Xcode 会为我们生成一个非常简单的 Core Data 数据模型，它只是一个简单的时间戳。

但是，我们今天是来了解如何添加同步功能的。为此，我们需要另一台设备。所以，让我们在 iPhone 上运行这个 App。你可以看到我们有主视图控制器，以及我们在 iPad 上添加的所有数据。现在让我们用手机添加一些数据。然后，观看它同步回 iPad。因为我在控制器里设置了一个神奇的推送通知，所以我可以随时触发同步。

但让我们看一些更真实的情况。我将从这个 App 中删除我在 iPad 上从 iPhone 添加的所有数据。就是最上面的四行。然后，我在 iPhone 上做同样的事情，删除从 iPad 添加的所有数据。

之前，我使用了神奇的推送通知。但我不再碰那个控制器了。就让视频继续播放，这样你们就能看到我在拍摄时，这两个设备真正收敛同步的过程。

对吧？尽管这可能有点人为设计，但仅需简单的几次点击，我们就构建了一个使用 Core Data 和 CloudKit 进行端到端同步的 App，这真是太棒了。如果我在应用程序委托（application delegate）的某个地方隐藏了 15000 行代码，那我对你们来说就是一种不负责任了。那么，让我们看看它实际是什么样子。

这是一个相当标准的应用程序委托。事实上，如果你以前使用 Xcode 构建过 Core Data 应用程序，你会觉得它非常眼熟，包括设置 Core Data 栈（stack）的这个地方。这个 App 唯一的不同之处在于，今年 Core Data 中引入了一些新的 API，叫做 NSPersistentCloudKitContainer，旨在帮助你管理由 CloudKit 数据库支持的 Core Data 存储。

如果你以前使用 Xcode 构建过 Core Data 应用程序，你会在这里看到的是 NSPersistentContainer，它是 NSPersistentCloudKitContainer 的超类（superclass）。正因为如此，你只需更改一行代码，就可以将 CloudKit 功能添加到现有的 Core Data 应用程序中。NSPersistentCloudKitContainer 到底是什么？它是我们看到的，每个人在想要使用 CloudKit 实现端到端同步时都必须构建的一组非常常见的模式的封装。它旨在为你节省数千行代码。

它也是一个基础，我们希望未来几年能与你一起在这个基础上迭代改进。当然，要做到这一点——准备好了，我要说了——我们需要你的帮助。

我们需要关于 NSPersistentCloudKitContainer 对你的效果如何、它缺少哪些功能，或者它现有的功能是否足以满足你的 App 需求的反馈。那么，让我们详细看看其中的一些功能。

NSPersistentCloudKitContainer 为你的 App 提供了一个本地副本（Local Replica）。可以说是底层 CloudKit 数据库的一个完整镜像。

同时，它还实现了一个健壮的调度和错误恢复事件循环，这样你的 App 就不必担心任何操作了。最后，它处理了我之前提到的 NSManagedObject 实例和 CKRecord 之间的转换。

现在，本地副本之所以重要，有很多原因。

但这意味着，当你的 App 处理对象时，它会将这些对象写入由 Core Data 管理的本地存储文件。同时，也会从该文件中读取它们。这是因为本地数据库和云存储的性能特征存在差异，对吧？当我们考虑访问本地文件的延迟时，最坏情况下，从磁盘上的文件读取只需要毫秒级的时间。而通过网络获取 App 所需的数据，则可能需要几秒甚至几分钟。同样，本地存储文件可以为你的 App 提供高得多的带宽，即使在我们的 iPhone 设备上，测量值也达到了每秒千兆字节；而云端的可用带宽有时则限制在每秒兆字节甚至千字节。

这种本地副本必然会增加显著的复杂性，这就是为什么 NSPersistentCloudKitContainer 为你实现了一个健壮的调度和错误恢复事件循环。这样，当你的 App 向本地存储写入数据时，NSPersistentCloudKitContainer 会自动将这些对象上传到云端。

并且，当 CloudKit 中发生任何变化时，NSPersistentCloudKitContainer 会安排在系统上执行任务，将这些变化下载下来并导入到你的本地数据库中，使它们对你的 App 可用。

当然，在这个过程中，NSPersistentCloudKitContainer 必须将你的对象从 NSManagedObject 实例转换为 CKRecord 实例。

同样，当云端发生任何变化时，这些 CKRecord 将以 NSManagedObject 实例的形式，在你的本地存储文件中对你可用。

这就是 NSPersistentCloudKitContainer 为你的 App 带来的功能。它是 CloudKit 中私有数据库（Private Database）内所有内容的完整本地副本。不过，你应该知道，我们确实为 Core Data 同步管理一个特定的自定义区域（Custom Zone）。我们实现了自动调度，这样你就不必担心优化任何操作或在系统中调度它们了。而且，我认为更重要的是，你不必在你的 App 中实现任何错误恢复逻辑。

最后，我们实现了从 NSManagedObject 到 CKRecord 的自动序列化（serialization）。我们利用你的 NSManagedObject 模型来弄清楚如何做到这一点。

但是，如果我站在这里告诉你们，一旦采用了 NSPersistentCloudKitContainer，就万事大吉了，你就拥有了一个功能完善的 App，那未免太迟钝了。所以，我想用讲座的剩余部分来思考一下，基于 NSPersistentCloudKitContainer 进行构建对你来说意味着什么。我认为，首先要构建由 Core Data 驱动的优秀 App。

稍后，我们还会看看如何扩展我们在 NSPersistentCloudKitContainer 中构建的基础，以根据你的需求进行定制。

对我来说，使用 Core Data 构建出色的 App 首先要吸收大量的知识。为此，我们今年编写了大量的文档，介绍了 NSPersistentCloudKitContainer 的工作原理以及如何将其集成到你的 App 中。

我觉得 Core Data 的一些功能与 NSPersistentCloudKitContainer 非常契合。比如 FetchResultsController，它能帮助你构建由大量数据支持的可扩展用户界面。

还有查询生成（query generations），它可以帮助你稳定用户界面，使其不受后台可能发生的更改的影响。

比如来自 NSPersistentCloudKitContainer 的更改。

最后，还有历史追踪（History Tracking），这是我们几年前引入的，用于帮助你了解数据库中发生了什么变化。配合 NSPersistentCloudKitContainer，你可以用它来决定这些后台更新是否与用户当前正在进行的操作相关。

我们将在周四下午 3 点的讲座中详细介绍这些内容以及更多其他功能。与此同时，我们今年还推出了一个新的示例 App，旨在让你能亲手体验 NSPersistentCloudKitContainer 以及 Core Data 所有这些其他功能是如何工作的。它旨在管理一组帖子（Post）。帖子是过去几年我们在 Core Data 中一直构建的一个主题。

对吧？它们是非常好的对象，能帮助我们理解对象图的不同部分将如何受到 CloudKit 的影响。这里你可以看到，我们的数据模型非常简单。我们有一个标题和一些内容。然后，我们有一组可以关联到每个帖子的标签。这个 App 甚至让你体验如何使用 CloudKit 管理照片。允许你从设备的相册（Photo Library）中附加文件到帖子。现在，让我们谈谈基于 NSPersistentCloudKitContainer 进行构建是什么样的体验。你可能已经猜到，这将是本次讲座中相当密集的部分。但你应该知道，我们的文档更详细地涵盖了今天我们即将讨论的许多内容。所以，即使有些内容你一时没跟上，也不用担心。我们发现，内部客户有多种方式来扩展 NSPersistentCloudKitContainer，首先就是处理多个存储。

同时，我们也看到客户喜欢自定义他们一直与 CloudKit 配合使用的模式（schema），实际上，也就是我们与 NSPersistentCloudKitContainer 一起使用的那个模式。你可能知道，这是因为 CloudKit 可以在许多不同的平台上使用，不仅限于 Apple 平台，还可以通过 Web Services 或 JavaScript 来使用。因此，即使你不在我们的某个平台上工作，也应该能够处理 NSPersistentCloudKitContainer 的对象。

最后，我们将讨论面向协作的数据建模。

现在，有很多很好的理由可以说明为什么我们可能需要在 App 中使用多个存储。特别是在处理网络支持的存储时。

多个存储可以帮助我们在 App 中不同的用例之间分离数据。并且，它们可以帮助我们提供不同类型的约束。

对吧？所以，如果我们想要有一个存储文件来管理一组非常特定的验证约束，比如验证用户输入，我们可以为此使用一个单独的存储。

多个存储也是节流或合并（coalesce）设备上频繁写入的数据的好方法。

当你从设备上读取某些由设备本身或你拥有的某个算法生成的数据时，就可能发生这种情况。如果这个算法以非常高的速率生成数据，那么持续将所有数据同步到 CloudKit 可能会非常昂贵。因此，我们看到客户会插入另一个存储文件到组合中，并用它来合并这些数据，直到数据准备好被分析，然后再稍后上传到 CloudKit。

为了展示这是如何工作的，以及 Core Data 如何让你轻松实现这一点，我们将利用 NSManagedObjectModel 的一个名为配置（Configuration）的功能。这里你可以看到我们的示例 App 的 NSManagedObjectModel 在 Xcode 的模型编辑器中。现在，假设我想为帖子添加位置信息。我想记录帖子创建时的位置。但是，系统可能以很高的频率生成位置数据，而只有在帖子实际在那个位置创建时，我才需要它们。所以，让我们把它们从数据模型的其余部分中分离出来。

我将通过点击左下角的加号（+）添加一个新实体来存储我的位置信息。现在，我的位置信息将非常简单。它只包括经度和纬度，两者都是双精度浮点数，由 Core Location 框架暴露给我。当然，你的位置信息可能还包括海拔或精度等其他内容。

现在，我们想将这些位置数据与其余数据分离开。为此，我将创建一个新的配置，再次点击加号（+）按钮，但这次按住点击以显示一个菜单，允许我添加一个配置。

我将这个配置命名为 Cloud，并添加所有四个我实际想要同步的实体。

这里你可以看到，现在 Cloud 配置只包含了我想与 CloudKit 同步的实体。让我们创建一个新的名为 Local 的配置，用于存储我们的位置对象。

只需几行代码，我们就可以让它为我们工作，使 Core Data 能够自动告诉我们的存储它存储了哪些类型的对象。在上面，你可以看到我们创建了一个 NSPersistentCloudKitContainer 实例，然后利用了一个叫做 NSPersistentStoreDescription 的东西，它告诉 NSPersistentCloudKitContainer 关于它正在管理的存储类型的信息。

我们创建一个指向名为 local.sqlite 的文件的 NSPersistentStoreDescription 实例，用于存储我们的位置信息。然后，我们给它分配刚刚创建的 local 配置。

接着，我们设置云存储。类似地，我们创建一个 NSPersistentStoreDescription 实例，并将其指向另一个不同的文件：cloud.sqlite。然后，我们给它分配 Cloud 配置，这告诉 NSPersistentCloudKitContainer，只有像 post、tags、attachments 和 image data 这样的实体才应该存储在这个存储中。

最后，我们给它分配一个 NSPersistentCloudKitContainerOptions 实例，该实例告诉 NSPersistentCloudKitContainer 这个存储应该与哪个 iCloud 容器标识符同步。最后但同样重要的是，我们将这两个存储描述（store description）分配给 NSPersistentCloudKitContainer 的 PersistentStoreDescriptions 属性。

有了 NSPersistentCloudKitContainer，我们甚至可以做得更多。

我们已经有了本地存储和云存储。但是，如果我们想在我们碰巧开发的多个 App 之间共享 CloudKit 中的某些数据呢？嗯，NSPersistentCloudKitContainer 也支持这一点。实际上，因为你使用的是 Core Data，你的 App 将能够轻松地同时处理来自这些存储的所有数据。而且，Core Data 会自动帮助你，将你插入的数据写入到正确的存储文件中。

我们只需添加三行代码就能做到这一点。对吧？我们创建一个指向共享存储文件的新 StoreDescription，并给它一个我们可能创建的新配置，叫做 shared。

最后，我们给它分配一个新的 NSPersistentCloudKitContainerOptions 实例，用于标识我们希望共享数据存储在哪个容器中；在这个例子中，是 iCloud.com.wwdc.shared。当然，最后也是最重要的是，我们将其分配给 PersistentStoreDescriptions。现在，让我们谈谈模式（Schema）。

我想涵盖关于模式的几个要点，我认为这些是重点。当你查看我们在 CloudKit 中创建的记录时，需要知道的最重要的事情。

我将首先讨论我们如何管理记录类型（Record Type），以及如何管理你在 NSManagedObjectModel 中创建的实体（Entity）。

然后，我们将看看我们如何实现一个名为资产外部化（Asset Externalization）的功能，它允许你使用 NSPersistentCloudKitContainer 在 CloudKit 中无缝存储任意大的值。最后，我们将讨论我们如何管理关系（Relationship），以及这与你可能习惯的 CloudKit 体验有何不同。

为此，我们将使用我们示例 App 的 ManagedObjectModel。我将首先关注帖子实体。你可以看到它有两个特性：一个标题字符串和一个内容字符串。它还有两个关系到附件（Attachment）和标签（Tag）实体。

Core Data 为你生成一个实际的类，作为 NSManagedObject 的子类供你在代码中使用，看起来像这样。你可以看到所有特性和关系都在这个类上有所体现。这是在 CloudKit 中与这个帖子一起生成的记录。

这些是我用来填充这个记录并使其成为我们所谓的完全具体化（Fully Materialized）的一些示例值。

现在，我想先向你强调一些事情。记录 ID（Record ID）。Core Data 拥有它在 CloudKit 中创建的所有对象的记录 ID。对于每个对象，我们将生成一个简单的 UUID 作为其记录名称（Record Name）。当记录名称与区域标识符结合时，你就会得到一个 CKRecord ID。在底部，你会看到 Core Data 如何管理类型信息。这里有两件有趣的事情。第一，这些 CD 下划线（CD_）到底是什么？这是 Core Data 将其管理的内容与 CloudKit 为你实现的内容——你不会相信有多少人会在他们的 CKRecord 中添加修改日期——或者你自己可能添加的内容区分开来的方式。因此，我们为所有内容添加前缀；记录类型和我们所有的字段名都以 CD_ 开头。

但是，在 CD_entityName 字段中，我们保留了与此记录对应的对象的实际实体名称。

我们这样做是为了实现一个称为实体继承（EntityInheritance）的功能，例如，你可以有帖子的子类。也许是一个图片帖子，或一个视频帖子。实际的实体将始终由 CD_entityName 字段标识。

我们这样做是为了让你能够通过查询单个记录类型，来实现 CK 查询，以获取你感兴趣的所有实体层级结构。

现在，让我们看看我们如何实现这两个字符串。因为它们是可变长度字段，我们将其转换为 CloudKit 的方式有一些有趣的特性。

你会看到我们将它们扩展成了总共四个字段。这样做的原因，正是我们如何实现资产外部化（Asset Externalization）的。

这里你可以看到，我们同时有一个 CD_content 字段和一个 CD_content_CKAsset 字段。这允许我们存储任意大的字符串。范围从简单的千字节一直到数百兆字节甚至千兆字节的长度。

当我说这个记录是我们所谓的完全具体化时，我的意思是，你永远不会同时看到所有这四个字段。如果字符串都非常短，那么你只会看到记录中的 CD_content 和 CD_title。但是，如果其中一个变得非常大，大约超过 750 KB，或者记录的总大小超过了 CloudKit 最大的 1 MB 限制，你就会开始看到替代出现的资产字段，或者在这种情况下，记录中的 CD_content_CKAsset。

如果你自行消费我们的记录，那么你需要检查这两个位置，以查看某个特定特性是否已经设置了值。

现在，让我们看看帖子上的关系。你可以看到，在 Core Data 为你生成的供你在代码中使用的对象中，它们都是 NSSet 的实例。这是因为一个帖子具有——我们称之为多重关系。这意味着一个帖子可以关联多个附件，或者它可能关联多个标签。附件关系是我们称之为多对一（Many-To-One）的关系，因为一个附件只能分配给一个帖子。

当我们为此生成代码时，你会看到帖子上有一个 NSSet，但在附件（Attachment）的 ManagedObject 上只声明了一个单一的 post 对象。

这是它们为一个附件生成的记录。你可以看到它有一个 UUID、一个实体名和一个记录类型，就像帖子一样，但你还会看到一个额外的字段叫做 CD_post。这是我们存储一对一（Two-One）关系的方式。

相关记录在 CloudKit 中的 UUID 将始终存储在与它链接的对象上。你可能想知道我们为什么不用 CKReference 来实现这一点。那是因为 CKReference 有一些局限性，我们认为它不适合 Core Data 的客户端。即，它最多只能处理 750 个对象。但是通过这种方式存储关系，只要你的 CloudKit 容器能容纳，你可以持有任意多的关系。现在，让我们看看多对多（Many-To-Many）关系。在这个例子中，是帖子与其标签之间的关系。

你可以看到这个对象上有两个 NSSet，这是因为两个对象都可以与许多另一个类型的对象关联。但是，当我们为这些对象生成记录时，没有任何字段是专门用来持有这种关系的。

相反，Core Data 会实例化一个自定义的连接记录（Join Record）。如果你熟悉关系型数据库，你会认出这个概念。它基本上是连接表（Join Table）中一行的外推。它被称为 CDMR，即 Core Data 镜像关系（Core Data Mirrored Relationship）。

一个 CDMR 包含一组有序对（twoples），旨在描述两个被链接的对象，首先是两个被链接对象的实体名称，以及它们的记录名称。正如我之前所说，这不是记录 ID。这是记录名称，你必须将其与区域标识符结合，才能获得被 CDMR 链接的记录的标识。最后，我们还封装了用于建立此链接的精确关系。

那么，为什么我要花这么多时间谈论关系呢？因为它们对我们如何为协作建模数据有着巨大的影响。我需要在这里非常明确地指出，协作不是冲突解决。冲突解决是由 NSPersistentCloudKitContainer 使用最后写入者胜出（Last Writer Wins）的合并策略自动实现的。

我们这样做的原因是，冲突解决的工作是保持对象图和 CloudKit 中的数据与你建模数据的方式保持一致。

但是，多年来我们听到，这有时会让人感到沮丧。那么，让我们看看如何实现更好的合并行为，并通过使用关系来使该合并行为与你的特定客户用例保持一致。

为此，我们将再次使用我们的帖子 App。我将创建一个帖子，但不给它分配任何内容。

我让它同步到另一台设备，比方说，然后我同时在每台设备上进行一些编辑。这通常是我们所说的冲突。但实际上，这是一个很好的例子，说明了两台设备尝试协作编辑一个值的情况。

现在，NSPersistentCloudKitContainer 发现后台的 CloudKit 中发生了一些变化，它会通过解决冲突来保留两个值中的一个。对吧？使用最后写入者胜出的合并策略。这意味着我们最终得到的结果要么是“协作很棒”，要么是“大家都该这么做”。确实如此。

当然，你可能会想——这有点蠢。Core Data，你为什么不能直接把两个字符串拼接起来呢？我们是可以这样做。但如果你这些年听从了我们的建议，实现了增量保存，你最终可能会得到像这样的结果，而这完全不是任何人期望的。它甚至不是英语。

那么，我们如何能做得更好呢？对吧？显然，这对我们来说非常重要，对我们的客户来说也至关重要。

那么，让我们看看我们的帖子实体，看看是否有一些改动可以让情况变得更好。首先要做的是停止在平面值（Flat Values）上制造冲突。内容只是一个平面字符串，仅仅从观察它，我们无法推断出你想要的合并行为。

但是，如果我们把它分解成一个关系，多个设备就可以各自为内容字段做出贡献。由于我们存储一对一关系的方式，许多设备可以同时贡献这些对象，而不会在帖子对象本身上产生冲突。

所以，这里我将其分解成一个非常简单的帖子内容（Post Content）实体，它带有一个简单的字符串。

现在，由于我们存储一对一关系的方式，这些设备会自行合并它们。对吧？我们需要遍历它们来组装最终的值。我们称之为最终一致性（Eventual Consistency）。当两台设备都贡献帖子内容对象时，它们会从另一台设备下载帖子内容对象，并将它们拼接起来或合并起来，或者使用你想应用于此问题的任何拓扑结构来组装最终的值。

但我们希望在所有设备上最终值都相同，而下载顺序的差异可能会导致不同的最终值。因此，我们可以用像日期这样简单的东西来给它们排序。通过这种方式，设备可以在使用 Core Data 中简单的排序描述符（Sort Descriptor）进行拼接之前，先对帖子内容对象进行排序，从而在所有设备上获得一致的排序和合并行为。

但是，我有点分布式系统迷，而时间是个魔鬼。

事实上，即使设备都在你家，它们对时间的感知也可能不一致。

因此，我们可以更进一步，通过利用与父贡献（Parent Contribution）的关系，并向实体提供一些关于实际进行贡献的设备的信息，来实现一个完整的因果树（Causal Tree）。

通过这种方式，我们粗略地勾勒出了一种叫做无冲突复制数据类型（Conflict-Free Replicated Data Type）的东西。这是计算机科学中一个令人兴奋的新兴领域，它允许我们部署算法来在不同的用户-用户场景中创建一致的合并行为。以上就是《将 Core Data 与 CloudKit 配合使用》的全部内容。我很荣幸能向你们展示 NSPersistentCloudKitContainer，以及如何用它轻松地在你的 App 中实现同步功能。

我们今年还为你准备了一些很棒的新示例代码和文档，我希望它们能让你在使用所有这些新 API 时获得出色的体验。最后，我迫不及待地想看到你们用 NSPersistentCloudKitContainer 构建出什么样的作品，以及你们会如何扩展它。今年我们会参加许多实验室活动。

本周每天都会在。正如你所知，我们在周四下午 3 点有一场讲座，涵盖 Core Data 中更多的功能。

非常感谢大家，希望你们能拥有一个精彩的 WWDC。[掌声]
