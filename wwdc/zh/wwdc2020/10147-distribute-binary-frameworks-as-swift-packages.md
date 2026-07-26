---
title: 把二进制框架以 Swift package 的形式分发
session_id: 10147
collection: wwdc2020
year: 2020
duration: '7:47'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10147/'
content_hash: 'sha256:bd609d710fe1eb88'
translated: true
---

# 把二进制框架以 Swift package 的形式分发

<sub>WWDC2020 · 7:47 · Swift</sub>

了解如何使用 Xcode 中的 Swift package，把第三方框架添加到你的 App 里，并保持它们是最新的。我们会给你展示如何……

> [!note] 归档理由
> 以 SwiftPM 分发二进制框架（XCFramework）

## Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10147/3/9A1289F5-A542-4604-BB2E-E7A77AF2C41F/wwdc2020_10147_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10147/3/9A1289F5-A542-4604-BB2E-E7A77AF2C41F/wwdc2020_10147_sd.mp4?dl=1)
- [Swift packages: Resources and localization](https://developer.apple.com/videos/play/wwdc2020/10169)
- [What's new in Swift](https://developer.apple.com/videos/play/wwdc2020/10170)
- [Binary Frameworks in Swift](https://developer.apple.com/videos/play/wwdc2019/416)
- [Creating Swift Packages](https://developer.apple.com/videos/play/wwdc2019/410)
- [向 Package Manifest 添加一个 Package 依赖](https://developer.apple.com/videos/play/wwdc2020/10147/?time=157)
- [Distributing Binary Frameworks as a Swift Package](https://developer.apple.com/videos/play/wwdc2020/10147/?time=184)
- [Computing the Checksum](https://developer.apple.com/videos/play/wwdc2020/10147/?time=343)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

你好，欢迎来到 WWDC。

大家好，我叫 Boris，今天我要讲讲如何把二进制框架以 Swift package 的形式分发。在 Xcode 11 中，我们引入了对 Swift package 的支持，提供了一种直接把库以源代码形式分发的简便方法。我们还引入了 XCFramework，它提供了一种更好的方式来分发闭源的二进制框架和库。现在，在 Xcode 12 中，我们把用 Swift package 分发库这一优势，也带给了闭源库，加入了对二进制依赖的支持。在这个视频里，我首先会讲讲如何在一个 App 里使用一个二进制依赖。接下来，我会讲讲如何把一个二进制框架以 Swift package 的形式分发。最后，我们会看看如何用 Xcode 创建一个二进制框架。虽然很多库都是以源代码形式提供的，但有些开发者选择不公开他们库的源代码，转而以二进制形式分发它们。使用这样一个二进制依赖，用起来就和添加一个基于源代码的依赖一样。我们在一个演示里来看看这一点。

我们先从一个简单的 iOS App 开始。你依次选择 File、Swift Packages、Add Package Dependency。

我们选择 BinaryEmoji 这个 package……

使用版本 1.0……

然后把这个二进制文件和我们的 App 链接起来。

现在，如果我们看看项目导航器，我们会看到一个新的分组，"Referenced Binaries"，里面包含了一个 XCFramework。

我们到访达（Finder）里看看它。

我们会看到它有一堆子目录，每一个都对应着一个由目标三元组（target triple）表示的平台和目标环境。

在里面，你会看到与那个特定三元组对应的一个框架。

我们回到 Xcode。

现在我们可以在 App 的代码里导入这个 emoji module 了。

如果我们跳转到"definition"（定义），我们就会看到它提供了哪些 API。这里有一个 EmojiView 类型，是我想在我的 App 里使用的。

如果我们现在刷新一下预览……

你会看到这个 EmojiView 被用上了。所以，使用一个二进制依赖，实际上和使用一个基于源代码的依赖是完全一样的。

如果你已经熟悉了 Xcode 11 里的 XCFramework，它们的处理方式实际上和直接把它们添加到你 App 里是一样的。

如果你想把同一个库当作一个 package 依赖来使用，它的工作方式也和你已经习惯的一样。在这个 package manifest 里，你可以往 dependencies 数组里添加一条记录，指向这个 package 所使用的仓库，并定义你为这个依赖选择的版本限制。

现在我们已经看过了如何使用别人写的二进制依赖，接下来，我们来看看如何创建这样一个 package，来分发我们自己的二进制框架。Xcode 12 提供了新的 tools-version:5.3，带来了新的 package manifest API。这新增了一种 target 类型："binaryTarget"。它有一个 name，对应着这个 XCFramework 的 module 名字……

一个 HTTPS URL……以及一个校验和（checksum），这样下载下来的压缩包就可以被校验。

这里还有一个选项，可以按路径指向一个 XCFramework，这是为开发场景准备的。请注意，较大的 XCFramework，就像任何大型二进制文件一样，不应该提交到你的 Git 仓库里，因为它们会拖慢检出（checkout）速度。

Product 可以引用 binary target，把它们提供给客户端，就像普通的 target 一样。正如我们之前看到的，Binary target 使用 XCFramework，只在 Apple 平台上受支持，可以是基于 HTTPS 的，也可以是基于路径的，其中路径可以指向你 package 内部的文件。如果使用的是 HTTPS，这个二进制产物会和你 package 的 Git 检出分开下载。这意味着你不会用大型二进制文件污染你仓库的历史记录，而且你可以把同一个下载地址用于其他用途，比如让人们手动下载你的框架。

这个 name 对应着 module 名字。名字在整个依赖图里是唯一的，所以不要把别人的二进制框架打包进去。每个二进制框架都应该有一个规范的、唯一的 package。随着你 package 里的 binary target 不断演进，你应该遵循语义化版本规范，就像你对基于源代码的 target 所做的那样。举例来说，对你的 XCFramework 做出破坏性改动，比如重命名一个方法或类型，就应该让你 package 的主版本号（major version）增加。同样地，你也应该用框架 Info.plist 里的 bundle version 字符串设置，给你的框架本身设定版本号。关于演进二进制框架的更多信息，在 WWDC 2019 的 "Binary Frameworks in Swift" 这个 session 里有讲到，我建议大家去看看。我们再来看一个演示，看看如何创建我们自己的二进制依赖。

这次我们从依次选择 File、New、Swift Package 来创建一个新 package 开始。

我们把它叫做 "Emoji"。我们删掉模板添加的那些 target……

然后插入一个 binary target。

它的 name 同样也是 "Emoji"。使用一个指向本地服务器的 URL，那台服务器上有我的 XCFramework。

现在我们需要一个校验和。我们该怎么生成它呢？要计算一个二进制框架的校验和，可以使用 "swift package compute-checksum" 命令。这会把校验和打印到终端里，你可以从那里把它复制出来，粘贴到你的 package manifest 里。当你的 package 被使用时，Xcode 会计算下载文件的校验和，如果它和 manifest 里的不匹配，就会拒绝它。这确保了你的客户端使用的正是你所期望的那个二进制文件。现在我们可以插入这个校验和，然后构建这个 package 了。

这就是你如何把一个 XCFramework 打包进一个 Swift package 来分发的方法。最后，我们来看看如何创建二进制框架本身。XCFramework 是在 Xcode 11 中引入的。它们把一个框架针对不同平台的多个变体打包在一起，既支持框架，也支持动态库和静态库，而且每个 XCFramework 只包含一个 module。要创建一个 XCFramework，需要在你现有的框架或库 target 上设置 "Build Libraries for Distribution" 这个构建设置，用 "xcodebuild archive" 命令为每个变体打包归档，然后用 "xcodebuild -create-xcframework" 命令把它们打包在一起。

关于这一点，在 WWDC 2019 的 "Binary Frameworks in Swift" 这个 session 里有更多细节，所以我建议大家在用 Xcode 创建二进制框架之前先看看那个 session。好，在结束之前，我想讲讲使用二进制依赖的利弊权衡。你应该始终仔细考虑，你要把哪些第三方组件引入你的项目。尤其是对二进制文件来说，调试会变得更困难，而且你没法自己动手修复问题。

你也会被限制在框架作者所支持的那些平台上，因为你没法重新构建一个二进制依赖。在给你的 App 添加新的二进制依赖之前，请记住这些要点。总结一下，你现在可以把现有的 XCFramework 以 Swift package 的形式分发了。依赖它们的方式，和依赖基于源代码的 package 是一样的。感谢大家收看。
