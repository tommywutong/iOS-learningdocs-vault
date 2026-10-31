---
title: 用数字签名验证 App 依赖
session_id: 10061
collection: wwdc2023
year: 2023
duration: '17:05'
topics: [App Services, Essentials, System Services, 'Privacy & Security']
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10061/'
content_hash: 'sha256:c59da1738636b7c1'
translated: true
---

# 用数字签名验证 App 依赖

<sub>WWDC2023 · 17:05 · App 服务、核心要素、系统服务、隐私与安全</sub>

了解你可以如何帮助保护你的 App 的依赖。我们将向你展示 Xcode 如何自动验证你引入的任何已签名的 XCFramework……

> [!note] 归档理由
> 依赖的数字签名校验，二进制信任链

## 章节

- [依赖签名](/videos/play/wwdc2023/10061/?time=138)
- [App 开发者](/videos/play/wwdc2023/10061/?time=540)
- [SDK 作者](/videos/play/wwdc2023/10061/?time=731)

## 相关资源

- [依赖签名](https://developer.apple.com/videos/play/wwdc2023/10061/?time=138)
- [App 开发者](https://developer.apple.com/videos/play/wwdc2023/10061/?time=540)
- [SDK 作者](https://developer.apple.com/videos/play/wwdc2023/10061/?time=731)
- [验证你的 XCFramework 的来源](https://developer.apple.com/documentation/Xcode/verifying-the-origin-of-your-xcframeworks)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10061/4/69744A23-9D87-4A87-B1D5-DC13BE88274F/downloads/wwdc2023-10061_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10061/4/69744A23-9D87-4A87-B1D5-DC13BE88274F/downloads/wwdc2023-10061_sd.mp4?dl=1)
- [隐私清单入门](https://developer.apple.com/videos/play/wwdc2023/10060)
- [Xcode 15 新变化](https://developer.apple.com/videos/play/wwdc2023/10165)
- [为 XCFramework 签名](https://developer.apple.com/videos/play/wwdc2023/10061/?time=877)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Kay：嗨，我是隐私工程团队的 Kay。我在这里向大家介绍 Xcode 中一个令人兴奋的全新隐私与安全特性，它会帮助你自动验证依赖的完整性。在 Apple，我们相信隐私应当处于每个人开发过程的核心，就像它是我们产品的核心一样。Xcode 内的依赖签名验证将帮助 App 开发者保护他们的 App，并帮助依赖作者保护他们分发的 SDK。

App 的开发需要用到一系列 SDK。例如 iOS SDK。有些由 Apple 出品，有些由 App 开发者编写供自己的所有 App 使用，还有些是 App 开发者从其他渠道获得的。这些共同构成了 App 的供应链，其中可能包括框架、Swift 源文件和其他类型的依赖。使用第三方 SDK 可以让 App 开发明显变得更轻松，还能提供扩展功能。然而，这确实会带来风险。

供应链安全就是化解这些风险的过程。你有责任通过谨慎选择要引入的依赖来保护你的用户，并确保你不会意外使用已被恶意篡改的版本。这份责任同样延伸到把其他 SDK 作为其开发一部分的 SDK 作者身上。用来化解这些风险的流程和工具如果手动操作，可能既繁琐又复杂。

依赖签名验证是 Xcode 的一个新特性，它可以让这项任务变得简单而自动。

既然你已经了解了什么是供应链安全，我将谈谈数字签名在保护开发者、减轻这一负担方面所扮演的角色。首先，我会概述 Apple 的代码签名技术是如何工作的，以及 Xcode 现在会做些什么来验证你的依赖的签名。然后我会谈谈 App 开发者可以如何使用这一特性来确保他们的依赖没有被攻破。最后，我会讨论 SDK 作者可以做些什么来提升生态系统的安全性。我从 Apple 的代码签名技术如何工作讲起。

当你在开发一个供 App 开发者使用的 SDK 时，你希望确保在它分发给你的 SDK 客户的过程中没有人能够修改或篡改它。代码签名是一种机制，它把最终编译出的二进制文件及相关元数据（例如你的框架的 Info.plist 或隐私清单，对于某些分发类型还包括源代码本身）以密码学方式与你的开发者身份关联起来。

从高层来看，代码签名的工作方式是：首先为你的编译后二进制文件生成一个代码目录哈希（Code Directory hash），也称为 CDHash。

然后，要对这个哈希进行签名，你使用你的开发者身份。这个身份由你的开发者证书表示。它由一把用于代码签名的私钥和一把随签名一起分发的公钥组成。这个签名可以追溯到你本人。这个身份随后被用来为哈希签名，并且可以与一个安全时间戳结合，用于验证签名是在某个特定时间点生成的。这确保了如果有人篡改了你的 SDK，签名将不再有效。它还允许 App 开发者使用内嵌在签名中的证书来验证签名者确实是你。

你在 App 中可能使用的一种常见依赖类型是 xcframework。对于 xcframework，签名位于 _CodeSignature 目录中。代码签名保护最终 xcframework 中所有文件的完整性，包括 WWDC23 视频「隐私清单入门」中提到的隐私清单文件。当然，你可以为你 App 中包含的每一个 xcframework 的每个版本手动验证这些代码签名，但这是一个耗时的过程，并且为了获得安全收益而给你带来了负担。签名验证是 Xcode 的一个新特性，它会自动处理你的 App 依赖的验证，并在检测到问题时通过警报来保护你的供应链完整性。Xcode 15 现在提供了工具，帮助你自动跟踪用于签名你项目中包含的任何 xcframework 的身份。

Xcode 现在在检查器（Inspector）中显示一个新板块，展示你 App 中包含的 xcframework 的签名状态。该板块包含有关签名的信息，例如作者身份。它会显示该 xcframework 是由 Apple Developer Program 身份签名的、由自签名证书签名的，还是目前完全未签名的。此外，Xcode 会在你首次使用该 xcframework 时记录其身份，并验证它在后续构建中不会发生变化。对于不同的开发者身份，Xcode 会根据对特定 xcframework 所用身份的信任程度提供不同级别的功能。对于 Apple Developer Program 身份，Apple 能够检查所用证书的有效性（包括它是否已被吊销），并确保多名开发者无法用同一个名称注册。如果所用的证书是自签名的，App 开发者应当直接与依赖作者确认其有效性与真实性。

当 xcframework 作者的签名证书过期时，对于 Apple Developer Program 身份，Xcode 能够自动验证新证书是否来自同一位开发者。对于自签名证书，你需要手动验证这一变更是合法的，因为没有像 Apple 这样的可信方为证书作担保。当依赖由 Apple Developer Program 身份签名时，Xcode 会在构建时进行验证，并在签名无效、身份发生变化、或 xcframework 是在证书过期之后才签名的情况下向你显示警报。如果 Apple Developer Program 证书已被 Apple 吊销，Xcode 也会发出警报。当 Apple 认定某个开发者账号是恶意的时就可能发生这种情况。这些警报会很少见，并且会自动确保你在解决问题之前无法构建你的 App。如果确实发生了这种情况，Xcode 会主动让你把该 xcframework 从项目中移除。对于自签名身份，Xcode 仍会比较该证书的 SHA-256 指纹与之前添加到项目中的那个。如果身份发生了变化，或者依赖的内容被修改过，它会向你显示警报。你可能需要联系 xcframework 作者以确认指纹与他们所使用的一致，或者 xcframework 作者可以自行公布这一信息。以上就是数字签名在 xcframework 上的工作方式。接下来，让我向你展示 App 开发者如何在 Xcode 中使用这一特性。为了演示，我将使用 Backyard Birds 示例 App。它提供一种数字观鸟体验：你拥有多个后院，可以放置鸟食和水，并观察鸟类访客何时出现。我打算使用一个名为 BirdFeeder 的 xcframework 来自动化喂食和换水的过程。BirdFeeder xcframework 的作者已经为最新的发布版本签了名。这里，我已经把 BirdFeeder 添加到了我的项目中。对于 xcframework，Xcode 15 会在检查器中提供一个「Signature」视图。它显示证书签名信息，包括团队详情。xcframework 开发者的身份会在首次见到时被存储到项目中。在构建期间，Xcode 会验证用于签名 BirdFeeder xcframework 的身份是否与项目中预期的身份相符。构建成功了。为了模拟一次供应链攻击，我将假装有人给了我一个更新版的 BirdFeeder xcframework，对方说它增加了许多激动人心的新功能并有更好的性能。当你从一个你不完全信任的网站下载 xcframework 时，同样的事情也可能发生在你身上。这里，我用这个更新版替换了我之前的版本。

当我构建我的 App 时，Xcode 会验证 App 中所有 xcframework 的签名。构建失败了，指出 BirdFeeder 开发者的身份与项目中先前记录的不符。选中该错误会给出一个警报，解释开发者身份已经改变，并展示预期身份与新版本中的身份的对比。在这个例子中，它显示预期的证书是一张 Apple Developer Program 证书，但项目中的这个使用的是自签名证书。这可能意味着该 xcframework 已被攻破，也可能这一变更是合法的。例如，他们可能把 xcframework 的所有权转让给了另一位开发者。如果你不确定，取消始终是安全的。这给了你时间去调查这一变更是否真实。Xcode 通过确保在这种变更发生时自动通知你来保护你和你的 App。

在这个例子中，这一变更并不在预期之内，所以我会在 Xcode 中把这个新版本移到废纸篓。然而，如果你知道这一变更是合法的——例如开发者已通过经过验证的公开渠道将此事告知你——那么你可以接受这一变更。

最后，我将谈谈这一特性对 SDK 作者意味着什么。对 SDK 作者而言，以密码学方式为 SDK 签名非常重要，因为它让 App 开发者能够确认身份，并保证代码在签名之后没有被更改或篡改。这两个属性对于建立信任和安全地分发 SDK 都极其重要。如前所述，你可以使用两种类型的身份：Apple Developer Program 和自签名。

Apple Developer Program 的成员应当使用该计划包含的证书，以确保你的 SDK 客户对你的信任。

如果你发布你的 SDK，应当使用 Apple Distribution 证书；如果你在分发测试版本，则使用 Apple Development 证书。Enterprise Program 的成员应当使用他们的 iOS Distribution 或 App Development 证书。当 Apple 向你签发证书时，Apple 是在证明你是 Apple Developer Program 的合法成员，并且已满足获取该证书的所有必要要求。这包括验证你的身份，以及你对 Apple 在隐私和安全方面的政策与准则的遵守。如果你手动吊销了用于为某个 SDK 签名的证书，你将需要发布一个使用有效证书签名的新版本，因为当开发者尝试构建他们的 App 时，Xcode 将不再能够验证该签名。使用 Apple Developer Program 证书签名的 SDK 具有一个基线级别的信任，并确保该 SDK 未被篡改。除此之外，由于 Apple 是可信的权威机构，当生成新证书时，证书验证会自动完成。在本视频的开头，我讨论了代码签名如何工作，以及它如何使用你的开发者身份在你的 SDK 中包含一个签名。现在让我们来看看如何使用 codesign 工具完成这件事。

你可以使用这里的命令和你的 Apple Developer Program 身份为你的 xcframework 签名。包含 timestamp 标志是为了确保签名含有由 Apple 担保的安全时间戳。不过，如果你不是 Apple Developer Program 的成员，你可以生成一个自签名证书，并将其用于 codesign 命令。你有责任把这个证书的指纹分享给你的 SDK 客户，以便他们可以验证该 xcframework 确实是由你签名的。在你的 App 中包含了你的 SDK 的开发者将能够使用 Xcode 中包含的这一新特性，确认该 xcframework 是由你签名的。如果你始终为你分发的 SDK 签名，Xcode 的这个新特性将帮助你的 SDK 客户对他们的供应链更有信心。做到这一点很简单。你可以直接从你已经发布的框架版本开始，无需任何新构建。即使你目前不是 Apple Developer Program 的成员，也可以使用自签名证书来完成。之后，你可以通过把 codesign 命令放入一个构建脚本，为你的 xcframework 的所有新版本都这样做，从此无需再操心。对于 App 开发者而言，Xcode 15 会自动帮助你确保 App 底层 SDK 的完整性与安全性。确保所有 SDK 签名都得到验证，是负责任的 App 开发和保护你的用户的重要一环。你可以通过鼓励你供应链中的开发者开始为他们发布的 SDK 签名来出一份力。对于 SDK 作者，请开始为你的 SDK 签名，以确保它们的安全性与真实性。通过为你的代码签名，你与你的 SDK 客户建立起信任，向他们表明你认真对待他们的安全与隐私。

祝 App 开发愉快！我是 Kay，就此收尾。♪ ♪
