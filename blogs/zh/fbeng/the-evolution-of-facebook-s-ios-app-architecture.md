---
title: Facebook iOS App 架构的演进
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2023/02/06/ios/facebook-ios-app-architecture/'
original_language: en
published: 2023-02-06
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5fbf6f5f9ea5cfd0'
translated: true
---

> 原文：[The evolution of Facebook’s iOS app architecture](https://engineering.fb.com/2023/02/06/ios/facebook-ios-app-architecture/)　·　Meta Engineering — iOS

Facebook for iOS（FBiOS）是 Meta 历史最久的移动端代码库。[自 2012 年该 App 被重写以来](https://engineering.fb.com/2012/08/23/ios/under-the-hood-rebuilding-facebook-for-ios/)，已有数千名工程师参与过它的开发，它被交付给数十亿用户，并且能够同时支持数百名工程师在其上进行迭代。

[经过多年的迭代](https://engineering.fb.com/2012/08/23/ios/under-the-hood-rebuilding-facebook-for-ios/)，Facebook 的代码库已经和典型的 iOS 代码库大不相同：

- 它充满了 C++、Objective-C(++) 和 Swift。
- 它拥有数十个[动态加载库（dylib）](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/UsingDynamicLibraries.html)，类多到无法一次性加载到 Xcode 中。
- 几乎没有直接使用 Apple 的 SDK——所有内容都被内部抽象层包装或取代了。
- 该 App 大量使用由我们的自定义构建系统 [Buck](https://www.buck.build/) 驱动的代码生成。
- 如果没有构建系统提供的强大缓存，工程师们将不得不花费一整个工作日来等待 App 的构建。

FBiOS 并非有意设计成这种架构。App 的代码库反映了 10 年的**演进**，这种演进是由为了支持越来越多的工程师在 App 上工作、保障其稳定性以及——最重要的——提升用户体验所必需的技术决策所推动的。

现在，为了庆祝代码库诞生 10 周年，我们将揭示这一演进背后的一些技术决策，以及它们的历史背景。

## 2014：建立我们自己的移动框架

在 Meta [启动 Facebook 原生 App 重写项目](https://engineering.fb.com/2012/08/23/ios/under-the-hood-rebuilding-facebook-for-ios/)两年后，News Feed 的代码库开始出现可靠性问题。当时，News Feed 的数据模型由 Apple 用于管理数据模型的默认框架——[Core Data](https://developer.apple.com/documentation/coredata?language=objc)——支持。Core Data 中的对象是可变的，这不利于 News Feed 的多线程架构。更糟糕的是，News Feed 使用了双向数据流，这源于它采用了 Apple 为 Cocoa App 设计的事实标准设计模式——[模型视图控制器（Model View Controller）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html)。

最终，这种设计加剧了非确定性代码的产生，使得调试或重现 Bug 变得极其困难。很明显，这种架构不可持续，是时候重新思考了。

在考虑新设计时，一位工程师研究了 [React](https://reactjs.org/)——Facebook 的（开源）UI 框架，它在 JavaScript 社区中变得非常流行。React 的声明式（declarative）设计抽象掉了那些导致 Feed（在 Web 上）出现问题的棘手命令式（imperative）代码，并利用了单向数据流，使得代码更容易理解。这些特性似乎非常适合 News Feed 所面临的问题。只有一个问题。

Apple 的 SDK 中没有声明式 UI。

[Swift 还要再过几个月才会发布](https://developer.apple.com/swift/blog/?id=14)，而 SwiftUI（Apple 的声明式 UI 框架）要到 2019 年才会发布。如果 News Feed 想要一个声明式 UI，团队必须构建一个新的 UI 框架。

最终，他们就是这么做的。

在花了几个月时间构建并将 News Feed 迁移到新的声明式 UI 和新的数据模型上运行后，[FBiOS 的性能提升了 50%](https://engineering.fb.com/2014/10/31/ios/making-news-feed-nearly-50-faster-on-ios/)。几个月后，他们开源了受 React 启发的移动端 UI 框架 [ComponentKit](https://engineering.fb.com/2015/03/25/ios/introducing-componentkit-functional-and-declarative-ui-on-ios/)。

时至今日，ComponentKit 仍然是 Facebook 中构建原生 UI 的事实标准选择。它通过视图重用池、视图扁平化和后台布局计算，为 App 带来了**无数**性能提升。它还启发了其 Android 对应框架 [Litho](https://engineering.fb.com/2018/01/31/android/improving-android-video-on-news-feed-with-litho/) 和 SwiftUI。

最终，用自定义基础设施替换 UI 和数据层是一种权衡。为了获得可靠维护的愉悦用户体验，新员工必须搁置他们对 Apple API 的行业知识，去学习自定义的内部基础设施。

这不是 FBiOS 最后一次需要在最终用户体验与开发者体验和开发速度之间做出决策。进入 2015 年，App 的成功引发了我们所说的一次“功能爆炸”。而这带来了其自身的一系列独特挑战。

## 2015：架构的转折点

到 2015 年，Meta 已全力贯彻其[“移动优先”方针](https://www.reuters.com/article/net-us-facebook-roadshow/facebooks-zuckerberg-says-mobile-first-priority-idUSBRE84A18520120512)，FBiOS 代码库的日常贡献者数量急剧上升。随着越来越多的产品被集成到 App 中，其启动时间（launch time）开始恶化，人们开始注意到这一点。到 2015 年底，启动性能已经变得非常慢（接近 30 秒！），以至于有被手机操作系统杀死的风险。

经过调查，很明显有许多因素导致了启动性能的下降。为简洁起见，我们只关注那些对 App 架构产生长期影响的因素：

- 随着 App 大小随每个产品增长，App 的“pre-main”时间也在无限制地增长。
- App 的“模块”系统赋予了每个产品对 App 所有资源的无约束访问权限。这导致了[公地悲剧问题](https://en.wikipedia.org/wiki/Tragedy_of_the_commons)，因为每个产品都利用其在启动过程中的“钩子”来执行计算密集型操作，以便初始导览到该产品时能够迅速响应。

为了缓解和改善启动性能所需的改变，将从根本上改变产品工程师为 FBiOS 编写代码的方式。

## 2016：动态库与模块化

根据 Apple 关于[改善启动时间](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time)的文档，在调用 App 的 `main` 函数之前，必须执行许多操作。通常，App 的代码越多，这个过程花费的时间就越长。

虽然“pre-main”只占启动过程中 30 秒的一小部分，但它是一个特别的担忧，因为随着 FBiOS 不断积累新功能，它会继续无限制地增长。

为了帮助缓解 App 启动时间的无限制增长，我们的工程师开始将大量产品代码移入一个称为动态库（[dylib](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/UsingDynamicLibraries.html)）的惰性加载容器中。当代码被移入动态加载库时，它不需要在 App 的 `main()` 函数之前加载。

最初，FBiOS 的 dylib 结构如下：

![Facebook iOS](https://engineering.fb.com/wp-content/uploads/2023/02/Evolution-of-FBiOS-image2.png?w=1024)

创建了两个产品 dylib（FBCamera 和 NotOnStartup），并使用第三个 dylib（FBShared）在各种 dylib 和主 App 的二进制文件之间共享代码。

dylib 解决方案效果很好。FBiOS 得以遏制 App 启动时间的无限制增长。随着时间推移，大多数代码最终都会被放入 dylib 中，这样启动性能就能保持快速，并且不受 App 中添加或删除产品的持续波动的影响。

dylib 的引入触发了 Meta 产品工程师编写代码方式的思维转变。随着 dylib 的加入，诸如 `NSClassFromString()` 之类的运行时 API 存在运行时失败的风险，因为所需的类存在于未加载的 dylib 中。由于许多 FBiOS 核心抽象是基于**遍历内存中所有类**构建的，FBiOS 不得不重新思考其许多核心系统的工作方式。

除了运行时失败，dylib 还引入了一类新的链接器错误。如果 Facebook（启动集）中的代码引用了 dylib 中的代码，工程师会看到类似这样的链接器错误：

```none
Undefined symbols for architecture arm64:
  "_OBJC_CLASS_$_SomeClass", referenced from:
      objc-class-ref in libFBSomeLibrary-9032370.a(FBSomeFile.mm.o)
```

为了解决这个问题，工程师需要用一种特殊的函数来包裹他们的代码，该函数可以在必要时加载 dylib：

突然之间：

```cpp
int main() {
  DoSomething(context);
}
```

就变成了这样：

```cpp
int main() {
  FBCallFunctionInDylib(
    NotOnStatupFramework,
    DoSomething,
    context
  );
}
```

这个解决方案有效，但存在不少代码异味：

- 这个**特定于 App 的** dylib 枚举被硬编码到了各种调用点。Meta 的所有 App 必须共享一个 dylib 枚举，读者需要自行判断代码运行所在的 App 是否使用了该 dylib。
- 如果使用了错误的 dylib 枚举，代码会失败，但仅在运行时才会暴露。考虑到 App 中代码和功能的庞大数量，这种滞后的信号在开发过程中带来了很多挫败感。

最重要的是，我们唯一用于防范在启动过程中引入这些调用的系统是基于运行时的，并且由于最后一刻引入的衰退（regression），许多发布被推迟了。

最终，dylib 优化遏制了 App 启动时间的无限制增长，但它标志着 App 架构方式的一个巨大转折点。FBiOS 的工程师在接下来的几年里致力于重新架构 App，以平滑 dylib 引入的一些粗糙边缘，并且我们（最终）交付了一个比以往任何时候都更加健壮的 App 架构。

## 2017：重新思考 FBiOS 架构

随着 dylib 的引入，FBiOS 的一些关键组件必须重新思考：

- 模块注册系统不能再基于运行时。
- 工程师需要一种方法来知道**任何**启动期间的代码路径是否可能触发 dylib 加载。

为了解决这些问题，FBiOS 转向了 Meta 的开源构建系统 [Buck](https://www.buck.build)。

在 Buck 中，每个“目标”（App、dylib、库等）都以一些配置声明，如下所示：

```none
apple_binary(
  name = "Facebook",
  ...
  deps = [
    ":NotOnStartup#shared",
    ":FBCamera#shared",
  ],
)

apple_library(
  name = "NotOnStartup",
  srcs = [
    "SomeFile.mm",
  ],
  labels = ["special_label"],
  deps = [
    ":PokesModule",
    ...
  ],
)
```

每个“目标”都列出了构建它所需的所有信息（依赖项、编译器标志、源代码等），当调用 `buck build` 时，它会在一个可查询的图中构建所有这些信息。

```none
$ buck query “deps(:Facebook)”
> :NotOnStartup
> :FBCamera

$ buck query “attrfilter(labels, special_label, deps(:Facebook))”
> :NotOnStartup
```

利用这个核心概念（和一些特殊方法），FBiOS 开始生成一些 Buck 查询，这些查询可以在构建期间生成 App 中类和函数的全局视图。这些信息将成为 App 下一代架构的基石。

## 2018：生成代码的普及

现在，FBiOS 能够利用 Buck 来查询关于依赖项中代码的信息，它可以创建一个“函数/类 -> dylib” 的映射，并可以动态生成。

```cpp
{
  "functions": {
    "DoSomething": Dylib.NotOnStartup,
    ...
  },
  "classes": {
    "FBSomeClass": Dylib.SomeOtherOne
  }
}
```

使用该映射作为输入，FBiOS 利用它生成代码，将 dylib 枚举从调用点中抽象出来：

```cpp
static std::unordered_map<const char *, Dylib> functionToDylib {{
  { "DoSomething", Dylib.NotOnStartup },
  { "FBSomeClass", Dylib.SomeOtherOne },
  ...
}};
```

使用代码生成具有几个吸引人的原因：

- 由于代码是基于本地输入重新生成的，所以无需检入，也不再有合并冲突！考虑到 FBiOS 的工程师数量每年可能翻一番，这是一个巨大的开发效率提升。
- `FBCallFunctionInDylib` 不再需要特定于 App 的 dylib（因此可以重命名为 `FBCallFunction`）。相反，该调用将读取为每个应用程序在构建期间生成的静态映射。

将 Buck 查询与代码生成结合使用被证明非常成功，以至于 FBiOS 将其作为新插件系统的基础，该系统最终取代了基于运行时的 App 模块系统。

### 将信号左移

借助新的基于 Buck 的插件系统，FBiOS 通过将部分基础设施迁移到基于插件的架构，得以将大多数运行时失败替换为构建时警告。

当构建 FBiOS 时，Buck 可以生成一个显示 App 中所有插件位置的图，如下所示：

![Facebook iOS](https://engineering.fb.com/wp-content/uploads/2023/02/Evolution-of-FBiOS-image1.png?w=1024)

从这个角度出发，插件系统可以显示构建时错误来警告工程师：

- “插件 D、E 可能触发 dylib 的加载。这是不允许的，因为这些插件的调用者位于 App 的启动路径中。”
- “在 App 中找不到用于渲染个人资料的插件……这意味着导览到该屏幕将无法工作。”
- “有两个用于渲染群组的插件（插件 A、插件 B）。应该移除其中一个。”

使用旧的 App 模块系统，这些错误将是“懒惰的”运行时断言。现在，工程师们确信，当 FBiOS 成功构建时，它不会因为缺少功能、App 启动期间加载 dylib 或模块运行时系统中的不变性而导致失败。

### 代码生成的代价

虽然将 FBiOS 迁移到插件系统提高了 App 的可靠性，为工程师提供了更快的信号，并使 App 能够轻松地与其他移动 App 共享代码，但这也付出了代价：

- 插件错误不在 Stack Overflow 上，并且可能难以调试。
- 基于代码生成和 Buck 的插件系统与传统的 iOS 开发相去甚远。
- 插件为代码库引入了一层间接性。大多数 App 会有一个包含所有功能的注册文件，而在 FBiOS 中，这些文件是生成的，可能出奇地难以找到。

毫无疑问，插件使 FBiOS 进一步偏离了传统的 iOS 开发方式，但这种权衡似乎是值得的。我们的工程师可以更改 Meta **许多** App 中使用的代码，并且确信只要插件系统正常工作，没有 App 会因为某个很少被测试的代码路径中缺少功能而崩溃。像 News Feed 和群组这样的团队可以为插件构建扩展点，并确保产品团队可以在不触及核心代码的情况下集成到他们的界面中。

## 2020：Swift 与语言架构

虽然本文大部分内容聚焦于 Facebook App 规模问题引发的架构变化，但 Apple SDK 的变化也迫使 FBiOS 重新思考其部分架构决策。

2020 年，FBiOS 开始看到 Apple 提供的纯 Swift API 数量增加，并且代码库中对于更多 Swift 的呼声也日益高涨。是时候正视一个事实：Swift 在 FB App 中已是不可避免的成员。

从历史上看，FBiOS 使用 C++ 作为构建抽象的杠杆，这节省了代码大小，这得益于 [C++ 的零开销原则](https://en.cppreference.com/w/cpp/language/Zero-overhead_principle)。但是 C++ 目前还不能与 Swift 互操作。对于**大多数** FBiOS API（如 ComponentKit），必须创建某种适配层才能在 Swift 中使用——这造成了代码膨胀。

以下图表概述了代码库中的问题：

![Facebook iOS](https://engineering.fb.com/wp-content/uploads/2023/02/Evolution-of-FBiOS-image4.png?w=1024)

考虑到这一点，我们开始制定一个关于何时何地使用各种代码的语言策略：

![Facebook iOS](https://engineering.fb.com/wp-content/uploads/2023/02/Evolution-of-FBiOS-image3.png?w=1024)

最终，FBiOS 团队开始建议，面向产品的 API/代码不应包含 C++，这样我们就可以自由地使用 Swift 和 Apple 未来的 Swift API。通过使用插件，FBiOS 可以抽象掉 C++ 实现，这样它们仍然驱动着 App，但对大多数工程师是隐藏的。

这类工作流标志着 FBiOS 工程师思考构建抽象方式的一点转变。自 2014 年以来，框架构建中一些最大的考量因素一直是对 App 大小和表现力的贡献（这就是 ComponentKit 选择 Objective-C++ 而不是 Objective-C 的原因）。

Swift 的加入是这些因素首次为开发者效率让路，我们预计未来这一趋势会更加明显。

## 2022：征程完成了 1%

自 2014 年以来，FBiOS 的架构已经发生了相当大的转变：

- 它引入了众多内部抽象，如 ComponentKit 和 GraphQL。
- 它使用 dylib 来保持“pre-main”时间最小化，并有助于实现极快的 App 启动。
- 它引入了一个（由 Buck 驱动的）插件系统，以便工程师与 dylib 解耦，并使代码可以在 App 之间轻松共享。
- 它引入了关于何时何地使用各种语言的语言指南，并开始调整代码库以反映这些语言指南。

与此同时，Apple 也在其手机、操作系统和 SDK 中引入了令人兴奋的改进：

- 他们的新手机**快**多了。加载的代价比以前小得多。
- dyld3 和 chain fixups 等操作系统改进提供了使代码加载更快的软件。
- 他们推出了 SwiftUI，这是一个声明式的 UI API，与 ComponentKit 共享许多概念。
- 他们提供了改进的 SDK 以及 API（例如 iOS 8 中的可中断动画），我们本可以为它们构建自定义框架。

随着更多的体验在 Facebook、Messenger、Instagram 和 WhatsApp 之间共享，FBiOS 正在重新审视所有这些优化，以确定可以在哪些方面更接近平台正统。最终，我们看到，共享代码最简单的方法是使用平台免费提供的东西，或者构建真正无依赖且能在所有 App 之间集成的组件。

我们 2032 年再见，届时将回顾代码库的 20 周年纪念！
