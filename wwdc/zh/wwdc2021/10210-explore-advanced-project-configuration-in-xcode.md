---
title: 探索 Xcode 中的高级项目配置
session_id: 10210
collection: wwdc2021
year: 2021
duration: '25:37'
topics: [Developer Tools]
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10210/'
content_hash: 'sha256:6579156210198e05'
translated: true
---

# 探索 Xcode 中的高级项目配置

<sub>WWDC2021 · 25:37 · Developer Tools</sub>

在处理更复杂的 Xcode 项目吗？你来对地方了。了解如何配置项目以构建……

> [!note] 归档理由
> Xcode 工程配置进阶：xcconfig、target 依赖，构建系统实操

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10210/4/391A6CFB-228A-4349-AE24-4809307D58F5/downloads/wwdc2021-10210_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10210/4/391A6CFB-228A-4349-AE24-4809307D58F5/downloads/wwdc2021-10210_sd.mp4?dl=1)
- [在配备 M1 的 Mac 上打造出色的 iPad 和 iPhone App](https://developer.apple.com/videos/play/wwdc2021/10056)
- [Shell 脚本 - 输出文件](https://developer.apple.com/videos/play/wwdc2021/10210/?time=458)
- [构建规则 - 代码](https://developer.apple.com/videos/play/wwdc2021/10210/?time=502)
- [Shell 脚本 - 代码](https://developer.apple.com/videos/play/wwdc2021/10210/?time=615)
- [XCFileList](https://developer.apple.com/videos/play/wwdc2021/10210/?time=694)
- [Shell 脚本 - 输入文件列表](https://developer.apple.com/videos/play/wwdc2021/10210/?time=717)
- [Shell 脚本 - 输出文件](https://developer.apple.com/videos/play/wwdc2021/10210/?time=731)
- [环境变量 - 脚本阶段](https://developer.apple.com/videos/play/wwdc2021/10210/?time=770)
- [环境变量 - 构建规则](https://developer.apple.com/videos/play/wwdc2021/10210/?time=780)
- [构建设置定义](https://developer.apple.com/videos/play/wwdc2021/10210/?time=1097)
- [带条件的构建设置定义](https://developer.apple.com/videos/play/wwdc2021/10210/?time=1110)
- [构建设置组合](https://developer.apple.com/videos/play/wwdc2021/10210/?time=1190)
- [构建设置求值运算符（路径）](https://developer.apple.com/videos/play/wwdc2021/10210/?time=1268)
- [构建设置求值运算符（替换）](https://developer.apple.com/videos/play/wwdc2021/10210/?time=1281)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ 低音音乐播放 ♪ ♪ Jake Petroules：大家好，欢迎来到"探索 Xcode 中的高级项目配置"。我是 Jake，和我的同事 Prachi 一起，我们将讨论充分利用 Xcode 项目构建配置的策略与技巧。我们将覆盖三个主要主题领域。首先，Prachi 将讨论多平台项目以及 Xcode 13 对多平台框架 target 的新支持。接下来，我将介绍通过 scheme、target 设置与依赖管理，以及构建阶段与规则来建模与配置项目的最佳实践。最后，Prachi 将带你们深入构建设置，涵盖它们的结构与行为、项目编辑器 UI、配置设置文件及其语法，以及更多内容！在整个讲座中，我们将使用一个名为 Fruta 的多平台 App 项目，展示这些技巧如何应用到真实项目。现在我将把时间交给 Prachi，她将谈论多平台框架。Prachi Pai Asnodkar：谢谢，Jake。Xcode 13 的新特性之一是对多平台框架的支持。多平台框架允许我们把多个框架合并为一个，提供简化的 target 管理、一组要管理的构建阶段和一组要管理的构建设置。让我们看看 Fruta App，更新项目以利用这个特性。这是 Fruta App。它是一个多平台 App，构建 macOS、iOS 和 watchOS。它还有三个 framework target——每个平台一个，包含 App 使用的一组共享代码。维护三个独立的框架会带来挑战，例如保持构建设置同步，以及确保所有源文件正确添加到编译源构建阶段。为了解决这些挑战，我们将从把其中一个框架转换为多平台框架开始。这里我们有三个框架——每个平台一个。所有这些 target 都完全相同，只是其中一个有一个只在 macOS 上构建的文件。首先，让我们在项目导航器中导航到 macOS framework target 的 Build Settings 标签。接下来，我们将通过进入 Supported Platforms 构建设置并选择 Any Platform，把框架配置为构建所有平台。你还可以看到 Allow Multiplatform Builds 已自动设置为 "Yes"。这会告知构建系统根据需要为每个支持的平台构建一次该 target。现在这是一个多平台 target，回想一下，原来的 macOS framework 有一个额外文件，应该只在为 macOS 构建时构建。为了配置框架做到这一点，我们可以添加平台过滤器，指定该文件只在 macOS 构建时构建。为此，我们首先进入 Build Phases 标签。接下来，展开 Compile Sources 构建阶段。最后，通过点击 Filters 项并取消勾选 macOS 之外的所有内容，配置 Ingredient+macOS.swift 只为 macOS 构建。现在我们配置好了新的多平台 target，可以删除框架的其他两个变体，因为不再需要它们。此外，因为我们只有一个 framework target，需要配置所有 App 链接并嵌入这个新的 target。macOS App 已经配置好了，因为我们从 macOS 那个开始设置多平台 target。我们可以通过进入每个 App target 的 General 标签，并把框架添加到 Frameworks and Libraries 构建阶段，把新框架添加到 iOS 和 watchOS App。总结一下：我们把 macOS framework target 启用为可构建 iOS 和 watchOS。我们用针对 macOS-only 源文件的平台过滤器自定义了该框架。最后，我们配置 App target 链接并嵌入新的单一多平台 framework target。这就是 Xcode 中的多平台 target。现在回到 Jake，他将更深入地探讨项目配置。Jake：谢谢，Prachi。我将讨论建模与配置 Xcode 项目的最佳实践，并展示几件你可以做来改善构建性能与正确性的事项。首先，让我们看看 scheme 的构建选项。我点击 scheme 选择器、Edit Scheme，然后进入 Build 部分。这里有几个简单的配置项。对于 Build Order，我们建议选择 Dependency Order，这将使项目中的 target 根据依赖图并行构建。这可以大大改善多核构建性能，并更快得到持续集成的结果。相比之下，选择 Manual Order 已弃用，不推荐使用。使用此选项会减慢构建，并在 scheme 中列出的 target 顺序与项目依赖不一致时导致循环错误。scheme 构建选项中的另一个重要设置是 Find Implicit Dependencies。勾选此选项允许 Xcode 根据项目信息（如构建设置中的链接器标志和构建阶段中链接库的名称）自动在 target 之间添加依赖。当相关 target 位于不同项目中、通常无法添加显式 target 依赖时，这尤其有用。如果你使用手动依赖顺序按特定顺序构建 target，是因为无法跨不同项目添加显式 target 依赖，那么启用 Find Implicit Dependencies 并配合选择 Dependency Order 往往是更好的解决方案。现在我将讨论脚本阶段与构建规则。我从项目的 target 列表中选择 SmoothieKit target，然后选择 Build Phases 标签。这里我们有一个 Process Recipes 脚本阶段，包含一些自定义构建逻辑。它的一个职责是从若干 recipe 文件生成代码，每个输入一个输出，我们按顺序处理。你可能意识到这些计算彼此完全独立。这提供了一个性能优化机会，我们可以通过并行运行它们来利用。构建规则允许我们做到这一点。让我们看看如何把这项工作提取到构建规则中。我进入框架项目编辑器的 Build Rules 标签，点击加号按钮添加新的构建规则。然后输入文件模式 "*.recipe"，对应我希望此规则处理的文件类型的扩展名。接下来，我将向此规则添加依赖。我不需要向构建规则添加任何额外输入，因为它会自动获得它处理的每个输入文件作为输入。然而，我需要告诉构建系统该规则为每个处理的文件将产生的输出文件路径。我点击加号按钮添加新的输出文件，并输入 $(DERIVED_ FILE_ DIR)/$ (INPUT_ FILE _BASE).compiledrecipe。最佳实践是把生成的文件写到 DERIVED_FILE_DIR 下，因为这会指向由构建系统管理的适当位置。你应该避免在源根目录下生成输出文件。这会干扰源代码管理，并在同时运行多个构建时导致冲突。现在，我们当然必须把脚本阶段代码复制到规则中。我回到脚本阶段，复制我们处理每个文件的代码。然后回到规则并粘贴进去。记住规则对每个输入运行一次。所以我移除 for 循环，把 $RECIPE 替换为 $SCRIPT_INPUT_FILE——对应当前正在处理的输入文件的绝对文件路径——并把 $DERIVED_FILE_DIR/ $RECIPE.compiledrecipe 替换为 $SCRIPT_OUTPUT_FILE_0，它引用我在下方 Output Files 部分输入的输出文件路径。别忘了给变量加引号，以确保文件路径中的空格和其他特殊字符被正确处理。很好。现在规则中还有一件事要配置。我提到规则对每个输入运行一次。默认情况下，它们还会对 target 编译的每个架构运行一次。例如，Mac App target 中的规则可能会对 arm64 和 x86_64 各运行一次，每个输入一次。所以如果有四个输入乘以两个架构，规则会被调用八次。当规则输出依赖架构时（如目标代码），这很有用。然而，在这种情况下，我的规则产生的输出与底层 CPU 架构无关，所以我将取消勾选 "Run once per architecture"。最后，为了让构建系统把输入文件传播到构建规则，我需要把所有 .recipe 文件添加到 framework target 的 Compile Sources 构建阶段。我回到 Build Phases，展开 Compile Sources，并使用加号按钮添加 recipe 文件。

现在让我们回到脚本阶段。它剩下的工作是把多个文本文件的内容合并为一个文件，以便在 App 运行时更高效地加载。为了有更好的源代码管理体验，我把脚本放在项目文件外部，并在这里的内联脚本编辑器中调用它们。所以让我们跟随 package.sh 的引用查看代码。在这种情况下构建规则不合适，因为我们需要一次性处理所有输入，把它们合并为一个。所以没有办法拆分为可并行运行的隔离单元，因此这项工作保留在脚本阶段是有道理的。但这让我们来到最重要的要点之一：脚本没有指定输入和输出依赖。这可能导致构建任务按错误顺序运行，并减慢构建，因为 Xcode 对并行运行其他任务必须更保守，因为它不知道脚本阶段可能使用哪些文件。所以添加输入和输出依赖很重要，以确保脚本阶段执行的工作相对于构建中的其他任务按正确顺序完成。对于这个特定脚本，我有大量输入。与其在项目文件中逐个输入，我可以使用 xcfilelist 通过外部文件管理这个输入列表。我现在添加一个。我进入 File > New File，并在 Other 部分选择 Build Phase File List。

我粘贴将由这个脚本阶段处理的输入文件列表，每行一个。如果你愿意，你甚至可以通过以 pound sign 开头一行来写注释，这很适合添加额外上下文。现在我从脚本阶段引用这个 xcfilelist。我回到脚本阶段并在 Input File Lists 中指定 xcfilelist 的路径。最后，我通过提供输出内容将写入的文件路径来指定输出依赖，就像我对构建规则做的一样。还有一件事要提。与构建规则类似，脚本阶段也为你提供一些关键环境变量。让我们回到 package.sh 仔细看看。源码中，我引用 SCRIPT_INPUT_FILE_LIST_COUNT；它指传递给我们脚本阶段的输入文件列表总数，SCRIPT_INPUT_FILE_LIST_n；它指第 n 个索引输入文件列表的已解析绝对文件路径，以及 SCRIPT_OUTPUT_FILE_0；它指第一个——在这种情况下也是唯一一个——输出文件的已解析绝对文件路径。这里概述了提供给脚本阶段的一些关键环境变量。target 的构建设置也提供给脚本阶段环境。这里概述了一些构建规则特有的环境变量，以及一些不太常见的。与脚本阶段一样，target 的构建设置也提供给构建规则环境。好的。现在如果我尝试构建项目，会遇到问题。

让我们进入构建日志仔细看看。因为 SmoothieKit 是多平台 target，它构建两次：一次 iOS，一次 watchOS，这意味着这些构建都在尝试在相同路径产生脚本阶段的输出。这是不允许的，因为构建系统要求在整个构建中只有一个任务可以在给定路径产生输出。有几种不同的解决方法。一个简单的解决方案是改变脚本阶段的输出路径，使每次 target 构建时唯一。在这种情况下，我可以考虑使用不同的构建设置，如 DERIVED_FILE_DIR，它是平台特定的，会使路径足够唯一并解决冲突。然而，如果脚本阶段实际执行的工作在每个 target 上下文中相同，那只会导致相同工作做两次。在这种情况下，更好的选项可能是把脚本阶段移动到一个新的 aggregate target，共享的 framework target 依赖它。这就是我要为我的项目做的。开始时，我点击 target 列表底部的加号按钮，选择 Other 标签，选择 Aggregate target。我称它为 Resources。然后我添加新的脚本阶段，并从 framework target 复制名称、脚本源、输入和输出。

最后，我从 framework target 删除原来的脚本阶段，然后添加对新 aggregate target 的 target 依赖。

这样，工作只会做一次，不会输出文件冲突，iOS 和 watchOS 两个 framework 变体都会相对于那个脚本阶段按正确顺序构建。构建成功。现在回到 Prachi，她将告诉你所有关于构建设置的内容。Prachi：谢谢，Jake！那么什么是构建设置？它是你可以应用到 Xcode target 上以配置构建方式各个方面的属性。Xcode 提供两种主要机制配置构建设置。第一种是通过构建设置编辑器。第二种是通过配置设置文件或 .xcconfig 文件。让我们先看看构建设置编辑器如何用于管理项目中的设置。为了打开构建设置编辑器，首先需要在 Project navigator 中选择项目。接下来，确保选择要配置的 target。最后，点击标签栏中的 Build Settings 标签。从这里，你可以添加新的构建设置或修改现有设置。你还可以通过打开 Quick Help inspector 了解所选构建设置的额外信息。构建设置在多个层级定义。你可以把它想成定义的堆栈。事实上，这些层级可以通过点击 Levels 过滤器来可视化。每个列代表构建设置可以定义的不同层级，它们从右到左求值。从最低层级开始：由当前选定 SDK 定义的默认值、项目层级的配置设置文件、Xcode 项目文件中的项目层级设置、配置设置文件中定义的目标设置、Xcode 项目文件中的目标层级设置，最后是构建设置的解析值。注意，如果你看到粗体设置，表示该层级对构建设置有显式值。Xcode 提供的管理构建设置的第二种机制是配置设置文件或 .xcconfig 文件。xcconfig 文件的一些好处包括：更好的源代码管理、跨 target 或配置共享设置、构建设置的高级组合，以及根据开发或测试环境包含额外 xcconfig 文件的能力。让我们看看如何在 xcconfig 文件中编写构建设置。最基本层面，构建设置由名称、赋值运算符和值组成。你可以使用条件语法缩小构建设置的值。条件设置使用方括号定义。支持的条件包括 configuration、architecture 和 SDK。如 SDK 条件所示，通配符可用于匹配。也可以使用熟悉的双斜杠语法添加注释。构建设置可以通过 dollar-parens 语法设置为另一个构建设置的值。在这个示例中，MY_OTHER_BUILD_SETTING 已设置为 YES。MY_BUILD_SETTING_NAME 的值使用 dollar-parens 语法求值 MY_OTHER_BUILD_SETTING。这里也可以求值多个值，就像我们看到的 MORE_SETTINGS。最后，可以使用 $(inherited) 值使用构建设置的现有值。这允许你在保留所有现有值的同时追加额外值。这是一种便利形式，你也可以使用构建设置名称 APPEND_TO_EXISTING_SETTINGS。构建设置求值语法的另一个用途是把构建设置从一组其他构建设置组合起来。首先，我们从控制设置 IS_BUILD_SETTING_ENABLED 开始。我们将使用这个设置的值作为两个额外构建设置 MY_BUILD_SETTING_NO 和 MY_BUILD_SETTING_YES 的后缀。最后，我们定义 MY_BUILD_SETTING 的值由 MY_BUILD_SETTING 和 IS_BUILD_SETTING_ENABLED 组合而成。因为构建设置求值由内向外进行，最内层设置被求值并返回 NO，这是 IS_BUILD_SETTING_ENABLED 的值。最后，组合的 BUILD_SETTING_NO 被求值为 -use_this_one。求值构建设置时，有一组运算符可用于对值进行基本转换。运算符的三个分类是：字符串运算符、路径运算符和替换运算符。支持的字符串运算符是 quote，它转义字符串中的字符；lower 和 upper，它们转换字符大小写；以及 identifiers，它把字符串转换为各种格式的有效标识符。我们提供一组路径运算符来获取目录、文件名、基本名称、后缀和标准化路径。对于每个路径运算符，都有一个替换对应项，允许你替换值的一部分。还有 default 运算符，如果构建设置为空则提供替换值，否则使用构建设置的现有值。最后一项是能够在其他 xcconfig 文件中包含 xcconfig 文件。有两种机制。第一种是必需包含，要求 xcconfig 文件在磁盘上存在。如果找不到文件，会产生编译器错误。第二种是可选包含，允许在存在时包含 xconfig 文件。如果文件不存在，不会失败。注意，路径相对于 Xcode 项目文件的位置。所以让我们看看如何在真实场景中把所有这些信息组合起来。在这个示例中，我们将看看如何解决以下问题。在我们的开发机器上，编译器应该对类型检查耗时过长的表达式积极警告。然而，CI 机器较慢，因此表达式检查的时间应该增加。对于我们的解决方案，有三个配置设置文件：debug、common 和 ci.xcconfig。debug xcconfig 文件用于 debug 构建，并通过 OTHER_SWIFT_FLAGS 构建设置向 Swift 编译器传递一些额外标志。common xcconfig 文件可选地包含 ci.xcconfig 文件。它还定义 OTHER_SWIFT_FLAGS 设置以控制类型表达式警告。它使用 $(inherited) 以确保包含其他标志设置，如来自 debug.xcconfig 文件和 MAX _EXPRESSION_TIME 的构建设置求值，默认值为 200。ci xcconfig 文件定义 MAX_EXPRESSION _TIME 的覆盖值。最后，Xcode 需要知道如何把这些 xcconfig 文件应用到支持的配置层级之一。这是通过我们这里看到的项目编辑器完成的。从 Configuration 部分，你可以把项目中的任何 config 文件应用到 project 或 target 层级，针对任何已定义的构建配置。这里你可以看到，debug.xcconfig 文件在项目层级为 Fruta 的 debug 配置应用。common.xcconfig 文件为项目中的每个 target 设置。总结解决方案：使用 default 运算符为 MAX_EXPRESSION_TIME 定义默认值。ci.xcconfig 文件被可选包含，因为它只会在 CI 系统上存在。在 ci xcconfig 文件中使用对 MAX_EXPRESSION_TIME 默认值的覆盖。这就结束了我们的实践示例。现在让我们回到 Jake 回顾我们涵盖的所有内容。Jake：谢谢，Prachi。让我们回顾。你了解了多平台框架，以及它们如何在多平台项目中提供更简单的构建设置与构建阶段管理方式。你看到了如何通过按依赖顺序并行构建 target 来改善项目配置与构建性能，如何正确使用构建规则与构建阶段，以及指定依赖的重要性。最后，你深入构建设置，了解如何使用配置设置文件更轻松地管理它们，并深入它们的语法和它提供的所有构造。我们希望这些经验为你提供一组有用的工具，帮助你充分利用开发体验。感谢观看！ ♪
