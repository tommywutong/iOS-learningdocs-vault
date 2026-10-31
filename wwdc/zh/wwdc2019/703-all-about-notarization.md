---
title: 关于公证
session_id: 703
collection: wwdc2019
year: 2019
duration: '33:40'
topics: [Developer Tools, 'App Store, Distribution & Marketing']
group: F · Mach-O / dyld / 编译链接 / 启动优化
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2019/703/'
content_hash: 'sha256:362a589ad6652759'
translated: true
---

# 关于公证

<sub>WWDC2019 · 33:40 · Developer Tools、App Store, Distribution & Marketing</sub>

公证关乎在分发之前识别并拦截恶意的 Mac 软件，而无需经过 App Review 或 Mac……

> [!note] 归档理由
> 公证流程（macOS 分发）

## 相关资源

- [Xcode Help: Upload a macOS app to be notarized](https://help.apple.com/xcode/mac/current/#/dev88332a81e)
- [Resolving common notarization issues](https://developer.apple.com/documentation/Security/resolving-common-notarization-issues)
- [Signing Your Apps for Gatekeeper](https://developer.apple.com/developer-id/)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2019/703yqvyjv9mi5ur6/703/703_hd_all_about_notarization.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2019/703yqvyjv9mi5ur6/703/703_sd_all_about_notarization.mp4?dl=1)
- [Presentation Slides (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2019/703yqvyjv9mi5ur6/703/703_all_about_notarization.pdf?dl=1)
- [Simplify distribution in Xcode and Xcode Cloud](https://developer.apple.com/videos/play/wwdc2023/10224)
- [What’s new in notarization for Mac apps](https://developer.apple.com/videos/play/wwdc2022/10109)
- [Faster and simpler notarization for Mac apps](https://developer.apple.com/videos/play/wwdc2021/10261)
- [Port your Mac app to Apple silicon](https://developer.apple.com/videos/play/wwdc2020/10214)
- [Advances in macOS Security](https://developer.apple.com/videos/play/wwdc2019/701)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家下午好，感谢大家今天参加。

我是 Garrett，我在 Apple 的信任与执行团队工作，今天我们要谈的，是关于公证的一切。这是本次讲座的简要议程。我们先从公证是什么、它带来哪些好处的简要概述开始。

然后我们会讲到让软件获得公证时需要满足的应用要求。最后再过一遍公证软件时需要使用的流程与工具。我们开始吧。公证到底是什么？嗯，这是我们在去年的 WWDC 上引入的一种流程，用来在分发之前帮助识别并拦截恶意软件。现在它是 Developer ID 计划的扩展，这意味着你不需要注册任何不同的东西，也不用使用不同的证书，这也意味着你仍然像公证引入之前一样，掌握着软件的签名与分发控制权。

关键就在于 Notary Service，它会对 Developer ID 签名的内容执行自动化的安全检查。我们来过一遍，当你需要第一次开始为软件进行公证时，流程大概是什么样的。

这里有一张图，讲的是开发流程可能长什么样，而本地开发完全保持不变。你用 Apple Developer 证书在自己的桌面上构建并签名，直到得到一个发布候选版本。到那时，你用 Developer ID 证书对软件进行签名，并可以把软件的副本发送给 Apple Notary Service 进行公证。

当公证完成且成功时，Notary Service 可以把一张 ticket 发送回来，你可以在分发之前把这张 ticket 装订（staple）到软件上，一旦装订完成，软件就和之前一样可以分发了。

值得一提的是，这个流程和去年相比完全没有变化，这只是一个简要的回顾。去年我们没有谈到的是，当某人下载你的软件并首次使用时会发生什么。

所以当用户下载了你装订了 ticket 的软件并双击启动它时，Gatekeeper 会进行验证。

它会检查本地的 ticket，同时还会通过 CloudKit 联系 Notary Service 来检查是否存在 ticket。只要 ticket 检查通过并且 ticket 与你的 App 内容匹配，Gatekeeper 就会放行该应用，用户会看到正常的一次启动提示。

我还要提醒大家，公证不是 App Review。

Notary Service 执行的是一组自动化的安全检查。

去年我们设定了一个目标，让大多数 Notary Service 的响应在 1 小时内返回，而实际情况是过去一年里 99% 的提交在 15 分钟内就得到了回复。

另外，Notary Service 的状态现在也显示在 Apple 的公开状态页面上。所以你可以很容易地检查是否有任何服务问题会造成麻烦。公证有哪些好处？嗯，有很多。我今天只挑其中几项重点讲讲。第一，Notary Service 可以帮助你避免无意间发布恶意的依赖项。

第二，采用 hardened runtime 的 App 默认更安全，我们稍后会再多谈一点。这可以帮助防止你的 App 被攻击者滥用。

第三，用户更愿意下载并试用新软件，因为他们知道 Apple 已经扫描过已知的安全问题。最后，公证还会为你的 Developer ID 账户下所有经过公证的软件提供一个审计轨迹，你可以用它来检查提交历史，确保没有你并不打算从你的账户发布的软件被发布出去。这就是公证的简要概述。现在请 Robert 上来谈谈公证软件时需要满足的应用要求。

Robert。

首先我要说的是，对于你之前分发过的任何软件，它都不需要满足任何新的要求。你可以把现有已分发的软件原样提交进行公证，无需改动，但对于新软件，你需要确保它满足几项安全要求。特别是，它必须被完整且正确地签名，并且需要采用 hardened runtime。而所谓新软件，我指的是在 2019 年 6 月 1 日或之后签名的软件。

所以我们会详细解释我们所说的这两件事，也就是正确签名与 hardened runtime。首先，要完整地签名所有内容，你需要签所有东西。也就是 bundle、Mach-O、安装包，无论它们在哪里；无论你的 Mach-O 是否在安装包里，安装包是否在 bundle 里，它们出现在产品的任何位置，都需要被签名，而且需要被正确地签名。

要正确签名，意味着你必须用 Developer ID Application 证书对 bundle、Mach-O 和代码进行签名，我稍后会多谈代码，并且一定要包含安全时间戳。

对于可执行文件，它们需要选择启用 hardened runtime。你不需要为 dylib、framework 或 bundle 启用 hardened runtime，只需为可执行文件启用。

对于安装包，你需要用 Developer ID Installer 证书对它们进行签名，这和你的 Developer ID Application 证书不同，所以要小心。

另外，如果你选择对磁盘映像进行签名以避免 Gatekeeper 路径随机化，这些磁盘映像必须用 Developer ID Application 证书签名，并包含安全时间戳。所以如果你用 Xcode 构建软件，这很容易。如果你开启了自动代码签名，Xcode 会替你做所有这些，但你必须小心。如果你使用脚本构建阶段或复制构建阶段，这些可能会把 Xcode 不知道的新代码引入到你的软件中，这时你就必须确保那些代码被正确签名。我提到了代码文件。所以当几年前我们引入代码签名时，我们在技术说明中记录了这些叫做 code places 的东西。所以 bundle 内任何这些位置里找到的任何文件，都被代码签名基础设施视为代码，这意味着它们需要附加签名。Mach-O 对此最合适。你可以把签名嵌入到你放在这些位置的任何 Mach-O 中，bundle 也一样，但如果你放置其他类型的文件，比如 JPEG 或原始二进制文件，它们也必须签名，但它们不会得到附加签名，相反签名会最终成为扩展属性。这意味着在打包代码时你必须小心，以确保那个扩展属性保留在其中。为了避免不得不对这个太过小心，我们建议你在组织 App 时，把任何不是 Mach-O 或包含 Mach-O 的 bundle 的东西，放到这些位置以外的地方。所以为了在 Xcode 之外正确完成签名，我们推荐所谓从内到外的代码签名（inside-out code signing）。这意味着你先对 App 内最深层嵌套的 bundle 或代码进行签名。在这个例子里，它会是 Watching Grass Grow App 中 Sparkle framework 里的 updater.app，然后你向上一层，分别对各个东西进行签名。注意，当你单独签名 Sparkle framework 时，或者签名 Sparkle framework 时，它会一并拉取 Sparkle 主可执行文件以及 updater.app。注意你需要分别处理 Watching Grass Grow、savergrowgrass.dylib 和 Watching Grass Grow Helper。

最后，在你签名了所有这些东西之后，你在顶层 bundle 上把一切都签名在一起，这又会签名你的 Info.plist 所指示的主可执行文件和 bundle。

有些人会在自定义流程中使用 `--deep` 标志，但你需要小心。`--deep` 标志只在 code places 中查找代码，而在这个例子里，Grow Grass dylib、Watching Grass Grow Saver 和 updater.app 不会被识别为代码。它们会被作为资源签名进去，但不会作为代码签名，因此除非你额外做从内到外的签名，否则它们会被公证拒绝。

更多关于从内到外签名与 code places 的信息，请参见 Technote 2206。

所以一旦你完整且正确地签名了你的 bundle、你的软件，你必须确保不会让签名失效。这意味着除了在安装或更新期间，你永远不应该更改 bundle 中的文件；而更新时，确保更新的结果在客户系统上被正确签名并经过公证。现在我们要更深入地了解 hardened runtime。我们去年在 WWDC 上引入了 hardened runtime，现在我们会给出更多细节，讨论它的益处与配置。 hardened runtime 把 macOS 上我们拥有的许多系统完整性保护扩展到了你的 App。这意味着运行时代码签名强制、库验证、DYLD 环境变量保护与调试保护。注意所有这些保护在 iOS 上默认开启且不可配置，但在 macOS 上它们可通过任何开发者可以设置的 entitlement 来配置。所以如果你用 Xcode，采用 hardened runtime 很容易。只需前往签名与 capabilities 标签页，确保你的 target 上存在 runtime capability。

然后你可以用提供的复选框，选择你需要的 entitlement 来为项目配置 hardened runtime。如果你在 Xcode 之外使用自定义流程，你可以用 codesign 命令来采用 hardened runtime，为此使用 `--options runtime` 选项来 codesign，并确保也使用 timestamp 选项，以确保你的应用上有安全时间戳。要验证你是否正确采用了 hardened runtime，使用 codesign 的 display 选项，verbosity 级别为 2，并在 flags 部分查找 runtime 这个词。还要注意 hardened runtime 是有版本的。当你用 hardened runtime 签名时，我们记录你签名时使用的版本，这样如果未来我们向 hardened runtime 添加了额外的保护，我们会确保只有你的 App 已经测试过的那些保护才会应用到未来的系统上。

运行时代码签名强制是什么？它防止在你的进程内创建没有关联代码签名的可执行内存，并且通过首先确保所有映射到你的进程中的字节在从磁盘读取时匹配它们关联的代码签名来做到这一点，这不仅包括你的 Mach-O 的可执行区域，也包括你的只读 section 之类的非可执行映射。

我们阻止执行与签名不匹配的已修改内存。所以通过验证从磁盘读入的内存是正确的，并确保我们不能改变它，我们确保了进程在运行时的完整性。

在处理运行时代码签名强制时，一个可能出现的挑战是如果你的代码使用 JIT 来让你 App 内的非原生代码快速运行。为此我们推荐你使用 allow JIT entitlement，然后在你编译代码所用的读/写/执行内存分配时使用 MAP-JIT 标志。这让我们可以在系统内所有其他内存上保留其余保护，同时给你这块可随意使用的内存来处理 JIT 相关的事情。

如果你无法采用 MAP-JIT 标志，因为你的 JIT 引擎没有源代码访问权限，你可以使用 allow-unsigned-executable-memory entitlement。这会把运行时代码签名强制提供的安全预测降低到仅验证：对于每个有关联代码签名的内存块，你从磁盘读取的所有字节确实与之匹配，但它允许修改你进程内的任何内存，并允许创建未签名的可执行区域。

我们还看到一些开发者遇到的另一个问题是，他们在采用 hardened runtime 之后尝试修补已加载的某些系统框架。我们不推荐你这样做，你应该查看 hardened runtime 的哪些特性是否实际上解决了你这么做的原因。但如果需要，allow-unsigned-executable-memory entitlement 会允许你修改映射进来的那些内存页。

所以关于运行时代码签名强制，我们还看到出现的另一件事是，有些人会在更新 App 时遇到崩溃。这是因为代码签名在内核中首次使用时就锁定了文件，这意味着如果你修改了一个已经运行过且已签名的文件，它就不再匹配内核中存放的签名，你会看到代码签名违规。我们推荐的做法是，不要在磁盘上修改现有文件，而是始终创建一个包含更新改动的新文件，把旧文件移开。这将确保新文件在首次使用时获得其代码签名，而不会造成你看到的代码签名违规。

接下来我们谈库验证。

库验证通过确保你的 App 只加载由你的团队签名或由 Apple 签名的代码，来保护你的 App 免受代码注入与 dylib 劫持。有些人可能会问，为什么需要加载 Apple 签名的代码？记住，你从操作系统加载的所有 framework 与库都是 Apple 签名的。所以你必须能够调用它们并把它们加载到你的进程里。

注意库验证阻止加载未签名与 ad hoc 签名的代码。所以在开发过程中要小心。确保你使用 Apple development 证书，而不是关闭代码签名或只是使用 ad hoc 签名。

库验证会对那些有进程内插件或生态系统的 App 带来挑战。我们推荐你考虑迁移到进程外插件模型，这样你就不用把未知的第三方代码加载进你的 App，但如果你无法做到，你可以使用 disable-library-validation entitlement，这将允许加载未签名与 ad hoc 签名的插件。注意你可以单独使用它，而不使用任何运行时代码签名强制相关的 entitlement：当系统看到你正在加载 ad hoc 签名或未签名的插件时，它会降低你进程的安全性以允许这种情况，因为你说过你想加载未签名的插件。

接下来是 DYLD 环境变量保护。DYLD 环境变量在开发过程中可能非常有用，可以在测试时把调试库加载进你的 App，或者使用你正在构建但还没准备好构建进 App 的库或 framework，只是为了测试它们，但它们可能很危险，因为你在构建与测试过程中能做的一切，攻击者在客户系统上也能做，以利用你的 App 可用的权限或数据。

因此，hardened runtime 默认会阻止这些变量在你发布时使用。如果你需要在调试过程中使用 DYLD 环境变量，你可以对调试构建使用 get-task-allow entitlement，注意 Xcode 会在你构建调试版本时自动加上它，在你构建发布版本时自动去掉它。但注意，如果你使用自定义流程，Notary Service 在大多数情况下不接受带有 get-task-allow entitlement 的二进制文件。所以确保在把发布构建提交给 Notary Service 之前移除这个 entitlement。

在少数情况下，我们看到开发者在向客户发布 App 时需要使用 DYLD 环境变量，再次强调，我们不推荐你这么做。这在客户系统上利用你的 App 时可能非常危险，但如果你需要，有一个 allow-DYLD-environment-variables entitlement 可以允许它们使用，并且会被 Notary Service 接受。接下来是调试保护。我们都知道调试器允许开发者检查寄存器与内存的状态并修改进程内存。这意味着它们允许黑客窃取敏感的用户数据并注入恶意代码。因此，默认情况下 hardened runtime 不允许调试 hardened 进程，但如果你需要在开发流程中使用调试器，再一次，get-task-allow entitlement 是你需要的。与 DYLD 环境变量一样，get-task-allow entitlement 允许你的 App 被调试。

但要小心，如果你所有的测试都是在调试器附加的情况下进行的。这会掩盖其他你可能遇到的与 hardened runtime 相关的问题，特别是围绕运行时代码签名强制的问题。基本上，一旦调试器附加，我们就不能再强制代码签名了，因为像自动设置断点这样的调试器会改变你进程内的数据，如果我们继续强制执行，它们会立即崩溃。所以确保测试一个发布构建，看看运行时代码签名强制还可能产生什么其他影响；然后如果你需要通过 Xcode 制作一个不带 get-task-allow 的调试构建，你可以使用 Xcode 项目中的 `CODE_SIGN_INJECT_BASE_ENTITLEMENTS=NO` 选项，来获得除 get-task-allow 之外的所有调试设置。

这在插件生态中也可能是一个挑战，因为插件开发者需要在要加载它们的 App 内调试插件。所以再一次，我们推荐考虑进程外插件模型，或者考虑发布一个调试版本的 App 给插件开发者，让他们有调试的能力，但你不要把那个发布给所有客户；但如果绝对必要，Notary Service 会接受 get-task-allow entitlement 与 disable-library-validation entitlement 的组合，来允许这个流程。

我们简要谈谈受保护的资源访问。

我们都知道，你的客户用他们的 Mac 存储了关于他们生活的大量信息，而 Mac 可以访问安全敏感的传感器。

为了……或者一旦你采用了 hardened runtime，你的 App 需要声明它打算访问任何这些受保护的资源。

所以我们去年就提到了，但如果你需要访问这些资源，你需要在主 bundle 上取用 entitlement，然后声明与该 entitlement 关联的 usage string，这样当你的 App 尝试访问这些资源之一时，系统可以弹出一个对话框，说，哦，这就是我需要访问这个资源的原因，以便你能收集用户的同意。

所以一些建议，本节的总结。只取你需要的 entitlement。Entitlement 会关闭 hardened runtime 提供的安全性，而且任何人都可以查看你的 App，试图看清一旦发布到客户那里，他们可以用它做些什么。所以要小心，只取你需要的，把 entitlement 只放在需要它们的进程上。如果你有多个进程、App 内的多个可执行文件，不太可能所有这些都需要相同的保护。你大概不会在每个进程里都做 JIT，大概也不会在每个进程里都加载插件。所以只在需要它们的进程里取用需要的那些；而声明资源访问时，确保这些 entitlement 只在你的 App 的主 bundle 上。它们会被其他可执行文件继承，它们不需要到处都是，只需在主 bundle 上。现在我把时间交还给 Garrett，介绍你实际需要做什么来提交公证。谢谢，Robert。现在你知道了在构建与设计应用时需要考虑的一切，以让它准备好进行公证，但你实际上如何把软件提交给 Notary Service？嗯，我们来谈一点关于公证流程，无论你用 Xcode 还是自定义构建流程，大概流程都差不多。

你提交 App 进行公证，检查 Notary Service 的状态。一旦公证完成，你可以装订 ticket，然后完成后你可能想验证装订与公证是否成功。在我们进一步谈之前，应该先谈提交什么、何时提交，至少你应该提交你分发的所有软件，但真的也可以更频繁地上传，任何在开发者机器之外运行的东西都可以随时上传给 Notary Service。你大概不需要上传每个 CI 构建，团队中的任何人都可以提交软件进行公证。这和去年不同，去年它被限制在特定角色。

所以现在你准备好提交给 Notary Service 了。嗯，如果你用 Xcode，这相当容易，它已经内建到 archive 与分发流程里。所以一旦你构建了一个 archive，你可以打开 Xcode organizer，像你之前用 Developer ID 那样，选择 distribute app。

选择 Developer ID，然后使用 upload 选项把副本提交给 Notary Service。上传期间你会看到一个进度条，完成后你会回到 organizer，你会注意到状态已经变为 processing。一旦 Notary Service 完成，它会向 Xcode 发送推送通知，当你回到 organizer 时，你会注意到状态已经变为 ready distribute，并且右下角的 export notarized app 现在可用。

当你点击 export notarized app 时，Xcode 会替你装订 App，你得到的就是完全准备好分发的东西。

现在我们稍后会谈一点你自己如何验证，因为那是自定义流程与 Xcode 共享的步骤。

现在，如果你不用 Xcode，使用自定义流程提交同样容易。第一件事你需要考虑的是，你想提交什么给 Notary Service。

Notary Service 接受 3 种主要格式：磁盘映像、安装包与 zip 归档。所以如果你的构建输出不是这 3 种之一，你需要在发送给 Notary Service 之前把它转换为这 3 种之一。并且记住，当你创建 zip 归档时，包含 macOS 特定的元数据（如扩展属性）很重要。如果你不知道该用什么工具，操作系统内建的 ditto 与 Archive Utility 都支持。

还有一件事需要考虑，就是如果你有自定义安装器，自定义安装器可能有点棘手，如果它们在安装过程中从 Internet 拉取内容，或者你使用自定义打包格式。

如果你的自定义安装器做了这些事情之一，你可能需要执行两步公证，也就是把你最终会落盘的所有内容，使用 3 种支持的格式之一提交进行公证，装订它，然后你再单独提交你的自定义安装器 App。所以现在你知道你想提交什么给 Notary Service 了，如何实际做到？嗯，Xcode 10 及更新版本包含一个名为 altool 的命令行工具，通常用于与 Notary Service 交互。如果你有多个版本的 Xcode，你会想用 Xcode select 确保你选择了 Xcode 10 或更新版本，然后你可以用 altool 的 notarize-app 命令。

你需要传入主 bundle ID 以及你想上传的文件。

你需要用 Apple ID 进行认证，但如果你看主页面，你会看到使用 keychain 或环境变量的选项，所以你不必总是输入密码。公证上传完成时，你会得到一个 RequestUUID。这是一个代表你提交的 UUID，你可以转而与 altool 的 notarization-info 命令一起使用，来检查处理状态，这就是你如何发现公证何时完成以及状态是什么。

这是成功公证的一个例子，其中一件重要的事是日志文件 URL。无论公证成功还是有问题，你都可以查看日志文件 URL 了解更多信息。现在日志文件 URL 不是长期有效的。

它们只有效大约一天。所以你大概想在每次调用 notarization info 时传入一个新的 UID，你就会得到一个新的日志文件 URL。

这是成功处理的一个示例 JSON 日志。

注意 status 是 accepted。

现在如果失败了，你真正想看的是 issues 数组。

在成功的公证中，这通常为空。

但如果出了什么问题，这里会有对象，每个都代表公证过程中的一些失败。它会指出诸如哪个二进制可能没有采用 hardened runtime，或者如果什么东西没有被正确签名。

所以如果有任何被拒绝，这将是关键。如果成功，你可能想查看 ticket contents，特别是如果你围绕软件打包做了任何有趣的事情。ticket contents 应该列出 Notary Service 发现的每个二进制，因此也列出包含在你将装订的 ticket 中的每个二进制的信息。

所以如果你注意到 ticket contents 中少了什么，你可能需要试图弄清楚出了什么问题并重试。

现在，无论你用 Xcode 还是 altool，当 Notary Service 完成处理一个提交时，你都会收到一封邮件。这是成功邮件的一个例子，表明这个软件已准备好装订。这把我们带到下一步。

装订使用的是 Xcode 10 及更新版本内建的另一个名为 Stapler 的工具。这里你可以看到 stapler 的一个调用示例，使用 staple 命令可以直接装订到 package 或磁盘映像。注意你不能直接装订到 zip 文件，所以你需要解压 zip 文件，装订 zip 文件的内容，然后你可以重新打包以便分发。注意命令行工具与库的装订目前不支持，即使这些项目仍然可以且应该进行公证。

装订之后的下一步是验证一切是否成功公证，这一步根据你想验证的内容会略有不同，但第一件事很简单。如果你真的只想检查某物是否被装订，你可以再次使用 Stapler 工具。这里你可以看到 stapler 工具与 validate 命令来检查一个项目是否被正确装订，但如果你想验证你没有自己装订或没有提交装订的东西的公证呢？嗯，那你一般会想使用 SPCTL 命令，这是 macOS 内建的运行 Gatekeeper 评估的工具。这会根据你想检查什么而略有不同，但如果你想检查一个应用 bundle，你可以使用 SPCTL 命令与 assess 选项、verbose 输出和指向 App 的路径。

source 会告诉你它是否被公证。

Notarized Developer ID 意味着它被成功公证，如果显示其他任何内容，就意味着它没有被公证。如果你反而想检查一个安装包的公证，你可以像之前一样使用 SPCTL 命令，但加上额外的 type 选项并传入它是 install。

这会向你显示相同输出，如果它被成功公证，你会看到 notarized developer id。

接下来如果你想检查已签名磁盘映像的公证呢？嗯，你可以使用相当相似的命令，只是现在你想使用 type open 并且需要传入幻灯片上列出的 context。

这会向你显示和之前相同的输出，如果它说 notarized Developer ID，那么那个已签名磁盘映像的公证就是成功的。

如果你想检查其他任何东西的公证状态，你需要回退到使用 codesign 命令。

这是使用 codesign 命令与 verify 函数、verbose 输出、测试一个非常具体的 requirement notarized，然后指向你想检查的二进制或东西的路径，输出的第三行会说 explicit requirements satisfied，表明你在命令行传入的测试 requirement 被成功满足，这在这种情况下意味着该二进制被公证了。

如果它说 explicit requirement failed，那意味着该二进制没有被成功公证。

这就是关于验证公证的一切。我想跳回来强调一下我在演讲开头提到的 altool 的另一个用法。

Altool 也能够使用 notarization history 命令，给你账户下所有提交进行公证的软件的公证历史。

这里你可以看到命令的一个例子和输出的一个例子。它还接受分页，以便你可以翻阅所有已作出的提交。

我知道在一篇简短的讲座里要消化大量信息，但有几件重要的事情我真的希望你们从这次对话中带走。

第一，使用从内到外的代码签名正确签名你的软件真的很重要。这不仅是为了让 Gatekeeper 能验证你的软件没有被篡改，也是为了公证。

第二，不要取你不需要的 hardened runtime entitlement。想想 hardened runtime 为你的 App 和你的用户提供的益处，记住你取的每个 entitlement 都会降低你应用的安全性。所以只取你需要的那些。

最后，公证并装订你分发的所有软件，以便它能在 macOS Catalina 上通过 Gatekeeper。

感谢参加，如果你有兴趣进一步讨论公证，请到本次 session 之后立即 4 点开始的公证 lab。另外，整个星期还有几个 lab 可以讨论更多关于安全、公证与签名的内容。谢谢。[ Applause ]
