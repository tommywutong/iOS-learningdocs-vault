---
title: 'Foundation 新变化'
session_id: 10109
collection: wwdc2021
year: 2021
duration: '37:35'
topics: [Essentials, System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10109/'
content_hash: 'sha256:70bc1d3071ca3d6e'
translated: true
---

# Foundation 新变化

<sub>WWDC2021 · 37:35 · Essentials、System Services</sub>

了解 Foundation 的最新更新如何帮助你改进 App 的本地化与国际化支持。了解……

> [!note] 归档理由
> Foundation 更新（AttributedString、格式化）

## 相关资源

- [Foundation](https://developer.apple.com/documentation/Foundation)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10109/5/31B61A71-9D39-4F29-97DF-66309DBA320E/downloads/wwdc2021-10109_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10109/5/31B61A71-9D39-4F29-97DF-66309DBA320E/downloads/wwdc2021-10109_sd.mp4?dl=1)
- [释放语法一致性的威力](https://developer.apple.com/videos/play/wwdc2023/10153)
- [Swift 正则表达式：进阶](https://developer.apple.com/videos/play/wwdc2022/110358)
- [本地化你的 SwiftUI App](https://developer.apple.com/videos/play/wwdc2021/10220)
- [认识 AsyncSequence](https://developer.apple.com/videos/play/wwdc2021/10058)
- [简化你的本地化字符串](https://developer.apple.com/videos/play/wwdc2021/10221)
- [SwiftUI 新变化](https://developer.apple.com/videos/play/wwdc2021/10018)
- [AttributedString 基础](https://developer.apple.com/videos/play/wwdc2021/10109/?time=170)
- [AttributedString 字符](https://developer.apple.com/videos/play/wwdc2021/10109/?time=264)
- [AttributedString Run（第 1 部分）](https://developer.apple.com/videos/play/wwdc2021/10109/?time=312)
- [AttributedString Run（第 2 部分）](https://developer.apple.com/videos/play/wwdc2021/10109/?time=349)
- [AttributedString 变更](https://developer.apple.com/videos/play/wwdc2021/10109/?time=396)
- [本地化字符串](https://developer.apple.com/videos/play/wwdc2021/10109/?time=449)
- [可 Codable 的 AttributedString](https://developer.apple.com/videos/play/wwdc2021/10109/?time=574)
- [Markdown 可解码属性](https://developer.apple.com/videos/play/wwdc2021/10109/?time=642)
- [自定义 Markdown 语法](https://developer.apple.com/videos/play/wwdc2021/10109/?time=690)
- [自定义 Markdown 属性](https://developer.apple.com/videos/play/wwdc2021/10109/?time=747)
- [属性作用域](https://developer.apple.com/videos/play/wwdc2021/10109/?time=795)
- [格式化日期](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1048)
- [使用样式格式化日期](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1096)
- [格式化日期：更多示例](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1116)
- [格式化时间间隔](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1230)
- [演示：SwiftUI 与 AttributedString](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1299)
- [解析日期](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1433)
- [解析日期：策略](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1463)
- [格式化数字](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1530)
- [使用样式格式化数字](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1536)
- [格式化列表](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1547)
- [收据提示视图](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1565)
- [自动语法一致](https://developer.apple.com/videos/play/wwdc2021/10109/?time=1781)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我叫 Tony，是 Foundation 团队的工程师。欢迎来到「Foundation 新变化」。Foundation 框架为所有 App 和框架提供基础功能，包含从文件处理到网络、通知在内的诸多特性。今天我想聚焦于所有 App 都需要的东西：国际化与本地化。在今年的版本中，我们在这个 API 上取得了有史以来最大的进步之一。我们从底层开始，重新思考了 Swift 中 attributed string 的含义；为 Swift 重建了格式化器，使其更快、更易用，并增加了新功能；最后，我们还带来了名为自动语法一致（automatic grammar agreement）的全新特性。它能大幅减少你需要提供的本地化字符串数量，同时让代码更简洁。让我们直接进入 attributed string。attributed string 是字符、一组范围和一个字典的组合。它允许你把属性（键值对）关联到字符串的特定范围。最常见的属性由 SDK 定义，但你也可以创建自己的属性。你经常会发现在支持富文本的 API 中使用 attributed string。来看一个例子。这是我正在开发的一个名为 Caffé 的 App，它是一个简单的菜单。我挑选想要的食物、尺寸和数量，最后它会显示一张包含所有已点内容的收据。底部这里，我加了一小段感谢语。这就是一个 attributed string：字符串的一部分是粗体，一部分是斜体，最后一个词还有链接。如你所见，属性可以重叠。自 Foundation 诞生以来，我们就有一个名为 NSAttributedString 的引用类型。今年，我们引入了新的结构体 AttributedString，它充分利用了 Swift 提供的所有特性。首要的一点是，它是一个值类型；它还与 Swift String 具有相同的字符计数行为。作为我们致力于让编写包容性软件更简单的承诺的一部分，AttributedString 现在完全可本地化。最后，它在设计时就考虑了安全与保障，包括通过强类型实现的编译期安全，以及使用 Codable 在反归档时的安全性。让我们快速浏览一下新的 AttributedString 能做什么。我们来构建感谢信息。首先，用一个简单的初始化方法创建一个 attributed string。我想给整个字符串设置一个属性，只需设置 font 属性即可。在结构体 AttributedString 中，所有属性都可直接访问，并使用正确的类型；例如这个属性就是 SwiftUI 的 Font。接下来，我们创建另一个 attributed string，它是我们网站的引用，因此把 link 属性设置为一个 URL。这里我对整个字符串设置了 font 和 link。稍后我们会看如何只改变字符串的一部分。另一个有用的工具是属性容器（attribute container）：它可以在不附着到字符串任何特定字符的情况下保存属性。这里我创建一个容器，并根据消息的重要性设置一些属性。最后，我把这些属性合并到两个 attributed string 中。如前所述，attributed string 是字符、范围和字典的组合；attributed string 本身并不是这些任一集合的集合。为了访问这些属性，它有所谓的视图（view）。最重要的两个视图是 characters（提供对字符串的访问）和 runs（提供对属性的访问）。这些视图都是 Swift 集合，因此你熟悉的 Array 等类型上的函数在这里也同样可用。再看一个例子。假设设计师告诉我们，给感谢信息加点趣味，把所有标点符号变成有趣的橙色。为此，首先我需要找到 attributed string 中标点所在的位置。像其他 Swift 集合一样，attributed string 的视图使用索引（index），它只是集合中某个元素的位置。为了按索引迭代，我使用标准库的 indices 函数。接下来，我用 isPunctuation 检查这个字符是否是我们需要改变的。最后，我使用 attributed string 的另一个特性——切片（slicing）——把属性应用到整个字符串的子范围上。范围从这个索引开始，持续到下一个索引之后，也就是一个字符。现在标点符号变成橙色了。再看另一个视图：runs。run 是某个属性的起始位置、长度和值。我们可以先统计消息中的所有 run。这会迭代字符串中每个属性值连续的范围。这个字符串里有四个 run。每个 run 对每个属性都有一个值或 nil。characters 和 runs 的范围可以互换，因此你可以找到某个属性的字符串，反之亦然。这里我用属性的范围作为 characters 视图的下标，把结果转换成独立的字符串。按特定属性聚焦 run 往往最有用。这里我们用键路径 link 只合并 link 属性。结果集合中的每个元素都会给出 link 属性的值，不考虑字符串中可能设置的其他属性。如果只看 link，我们有三个 run：第一个未设置；第二个设置为某个值；第三个是句末的句号，再次未设置。迭代 run 会得到值与范围的元组。由于值是类型安全的，我们可以使用 URL 上的 scheme 这类 API，而无需强制转换或担心类型错误。这里我检查 attributed string 中的每个链接是否都是 https。另一个有用的技术是查找子字符串，并用该范围编辑字符或属性。假设我想把单词「visit」替换为更有复古感的词。首先，我查找子字符串的范围。接下来，我用该范围只设置该子范围的属性与字符。结果是一个有六个 run 的 attributed string，如下所示。接下来聊聊本地化。AttributedString 完全可本地化；我们也在 Objective-C 中为 NSAttributedString 增加了本地化支持。attributed string 与普通字符串一样，位于 App 的 strings 文件中。在 Swift 中，我们现在支持使用字符串插值来本地化格式化 String 和 AttributedString，就像 SwiftUI 的 Text 视图一样。这里是一个简单示例：这个函数返回一个用用户文档名自定义的本地化字符串。你不再需要使用 %@ 或 %d 这类格式说明符并调用格式化函数，可以直接传入值。同样的方法也适用于 AttributedString。Xcode 可以使用编译器从这些新的初始化方法生成 strings 文件。要开启它，进入构建设置，找到本地化设置，打开「Use Compiler to Extract Swift Strings」。你可能会好奇，本地化的 attributed string 是如何获得其属性的。我很高兴地告诉你，我们为 AttributedString 增加了 Markdown 支持。这里是一个直接在 SwiftUI Text 中使用本地化 attributed string 的示例。我从一个纯字符串开始。在文本两侧加上两个星号，我把它设为强强调，SwiftUI 会把它渲染为粗体。我可以使用下划线把它设为强调，SwiftUI 会把它渲染为斜体。我们还支持链接。这对本地化人员来说是提供不同语言自定义 URL 的绝佳机会。我们还支持其他内联样式，如删除线和代码字体。最后，聊聊归档 attributed string。首先，我们需要能够在引用类型 NSAttributedString 与之相互转换。attributed string 可以成为数据模型的一部分，这意味着我们需要能够编码和解码它。最后，我们希望有一种在 Markdown 中指定自定义属性的方式。这些操作彼此相关。先从转换开始。我们都写过大量使用 NSAttributedString 的代码，因此我们让从结构体转换为类类型变得很容易。这里有一个具有 NSAttributedString 属性的视图。要转换，只需把结构体 AttributedString 传给 NSAttributedString 的初始化方法。对于 SDK 提供的属性，这就是我需要做的全部。现在看编码与解码。这里有一个保存 Caffé App 收据的结构体。同样，我使用的是 SwiftUI、UIKit、AppKit 和 Foundation 提供的属性，这意味着 AttributedString 的默认 Codable 实现就是我需要的全部。我只需给 Receipt 添加 Codable 一致性，就完成了。让我们再进一步，增加对编码自定义属性的支持。我们先从属性本身谈起。属性由两部分组成：键和值。键是一个符合新 AttributedStringKey 协议的类型，它定义了所需的值类型以及归档时的名称。这个键还可以符合其他协议，以自定义值的编码或解码方式。假设我们想把 attributed string 的某个范围定义为具有额外颜色。这种彩虹效果有三个级别：plain、fun、extreme。我们用枚举表示该值，并把名称设为 rainbow。定义类型和名称是该协议的唯一要求。现在，假设我们想让这个属性可 Codable，以便它成为编码后的 attributed string 的一部分。我只需像这样添加 Codable 一致性。最后，假设我们希望彩虹级别成为本地化字符串的一部分，这意味着它无论在任何语言中都能应用到字符串的正确部分。我们只需要再添加一个协议一致性来选择加入。当一个属性是 Markdown 可解码的，我们就可以直接从 Markdown 解码它并插入到 attributed string 中。唯一的要求是值是 Codable 的。接下来，看看 Markdown 的自定义属性语法。在第一个示例中，我们有一个链接引用。它使用方括号表示链接文本，圆括号表示链接目的地（URL）。第二个示例是图片引用。它以感叹号开头，然后使用方括号表示图片描述，圆括号表示图片来源。前两个示例在 Markdown 中很常见。第三个示例展示了我们自定义属性的语法。它以插入符号（caret）开头，然后使用方括号表示文本，圆括号表示其属性。属性用 JSON 5 表示。JSON 5 与 JSON 兼容，并允许无引号键、注释等特性，非常适合这种人类友好的字符串。我们还在 Foundation 的其他 JSON API 中增加了 JSON 5 支持。因为自定义属性使用 JSON，任何能用 JSONDecoder 解码的内容都自动与新的自定义 Markdown 语法兼容。这里我们有单个属性、两个属性（一个字符串和一个数字），以及一个具有多个属性的单个属性。还有一块内容，即如何把这些 Markdown 中的名称连接到 Swift 类型。这块叫做属性作用域（attribute scope）。作用域是一组属性键。作用域在从 JSON 或 Markdown 解码时很有用，因为它们告诉我们预期会找到哪些属性、它们的名称以及如何解码。我们为 Foundation、UIKit、AppKit 和 SwiftUI 各定义了一个作用域。你也可以定义自己的属性作用域。让我们为 Caffé App 定义一个作用域。我们把作用域嵌套在 AttributeScopes 内，并使其符合 AttributeScope 协议。然后只需用「let」列出作用域内的属性。到目前为止，我们只有 rainbow 属性。接下来，我们在其中包含 SwiftUI 的作用域。这允许除了我们自己的属性之外还能使用所有那些属性。作用域会递归嵌套，因此这也包括 Foundation 的属性。为新作用域定义一个属性很有用，这允许我们在接受作用域作为参数的函数中使用键路径语法。最后，我们现在可以从自定义 Markdown 加载本地化且多彩的 attributed string。你还会在归档以及与 NSAttributedString 相互转换的函数中找到接受作用域的版本，从而在每一步自定义行为。这里再次展示了 Caffé App 的第一屏，你可以在标题中看到我们的自定义 rainbow 属性。本地化字符串从 Markdown 转换为 attributed string 之后，App 会找到该属性，并只对字符串的该范围应用有趣的特效。因为该属性来自本地化 strings 文件，这对 Caffé 支持的所有语言（如西班牙语）都正确有效。不过我们才刚刚开始。我们还有全新的 Formatter API。格式化器是 Foundation 长期以来的特性，负责把数字、日期、时间等数据转换为本地化且可呈现给用户的字符串。格式化器背后有相当多的配置数据，因此缓存并复用它们是常见模式。然而，App 由许多不同的代码片段组成， formatter 不一定在所有片段之间共享才有意义。此外，由于人们阅读日期和时间的方式种类繁多，加上作为 App 作者我们希望以符合设计的方式呈现这些数据，因此有很多边界情况的机会。今年，我们通过从零开始重新思考 Formatter API，同时改进了性能与可用性。简而言之，我们的新 API 聚焦于格式本身。让我们看看 Earthquakes 示例 App 中的这段代码，其中可以看到缓存模式的作用。它是一个两步过程：首先创建并配置一个 formatter；然后把日期交给 formatter，得到字符串。还能怎么更简单？让我们先移除必须自己创建日期格式化器的要求。很容易忘记这需要被缓存，从而导致为表格中的每个单元格都重新创建相同的 formatter。接下来是格式化步骤。我们不再把日期传给 formatter，而是直接使用日期本身。现在只需一行代码。你指定想要的格式，就这样。让我们多谈一点这个数字格式。代码不多，但它隐藏了一些复杂性，并有几个需要注意的陷阱。如果参数不是浮点数，你会得到完全错误的输出。读者必须知道用于格式化浮点数的特殊语法，以及一组只是字符串常量的修饰符。我们认为这段代码更容易理解、维护和阅读。它使用常规 Swift 函数来精确指定我们希望数字如何格式化。你还能获得自动补全和类型安全。我们把这种新方法应用到了 Foundation 的全部十个格式化器。我们清理并简化了接口，在避免常见陷阱方面做了改进，并在此过程中增加了一堆新功能。让我们详细看看两种最流行的格式化类型：日期和数字。日期格式化是使用日历和时区把一个绝对时间点转换为人类理解的日期。不仅如此，它还考虑到人类对自己喜欢的日期外观的所有偏好。我们把这些偏好称为 locale（区域设置）。看看格式化日期所需的少量代码。首先，我用 Date.now 获取当前时间点。接下来，调用 formatted 函数。就这样。当然，正如我们刚在示例中看到的，日期格式化有很多选项。让我们把它展开一点。formatted 函数可以配置为只显示日期或只显示时间。这两个参数都有几个选项可选。这个新格式化 API 的一个重要目标，是在创建正确格式时提供尽可能多的编译期帮助。使用魔法字符串值进行格式化，因在正常情况下看起来正确但在边界情况下（如年末）产生完全错误的值而臭名昭著。这里再次是我们的默认格式。这是要求日期和时间样式的简短写法，像这样。对于无参数和简单样式版本，我们为你挑选默认格式。然而，如果你真的想自定义日期，只需从这里开始，添加你关心的字段。在这个示例中，我通过把字段追加到样式来构建一个格式。我只需要年、日和月。其他可能性包括小时、分钟、秒等。输出格式会根据用户的 locale 自动调整。这些字段也是可配置的。这里我把月份改为 wide 格式，意味着会打印完整月份名。用这个 API 只格式化日期的一部分也很容易。这里我只想获取星期几。日期也可以格式化成不同样式。这里我选择使用 ISO 8601 格式 iso8601，但只包含年、月、日，并用短横线分隔。通过这些示例，格式化模式变得清晰：我们从想要格式化的值开始，调用 formatted 函数，参数是样式。每种类型可能不止一种样式。例如 Date 同时有 dateTime 和 iso8601。样式可以使用默认配置或自定义。这个格式化 API 通过指定一个字段列表来工作，其中一些字段还有额外选项。你提供的字段顺序并不重要。每个字段只是告诉格式化器，最终输出中应该在某处包含哪些值。对于最短的 API 版本（无参数或仅样式名），我们选择一个合理的默认值。一旦你开始向其中添加字段，输出就会变得自定义，只反映你选择显示的内容，有点像 UI 中的占位文本。还有用于格式化两个相对日期的新 API。这里是一些示例。首先，格式化一个日期范围。你可以直接使用两个日期的常规 Swift 范围语法。格式化范围允许配置显示日期和时间，就像我们对单个日期所做的那样。你可以把这个范围格式化为时长、组件，或相对于当前时刻的单个日期。格式化中的另一个新功能是 attributed 输出。它允许你在格式化器把某个格式化值重新排列以适应用户偏好之后，找到它把该值的特定部分放在哪里。这当然使用了我们新的结构体 AttributedString。对格式化输出应用样式在各种地方都会出现。在 watchOS 上，许多复杂功能（complication）都是格式化字符串。由于 Apple Watch 是非常个人化的设备，考虑用户偏好很重要，但这也是我们希望应用某种设计语言的地方，比如把日期的一部分染成用户选择的颜色。在 SwiftUI 中设置这件事其实相当有趣。让我们一起在演示中看看。这里是我 Caffé 伴侣 App 的起点，它显示你的下一杯免费咖啡是什么时候。我有一个 SwiftUI 视图，只是显示一个格式化日期。我在格式上设置了 locale，以便在 SwiftUI 预览中控制它。这是个相当不错的开始，但我想

接下来，我们将使用属性容器。它可以保存属性，而不附着到字符串的任何特定字符上。我们将为日期格式化器输出中的 weekday 属性创建一个。它被设置在包含 weekday 的字符串范围上。

接下来，我们将为想要设置的 color 属性创建一个容器。

最后，我们将使用 attributed string 函数，把第一个容器中匹配的属性替换为第二个容器中的值，作用在我们的 attributed string 上。

因为 AttributedString 是值类型，而 replacing 是一个 mutating 函数，我们需要把「let」改为「var」。看起来不错。更棒的是，它适用于所有 locale。让我们在预览中再加几个，以双重检查。

你可以看到，无论这些 locale 的格式化日期中 weekday 出现在哪里，它都是橙色的。让我们继续学习更多新的格式化器 API。既然我们已经看到如何把日期转换成字符串，接下来聊聊如何把字符串转换成日期。Date 现在有一个接受 strategy 参数的初始化方法。strategy 用于告诉解析器，输入中应该期待哪些字段。对于日期，格式也是一种 strategy。这在往返转换日期时很有用，比如在同时显示输出并允许用户输入新日期的文本栏中。这里是一个往返转换的示例。你会注意到解析可能抛出错误。这是因为根据输入，解析可能失败。有些 strategy 有更高级的解析选项。这里，我们解析一个固定格式，这在日期格式是从服务器接收时很有用。要使用它，用格式字符串初始化一个 strategy。不过，我们不用魔法字符串值，而是使用字符串插值。在这种情况下，我们期待 year-month-day 格式的字符串。每个插值都明确由字段标识，并各自指定期望的精确格式。其中很棒的一点是自动补全体验。如果我想使用不同的日格式，自动补全会显示有效选项，并附带每个选项的文档说明。再也不用猜应该用多少个 Y 字符来解析年份了。让我们继续数字。数字格式化是把整数或浮点数值转换成人类可读的内容。和所有格式化一样，它会考虑数字应如何显示的偏好。这包括从使用的数字种类到用于分组数字的字符等一切。和日期格式化一样，无需额外参数就能轻松得到很好的输出。支持许多种选项和输出种类。这里我们展示了百分比、科学记数法和货币。最后，让我们把几种格式放到……

这是显示尺寸选择屏幕的视图。让我们添加一个新尺寸，这样我们就可以看到，对于西班牙语，我们只需为新尺寸添加一个本地化字符串，而不是为每种食物、每种尺寸和每种数量各添加一个。这一行显示列表。列表来自我们的模型对象。让我们去那里看看。

尺寸枚举已经有了 small 和 large。我将添加一个新尺寸，给最饥饿的顾客，叫做「huge」。为此，我将添加一个新 case，以及一个本地化字符串。

现在我只需要为 huge 尺寸添加价格。在这个演示中，我只是把它们放在初始化方法里。现在我只需要为 huge 尺寸添加价格。在这个演示中，我只是把它们放在我们的初始化方法里。

让我们再看看我们的视图。

在预览中，我们有了新尺寸。我们的源代码已经包含一个英文字符串。现在我只需要一个西班牙语字符串。为了生成新字符串，我将使用编译器来查找「huge」的新本地化字符串。为此，我选择 Product > Export Localizations，并保存西班牙语字符串。

现在让我们为西班牙语添加翻译。

我可以过滤出我们的新字符串，并输入西班牙语单词。

接下来，我导入这些本地化内容，把它们放入我的 App。

现在我将再次运行 App，但使用西班牙语。为此，我选择 Product > Scheme > Edit Scheme。

在 Options 中，我可以选择想要测试的语言。

然后运行。从我们的标题可以看出，我们现在已经运行在西班牙语环境下。让我们再下一笔订单，从沙拉开始。注意当我改变数量时，订单按钮会自动修正。我们的新 huge 尺寸对 2 份沙拉正确地进行了复数形式处理。而且它匹配了「ensalada」的语法性别，全部只需一个字符串。Foundation 今年有很多很棒的新功能，它们已经准备好供你在 App 中试用。AttributedString 为字符串范围添加键值对提供了快速、易用且 Swift 优先的接口。你可以在 SwiftUI 的 Text 中使用它，并开始在本地化字符串中使用 Markdown。我们新的 Formatter API 聚焦于格式，简化了代码并提升了性能。在 App 展示数据的所有地方使用格式。最后，自动语法一致会智能地修正本地化字符串，使其匹配语法性别、数量和用户自己的称呼方式。我希望你会喜欢这些新功能。我们期待在你的 App 中看到它们。谢谢。[音乐]
