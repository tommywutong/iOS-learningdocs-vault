---
title: '在 Xcode 中采用 Swift 软件包'
session_id: 408
collection: wwdc2019
year: 2019
duration: '33:24'
topics: [Developer Tools, Swift]
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2019/408/'
content_hash: 'sha256:45f71b2f4320516b'
translated: true
---

# 在 Xcode 中采用 Swift 软件包

<sub>WWDC2019 · 33:24 · Developer Tools、Swift</sub>

Swift 软件包是组织和共享代码的绝佳方式，现在在 Xcode 11 中构建所有 Apple 平台的 App 时都已支持……

> [!note] 归档理由
> Xcode 中采用 SwiftPM

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/408bmshwds7eoqow1ud/408/408_hd_adopting_swift_packages_in_xcode.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/408bmshwds7eoqow1ud/408/408_sd_adopting_swift_packages_in_xcode.mp4?dl=1)
- [演示文稿（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2019/408bmshwds7eoqow1ud/408/408_adopting_swift_packages_in_xcode.pdf?dl=1)
- [认识 Swift Package 插件](https://developer.apple.com/videos/play/wwdc2022/110359)
- [使用集合发现和管理 Swift 软件包](https://developer.apple.com/videos/play/wwdc2021/10197)
- [Swift 软件包：资源与本地化](https://developer.apple.com/videos/play/wwdc2020/10169)
- [Swift 中的二进制框架](https://developer.apple.com/videos/play/wwdc2019/416)
- [创建 Swift 软件包](https://developer.apple.com/videos/play/wwdc2019/410)
- [Xcode 入门](https://developer.apple.com/videos/play/wwdc2019/404)
- [Swift 新功能](https://developer.apple.com/videos/play/wwdc2019/402)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

下午好。我叫 Anders，我在 Xcode 工作。

在这场讲座中，我与同事 Balraj 将讨论如何在 Xcode 项目中使用 Swift 软件包。

Swift Package Manager 是开源 Swift 工具链的一部分。它在 Swift 3 中引入。从那时起，已经创建了许多 Swift 软件包。

此外，许多为其他软件包管理器编写的开源库也被适配为与 Swift Package Manager 兼容。Swift 软件包让你管理依赖项的版本，确保在你所依赖的软件包更新时获得错误修复，而不会让代码遭受源代码层面的破坏性更改。

Swift 软件包也是在你自己的 App 之间共享代码的绝佳方式，无论是在小团队、大型组织内，还是只是你自己正在开发的 App 之间。

而现在在 Xcode 11 中，你可以直接从 Xcode 项目访问 Swift 软件包。

我们也很兴奋。

所以在这场讲座中，我们将先谈谈如何使用软件包，如何通过使用软件包扩展 App 的功能。然后我们稍微谈谈软件包里到底有什么，它们是如何构造的，软件包的数据存储——文件格式中有什么。

当我们谈论软件包解析时，Xcode 如何获取软件包的正确版本并将其纳入你的 App。然后我们稍微谈谈更新软件包，当软件包的新版本发布时会发生什么，以及你如何利用它。我们还将讨论更新软件包时可能发生的任何版本冲突的解决。

那么，让我们开始通过扩展 NAP 的功能来利用软件包。

这里有一个小 iPhone App，它只是显示我工作场所附近一些咖啡馆的午餐菜单 offerings。我们看到这里有两个条目。这是一个 SwiftUI App。所以我可以在不运行 App 的情况下在 Xcode 中看到预览。

所以我们看到来自两个不同地方的午餐菜单正在显示。在真实版本的这个 App 中，我们会通过网络获取这些数据。但在这个演示 App 中，我只是把它们作为本地文件放在源代码中。所以你可以说这个菜单是本地采购的。这两个 JSON 文件显示得很正常。但这家咖啡馆更现代、更高端。所以他们有一个 YAML 菜单，对吧？所以我们无法解析它。我们没有看到它。那么让我们来看看加载这些数据的源代码。我们看到这里处理了 JSON，但没有处理 YAML。现在幸运的是，我知道一个能很好地解析 YAML 的库。它有一个不错的 Swift 接口。它叫做 Yams。我打算去使用它。

为此，我下拉到文件菜单。我进入这个新的 Swift Packages 子菜单，选择 Add Package Dependency。这个子菜单还有几个其他菜单命令，用于软件包进入你的 App 后进行处理。

但你说 Package Dependency。在这里，因为我把我的 GitHub 账户添加到了 Swift——Xcode 的偏好设置中，我在这里看到该账户中所有软件包仓库。我还看到任何我收藏过的其他仓库。

在这种情况下，我收藏了这里的 Yams。但我也可以，如果我有软件包的 URL，我可以在这里输入。

在这种情况下，我将点击这里的 readme 链接，前往 Yams 项目的主页。那看起来不错。

我将在这里看看 API。这看起来像我需要的。当然，当你使用开源库时，你是把别人的代码带入你的 App。所以有很多事情你需要小心。你要确保你信任软件包的来源。你要确保你知道这个库究竟在做什么，这样你才不会有意外。你要确保这个开源库的许可证与你的 App 的许可证兼容。

所以我已经做了所有这些。我将回到 Xcode。我将在这里点击 Next。我们将添加一个对 yams 的引用、一个依赖。

现在 Xcode 显示给我可用的版本。它自动设置我使用软件包的最新版本。我们稍后会在讲座中更多地讨论这些选项的细节。但大多数情况下，这里的默认选项就是你想要的。它 anyway 使用 2.0 版本，最高到但不包括下一个主要版本。我将点击 Next。

现在 Xcode 正在获取 Yams 软件包的内容。它为我预选了这里的单个产品。有些软件包可以有多个产品。在这种情况下只有一个。它是一个库。与软件包同名。如果你的项目中有多个 App，你可以选择在哪里链接它。在这种情况下只有一个，所以我将把它链接到 Lunch App。我点击 finish。

现在我们看到几样东西。一方面，Xcode 在我的 Project Editor 的新 Swift Packages 选项卡中添加了对 Yams Package Dependency 的引用。

我们还看到 Yams 软件包出现在下面的 Swift Package Dependency 部分。

我们暂时不会查看那个软件包——现在。我们稍后会看。我们现在要做的，是再进入 food menu。现在，我们将从代码中使用它。所以我将在这里输入 import Yams。我们看到针对 import 名称的代码补全。我还可以 Command-Click 这个 import 语句。我可以跳转到定义。这里我看到为 Yams 项目接口渲染的文档版本。

所有这些都来自包含在软件包中的源代码中的文档注释。所以我回到我的代码。我将在这里添加另一个 case。Case，YAML。

我将输入——就输入 YAML decoder。我对所有库方法都有代码补全。我还有 Quick Help，因为软件包包含它。所以这看起来和感觉起来就像内置 API 一样，就支持质量而言。我将使用这个方法。我将对 JSON case 使用相同的前几个参数。现在这个 API 恰好接受一个字符串而不是数据。所以我将使用那个。我不需要这里的第三个参数，因为我将只使用默认值。

所以现在，我们可以再次回到列表视图。因为这是一个相当大的更改，导入一个新模块，我将点击 resume。Xcode 将在后台重新构建应用程序。我将在这里看到预览。现在我们看到我看到 YAML 数据文件中的内容了。好的，所以现在我可以把这个提交到我的仓库。

我们在这里看到我们所期望的。我们看到我做的源代码更改，当然，作为提交表单的一部分。我们还看到项目文件已更改，因为我添加了对 Yams 软件包的引用。我们还在这里看到一件事，就是 Xcode 在共享数据下的 workspace 下创建了一个名为 SwiftPM 的目录，那是给 Swift Package Manager 的。你想要签入它，因为稍后在讲座中我们会谈它里面到底有什么。但 Xcode 存储了已解析的软件包版本信息。你想要签入它，以便你团队中的每个人都获得相同的版本。好的，现在我可以签入并说 useYAML。

并使用。好的，回到幻灯片。

好的，我们快速看到了如何在项目中使用开源软件包。让我们更仔细地看看 YAML 软件包里有什么。

软件包是一个包含 Swift Package 清单的目录。清单是一个名为 Package.swift 的文件，它把这个目录标识为 Swift 软件包。它还包含源代码，当然，还包含单元测试，以确保这些源代码继续正常工作。

在 sources 下面，每个单独的目标都有一个子目录。这些是软件包中可单独构建的组件。

类似地，在 test 目录下，每个测试套件都有一个单独的子目录。

那么让我们更仔细地看看其中一个目标目录的内容。每个目标都可以有基于 C 的语言之一或 Swift 的实现。因此在 YAML 的情况下，有一个用 C 编写的 core CYAML 解析器。它还可以包含 Objective-C++ 文件。然后在另外的目标中有一个 Swift 接口，调用 CYAML 代码。然后单元测试用 Swift 编写。

所以如果我们查看 Swift Package 清单的内容，第一行是软件包需要的工具版本声明。这表示能够解析这个软件包清单的最低版本。

软件包描述 API 是由 Package Manager 的 package description 库提供的声明式 API。通过导入它，这个文件的其余内容可以声明软件包的特性。

这包括软件包的名称。

它还包含一个列出软件包向客户端提供的产品的部分。因此软件包可以控制其代码的哪些部分可以被客户端直接导入。在这种情况下，有一个与软件包同名的库，叫做 Yams。我们稍后会谈 targets 部分。它基本上说这个库把 Yams 目标作为库发布给客户端。

targets 部分列出软件包中可单独构建的部分。正如我们在这里看到的，源文件夹和 targets 之间有一对一的对应关系。这些源文件夹可以有其他子文件夹用于组织目的，但 sources 下的顶层是每个软件包、每个 target 一个文件夹。

在这种情况下，我们看到 CYAML target 列出时没有任何依赖。Yams target 列为依赖 CYAML target。这意味着当 product 引用 Yams 时，它将间接地把 CYAML 也带进来。然后这里有一个测试 target 用于单元测试。这段代码实际上不会链接到客户端。但它对于确保你的库继续正常运行是必要的。在这种情况下，Yams 软件包清单还列出了代码兼容的一些更旧的 Swift 版本。还有其他特性可以指定，在这个声明式语言中，我们稍后会谈到其中一些。那么当实际构建和运行 App 时，这是如何链接到你的 App 中的？所以你的项目由源文件组成。可能是 Swift。可能是其他语言。

你所依赖的软件包，它们也是源文件。所以 Xcode 所做的是，它取所有这些源文件，并编译它们，特别是以与你项目中的 App 代码兼容的方式编译软件包代码。这包括架构、平台等。如果需要，它会多次重新编译，具体取决于你的 App 需要什么。然后它链接进来，把所有这些组合成应用程序。

软件包库默认是静态的。所以所有代码都被链接在一起。

对于使用同一软件包的项目中的各种 App，这都会重复。所以如果你有一个 iOS App 和 WatchOS App，它们使用同一个软件包。Xcode 可能会根据每个 App 的需要多次构建代码。

现在，我们看到了一个项目可以依赖一个软件包的情况。我们看到这显示在 target 编辑器的 Package Dependencies 部分。但软件包也可以依赖其他软件包。这通过软件包清单完成。

因此软件包清单的 sections 之一，Yams 没有，就是 Dependencies 部分。它没有，因为它实际上不依赖其他软件包。但你拥有的某些软件包可能依赖。因此软件包依赖图可以包括直接和间接依赖。

现在，我之前提到你可以用软件包管理器管理你的版本。这使用一种叫做语义化版本控制（semantic versioning）的东西。这是一种相当广泛使用的策略，为三部分版本的每个组件赋予语义含义。

因此，例如，在这种情况下，major version 在每次 API 有破坏性更改时递增。这是任何会导致客户端必须修改的事情。例如，如果你重命名一个方法或移除一个方法，或者如果软件包做出了语义上有意义的更改，导致现有客户端必须适应。

这就是为什么初始版本限制会升到但不包括下一个主要版本号。

软件包的 minor version number 在以不破坏现有客户端的方式添加功能时递增。例如添加一个方法。

最后，patch version 是当有错误修复而没有语义更改时。软件包可以安全地更新以合并错误修复，而不会改变 App 的语义。

好的，我们已经看到了如何使用软件包。我们更仔细地查看了那个软件包。现在我想邀请我的同事 Balraj 上台，更详细地讨论软件包解析。谢谢你，Anders。

软件包解析是 Xcode 在选择要在 workspace 中使用的软件包版本时所经历的过程。让我们更详细地了解它是如何工作的——以及它在 Anders 刚才演示的 Lunch 项目中是如何工作的。

所以这里在 Project Editor 的 Swift Packages 选项卡中，我们可以看到我们的依赖——Lunch 对 Yams 的依赖。使用 Version Rule 2 到下一个主要版本，意味着 Yams 的任何版本从 2 起，最高到但不包括 3。然后，在 Project Navigator 的 Swift Package Dependencies 部分，我们可以看到 Yams 在 2.0 版本。

让我们更深入地看看。

Lunch 选择 Yams 在版本 2，是因为它的版本要求，2 到下一个主要版本。

如果存在 2.1 版本，Xcode 会选择那个，因为 2.1 是匹配我们版本要求的最新版本。

然而，如果存在 3 版本，Xcode 不会选择它，因为它不符合我们指定的约束。

在这种情况下，2.1 和 3 是假设的例子。你将在本演示的其余部分继续看到 Yams 在版本 2 解析。

在这个例子中，有一个软件包有一个版本可供选择。所以让我们进入更多有趣的案例，软件包解析可能变得更复杂。

所以这里是我们今天的 Lunch App。它有一个非常基本的 UI，并且只使用一个软件包，正如我们刚说的。

我的团队随着时间推移向我们的应用程序添加更多软件包，他们使用这些软件包来展示我们团队拥有的所有应用程序之间的通用设计主题。所以当我们几周后回到 Lunch 应用程序时，我们可以看到 UI 已更新，并且 workspace 中有三个额外的软件包。

这三个软件包是 DesignFont、DesignTheme 和 DesignColor。

各自解析到它们各自的版本。所以 Xcode 为我们做了很多工作，选择这些软件包的版本。但我想了解为什么这些软件包解析到这些版本。所以为了做到这一点，我回到 Project Editor。

这里在 Swift Package Dependency 部分，我们可以看到我们新的对 DesignTheme 的依赖，Version Rule 1 到下一个主要版本。

在这种情况下，Xcode 选择 DesignTheme 在版本 1，因为它从 1 解析到下一个主要版本。

所以我们也看到我们对 Yams 的依赖仍然相同。你可能会想。DesignFont 和 DesignColor 在哪里？我们在 Project Editor 中查看，但我们在那里看不到它们。嗯，原因是 Project Editor 显示我们 Lunch 应用程序与它的直接软件包之间的所有直接依赖。

所以为了查看我们软件包的依赖，我们想去看 DesignTheme 软件包。因为它是最近添加到我们 workspace 的软件包。并且可以安全地假设它们不是来自 Yams。所以为了做到这一点，我们回到 Xcode 的高层视图，查看 Swift Package Dependencies 部分。这里我们看到我们的软件包 DesignTheme。我们展开软件包，看到其中的所有内容。在这种情况下，我们想查看 Package.swift 清单文件。这是因为我们将在这里找到这个软件包的所有依赖信息。

所以我们打开这个文件。在 dependencies 数组中，我们看到 DesignFont 和 DesignColor，以及它们的版本要求。

DesignFont 按我们之前看到的方式解析，1 到下一个主要版本。所以 Xcode 将选择版本 1.2，因为它是软件包的最新版本。

DesignColor 解析方式有些不同。这是使用 1 到下一个 minor version，意味着 DesignColor 的任何版本从 1 起，最高到但不包括 1.1。这通常用于软件包在更新时想要对新版本更保守。所以 Xcode 选择 DesignColor 软件包的 1.0.1 版本。

所以现在这是我们新添加的软件包及其解析到这些版本的原因的完整视图。你还记得 Anders 在前一个演示中的最后一步是导入 Yams 然后使用其 API。让我们谈谈这是如何工作的，以及它与软件包解析的关系。

我们所有的软件包都在生成同名的库。

我们可以看到 Lunch 正在从 DesignTheme 导入内容，也从 Yams 导入内容。然后 DesignTheme 库也从 DesignFont 和 DesignColor 导入内容。

当我们查看完整图时，我们可以看到这与软件包解析的工作方式非常相似。这是有意的。当我们添加了对软件包的直接依赖时，我们最终也导入了它们的内容，并实际上在应用程序中使用了 API。但如果我想把子依赖的内容导入到我们的项目中会发生什么？让我们谈谈如何做到这一点。

我们有 Lunch 项目，它依赖于 DesignTheme。DesignTheme 依赖于 DesignFont 软件包。DesignFont 软件包生成同名的库。在这种情况下，我们不想立即将 DesignFont 的内容导入到 Lunch 中，因为如果 DesignTheme 在更新中失去了对 DesignFont 的依赖，Xcode 将失去对 DesignFont 的引用。现在，我们就无法使用 DesignFont 库了。

所以更好的方法，让我们回到我们例子的开始，是在 Lunch 项目和 DesignFont 软件包之间创建直接的软件包依赖。然后我们可以从 DesignFont 导入内容到 Lunch，因为如果 DesignTheme 在更新中失去了对 DesignFont 的依赖，我们仍然在 Xcode 中保留对该库的引用。

所以这就是 Xcode 如何选择软件包的不同版本。让我们进入——进入如何获取这些软件包的新版本，它们提供 API 改进和错误修复。

有一天，我与维护 DesignFont 的团队一起午餐。他们告诉我 DesignFont 软件包的新版本，其中包含一些小的错误修复，版本 1.2.1。当我回到办公桌时，我看到 DesignFont 使用版本 1.2。Lunch 项目使用 DesignFont 在版本 1.2。

所以我想更新这个软件包。为此，我点击 File，Swift Packages。在这里，我面对关于 Swift Packages 的多个选项。在这种情况下，我想更新到最新的软件包版本。

所以继续点击，更新操作发生。

我们现在使用 DesignFont 版本 1.2.1。那么更新软件包版本究竟做了什么？在更新操作期间发生了什么？所以存在一个名为 Package.resolved 的文件，这对这个过程至关重要。

Package.resolved 记录了 workspace 中所有软件包的版本信息。当你进行更新操作时，这个文件被更新，然后 Xcode 将选择——为你拉取新版本。

这个文件存在于 xcsharedata 中，通常与你的团队和源代码控制共享。所以一个重要的注意事项是，我们刚刚做的更新操作是一个本地操作。为了把这个更新分享给我的团队，我必须提交并推送我的 Package.resolved 文件的更改。

如果你想自己查看所有这些，它在 Xcode Project 文件中。但请注意，你实际上不必自己编辑 Package.resolved 文件。Xcode 应该为你完成所有工作。

所以如我之前所说，我们实际上还没有把这个更新分享给我们的团队。让我们来做。我们可以在 Xcode 中通过 Source Control 菜单点击 Commit 来做这一切。

在这里，我们将看到对 Package.resolved 文件所做的所有更改，以及它如何从我们之前使用的 1.2 版本更新到 1.2.1 新版本。因为我想要推送，我继续点击左下角的复选框，push to remote。然后我可以提交并推送我的更改。我们现在已经成功地把这次更新分享给了我们的团队。

所以所有这些引出一个问题：我们为什么需要 Package.resolved 文件？这个文件的存在是为了确保当人们使用——我的团队的人在相同的 commit 上使用 Lunch 项目时，他们都能获得相同版本的 DesignFont。如果这个文件——如果 Package.resolved 文件不存在，你可能会遇到一种情况，即你团队中的多个人使用相同版本的项目，但没有软件包版本的一致性。

所以一个极其重要的注意事项是签入你的 Package.resolved 文件。否则，你可能会在团队中使用不一致的软件包版本。所以这个文件被签入是非常重要的。

然后一定要留意软件包的新版本。然后，有目的地更新。否则，你可能会错过软件包为你提供的一些关键错误修复和 API 改进。

所以这就是你如何更新软件包。让我们进入一个更高级的例子，关于如何解决软件包冲突，它将结合我们今天讨论的许多不同主题。

所以我启动一个项目，更改 Lunch 应用程序中我们用于价格的字体。

我想使用的系统字体在 DesignFont 的版本 2 中可用，这有助于保持我们团队拥有的应用程序之间使用的字体版本一致。所以让我们来做。为了使用 DesignFont 软件包，我们需要在 Lunch 和 DesignFont 之间创建直接依赖。然后，因为版本 2 的 DesignFont 发布了这个新字体，我们想专门使用那个版本。

所以我们回到 Xcode，我们通过 Add Package 工作流。我们点击 DesignFont，因为它在我们收藏的账户中。我们说 Next。我们选择到下一个主要版本，因为我们想要对 DesignFont 发布的任何更新或新版本开放。然后我们点击 Next。这里，我们遇到了一个软件包解析错误，因为我们在 2 到下一个主要版本之间对 DesignFont 有新的依赖要求。

所以让我们看看这里发生了什么，调试发生了什么。

调试软件包解析时，要记住的一件非常重要的事情是看全貌。

我们想考虑影响我们软件包的每一个要求，而不仅仅是局限于我们刚刚添加的内容。

所以我们退一步，看看之前是如何工作的。Lunch 对 DesignTheme 有很好的依赖，版本 1。DesignTheme 对 DesignFont 有直接依赖，版本 1.2.1，使用版本要求 1 到下一个主要版本。

然后当我们添加了 Lunch 和 DesignFont 之间从 2 到下一个主要版本的直接依赖时，我们遇到了软件包解析冲突。

你会注意到 DesignTheme 对 DesignFont 的要求是 1，最高到但不包括 2。而 Lunch 对 DesignFont 的要求是 2，最高到但不包括 3，无法选择一个版本同时满足这两个要求。

因此在 SwiftPM 集成到 Xcode 中，workspace 中只能有一个软件包版本。

这解释了为什么我们在这里看到软件包解析错误。Xcode 不可能选择一个同时满足两个版本要求的版本。

解决这个问题是非常具体情况的。但通常，当我遇到这样的软件包解析错误时，我想查看可用给我的软件包的较新版本。然后我可以看看那些较新版本是否对它们的子依赖提供了任何更新。

在这种情况下，我注意到有一个我们还没有真正查看的 DesignTheme 版本 2。所以让我们去 GitHub 查看 DesignTheme 的版本要求。

当我们去 GitHub 时，我们可以查看 Swift Package 清单的 dependencies 数组。这里，我们看到 DesignFont 的版本要求已更新——从 1 到下一个主要版本更新为 2 到下一个主要版本。

这与我们试图在 Lunch 和 DesignFont 之间添加的版本要求匹配。所以如果我们能把 DesignTheme 的版本要求更新为解析到版本 2，我们现在就可以在 Lunch 和 DesignFont 之间可满足地添加直接依赖。

所以让我们来做，更新 DesignTheme 的 major version。之前，Lunch 使用 DesignTheme 从 1 到下一个主要版本。我们想改变它，使它现在使用 2 到下一个主要版本。

所以我们回到 Xcode。现在，我们只需点击 Project Editor 中的 DesignTheme 软件包。然后我们回到编辑版本规则表单。这里，我们之前指定 1 到下一个主要版本。但现在我们想把它改为 2 到下一个主要版本。

所以我们只需把 1 改为 2，然后点击 Done。

现在，更新操作发生。我们可以看到 DesignTheme 在版本 2，DesignFont 在版本 2。

但这里发生了一件重要的事。当我们从一个 major version 更新到另一个时，我们遇到了构建失败。这是因为从软件包的一个 major version 到另一个，可能会有 API 更改。这可能会导致你项目中的破坏性更改。

这意味着当你从一个 major version 更新到另一个时，你应该准备好更改一些 API，或者更改新版本软件包中 API 的工作方式。

这可能是非常小的更改，也可能是稍微复杂一些。在这种情况下，我们已经为你做了所有工作，以便把更多时间花在软件包上。所以当我们回到 Lunch 应用程序时，我们的构建错误已解决。我们成功地在版本 2 使用 DesignTheme。

所以我们的构建现在成功了。我们想在 Lunch 和 DesignFont 之间添加直接依赖。因为现在我们处于 DesignTheme 的版本 2，我们可以添加我们想要的版本要求。

所以我们回到 Xcode，我们通过 Add Package 工作流。我们选择 DesignFont。我们选择 2 到下一个主要版本。

现在，我们可以把 DesignFont 库与我们的应用程序链接。现在在 Project Editor 中，我们可以看到我们成功地从 2 到下一个主要版本使用 DesignFont。

现在我们已经这样做了，我们现在可以导入 DesignFont 中的内容，成功使用它的库，然后通过一些小的代码更改，更新价格的字体。

所以我们现在已经成功做到了并解决了我们的软件包冲突。我们更新了我们的软件包版本，并成功回顾了如何在 Xcode 中调试软件包解析。

所以今天我们讲了很多东西。

我们谈到了如何开始在你的项目中使用开源软件包并快速开始使用其 API。

我们更仔细地查看了软件包是什么，以及 Package.swift 清单如何把所有东西整合在一起。

我们回顾了 Xcode 如何选择要在你的项目中使用的软件包版本。

然后我们回顾了如何保持这些版本的更新并持续获得软件包的新更新。

然后我们查看了一个更高级的例子，关于如何解决软件包冲突，这教会了我们如何调试软件包，以及如何更新软件包版本。

GitHub 上已经有很多可用的软件包。

我们建议你浏览这些软件包，看看可以在哪里把它们纳入你现有的应用程序。

但我们还没有结束。明天我的同事 Ankit 和 Boris 将举行一场关于如何创建 Swift 软件包的讲座。这场讲座将更深入地探讨软件包是什么，如何编辑软件包，SwiftPM 开源工具，以及更多更多。

这场讲座将帮助你成为软件包在 Xcode 中如何工作的更专家，你不会想错过的。然后如果你对 SwiftPM 团队有更多问题，我们将在本讲座结束后在 Swift Open Hours Lab。然后整个星期还有两场讲座，一场是周四中午 12:00 在 Swift Packages Lab，另一场同名讲座是周五中午 12:00。

非常感谢大家今天前来，祝大家一周余下时光愉快。谢谢。[ 掌声 ]
