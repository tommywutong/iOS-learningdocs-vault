---
title: Foundation 的新进展
session_id: 723
collection: wwdc2019
year: 2019
duration: '15:54'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2019/723/'
content_hash: 'sha256:b79a147048a2f1fe'
translated: true
---

# Foundation 的新进展

<sub>WWDC2019 · 15:54 · System Services</sub>

Foundation 框架为 App 和框架提供一层基础功能，被 macOS、iOS、watchOS……

> [!note] 归档理由
> Foundation 底层进展（Unicode、Data）

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/723ijngq6f3vi97/723/723_hd_advances_in_foundation.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/723ijngq6f3vi97/723/723_sd_advances_in_foundation.mp4?dl=1)
- [演示文稿 (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2019/723ijngq6f3vi97/723/723_advances_in_foundation.pdf?dl=1)
- [Combine 与 Foundation 进展介绍](https://developer.apple.com/videos/play/wwdc2019/711)
- [macOS 的 AppKit 新变化](https://developer.apple.com/videos/play/wwdc2019/210)
- [文件管理与快速查看的新变化](https://developer.apple.com/videos/play/wwdc2019/719)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我叫 Tina，是 Foundation 团队的一名工程师。我要介绍我们添加到 Foundation 的新 API 的亮点。现在，让我们从 API 亮点开始。今天我们要谈的内容多种多样。

我们先从有序集合差异（Ordered Collection Diffing）讲起。它是一个 API，让你可以在集合之间计算差异、对差异编码并应用差异。为了说明这一点，我要讲个小故事。有一个“熊”（bear）字符串，非常想变成一只“鸟”（bird）。我们来看看怎么做。我们注意到，熊有一个鸟没有的 E 和一个 A，而它还需要鸟的 I 和 D。

那么我们就移除 E 和 A，在中间插入一个 I，在末尾插入一个 D。

就这样，用了两次移除和两次插入，把熊变成了鸟。

用有序集合差异 API，你可以非常轻松地做到这一点。

这里的差异是一个 CollectionDifference 类型。它是一个由插入和移除组成的集合，描述被插入或被移除的元素，以及该元素在集合中的偏移量。正如我们刚才看到的，这里包含两次插入和两次移除。我们可以把这份差异应用到熊上，得到新的鸟字符串。这是一个非常强大的 API，不仅适用于字符串，也适用于任何集合类型。这就是有序集合差异。接下来谈谈数据与连续性。

你的 App 可能会从磁盘构建图片或其他类型的文件。通常这些形式的数据可以很容易地用内存中一段连续的区域表示。

另一方面，你的 App 可能正通过 dispatch data 或 URL session 之类的东西从互联网下载数据。这产生的字节会在不同时间分多个数据块到达，占据内存中这些不连续的区域。

在 Swift 5 之前，struct Data 同时表示连续和不连续的区域。这种统一接口用起来很简单，但也意味着，为了提供对底层原始字节的整段缓冲访问，我们需要把这些区域复制到一个连续的区域里。这意味着性能有时可能不可预测。事实上，我们考察了 Data 的真实使用情况，发现每一个不连续的 Data 在其生命周期的某个时刻都会被展平。

所以从 Swift 5 开始，我们承诺 struct Data 是一种连续缓冲类型。为了在语法上体现这一承诺，我们引入了 ContiguousBytes 协议。

在类型提供对底层原始字节的连续直接访问的情况下，遵循该协议即可。这样你就不用担心不小心把你的数据展平了。那么，我们要如何与其他不承诺连续性的缓冲类型协作呢？我们把 struct Data 的接口中与连续性无关的部分抽取出来，推广到各种缓冲类型上，得到了两个新协议：DataProtocol——一个字节集合，以及提供额外可变性保证的 MutableDataProtocol。

由 Foundation、Swift 标准库和 dispatch 框架提供的缓冲类型都已经遵循了这些协议。你大概已经用过其中一些类型了，包括 Data、UInt8 数组和 DispatchData。

我们鼓励你也在自己的类型或方法上采用它们，作为泛型约束使用。

现在，我们来谈谈压缩。

很多时候，你想让你的数据尽可能小。可能是你的应用运行在磁盘空间有限的设备上，或者你需要向互联网发送资源或从互联网接收资源。

这是一项非常常见的任务。所以我们把压缩 API 加入了 Swift 的 Data。现在它简单到——谢谢——简单到只需这一行代码。

该 API 还支持四种压缩算法，在速度、内存和压缩比之间提供不同的平衡。我相信你能找到最适合你需求的那一种。

接下来是单位。Foundation 已经支持 21 个类来表示常见的物理单位，例如长度、速度和时长。

我们为时长单位类扩展了亚秒级精度的单位，最小到皮秒。那是一万亿分之一秒。

频率单位类目前以赫兹为基本单位，今年它增加了 framesPerSecond。它在功能上与赫兹等价，但其明确的语义让它非常适合表示设备上的 FPS 测量值。

UnitInformationStorage 类是新的。它可以用来表示数字信息的量。基本单位有比特、字节和半字节（nibble）。从 kilo 和 kibi 到 yotta 和 yobi 的常用 SI 前缀和二进制前缀单位也都支持。

你可以把它与 MeasurementFormatter 一起使用来格式化，比如说，数据大小；如果你想要更精确的控制，也可以与 ByteCountFormatter 一起使用。我们还为你准备了更多格式化器。你大概每天都在某处见过这样的字符串。比如，你发送的一条消息的状态是“1 小时前已读”，或者“明天有一笔付款到期”。也就是以相对当前时点的方式显示的日期或时间。

要让它在所有语言环境中都正确并不简单，所以我们添加了 RelativeDateTimeFormatter 来帮你。

谢谢。与其他格式化器一样，返回的字符串是符合语言环境习惯的，而且有多种样式可供使用。

你可能还想格式化的另一件事是列表，我们也为此添加了 ListFormatter，让你轻松搞定。它会把一个列表格式化为一个字符串，并为所有语言环境使用正确的分隔符和连接词。

还有另一个例子。假设有一个活动将在三个不同的日期举行。你可能想在你的活动页面上显示像上面或下面这样的字符串，把月份名称完整写出来。

当然，你会希望针对不同的语言环境使用正确的格式和本地化的名称来显示。这很重要，因为举例来说，在欧洲，书写时通常是日子在月份之前。

用 ListFormatter 同样可以轻松做到。

它带有一个叫 itemFormatter 的属性，作用是格式化列表中的每一个条目。在这个例子里，我们要格式化一个日期列表，而我们知道 Foundation 支持用 DateFormatter 做日期格式化。那就用它作为我们的日期 itemFormatter。

这就是我们需要的全部。一切就绪。

它会像底部的示例那样，给你本地化的字符串。

你可以通过设置 DateFormatter 上的属性轻松更改日期样式。ListFormatter 可以与所有格式化器配合使用，所以请善用它，让你的应用中的字符串本地化做得更好。

这就是格式化器部分。接下来是 Operation Queue。

想象一下你的应用里有一堆后台任务正在并发运行。此时用户想保存这个正在运行的 App 的状态，你会怎么做？嗯，你要确保所有正在运行的任务都完成之后才能保存。所以你可能很想写出这样的代码。

也就是检查并发队列中正在运行的操作数量，如果一个都没有，那一定意味着我们调度的所有任务都已完成。所以我们准备好保存了，对吧？不，这是错的。请不要这么做。

有可能在同一时刻，其他任务正在所有线程上被调度，比如恰好在校验通过之后、保存发生之前。你在这里真正想要的是一个屏障（barrier），来保障安全操作，并确保在保存 App 的过程中没有其他任务可以运行。

像这样。所以我们非常高兴地告诉大家：Operation Queue 现在支持屏障了。你应当添加 BarrierBlock，并把你的保存操作放进屏障里。这能保证在那一特定时间段内，保存操作是唯一在运行的任务，而且它只会在之前调度的所有任务都完成后才执行，并且在它完成之前不会有其他新任务运行。我们对 Operation Queue 的另一项更新是进度报告。有时你可能想跟踪并发任务的整体进度，也许还要在 UI 里显示一个进度条。现在你可以通过在 Operation Queue 的 progress 属性上设置 totalUnitCount 来做到。

你添加到 Operation Queue 的每个操作，都会在完成后为整体进度贡献一个完成单位。

下一个：文件系统。iOS 现在支持 USB 和 SMB 卷了，SMB 是一种网络文件系统。这意味着你应当准备好处理可能存在于其他卷上的文件。所以，在执行“原子安全保存”（Atomic Safe-Save）操作、选择写入新文件内容的位置时，请务必使用 FileManager 的 itemReplacementDirectory。

其次，要有心理准备：如果用户拔出 USB 驱动器，或者你失去与 SMB 服务器的网络连接，卷可能会彻底消失。

所以如果你在读数据对象时选择了内存映射文件，请确保使用 mappedIfSafe 作为读取选项。这会让系统把文件映射进虚拟内存，但前提是文件位于不可移除的卷上。从 USB 或 SMB 驱动器访问文件可能比访问内置驱动器上的文件明显更慢。

如果你还没有这么做，请把文件系统访问推迟到非主线程，以确保你的 App 保持响应。你可能需要在使用某些文件系统能力之前先测试它们。比如，你所熟悉的那些 APFS 特性（例如克隆）在通过 USB 或 SMB 访问外部卷时可能不可用。

你可以用各种 URL 资源键在事件中测试这些能力，或者确保你已准备好处理并接收错误。

你可以在“文件管理与快速查看的新变化”那场演讲中找到更多相关信息。

接下来是 Swift 更新。

一些 Swift API 最初设计时考虑的是 Objective-C，多年来我们持续改进它们。第一个是 scanner。这是 Swift 4 里的 API。它过去使用 NSString，并通过引用返回对象。

在 Swift 5.1 中，我们把这一接口简化成了这一行代码。

更重要的是，新 API 使用 Swift 的字符串类型，因此字符串是字素（grapheme）的集合而不是码位的集合。这意味着你现在可以用新的 scanner API 完美地处理复杂序列，比如表情符号。

另一项改进是 FileHandle。它过去在底层文件描述符发生错误时会抛出异常。今年我们引入了基于错误的 API，所以你现在可以在调用处立即处理错误。写数据的 API 现在也能配合 DataProtocol 使用。它还针对非连续数据做了优化。

以上就是新 API 的亮点。我们鼓励你获取新的 Xcode，试一试这些激动人心的特性。

在编写处理二进制数据的新方法时，考虑把它们约束在 DataProtocol 类型上，而不是要求特定的集合，比如 UInt8 数组。

如果你在 UI 里用字符串显示日期或列表，请使用 RelativeDateTimeFormatter 或 ListFormatter，确保字符串在每种语言环境中都正常。我们敦促你使用 Operation Queue 的屏障来避免竞态条件。如果你正在使用某种进度报告机制，请改用 Operation Queue 提供的那一种。谢谢。［掌声］
