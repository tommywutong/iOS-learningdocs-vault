---
title: 深入了解 Swift 宏
session_id: 10167
collection: wwdc2023
year: 2023
duration: '39:43'
topics: [Developer Tools, Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10167/'
content_hash: 'sha256:2add303c16818163'
translated: true
---

# 深入了解 Swift 宏

<sub>WWDC2023 · 39:43 · Developer Tools、Swift</sub>

了解 Swift 宏如何帮助你减少代码库中的样板代码，更轻松地采用复杂特性。了解宏如何……

> [!note] 归档理由
> 宏进阶，理解 SwiftSyntax

## Chapters

- [Introduction](/videos/play/wwdc2023/10167/?time=0)
- [Why macros?](/videos/play/wwdc2023/10167/?time=51)
- [Design philosophy](/videos/play/wwdc2023/10167/?time=133)
- [Translation model](/videos/play/wwdc2023/10167/?time=288)
- [Macro roles](/videos/play/wwdc2023/10167/?time=378)
- [Macro implementation](/videos/play/wwdc2023/10167/?time=1068)
- [Writing correct macros](/videos/play/wwdc2023/10167/?time=2016)
- [Wrap up](/videos/play/wwdc2023/10167/?time=2322)

## Resources

- [Introduction](https://developer.apple.com/videos/play/wwdc2023/10167/?time=0)
- [Why macros?](https://developer.apple.com/videos/play/wwdc2023/10167/?time=51)
- [Design philosophy](https://developer.apple.com/videos/play/wwdc2023/10167/?time=133)
- [Translation model](https://developer.apple.com/videos/play/wwdc2023/10167/?time=288)
- [Macro roles](https://developer.apple.com/videos/play/wwdc2023/10167/?time=378)
- [Macro implementation](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1068)
- [Writing correct macros](https://developer.apple.com/videos/play/wwdc2023/10167/?time=2016)
- [Wrap up](https://developer.apple.com/videos/play/wwdc2023/10167/?time=2322)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10167/4/EAAEDDF4-5E7C-4AE9-A20C-CCD2E061E331/downloads/wwdc2023-10167_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10167/4/EAAEDDF4-5E7C-4AE9-A20C-CCD2E061E331/downloads/wwdc2023-10167_sd.mp4?dl=1)
- [Discover Observation in SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10149)
- [What's new in Swift](https://developer.apple.com/videos/play/wwdc2023/10164)
- [What's new in Xcode 15](https://developer.apple.com/videos/play/wwdc2023/10165)
- [Write Swift macros](https://developer.apple.com/videos/play/wwdc2023/10166)
- [#unwrap 表达式宏：一个更复杂的参数](https://developer.apple.com/videos/play/wwdc2023/10167/?time=44)
- [Existing features using expansions (1)](https://developer.apple.com/videos/play/wwdc2023/10167/?time=50)
- [Existing features using expansions (2)](https://developer.apple.com/videos/play/wwdc2023/10167/?time=71)
- [Macros inputs are complete, type-checked, and validated](https://developer.apple.com/videos/play/wwdc2023/10167/?time=196)
- [Macro expansions are inserted in predictable ways](https://developer.apple.com/videos/play/wwdc2023/10167/?time=225)
- [How macros work, featuring #stringify](https://developer.apple.com/videos/play/wwdc2023/10167/?time=291)
- [Macro declaration for #stringify](https://developer.apple.com/videos/play/wwdc2023/10167/?time=343)
- [What's an expression?](https://developer.apple.com/videos/play/wwdc2023/10167/?time=431)
- [The #unwrap expression macro: motivation](https://developer.apple.com/videos/play/wwdc2023/10167/?time=454)
- [The #unwrap expression macro: macro declaration](https://developer.apple.com/videos/play/wwdc2023/10167/?time=483)
- [The #unwrap expression macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=501)
- [The #makeArrayND declaration macro: motivation](https://developer.apple.com/videos/play/wwdc2023/10167/?time=549)
- [The #makeArrayND declaration macro: macro declaration](https://developer.apple.com/videos/play/wwdc2023/10167/?time=603)
- [The #makeArrayND declaration macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=615)
- [The @AddCompletionHandler peer macro: motivation](https://developer.apple.com/videos/play/wwdc2023/10167/?time=683)
- [The @AddCompletionHandler peer macro: macro declaration](https://developer.apple.com/videos/play/wwdc2023/10167/?time=711)
- [The @AddCompletionHandler peer macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=719)
- [The @DictionaryStorage accessor macro: motivation](https://developer.apple.com/videos/play/wwdc2023/10167/?time=756)
- [The @DictionaryStorage accessor macro: declaration](https://developer.apple.com/videos/play/wwdc2023/10167/?time=784)
- [The @DictionaryStorage accessor macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=800)
- [The @DictionaryStorage member attribute macro: macro declaration](https://developer.apple.com/videos/play/wwdc2023/10167/?time=836)
- [The @DictionaryStorage member attribute macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=886)
- [The @DictionaryStorage member macro: macro definition](https://developer.apple.com/videos/play/wwdc2023/10167/?time=952)
- [The @DictionaryStorage member macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=986)
- [The @DictionaryStorage conformance macro: macro definition](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1019)
- [The @DictionaryStorage conformance macro: usage](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1029)
- [@DictionaryStorage starting point](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1048)
- [@DictionaryStorage ending point](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1052)
- [@DictionaryStorage ending point (without expansions)](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1055)
- [Macro implementations](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1081)
- [Implementing @DictionaryStorage's @attached(member) role (1)](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1158)
- [Code used to demonstrate SwiftSyntax trees](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1192)
- [Implementing @DictionaryStorage's @attached(member) role (2)](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1320)
- [A type that @DictionaryStorage isn't compatible with](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1469)
- [Expansion method with error checking](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1517)
- [Parameter list for `ArrayND.makeIndex`](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1772)
- [The #unwrap expression macro: revisited](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1817)
- [Implementing the #unwrap expression macro: start](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1838)
- [实现 #unwrap 表达式宏：消息字符串](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1857)
- [实现 #unwrap 表达式宏：变量名](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1881)
- [实现 #unwrap 表达式宏：把一个字符串作为字面量插值](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1904)
- [实现 #unwrap 表达式宏：把一个表达式添加为字符串](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1931)
- [实现 #unwrap 表达式宏：插入文件名和行号](https://developer.apple.com/videos/play/wwdc2023/10167/?time=1980)
- [#unwrap 表达式宏：一次命名冲突](https://developer.apple.com/videos/play/wwdc2023/10167/?time=2045)
- [The MacroExpansion.makeUniqueName() method](https://developer.apple.com/videos/play/wwdc2023/10167/?time=2070)
- [Declaring a macro's names](https://developer.apple.com/videos/play/wwdc2023/10167/?time=2144)
- [Macros are testable](https://developer.apple.com/videos/play/wwdc2023/10167/?time=2308)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Becca：大家好，我是 Swift 团队的 Becca。今天我们要聊聊 Swift 宏，这是一个令人兴奋的新特性，可以让你根据自己的需要定制 Swift 这门语言。我们先从宏是用来做什么的说起。

然后，我们会聊聊我们在设计 Swift 宏时牢记的一些原则。接着我们会讲讲 Swift 宏是如何工作的，以及它们能以哪些具体方式和项目里的其他代码交互。

之后，我们会讲讲如何实现宏，最后再讨论一下如何确保你的宏能正确工作。

那我们先从"为什么 Swift 要支持宏"开始讲起。Swift 喜欢让用户能写出富有表现力的代码和 API。这就是为什么它提供了诸如派生一致性和结果构建器这样的特性，帮助用户避免写重复的样板代码。这些特性基本上都以同样的方式工作。举例来说，当你在不为其成员提供实现的情况下遵循 Codable 时，Swift 会自动把这个一致性展开成一组成员，插入到程序里。我在这个灰色框里展示了这个一致性的展开结果。为你生成这段代码，让你可以在不需要确切了解它是怎么运作的情况下使用 Codable，也让你不必去纠结"添加 Codable 支持是否值得写满满一屏幕的代码"。Swift 有很多以这种方式工作的特性。你写一些简单的语法，编译器就会自动把它展开成一段更复杂的代码。但如果现有的特性做不到你想要的呢？你当然可以给 Swift 编译器添加一个新特性，因为它是开源的。但这实际上意味着我要亲自去开一个视频会议，和其他 Swift 项目的负责人讨论你的这个特性，所以这并不是一个能规模化的流程。这就是我们为什么要引入宏。它们让你可以给 Swift 添加自己的语言特性，消除繁琐和样板代码，而且你可以把它打包在一个 Swift package 里分发出去，不需要修改编译器。你们当中有些人可能没在其他语言里用过宏。但如果你用过，你可能对它们心情复杂。这部分是因为很多 Swift 开发者都熟悉 Objective-C 或其他使用 C 预处理器的语言，他们了解 C 宏的种种局限和陷阱。但 Swift 宏在很多方面都截然不同，从而避开了那些问题中的许多。我们在设计时牢记了四个目标。第一个目标是：当你在使用一个宏时，这一点应该相当明显。宏有两种：独立宏（freestanding macro）代替你代码里的某个东西，它们总是以井号（#）开头。而附加宏（attached macro）则被用作你代码里声明上的一个属性，它们总是以 at 符号（@）开头。Swift 早就在用井号（#）和 at 符号（@）来表示特殊的编译器行为了。宏只是让这一点变得可扩展。而如果你没看到 # 或 @，你就可以确信这里面没有涉及任何宏。第二个目标是：传入宏的代码和从宏里返回的代码,都应该是完整的，并且经过错误检查。你不能把 "1 +" 传给一个宏，因为参数必须是完整的表达式。你也不能传入一个类型不对的参数，因为宏的参数和结果都会像函数参数一样经过类型检查。而且一个宏的实现可以验证它的输入，如果哪里出了问题，就发出编译器警告或错误，所以你能更容易确信自己是在正确地使用一个宏。第三个目标是：宏的展开应该以可预测的、增量式的方式融入程序。一个宏只能对你程序里可见的代码做增量添加。它不能删除或修改代码。所以，即便你完全不知道 "someUnknownMacro" 是做什么的，你仍然可以确信，它不会删掉对 "finishDoingThingy" 的调用，也不会把它挪到一个新函数里。这让阅读使用了宏的代码变得容易得多。最后一个目标是：宏不应该是一种高深莫测的魔法。宏只是给你的程序添加了更多代码，而这一点你可以直接在 Xcode 里看到。

你可以在一个宏的使用点右键点击，请求查看它展开成了什么。你可以在展开结果里设置断点，或者用调试器单步进入它。当一个宏展开出来的代码编译不通过时，你既能看到错误出现在展开结果的哪个位置，也能看到那个展开在你的源代码里对应哪里。而所有这些工具，即便这个宏是由一个闭源库提供的，也同样适用。宏的作者甚至可以为他们的宏编写单元测试，来确保它们按预期工作；我们非常鼓励他们这样做。

我们认为，这些目标能让 Swift 宏对开发者来说，既容易理解，也容易维护。既然我们已经了解了 Swift 宏想要达成的目标，那我们来聊聊它们是如何做到的。在陷入细节之前，我们先把基本概念搞清楚。当 Swift 在你的代码里看到你调用一个宏时，比如 Xcode 宏 package 模板里的 "stringify" 宏，它会把这次使用从代码里提取出来，发送给一个特殊的编译器插件，这个插件里包含了那个宏的实现。这个插件作为一个独立进程，运行在一个安全沙盒里，里面包含了宏作者写的自定义 Swift 代码。它会处理这次宏的使用，返回一个"展开结果"（expansion），也就是这个宏创建出的一段新代码片段。然后 Swift 编译器会把这个展开结果加入到你的程序里，把你的代码和这个展开结果一起编译。所以当你运行这个程序时，它的运作方式就好像你自己写了这个展开结果，而不是调用了这个宏一样。现在，这里有一个我一带而过的重要问题：Swift 是怎么知道 "stringify" 这个宏存在的？答案是，它来自一个宏声明。一个宏声明提供了这个宏的 API。你可以直接在你自己的 module 里写这个声明，也可以从一个库或框架里导入它。它指定了这个宏的名字和签名——它接受多少个参数、参数的标签和类型，以及如果这个宏有返回值的话，返回值的类型，这一切都和一个函数声明很像。而且它还有一个或多个标注，用来指定这个宏的角色（role）。写一个宏而不去想清楚它的角色是什么，是不可能的。所以我们来聊聊什么是角色，以及你可以如何用不同的角色来写出不同种类的宏。角色是针对一个宏的一整套规则。它规定了你在哪里、以怎样的方式应用这个宏，它会展开成什么样的代码，以及那个展开结果会被插入到你代码的什么位置。归根结底，正是宏的角色，负责实现我们那个"以可预测的、增量式的方式插入展开结果"的目标。

有两种角色会创建独立宏：表达式（expression）和声明（declaration）。还有五种角色会创建附加宏：对等（peer）、访问器（accessor）、成员属性（member attribute）、成员（member）和一致性（conformance）。我们来看看这些角色，以及你可能会在什么时候用到它们。我们先从"独立表达式"（freestanding expression）角色开始讲起。如果"表达式"这个词让你没什么印象，表达式指的是我们称之为"一个会执行并产生结果的代码单元"的东西。在这条 let 语句里，等号后面的这段算术运算就是一个表达式。但表达式有一种递归的结构——它们通常是由更小的表达式组成的。所以单独的 "x + width" 也是一个表达式，单独的 "width" 这个词同样也是。那么，一个"独立表达式"宏，就是一个会展开成一个表达式的宏。你会怎么用它呢？设想你需要强制解包一个可选值。Swift 提供了一个强制解包运算符，但有些团队觉得，不假思索地扔进去一个强制解包实在太容易了，所以他们的风格指南要求开发者写一些更复杂的东西，来说明为什么这个值永远不应该是 nil。但这些替代写法里的大多数——比如用一个 "guard let"，然后在 "else" 分支里调用 "preconditionFailure"——都有点太繁琐了。我们来设计一个宏，在这两个极端之间取得更好的平衡。我们希望这个宏能计算并返回一个值，所以我们把它做成一个 "freestanding(expression)" 宏。我们给它起名叫 "unwrap"，并给它一个泛型类型，传入的值是可选的，但返回的值是非可选的。我们还传入一个字符串，作为解包失败时打印出的消息的一部分。于是我们最终得到了一个宏，调用它就像调用一个函数一样，但它会展开成一个包在闭包里的 "guard let" 表达式。这条错误信息甚至还包含了变量名，这是普通函数根本做不到的。现在我们已经了解了独立表达式角色，我们来看看独立声明（freestanding declaration）角色。它会展开成一个或多个声明，比如函数、变量或类型。你可以用它来做什么呢？设想你正在写某种统计分析，需要一个二维数组类型。你希望这个数组里所有的行都有相同数量的列，所以你不想用一个"数组的数组"。

相反，你想把这些元素存储在一个扁平的一维数组里，然后根据开发者传入的二维索引，计算出一个一维索引。要做到这一点，你可能会写出这样一个类型。这个 "makeIndex" 函数接受二维索引所需的两个整数，然后做一点算术运算，把它们转换成一个一维索引。但接着你发现，在程序的另一部分，你需要一个三维数组。它和这个二维数组几乎一模一样，只是多了几个索引，计算过程也稍微复杂一点。然后你又需要一个四维数组，接着又是一个五维数组，很快你就淹没在了一堆几乎一模一样、但又不够接近到可以用泛型、协议扩展、子类，或者 Swift 为这类情况提供的其他任何特性来处理的数组类型里。幸运的是，这些结构体中的每一个都是一个声明，所以我们可以用一个声明宏来创建它们。那我们就来声明一个名叫 "makeArrayND" 的独立声明宏，因为它将会创建一个 N 维数组类型。我们会把维度数量作为一个 Int 参数传进去，我们不会声明返回类型，因为这个宏会给我们的程序添加一个声明，而不是计算一个供其他代码使用的结果。现在，我们可以用二维、三维、四维和五维分别调用这个宏四次，每次调用都会展开成一个完整的多维数组类型，参数数量正确，对应大小的计算也正确。到目前为止，我们只看了独立宏。现在我们来看看附加宏的各种角色。顾名思义，附加宏是附加在某个具体声明上的。这意味着它们有更多可以利用的信息。独立宏只能拿到传给它们的参数，但附加宏还可以访问它们所附加的那个声明。它们经常会检查那个声明，从中提取出名字、类型和其他信息。我们先从附加对等（attached peer）角色开始讲起。一个对等宏可以附加到任何声明上，不仅仅是变量、函数和类型，甚至包括像 import 和运算符声明这样的东西，并且可以在它旁边插入新的声明。所以，如果你在一个方法或属性上使用它，你最终会创建出这个类型的成员；但如果你在一个顶层函数或类型上使用它，你最终会创建出新的顶层声明。这让它们变得极其灵活。这里有一种你可能会用到它们的方式。假设你正在写一个使用 Swift 并发的库，但你知道你的一些客户仍然在使用较旧的并发技术，所以你想给他们提供一些使用完成处理程序（completion handler）的 API 版本。写这些方法并不难。你只需要去掉 "async" 关键字，添加一个完成处理程序参数，把返回类型挪到参数列表里，然后在一个分离的任务（detached task）里调用这个 async 版本就行了。但你要经常这么做，而你不想每次都手写一遍。这正好是附加对等宏可以大显身手的地方。我们会声明一个叫做 "AddCompletionHandler" 的宏，给它一个用于完成处理程序参数标签的参数，然后把这个宏附加到这个方法的 async 版本上。这个宏会创建一个和原方法等价的、基于完成处理程序的签名，写好方法体，甚至还会为这个完成处理程序附加一段带额外说明文字的文档注释。相当酷。接下来，我们来看看附加访问器（attached accessor）角色。这些角色可以附加在变量和下标（subscript）上，并且可以为它们安装访问器，比如 "get"、"set"、"willSet" 或者 "didSet"。那这有什么用处呢？假设你有一堆类型，它们基本上都是对字典的包装，让你可以通过属性来访问其中的内容。举例来说，这个 "Person" 结构体让你可以访问 "name"、"height" 和 "birth_date" 这几个字段，但如果字典里除了这三个字段之外还有别的信息，它就会被原样保留，被你的程序忽略掉。这三个属性都需要计算型的 getter 和 setter，但手写它们很乏味，而我们又不能用属性包装器，因为属性包装器无法访问它所在类型上的其他存储属性。所以，我们来写一个附加访问器宏来帮上这个忙。我们把它叫做 "DictionaryStorage"。我们会给它一个 "key" 参数，因为这个字典里 "birth_date" 是带下划线拼写的，不过你也可以直接省略这个 key，它会默认为 nil，这样宏就会用这个属性的名字作为 key。所以现在，你不需要再写那一大段访问器代码块了，只需要在每个属性前面加上 "@DictionaryStorage"，这个宏就会替你生成访问器。这是个不错的改进，但这里仍然有一些样板代码：那些一模一样的 "DictionaryStorage" 标注。它们的样板程度已经降低了，但终究还是样板代码。有些内置的标注可以让你把它们应用到整个类型或扩展上，来处理这种情况。"附加成员属性"（attached member attribute）角色也可以让你的宏表现得像那样。这个宏会被附加到一个类型或扩展上，然后它可以给它所附加的那个东西的各个成员添加标注。我们来看看这是怎么做到的。这里我们要做一件稍微有点不一样的事情。我们不会声明一个新的宏，而是会给 "DictionaryStorage" 宏再添加一个角色标注，和它已有的"附加访问器"角色并列在一起。这是创建宏时一个非常有用的技巧。除了两个独立角色之外，你可以任意组合各种角色，因为在有些地方，Swift 没法判断该用哪一个。Swift 会在你应用这个宏的地方，展开所有说得通的角色，但至少要有一个角色在那里能用才行。所以，如果你把 "DictionaryStorage" 附加到一个类型上，Swift 会展开这个"成员属性"角色。如果你把它附加到一个属性上，Swift 会展开这个"访问器"角色。但如果你把它附加到一个函数上，你就会得到一个编译错误，因为 "DictionaryStorage" 没有任何可以附加到函数上的角色。

给 "DictionaryStorage" 添加了这第二个角色之后，你不需要再把它逐一附加到每个属性上了，只需要把它附加到整个类型上就行。这个宏会有一套逻辑，跳过某些成员，比如初始化方法、"dictionary" 属性，以及像 "birth_date" 这样已经有 "DictionaryStorage" 标注的属性。但它会给其他任何存储属性都加上一个 "DictionaryStorage" 标注，然后这些标注就会展开成我们之前已经见过的那些访问器。这是个不错的改进，但这里仍然还有更多可以消除的样板代码：初始化方法和存储属性。这些是 "DictionaryRepresentable" 协议所要求的，而且这个属性也会被那些访问器用到，但在任何使用 DictionaryStorage 的类型里，它们都完全一样。我们来让 DictionaryStorage 宏自动添加它们，这样我们就不用手写了。我们可以用"附加成员"（attached member）角色来做到这一点。和成员属性宏一样，你可以把这些宏应用到类型和扩展上，但它们不是给已有的成员添加标注，而是添加全新的成员。所以你可以添加方法、属性、初始化方法等等。你甚至可以给 class 和 struct 添加存储属性，或者给 enum 添加 case。我们再一次给 DictionaryStorage 宏添加一个新的"附加成员"角色，把它和另外两个角色组合在一起。这个新角色会添加一个初始化方法和一个叫做 "dictionary" 的属性。你可能会想，当两个不同的宏被应用到同一段代码上时，哪一个会先被展开？答案是，这其实无关紧要。每一个宏看到的都是这个声明的原始版本，不包含其他宏提供的展开结果。所以你不需要担心顺序问题。不管编译器什么时候展开你的宏，你看到的结果都是一样的。加上了"附加成员"角色之后，我们甚至都不需要再写那两个成员了。只需要在这个类型上使用 DictionaryStorage，它们就会自动被添加进来。然后另一个角色会给这些属性添加 DictionaryStorage 标注，而这些标注又会展开成访问器，如此等等。

但这里仍然还有最后一点样板代码需要消除：对 DictionaryRepresentable 协议的一致性。

"附加一致性"（attached conformance）角色正适合用来做这件事。它可以给一个类型或扩展添加一个一致性。我们再给 "DictionaryStorage" 宏添加最后一个"附加一致性"角色，把它和另外三个组合在一起。这个新角色会添加一个对 "DictionaryRepresentation" 的一致性。所以现在，我们不需要手动写这个一致性了。我们已经为访问器和生成的成员添加的这个 DictionaryStorage 标注，现在也会自动添加这个一致性，连同它已经在做的其他所有事情一起。距离我们看到最初的起点已经过去很久了，所以提醒一下大家，我们拿了一个庞大、杂乱、充满重复代码的类型，把这些代码中的大部分都挪进了一个超强宏的几个角色里，这样剩下的部分就能简洁地只表达出这个特定类型真正特别的地方。设想一下，如果你有 10 个或 20 个类型都可以用上 DictionaryStorage，处理它们全部会变得多么轻松。我们已经花了不少时间讲声明和角色了，但到目前为止，它们所展开出的那些代码，看起来就像是凭空变出来的一样。我们现在来填补这个空白，聊聊你该如何实现你的宏。到目前为止，当我给大家展示宏声明的时候，我漏掉了一个非常重要的东西：实现。它在等号之后，而且它总是另一个宏。有时候它是你自己写的另一个宏，只是重新排列了参数，或者把额外的参数指定成字面量。

但通常情况下，你会用一个外部宏（external macro）。外部宏是由一个编译器插件实现的宏。你可能还记得我之前讲过编译器插件。我说过，当编译器看到一个宏被使用时，它会在一个独立进程里启动一个插件，请求它展开这个宏。"#externalMacro" 定义的正是这层关系。它指定了编译器应该启动哪个插件，以及那个插件里哪个类型的名字。所以当 Swift 展开这个宏时，它会启动一个叫做 "MyLibMacros" 的插件，请求一个叫做 "StringifyMacro" 的类型来展开它。所以宏声明放在你普通的库里，和你其他的 API 放在一起，但宏的实现放在一个独立的编译器插件 module 里。而 "#externalMacro" 建立起了声明和实现它的那个类型之间的联系。一个宏的实现看起来是什么样的呢？我们来看看 DictionaryStorage 可能是怎么实现的。如果你还记得，我们的 "DictionaryStorage" 宏有一个"附加成员"角色，会给这个类型添加一个存储属性和一个初始化方法。这里是这个角色的一个简单实现。我们会一步一步地过一遍，了解它是怎么运作的。在最上面，我们先导入一个叫做 SwiftSyntax 的库。SwiftSyntax 是由 Swift 项目维护的一个 package，可以帮助你解析、检查、操作和生成 Swift 源代码。随着这门语言的演进，Swift 的贡献者们会持续维护 SwiftSyntax，让它保持最新，所以它支持 Swift 编译器所支持的每一个特性。SwiftSyntax 把源代码表示为一种特殊的树状结构。举例来说，这段代码示例里的 "Person" 结构体，被表示为一个叫做 "StructDeclSyntax" 的类型的实例。但这个实例有各种属性，每个属性都代表了这个结构体声明的某一部分。标注的列表在 "attributes" 属性里。真正的关键字 "struct" 在 "structKeyword" 属性里。这个结构体的名字在 "identifier" 属性里。而带花括号的主体、以及这个结构体的成员，则在 "memberBlock" 属性里。还有一些属性，比如 "modifiers"，代表的是某些结构体声明会有、但这一个没有的东西。这些属性就是 nil。

这些属性里的一些语法节点被称为"token"（词法单元）。它们代表源文件里的某一段具体的文本，比如一个名字、一个关键字，或者一小段标点符号，它们只是包含了那段文本，以及周围的任何琐碎内容（trivia），比如空格和注释。

如果你在语法树里钻得足够深，你会发现，源文件的每一个字节，都被某个 token 节点覆盖着。但其中一些节点，比如 "attributes" 属性里的 "AttributeListSyntax" 节点，以及 "memberBlock" 属性里的 "MemberDeclBlockSyntax" 节点，并不是 token。它们在自己的属性里有子节点。举例来说，如果我们看看 "memberBlock" 属性内部，我们会找到一个代表左花括号的 token，一个代表成员列表的 "MemberDeclListSyntax" 节点，以及一个代表右花括号的 token。如果你继续深入探索那个 "MemberDeclListSyntax" 节点的内容，你最终会为每个属性都找到一个对应的节点，如此等等。使用 SwiftSyntax 本身就是一个巨大的话题，所以与其把这个视频拉长一倍，我打算给大家推荐另外两个资源。一个是配套的 "Write Swift Macros" 这个 session，里面有一些实用技巧，教你如何弄清楚一段特定的源代码是怎么被表示为一棵语法树的。另一个是 SwiftSyntax package 的文档。你可以在网上找到它，或者，如果你在你的宏 package 里使用 Xcode 的 Build Documentation 命令，SwiftSyntax 的文档就会出现在 Developer Documentation 窗口里。除了主要的 SwiftSyntax 库之外，我们还导入了另外两个 module。一个是 "SwiftSyntaxMacros"，它提供了写宏所需要的协议和类型。另一个叫做 "SwiftSyntaxBuilder"。这个库提供了一些便捷的 API，用来构造语法树，以表示新生成的代码。你可以在不使用它的情况下写一个宏，但它非常好用，我们强烈建议你善加利用。既然我们已经导入了这些库，我们就开始动手写这个 "DictionaryStorageMacro" 类型，也就是我们插件应该提供的那个类型。注意，它遵循了一个叫做 "MemberMacro" 的协议。每种角色都有对应的协议，而这个实现必须遵循这个宏所提供的每一种角色所对应的协议。"DictionaryStorage" 宏有这四种角色，所以 "DictionaryStorageMacro" 类型需要遵循这四个对应的协议。但为了简单起见，我们现在先只关注 "MemberMacro" 这个一致性。继续看这个类型的主体，我们会看到一个叫做 "expansion(of:providingMembersOf:in:)" 的方法。这个方法是 MemberMacro 协议要求的，当这个宏被使用时，Swift 编译器就会调用它来展开这个 member 角色。我们现在还没有用到这些参数，但我们稍后会讲到它们。现在，注意这是一个静态方法。所有的 expansion 方法都是静态的，所以 Swift 实际上不会创建 DictionaryStorageMacro 类型的实例。它只是把这个类型当作方法的容器来用。每个 expansion 方法都会返回被插入到源代码里的 SwiftSyntax 节点。一个成员宏会展开成一份声明列表，作为成员添加到这个类型上，所以一个成员宏的 expansion 方法会返回一个由 "DeclSyntax" 节点组成的数组。如果我们看看这个方法体内部，我们会看到那个数组是怎么被创建出来的。里面有我们想让这个宏添加的初始化方法和存储属性。现在，这里的 "var dictionary" 这一部分看起来像是一个普通的字符串，但其实并不是。这个字符串字面量被写在了一个期望出现 DeclSyntax 的地方，所以 Swift 实际上会把它当作一段源代码片段，请求 Swift 的解析器把它转换成一个 DeclSyntax 节点。这正是 SwiftSyntaxBuilder 库提供的便利之一。幸好我们之前导入了它。所以，有了这个，再加上对另外三个角色所对应协议的遵循，我们就有了一个可用的 DictionaryStorage 宏实现。但是，虽然这个宏在你正确使用它时现在可以正常工作，如果你用错了会怎么样呢？举例来说，如果你试图把它应用到一个 enum 上，而不是一个 struct 上呢？"附加成员"角色会试图添加一个存储的 "dictionary" 属性。但 enum 不能有存储属性，所以 Swift 会产生一个错误："Enums must not contain stored properties."（枚举不能包含存储属性）。Swift 能阻止这段代码编译通过固然很好，但这条错误信息有点让人摸不着头脑，不是吗？并不清楚为什么 DictionaryStorage 宏会试图创建一个存储属性，也不清楚你本该做些什么不同的事情。我之前说过，Swift 的目标之一，就是让宏能够检测出自己输入中的错误，并发出自定义的错误信息。所以我们来修改一下我们这个宏的实现，为这种情况生成一条清楚得多的错误信息："@DictionaryStorage can only be applied to a struct."（@DictionaryStorage 只能应用于 struct）。这会让开发者更清楚地知道自己哪里做错了。要做到这一点，关键在于 expansion 方法的这些参数，我们到目前为止一直都忽略了它们。不同角色的具体参数会略有不同，但对于一个成员宏来说，有三个参数。第一个叫做 "attribute"，它的类型是 AttributeSyntax。这就是开发者写下的、用来使用这个宏的那个实际的 DictionaryStorage 标注。第二个参数叫做 "declaration"，它的类型遵循 "DeclGroupSyntax"。DeclGroupSyntax 是一个协议，struct、enum、class、actor、protocol 和 extension 对应的节点都遵循它。所以这个参数给了我们开发者把这个标注附加上去的那个声明。最后一个参数叫做 "context"，它的类型遵循 "MacroExpansionContext"。当宏的实现想要和编译器通信时，就会用到这个 context 对象。它可以做几件不同的事情，包括发出错误和警告。我们会用到这三个参数，来发出我们的错误。我们来看看这是怎么做到的。首先，我们需要检测出这个问题。我们会通过检查 "declaration" 参数的类型来做到这一点。每一种声明都有不同的类型，所以，如果它是一个 struct，它的类型就会是 "StructDeclSyntax"；如果它是一个 enum，就会是 "EnumDeclSyntax"，以此类推。所以我们会写一个 guard-else，调用 "declaration" 参数的 "is" 方法，传入 "StructDeclSyntax"。如果这个声明不是一个 struct，我们就会进入这个 "else" 代码块。现在，我们先返回一个空数组，这样这个宏就不会给项目添加任何代码，但我们真正想做的是发出一个错误。

现在，简单的做法是直接抛出一个普通的 Swift 错误，但那样你对输出内容就没什么控制权了。所以，我来给大家展示一种更复杂一点的做法，可以让你创建出更精细的错误。第一步是创建一个叫做 "Diagnostic"（诊断）的类型的实例。这是一点编译器术语。就像医生看着你骨折的 X 光片诊断出一处骨裂一样，编译器或者宏看着你出错代码的语法树，诊断出一个错误或警告。所以我们把代表这个错误的实例称为一个 "Diagnostic"。一个 diagnostic 至少包含两条信息。第一条是这个错误发生所在的那个语法节点，这样编译器就知道该把哪一行标记为有误。这里，我们想指向用户写下的那个 DictionaryStorage 标注，很巧的是，这正是方法被传入的 "attribute" 参数所提供的。第二条是你想让编译器产生的实际消息内容。你通过创建一个自定义类型，然后传入它的一个实例，来提供这条信息。我们快速看一下它。

"MyLibDiagnostic" 这个类型定义了这个 module 可能产生的所有诊断信息。我们选择用一个 enum，为每种诊断提供一个 case，不过你也可以用别的类型。这个类型的工作方式有点像一个可抛出的 Swift 错误。它遵循 "DiagnosticMessage" 协议，并且有一堆属性，提供关于这个诊断的信息。其中最重要的属性之一是 "severity"（严重程度）属性。它指定了这个诊断是一个错误还是一个警告。

然后是 "message" 属性，它产生实际的错误信息，还有 "diagnosticID" 属性。你应该用这个插件的 module 名字作为 domain，用某种唯一的字符串作为 ID。我选择用字符串原始值来实现这个 enum，但那只是为了方便。所以，有了这条消息，你就可以创建这个 diagnostic 了。然后你告诉 context 去诊断它，就完成了。

这是一个相当基础的诊断，但如果你愿意，你可以把它们做得花哨得多。举例来说，你可以给一个诊断添加 Fix-It，让 Xcode 的 Fix 按钮自动应用它。你也可以添加高亮，附加指向代码中其他位置的注释。所以你确实可以为你的开发者提供一流的错误体验。但一旦你确保了你的宏被正确地应用了，你仍然需要实际创建出这个展开结果。SwiftSyntax 为此提供了几种不同的工具。语法节点是不可变的，但它们有很多 API，要么创建新节点，要么返回已有节点的修改版本。SwiftSyntaxBuilder 库添加了一些 SwiftUI 风格的语法构建器，其中一些子节点是通过一个尾随闭包来指定的。举例来说，那个多维数组宏可以用一个语法构建器，为它正在创建的类型生成任意数量的合适参数。而我们用来创建 DictionaryStorage 属性和初始化方法的那个字符串字面量特性，同样也支持插值。

所有这些特性在不同的情况下都很有用，在特别复杂的宏里，你可能会发现自己会把好几种特性组合在一起使用。但字符串字面量特性尤其擅长为大量代码生成语法树，而且它的插值特性也有一些值得学习的地方。那我们来看看你可以怎样用它们来生成一些代码。前面，我们讲到了 "unwrap" 宏。它接受一个可选值和一个消息字符串，展开成一个包在闭包里的 "guard let"。这段代码的总体形状总是一样的，但很多具体内容是要根据具体使用点来定制的。我们把注意力集中在这条 "guard let" 语句上，看看我们能不能写一个函数，专门生成这条语句。首先，我们直接拿我们刚看到的那段代码示例，放进一个叫做 "makeGuardStatement" 的辅助方法里，返回一个 StatementSyntax 节点。然后我们再慢慢地加上插值，替换掉那些需要根据使用位置而不同的内容。我们要做的第一件事是加上正确的消息字符串。这个消息字符串是一个任意的表达式，所以我们会把它作为一个 ExprSyntax 节点传进来，然后把它插值进去。像这样一个普通的插值可以把一个语法节点添加到代码里，但它不能添加一个普通的 String。这是一个安全特性，防止你不小心插入了无效的代码。这个 guard-let 的条件也类似，只不过它就是一个变量名，所以它是一个 token，而不是一个表达式。没关系，我们添加一个 TokenSyntax 参数，把它插值进去，就像我们插值那个表达式一样。当你要把被解包的那个表达式，添加到错误信息里时，情况就有点棘手了。我们这个宏的一个特性是，当它失败时，会打印出你原本试图解包的那段代码。这意味着我们需要创建一个字符串字面量，里面包含一个语法节点的字符串化版本。

我们先把这个前缀从 StatementSyntax 字面量里提取出来，放进一个纯字符串的变量里。我们会把这个字符串插值进去，但我们会用一种以 "literal:" 开头的特殊插值方式。当你这样做时，SwiftSyntax 会把这个字符串的内容作为一个字符串字面量加进去。这对于用宏计算出的其他种类的信息——数字、布尔值、数组、字典，甚至可选值——来生成字面量，同样有效。既然我们现在是在一个变量里逐步构建这个字符串，我们就可以改一下它，让消息里包含正确的代码。只需要为原始的表达式加一个参数，把它的 "description" 属性插值进这个字符串就行了。你不需要做任何特殊处理来转义它。这个 "literal:" 插值会自动检测这个字符串是否包含特殊字符，并添加转义符，或者切换到一个原始字面量，来确保这段代码是有效的。所以 "literal:" 这种插值方式，让做正确的事情变得超级简单。最后要处理的是文件名和行号。这有点棘手，因为编译器并不会告诉这个宏它正要展开到的源代码位置。不过，宏展开上下文（macro expansion context）有一个 API，你可以用它来生成特殊的语法节点，编译器会把这些节点转换成带有源代码位置信息的字面量。我们来看看这是怎么做到的。我们会为宏展开上下文再加一个参数，然后使用它的 "location(of:)" 方法。这会返回一个对象，可以为你提供的任意节点生成表示其位置的语法节点。如果这个节点是你的宏自己创建出来的，而不是编译器传给你的，它就会返回 nil，但我们知道 "originalWrapped" 是用户写下的参数之一，所以它的位置永远不会是 nil，我们可以放心地对结果做强制解包。现在你要做的，就是把文件名和行号对应的语法节点插值进去，就完成了。我们现在生成的就是正确的 "guard" 语句了。到目前为止，我们讨论的都是如何让宏能够工作。但我们接下来要聊聊，如何让它们工作得更好。我们先从命名冲突说起。之前我们看 "unwrap" 宏的时候，看的是一个解包简单变量名的例子。

但如果我们试着解包一个更复杂的表达式，这个宏就得用不同的方式展开。它会生成代码，把这个表达式的结果捕获进一个叫做 "wrappedValue" 的变量里，然后再解包它。

但如果你试图在这条消息里用一个叫 "wrappedValue" 的变量呢？当编译器去查找 "wrappedValue" 时，它最终会找到离它更近的那个，于是就会用那个，而不是你真正想用的那个。

你可以试着通过挑一个你觉得用户大概率不会不小心用到的名字来解决这个问题，但让这种情况完全不可能发生，岂不是更好？这正是宏展开上下文上的 "makeUniqueName" 方法所做的事。它会返回一个变量名，保证不会被用户代码或者任何其他宏的展开结果用到，所以你可以确信，这个消息字符串不会不小心引用到它。你们当中有些人可能会想，为什么 Swift 不自动阻止这种情况发生呢？有些语言有所谓"卫生的"（hygienic）宏系统，宏内部的名字和宏外部的名字是彼此独立的，所以它们不会互相冲突。

Swift 并不是这样设计的，因为我们发现，很多宏都需要用到它们自身之外的名字。想想 DictionaryStorage 宏，它用到了这个类型上的一个 "dictionary" 属性。如果宏内部的 "dictionary" 和宏外部的 "dictionary" 意思不一样，那要让这一切正常运作就相当困难了。

而且有时候，你甚至想引入一个全新的、非宏代码也能访问到的名字。对等宏、成员宏和声明宏基本上就是完全为了做这件事而存在的。但当它们这样做的时候，它们需要声明自己添加的那些名字，这样编译器才能知道它们的存在。而它们是在自己的角色标注内部来做这件事的。

你可能之前没有注意到，但实际上我们一直都在看这些声明。DictionaryStorage 宏上的 "member" 角色有一个 "names:" 参数，指定了 "dictionary" 和 "init" 这两个名字。而事实上，我们在这次 session 里看到的大多数宏，至少都有一个带 "names" 参数的角色。

你可以用五种名字指定方式："Overloaded"（重载）表示这个宏添加的声明，和它所附加的对象具有完全相同的基础名字。"Prefixed"（前缀）表示这个宏添加的声明，具有相同的基础名字，只是加上了指定的前缀。"Suffixed"（后缀）也是同样的道理，只不过用的是后缀而不是前缀。"Named"（命名）表示这个宏添加的声明，具有一个特定的、固定的基础名字。而 "arbitrary"（任意）表示这个宏添加的声明，用的是某种没法用上面这些规则来描述的其他名字。使用 "arbitrary" 其实相当常见。举例来说，我们那个多维数组宏声明了一个类型，它的名字是根据它的一个参数计算出来的，所以它需要指定 "arbitrary"。但当你能用其他某个指定方式的时候，请尽量使用它们。这会让编译器和其他工具（比如代码补全）都更快。好，到这个 session 的这个节点，我猜你们都已经跃跃欲试，想写自己的第一个宏了。而你可能已经有了一个很棒的想法：写一个宏，插入它被展开时的日期和时间。听起来是个好主意，对吧？错了。事实证明，你绝对不能写这个宏。让我解释一下为什么。宏只应该使用编译器提供给它们的信息。编译器假定宏的实现是纯函数，也就是说，如果它提供的数据没有变化，那么展开结果也不应该变化。

如果你绕开这一点，你可能会看到不一致的行为。

现在，这套宏系统在设计时，就防范了某些可能违反这条规则的行为。编译器插件运行在一个沙盒里，阻止宏的实现读取磁盘上的文件，或者访问网络。

但这个沙盒并不能阻止所有的坏行为。你还是可以用一些 API 来获取诸如日期或随机数这样的信息，或者你可以把一次展开中的信息保存到一个全局变量里，然后在另一次展开中使用它。但如果你这样做，你的宏可能就会出问题。所以不要这样做。最后，但绝对同样重要的是，我们来聊聊测试。你的宏插件只是一个普通的 Swift module，这意味着你可以，而且绝对应该，为它写正常的单元测试。

测试驱动开发是开发 Swift 宏时一种非常有效的方法。来自 SwiftSyntaxMacrosTestSupport 的 "assertMacroExpansion" 这个辅助函数，会检查一个宏是否产生了正确的展开结果。你只需要给它一个宏的使用示例，以及它应该展开成的代码，它就会确保两者是匹配的。所以今天我们了解了很多关于 Swift 宏的知识。宏让你可以通过设计新的语言特性，把一个小小的使用点"展开"成一段更复杂的代码，从而减少样板代码。你会把一个宏和其他 API 一起声明出来，通常是在一个库里，但你实际上是在一个独立的插件里实现它，这个插件会在一个安全沙盒里运行 Swift 代码。一个宏的角色，表达的是你可以在哪里使用它，以及它的展开结果是如何融入程序其余部分的。而你可以，也绝对应该，为你的宏编写单元测试，确保它们按预期工作。如果你还没看过的话，"Write Swift Macros" 这个 session 应该是你接下来要看的。它会给你展示如何使用 Xcode 的宏开发工具和宏 package 模板，如何检查 SwiftSyntax 树并从中提取信息，以及如何围绕你的单元测试来搭建一套宏开发工作流程。感谢大家收看，编程愉快。♪ ♪
