---
title: 创建 Swift 包
session_id: 410
collection: wwdc2019
year: 2019
duration: '31:05'
topics: [Swift]
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2019/410/'
content_hash: 'sha256:3b3cb81bc9b92bec'
translated: true
---

# 创建 Swift 包

<sub>WWDC2019 · 31:05 · Swift</sub>

无论你想发布代码与社区分享，还是只是想方便地组织 App 中的代码，Swift……

> [!note] 归档理由
> 创建 Swift 包

## 相关资源

- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/410p24ercmpgj258x/410/410_hd_creating_swift_packages.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/410p24ercmpgj258x/410/410_sd_creating_swift_packages.mp4?dl=1)
- [演示文稿幻灯片（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2019/410p24ercmpgj258x/410/410_creating_swift_packages.pdf?dl=1)
- [创建 Swift 包插件](https://developer.apple.com/videos/play/wwdc2022/110401)
- [使用 Xcode 进行服务端开发](https://developer.apple.com/videos/play/wwdc2022/110360)
- [使用 Collections 发现与策展 Swift 包](https://developer.apple.com/videos/play/wwdc2021/10197)
- [构建可扩展的企业级 App 套件](https://developer.apple.com/videos/play/wwdc2020/10142)
- [把二进制框架作为 Swift 包分发](https://developer.apple.com/videos/play/wwdc2020/10147)
- [Swift 包：资源与本地化](https://developer.apple.com/videos/play/wwdc2020/10169)
- [在 Xcode 中采用 Swift 包](https://developer.apple.com/videos/play/wwdc2019/408)
- [Swift 中的二进制框架](https://developer.apple.com/videos/play/wwdc2019/416)
- [Swift 新变化](https://developer.apple.com/videos/play/wwdc2019/402)
- [了解 Swift Package Manager](https://developer.apple.com/videos/play/wwdc2018/411)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好。我叫 Boris，是 Xcode 团队的成员。欢迎来到 "Creating Swift Packages" 这场会议。你很可能已经听说过 Xcode 对包的支持，但今天你将学习如何创建自己的包。

今天我们主要谈五件事。我们学习如何创建自己的本地包。

我们学习如何发布它。

我们会多讲一点包清单 API。以及如何编辑包。最后，我还会讲一下 Swift Package Manager 开源项目。我们还有另一场关于包的会议。

那场叫 "Adopting Swift Packages"。

你也应该看那场，因为那里有其他相关信息，比如如何解决包解析冲突，以及如果你还没听说过包，它也会讲一些包的基础知识。

包是共享代码的绝佳方式，无论是在你的工作空间与团队内共享，还是与更广泛的开源社区共享。

先来看看如何创建我们自己的本地包。你可以把本地包看作类似于工作空间中的子项目。它们本质上是平台无关的，因此你可以以直接的方式在 Apple 的所有平台上使用你的代码。

它们非常适合把可复用代码重构出去。

它们没有版本，但一旦准备就绪，只需几步就能发布。让我们在第一个演示中看看如何创建自己的本地包。这个演示中，我们将使用一个 App，它显示我工作地点附近几家咖啡馆的午餐菜单。我们有这个 App 的 iOS 版和 watchOS 版。现在我们有一个数据模型，通过 target 成员关系在两者之间共享。随着 App 演进，这实际上变得有点麻烦。所以我想把它重构为一个本地包。要开始，我们选择 File > New > Swift Package。我们把包命名为 "food and stuff"。我们把它添加到现有项目及其根分组中，然后点击 Create。现在，Xcode 为我们创建了包的基本结构，包括 Readme、Package.swift 清单文件、Sources 和 Tests。

我们把数据模型代码从 App 中拖进包里。接下来，我们要把这个代码与 App 链接起来。快速看一下清单文件，它描述了包如何构建，其中有一个 Products 部分，我们在这里定义一个库。这个库可以与 App 链接。我们稍后会在演讲中更详细地讨论清单和 Products 部分。但现在，我们可以进入项目编辑器，打开 iOS App 的 target，进入 Frameworks、Libraries and Embedded Content 部分。这里点击 Plus，然后从列表中选择 "food and stuff" 库产品。

我们要对 watch App 执行同样的步骤。进入那个 target，进入同一部分，再次点击 plus，并把包产品也链接进去。

所以，包也会带来一个或多个 module。因此，我们必须把这些 module 导入 App。这里我们只有一个。进入 iOS App 的代码。

在这里导入 module。

我们对 watch App 也做同样的事。

现在，因为我们对工作空间做了较大改动，预览被暂停了。所以按 Command + Option + P 恢复它。然后我们的 App 就像之前一样工作了。所以只需几步，我们就把可复用代码重构成了自己的本地包。

你可能也注意到了，我们不必显式配置任何平台。这是因为包本质上是平台无关的。因此，它们为客户端需要的任何平台构建。在这个例子中，我们的 scheme 同时包含 iOS 和 watch App。所以包产品会被构建两次，一次针对 iOS，一次针对 watchOS。所有这些都由 Xcode 自动处理。最后，这为发布包提供了良好的第一步。但在我们发布之前，让我们回到幻灯片了解更多内容。

你刚刚了解了本地包。现在来看看如何发布包，以便与更广泛的受众分享。在看发布包的具体步骤之前，我们必须了解版本控制。

更具体地说，是 Swift 包所使用的语义化版本控制。

为了确保你能从依赖项的 bug 修复中受益，而不用频繁折腾，Swift 包遵循语义化版本控制。这是一个广泛的标准，为版本号的每个组成部分赋予特定语义。主版本号表示对 API 的破坏性更改，需要更新现有客户端。例如，重命名现有类型、移除方法或更改方法签名。但这也可能包括任何向后不兼容的 bug 修复或对现有 API 的重大行为更改。

更新次版本号时，功能会以向后兼容的方式添加。例如，添加新方法或类型。当你做向后兼容的 bug 修复时，增加修订版本号。这允许客户端从你的包的 bug 修复中受益，而不会增加维护负担。主版本号为 0 是一个特殊情形，你可以在初始开发期间使用。

对次版本号和修订版本号的更改也可以破坏 API。这简化了 bringup 期间的工作，但一旦人们开始采用你的包，你应该发布 1.0 版本。一旦你发布包一段时间，客户端会期望稳定的 API。你可以使用预发布版本，让客户端在最终发布某版本之前测试 API。

你可以通过在版本规则中添加预发布标识符来选择启用预发布版本。在这个例子中，我在下界使用了 beta 1。

注意，这使你能够解析预发布版本，但你仍然会获得更新。例如，这里我有 beta 6。一旦稳定的 5 版本发布，包解析会自动选择它，但测试完成后你应该移除预发布标识符。让我们在下一个演示中看看发布包的具体步骤。

我们回到第一个演示离开的地方。要开始，我将把包从项目中拖出来。现在，你想在拖放时按住 Option，以便制作副本。关闭项目，在 Finder 中打开这个文件夹，双击 Package.swift 文件。

这会像打开项目一样独立打开这个包。

如果我们查看 Run destinations，我们会看到还有 Mac 和 tvOS，尽管我们之前是为 iOS 和 watch 开发这个包的。

这再次强调了包本质上是平台无关的。在 Xcode 中为 Apple 的所有平台构建它们，不需要特殊配置。

现在，既然你要发布这个包，让我们把 Readme 补充一下。我们可以说这个包提供用于表示食物菜单并从 JSON 加载它的数据模型。对于真正的包，你希望在 Readme 中包含更多信息，比如如何使用、任何平台限制、如果你使用了平台特定 API（如 UIKit），以及许可证信息。但因为这只是演示，这样就够了。

另一件你要做的事是添加测试。Xcode 早些时候为我们创建了一个示例测试用例，但我们要实际测试我们的数据模型。让我们创建一个 food item，叫做 chicken，价格 $42。然后对 item 的价格做断言，它应该恰好是该值。现在，按 Command + U，我们的包会构建，测试会运行，就像在项目中一样。测试通过了，所以我们可以继续。让我们先为包创建一个仓库。为此，我们可以打开源代码管理菜单，选择 Create Repositories 选项。Xcode 已为我们预选了包，所以只需点击 Create。这会在本地创建一个仓库并提交我们当前的状态。

但我们也需要一个 GitHub 上的仓库。我们也可以直接从 Xcode 内部创建。让我们进入 SEM 导航器。在仓库上打开上下文菜单，选择 Create Remote 选项。由于我已在 Xcode 偏好设置中配置了 GitHub 账号，它会自动预选。我们可以更改仓库名，但我们就保持原样，也暂时省略可选的描述。我们把可见性设为 private，因为我想先只与团队共享这个包，而不是面向广泛受众。点击 Create。

Xcode 创建包、在 GitHub 上创建仓库，并把我们当前的状态推送上去，一步完成。现在我们已经发布了包，但还想发布第一个版本。为此，回到这里的上下文菜单，选择 Tag Master 选项。我们要发布 1.0.0 版本，暂时留空消息。这会在本地创建一个 tag，所以我们仍需把它推送到 GitHub。为此，回到源代码管理菜单，选择 Push 选项。勾选包含 tags 的复选框，以便真正推送 tags，然后点击 push。

现在我们在 GitHub 上发布了包，让我们看看它。从上下文菜单选择 View in GitHub 选项，它会直接在那里打开。

所以我们可以在这里结束演示，但作为最后一步，我想把包的远程版本重新集成到我们早先的午餐 App 中。所以我点击 clone or download 按钮并复制这里的 URL。关闭 Safari、Xcode 以及 Finder。

然后回到 Xcode 的欢迎窗口，重新打开 lunch 项目。

这里我们打开文件菜单，以及这个 Swift Packages 子菜单。

这个菜单包含几个用于处理包的选项，但我想添加包依赖。把 URL 粘贴到这里。

Xcode 推荐给我们的默认版本规则包含我们刚发布的 1.0.0 版本。所以可以点击 Next。包被解析了，现在我们看到产品选择。我们要把库产品链接到 iOS App。所以点击 Finish。现在我其实刚才忘做了一件事，就是删除我们早先的本地包。所以现在做，把它移到废纸篓。

现在我们实际上在获取远程版本。让我们看看 Project Navigator 中的 Swift Package Dependency 部分。它显示你所有的包依赖。

所以，因为我们作为 assistant 工作流的一部分链接了产品，它已经链接到 iOS App。但我们还必须把它添加到 watch App。为此，回到 frameworks、libraries and embedded content 阶段。

在这里点击 plus，选择包产品。现在可以回到预览。

恢复它。我们可以看到它像之前一样工作。

所以只需几步，我们就发布了一个包。让我们回到幻灯片。

接下来，我想邀请我的同事 Ankit 上台，向你多讲一点包清单 API。

谢谢，Boris。Boris 向你展示了如何在 Xcode 项目中使用本地包，以及如何发布它以与更广泛的受众分享。在本节中，我们将学习更多用于配置包的包清单 API。Swift 包是一个包含 Package.swift 清单文件的目录。

清单的第一行始终是 Swift tools version。这是构建你的包所需的 Swift 编译器的最低版本。我们稍后会在演讲中了解更多。然后是包描述的 import 语句。这是 Xcode 提供的库，包含清单文件所使用的 API。

最后是包初始化器语句。整个包通过单个包初始化器语句进行配置。在这个例子中，我只有包名，以便它在一个 target。Swift 包有标准的 target 布局。

库 target 位于名为 Sources 的目录下，每个 target 都应该有自己的子目录。它们随后在包初始化器的 Target 部分声明。

标准布局真的很强大，因为你不必在清单中单独列出源文件。你只需把它们放进正确的目录，Xcode 就会自动拾取它们。

如果我想添加另一个 target，我会创建一个新的子目录，然后在清单文件中声明该 target。测试 target 位于名为 Tests 的目录下，也有自己的子目录。它们使用 test target API 声明，由于测试 target 通常测试另一个 target，你需要声明对它所测试 target 的依赖。

这通过 test target API 的 dependencies 参数完成。作为最后一步，我们需要为包声明 product。Product 用于从包中导出 target，以便其他包使用。在这个例子中，我有一个库 product，它导出我的单个库 target。我们刚刚看到了一个基本 Swift 包如何配置。现在让我们看看如何在现有 Xcode 项目中添加对 Swift 包的支持。我有一个名为 Menu Downloader 的项目，之前一直配合其他包管理器使用，比如 CocoPods 和 Carthage。它有一个 Swift target、一些遗留 C 代码、Xcode 项目文件，以及一个供 CocoPods 包管理器使用的 Podspec 文件。要开始，你只需添加 Package.swift 清单文件，现在就可以配置它的 target 了。从遗留 C 代码开始，我们先给它一个名字，然后一个自定义路径。我们必须这么做，因为这个 target 不在标准的 sources 目录下。

我还发现 C 代码中有一个宏，如果定义了，就会下载秘密午餐菜单。所以我使用 C settings API 定义了它。类似地，我们可以配置 Swift target，给它一个自定义路径，然后声明对遗留 C target 的依赖。这个包有两个 product。第一个 product 导出 Swift target，第二个 product 导出我们的 C target。我们单独导出 C target，因为有些用户可能直接使用 C target，那种情况下他们不需要 Swift 桥接。

它还被标记为，因为我知道有些用户会在某个时刻加载这个库。现在让我们看看包依赖如何在包中配置。

包依赖位于名为 Dependencies 的部分，它有两个组成部分——源 URL 和版本要求。

在这个例子中，我使用 uptoNextMajor 版本要求。这意味着我的包需要 yams 的一个版本，从主版本 2 开始，直到下一个主版本，也就是根据语义化版本控制将是 3。

uptoNextMajor 是声明版本要求的推荐方式。

这是因为你可以指定一个最小版本，且通常明确到下一个主版本。它足够灵活，可以避免包图中的潜在冲突。它还有一个简写，就叫 from。

还有其他一些基于版本的要求类型。我们刚看到了 from 和 uptoNextMajor。

有 uptoNextMinor，允许你声明对版本下一个次版本组件的要求。

如果你希望对所接受的更改保守一些，这很有用。

然后是 exact 版本要求。这允许我们把依赖固定到特定版本。除非你真的需要，否则我们不推荐使用，因为它可能导致包图中更多的冲突。

还有一些非基于版本的要求。有基于分支的依赖，如果你正在开发多个包并希望保持它们同步，这很有用。还有基于 revision 的要求，用于把依赖固定到特定 revision。

注意，基于分支和基于 revision 的要求在已发布的包中是不允许的。

在发布包之前，你必须移除所有基于分支和基于 revision 的要求。现在，在选择包依赖之后，我们需要声明对它一个或多个 product 的依赖。在这个例子中，我在 Swift target 中声明对 yams product 的依赖。现在让我们回到 Swift Tools version。

如我之前所提，Swift Tools version 始终是清单的第一行。

就像其他 API 一样，包描述 API 也会随时间演进，你得到的库版本来自 Tools version。

它还参与依赖解析过程。Xcode 确保你所有包依赖的 Tools version 始终与你的包的 Tools version 兼容。最后，它声明构建你的包所需的 Swift 编译器的最低版本。

如果你试图用不兼容的旧版 Xcode 使用你的包，这对产生良好的诊断很有用。正如 Boris 早先提到的，Swift 包始终是平台无关的。

如果你的包支持多个平台，并且你有平台特定代码，我们可以使用 Swift 的条件编译功能。对于平台起始支持可用性，Xcode 为每个平台分配默认的部署目标。你可以在包初始化器的 platforms 部分自定义部署目标。

注意，这并不限制包可以构建的平台。它只针对列出的平台进行自定义。在这个例子中，我为 macOS 自定义到 10.15，为 iOS 自定义到 13。

如果你当前的 Tools version 没有你想要的部署目标 API，你可以使用基于字符串的 API。我们刚经历了很多 API。所有包清单 API 都有文档，你可以在生成的 module interface 中查看文档。

你可以通过在任何清单文件中 Command 点击 package description import 语句，进入生成的 module interface。

这样，回到 Boris 来讲如何编辑 Swift 包。谢谢。

谢谢，Ankit。一旦你发布包一段时间，以便与团队或开源社区共享，你很可能需要在 App 的上下文中处理它。所以，让我们谈谈编辑包。

在早先的演示中，我在原地编辑包。其中一个是作为工作空间一部分构建的本地包。另一个是通过双击 Package.swift 独立打开的。两者始终可编辑。包依赖 however 是锁定编辑的，因为它们由 Xcode 自动管理。如果你看看我们早先的 App，我们对 GitHub 上的 "food and stuff" 包的依赖。如果我们现在把包单独 checkout 并作为本地包添加到项目，它会在不移除的情况下覆盖现有依赖。

覆盖基于最后一个路径组件。所以由于两者相同，本地的那个会覆盖远程依赖。由于本地包始终可编辑，你可以以这种方式同时编辑 App 和包。让我们在演示中看看编辑包。我们再次回到早先演示离开的地方。

如果你记得，有一个 Swift Package Dependency 部分，显示了我们添加的包依赖。

既然我们之前已经单独 checkout 了包，就可以直接把它拖进项目。现在 Swift Package Dependency 部分消失了，因为我们不再使用远程依赖，而是在使用本地的。

所以，我们的用户要求午餐 App 有一个新功能。他们想看到哪些菜可以吃。所以我们要明确标记哪些菜是素食的。幸运的是，我们的数据模型已经包含该信息。

不是我们的数据模型，是我们的底层数据。我们必须更改数据模型，真正暴露出来。让我们进入包。

打开 food item 类型。

我在这里添加一个名为 vegetarian 的新属性，类型为 Bool。复制这部分。把它作为参数添加到初始化器。最后我们把属性设置为初始化器参数。现在我们有了数据模型中关于是否素食的信息。让我们在 UI 中添加一些东西，向用户指示这一点。

进入 iOS App 的代码。让我们隐藏项目导航器，以便有更多空间，并恢复预览，以便我们看到正在处理的内容。我们可以使用 jump bar 跳转到 food item row view 类型。如果我们进入编辑器中的 UI 代码，我们看到高亮显示，这代表每个 table view cell。所以我准备了一段 snippet 来计算一个 label，它使用 food item 的名字，但添加一个表示菜品是否素食的 emoji。我们可以进入文本字段，在这里使用这个 label。让我们恢复预览。然后我们可以看到，现在每道菜都清楚地标记了是否素食。通过这些步骤，你可以同时编辑你的 App 和包。让我们回到幻灯片。

这种覆盖行为也可以用来编辑你不拥有的包，如果你需要修复 bug 或在你的问题中做小改动。

为了总结，让我们看看 Swift Package Manager 的开源项目，我们将其缩写为 Swift PM。Swift PM 已经出来几年了，Xcode 对 Swift 包的支持是构建在它之上的。Swift 是一门跨平台语言，Swift PM 是用于 Swift 包的跨平台构建系统。使用它，你可以在客户端和服务器端 App 之间共享代码。Swift PM 由四个命令行工具组成，位于顶层 swift 命令下。有 swift build，用于构建包。swift run，用于运行可执行 product。swift test，用于运行测试。最后是 swift package，用于对包执行各种非构建操作。这些命令行工具可用于为 macOS 和 Linux 构建包。

要了解更多关于 Swift PM 命令行工具以及其演进的未来想法，你可以查看 WWDC 2018 的会议 "Getting to Know Swift Package Manager"。

当然，你也可以使用 Xcode Build 在命令行或 CI 上构建包。这也是在命令行上为 iOS、watchOS 和 tvOS 构建包的一种方式。Xcode 中的 Swift 包支持是构建在 libSwiftPM 库之上的，它是开源项目的一部分。

libSwiftPM 可用于支持 Swift 包和其他开发者工具的 IDE。我们很高兴与社区合作，朝着稳定的 API 前进。一个例子是 SourceKit-LSP，它是 Swift 和基于 C 的语言的语言服务器协议（LSP）实现。LSP 定义了编辑器或 IDE 与提供语言功能（如自动补全、跳转到定义或查找引用）的语言服务器之间使用的协议。使用 SourceKit-LSP，支持语言服务器协议的 IDE 或编辑器为 Swift 包获得这些功能。这是构建在开源 libSwiftPM 之上的。Swift Package Manager 是更大的 Swift 开源项目的一部分。Swift.org 网站是了解社区和流程的好地方。

包管理器遵循 Swift 演进流程，就像 Swift 项目的其余部分一样。任何人都可以开发并最终提交功能或重大更改。

在你花时间起草提案之前，先去论坛的包管理器部分，开始对话，找到有有用想法或反馈的人。Swift 包目前只支持源代码和单元测试。

我们期待与社区合作，添加对资源的支持，如图像、文本文件或其他数据文件。我们已经有了包资源的草稿提案。你可以跟随这个流程，并影响这个功能会是什么样子。

在 Swift.org 上，我们还有定期更新的 toolchain，以便你可以自己尝试最新更改。

开源项目的更改也将成为未来 Xcode 版本的一部分。作为最后的要点，包现在在 Apple 平台上得到支持，Xcode 也是。

在你的项目中寻找可复用代码，把它重构为 Swift 包。我们对扩展中的 Swift 包生态系统感到兴奋。如果你对采用或创建包还有任何问题，我们有两个即将举行的 lab。一个是今天 12 点，另一个是明天同一时间。非常感谢大家的到来，祝大家本周愉快。

[ Applause ]
