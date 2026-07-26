---
title: 编写 Swift 宏
session_id: 10166
collection: wwdc2023
year: 2023
duration: '33:58'
topics: [Developer Tools, Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10166/'
content_hash: 'sha256:2a6306784ee8b99a'
translated: true
---

# 编写 Swift 宏

<sub>WWDC2023 · 33:58 · Developer Tools、Swift</sub>

了解如何使用 Swift 宏让你的代码库更具表达力、更易读。跟着我们一起探索宏可以怎样……

> [!note] 归档理由
> 宏的展开机制（编译期代码生成）

## 章节

- [Overview](/videos/play/wwdc2023/10166/?time=75)
- [Create a macro using Xcode's macro template](/videos/play/wwdc2023/10166/?time=310)
- [Macro roles](/videos/play/wwdc2023/10166/?time=650)
- [编写一个 SlopeSubset 宏来定义一个枚举子集](/videos/play/wwdc2023/10166/?time=700)
- [在调试器里检查语法树结构](/videos/play/wwdc2023/10166/?time=1217)
- [Add a macro to an Xcode project](/videos/play/wwdc2023/10166/?time=1475)
- [Emit error messages from a macro](/videos/play/wwdc2023/10166/?time=1625)
- [Generalize SlopeSubset to a generic EnumSubset macro](/videos/play/wwdc2023/10166/?time=1812)

## 相关资源

- [Overview](https://developer.apple.com/videos/play/wwdc2023/10166/?time=75)
- [Create a macro using Xcode's macro template](https://developer.apple.com/videos/play/wwdc2023/10166/?time=310)
- [Macro roles](https://developer.apple.com/videos/play/wwdc2023/10166/?time=650)
- [编写一个 SlopeSubset 宏来定义一个枚举子集](https://developer.apple.com/videos/play/wwdc2023/10166/?time=700)
- [在调试器里检查语法树结构](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1217)
- [Add a macro to an Xcode project](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1475)
- [Emit error messages from a macro](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1625)
- [Generalize SlopeSubset to a generic EnumSubset macro](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1812)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10166/5/58425163-99DA-4506-A86E-A2D794244136/downloads/wwdc2023-10166_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10166/5/58425163-99DA-4506-A86E-A2D794244136/downloads/wwdc2023-10166_sd.mp4?dl=1)
- [Discover Observation in SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10149)
- [Expand on Swift macros](https://developer.apple.com/videos/play/wwdc2023/10167)
- [Meet the presenter: Write Swift macros](https://developer.apple.com/videos/play/wwdc2023/10296)
- [What's new in Swift](https://developer.apple.com/videos/play/wwdc2023/10164)
- [What's new in Xcode 15](https://developer.apple.com/videos/play/wwdc2023/10165)
- [Invocation of the stringify macro](https://developer.apple.com/videos/play/wwdc2023/10166/?time=355)
- [Declaration of the stringify macro](https://developer.apple.com/videos/play/wwdc2023/10166/?time=391)
- [Implementation of the stringify macro](https://developer.apple.com/videos/play/wwdc2023/10166/?time=430)
- [Tests for the stringify Macro](https://developer.apple.com/videos/play/wwdc2023/10166/?time=552)
- [Slope and EasySlope](https://developer.apple.com/videos/play/wwdc2023/10166/?time=725)
- [Declare SlopeSubset](https://developer.apple.com/videos/play/wwdc2023/10166/?time=856)
- [Write empty implementation for SlopeSubset](https://developer.apple.com/videos/play/wwdc2023/10166/?time=924)
- [Register SlopeSubsetMacro in the compiler plugin](https://developer.apple.com/videos/play/wwdc2023/10166/?time=983)
- [Test SlopeSubset](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1121)
- [Cast declaration to an enum declaration](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1165)
- [Extract enum members](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1274)
- [Load enum cases](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1292)
- [Retrieve enum elements](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1318)
- [Generate initializer](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1451)
- [Return generated initializer](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1459)
- [Apply SlopeSubset to EasySlope](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1551)
- [测试我们在把 SlopeSubset 应用到结构体上时会生成一个错误](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1680)
- [定义 SlopeSubset 被应用到非枚举类型时要报出的错误](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1728)
- [如果 SlopeSubset 被应用到非枚举类型上就抛出错误](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1749)
- [Generalize SlopeSubset declaration to EnumSubset](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1863)
- [Retrieve the generic parameter of EnumSubset](https://developer.apple.com/videos/play/wwdc2023/10166/?time=1893)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Alex Hoppen：有谁喜欢写重复的样板代码？没有人喜欢！这就是为什么在 Swift 5.9 里，我们要引入 Swift 宏。Swift 宏能让你在编译期生成这些重复的代码，让你 App 的代码库更具表达力、更易读。我叫 Alex Hoppen，今天我要给大家展示，怎样编写你自己的宏。我会先给大家简单介绍一下宏是怎么工作的。

之后，我们会直接进入 Xcode，看看你可以怎样创建你的第一个宏。看过我们的第一个宏之后，我们会探索更多可以使用宏的角色（role），我还会给大家展示，我是怎样用宏来简化我目前正在开发的一个 App 的代码库的。

最后，我会展示宏在某个上下文里不适用时，是怎样把错误或警告反馈给编译器的。我们开始吧。这里有一个列表，是给一年级学生练习算术能力用的一组算式。元组的左边是作为整数的结果，右边是作为字符串字面量的算式。注意这里有多重复、多冗余，甚至还容易出错，因为没有人能保证这个结果真的和这个算式相符。幸运的是，有了 Swift 5.9，我们可以定义一个 stringify 宏来简化这一切。碰巧，这个宏正是 Xcode 模板里自带的那个。stringify 宏只接收算式作为唯一一个参数，在编译期，它会展开成我们之前看到的那个元组，从而保证算式和结果是相符的。那这是怎么运作的呢？我们来看看这个宏本身的定义。注意，它看起来非常像一个函数。stringify 宏接收一个整数作为输入参数，输出一个包含结果（一个整数）和算式（一个字符串）的元组。如果宏表达式的参数和宏的参数不匹配，或者本身类型检查不通过，编译器会报出一个错误，而不会应用这次宏展开。举个例子，如果我给这个宏传一个字符串字面量，编译器就会抱怨说 'String' 不能转换成期望的参数类型 'Int'。这一点和比如 C 宏是不同的——C 宏是在类型检查之前的预处理阶段就被求值的。但这也让我们能够使用你熟悉且喜爱的 Swift 函数的一切能力，比如让你的宏具有泛型。

还要注意，这个宏是用 freestanding expression（独立表达式）这种宏角色声明的。这意味着，你可以在任何能使用表达式的地方使用这个宏，而且它会用 # 号来标示，就像我们看到的 #stringify 那样。另一类宏是附加宏（attached macro），它可以为声明添加内容，我稍后会讲到。在确认所有参数都和宏的参数匹配之后，编译器会执行宏展开。要看看这是怎么运作的，我们来聚焦一个单独的宏表达式。

为了执行这次展开，每个宏都会在一个编译器插件里定义它的实现。编译器会把整个宏表达式的源代码发送给那个插件。宏插件做的第一件事，是把这个宏的源代码解析成一棵 SwiftSyntax 树。这棵树是这个宏的一种忠实于源码的结构化表示，也是这个宏进行操作的基础。举个例子，我们的 'stringify' 宏在这棵树里表示为一个宏展开表达式节点。这个表达式的宏名是 'stringify'，它接收一个单独的参数，也就是把中缀运算符加号应用在 2 和 3 上得到的结果。Swift 宏真正强大的地方在于，宏的实现本身就是一个用 Swift 写的程序，可以对语法树执行它想要的任何变换。在我们这个例子里，它会生成一个像我们之前看到的那样的元组，然后把生成出来的语法树重新序列化成源代码，再发送给编译器，由编译器把这个宏表达式替换成展开后的代码。

这真的很酷，但现在我想搞清楚，这一切在代码里到底是什么样子。Xcode 里新的宏模板定义了我们刚看到的这个 stringify 宏。我们来走一遍这个模板，探索这个宏的定义、展开是怎么运作的，以及这个宏怎么被测试。要创建这个模板，我点击 File、New、Package，然后选择 Swift Macro 模板。

我们把第一个宏叫做 "WWDC"。

那这个模板给了我们什么呢？这里有一次对 #stringify 宏的调用，和我们之前看到的类似。它接收一个参数 "a + b"，返回结果，以及产生这个结果的代码。如果我想知道这个宏展开成什么，我可以右键点击它，选择 Expand Macro。

正是我们之前看到的那样。但这个宏是怎么定义的呢？我们跳转到它的定义。

这里是我们之前那个 'stringify' 宏的一个稍微泛化的版本。这个宏是泛型的，可以接收任意类型 T，而不是只接收一个整数。

这个宏被声明为一个外部宏（external macro）。

这告诉编译器，要执行这次展开，需要去 WWDCMacros 模块里查看 StringifyMacro 这个类型。

那个类型是怎么定义的呢？我们仔细看看。因为 stringify 被声明为一个独立表达式宏，所以 StringifyMacro 类型需要遵循 ExpressionMacro 协议。

这个协议只有一个要求：expansion（展开）函数。它接收这个宏表达式本身的语法树，以及一个可以用来和编译器通信的 context。

expansion 函数随后返回改写后的表达式语法。

它在实现里做了什么呢？首先，它取出这个宏表达式的那个唯一参数。它知道这个参数一定存在，因为 stringify 被声明为只接收一个参数，而且所有参数在这次宏展开被应用之前都必须通过类型检查。然后，它用字符串插值来创建一个元组的语法树。第一个元素是这个参数本身，第二个元素是一个包含这个参数源代码的字符串字面量。

注意，这个函数在这里返回的不是一个字符串，它返回的是一个表达式语法（expression syntax）。这个宏会自动调用 Swift 解析器，把这个字面量转换成一棵语法树。而且因为它对第二个参数用的是字面量插值的写法，它会确保这个字面量的内容被正确转义。没有人喜欢 bug。但我更不喜欢的是那些藏在代码里、除非我主动展开这个宏去看，否则根本看不到的 bug。这就是为什么你要确保自己的宏得到了充分的测试。因为宏没有副作用，而且语法树的源代码很容易比较，所以测试它们的一个绝佳方式就是写单元测试。这个宏模板里已经自带了一个。

这个测试用例使用 SwiftSyntax 包里的 'assertMacroExpansion' 函数，来验证 'stringify' 宏能正确展开。

它接收我们之前看到的那个 '#stringify(a + b)' 表达式作为输入，并断言在这个宏展开之后，会生成一个包含 'a + b' 和字符串字面量 'a + b' 的元组。

为了告诉这个测试用例该怎样展开这些宏，它传入了 'testMacros' 这个参数，指定 '#stringify' 这个宏应该用 'StringifyMacro' 这个类型来展开。我们就用你可能已经用来运行 App 测试的那种方式，来运行这些测试，看看它们是不是真的通过了。

测试通过了，这样我们就已经有了自己的第一个宏。

在这个过程中，我们看到了它的基本构建模块：宏声明定义了这个宏的签名，也声明了这个宏的角色；编译器插件负责执行展开，它本身就是一个用 Swift 写的程序，操作的对象是 SwiftSyntax 树。

我们还看到，宏是非常易于测试的，因为它们是对语法树的确定性变换，而语法树的源代码很容易比较。所以你可能会想：「我们还能在哪些其他场景里用宏？」我们已经看过一个独立表达式宏了。简单回顾一下，这种宏用 # 号书写，能让你改写整个宏表达式。还有一种独立声明（freestanding declaration）角色，它展开出来的是一个声明，而不是一个表达式。另一类宏是附加宏（attached macro），它们像特性（attribute）一样用 @ 书写，能让宏为它所附加的那个声明添加内容。举个例子，一个附加成员宏（attached member macro）会给它所附加的类型添加新的成员。要了解更多关于这些其他角色的内容，我强烈推荐大家去看看《深入了解 Swift 宏》这场演讲，Becca 在那里非常详细地讲解了它们。但我想重点讲讲附加成员这个角色，因为它帮我改进了我目前正在开发的一个 App 的代码库。我还是一名滑雪教练，最近我一直在开发一个 App，用来规划我想带学生去滑的路线。作为一名滑雪教练，你绝对想避免的一件事，就是带初学者去滑对他们来说太难的坡道。我想用 Swift 的类型系统来强制保证这一点。这就是为什么，除了包含我最喜欢的滑雪场里所有坡道的 Slope 枚举之外，我还有一个 EasySlope 类型，它只包含适合初学者的坡道。它有一个初始化方法，可以在某个坡道确实简单的情况下，把一个 Slope 转换成一个 EasySlope；还有一个计算属性，可以把一个 EasySlope 转换回一个通用的 Slope。

虽然这提供了很好的类型安全性，但它真的非常重复。如果我想加一个简单坡道，我需要把它加到 Slope 里……

加到 EasySlope 里，加到那个初始化方法里，还要加到那个计算属性里。我们来看看能不能用一个宏来改善这一切。我们想做的，是自动生成这个初始化方法和这个计算属性。我们该怎么做呢？初始化方法和计算属性都是 EasySlope 类型的成员，所以我们需要声明一个附加成员宏。

接下来，我们会创建包含这个宏实现的编译器插件。为了确保我们的宏行为符合预期，我们想用测试驱动的方式来开发它。所以，在我们为它写一个测试用例之前，我们会先让它的实现保持为空。

在我们用一个测试用例定义好这个宏的行为之后，我们会写出与那个测试用例相匹配的实现。

最后，我们会把这个新宏集成到我的 App 里。如果一切顺利，我们就能删掉那个初始化方法，让宏替我们生成它。

要开发这个宏，我们用之前创建的那个模板来做。既然我在自己的 App 里其实不需要 '#stringify' 宏，我已经把它删掉了。我先用 '@attached(member)' 这个特性来声明一个新的附加成员宏。

我把它叫做 SlopeSubset，因为 EasySlope 是 Slope 的一个子集。

这个宏还定义了它引入的这些成员的名字。

在这个演示里，我只会给大家展示怎样生成那个初始化方法，生成那个计算属性的做法非常类似，因为它同样只是一个针对所有 case 做 switch 的语句。有了这个声明，我们就定义好了这个宏，但我们还没实现它实际执行的那个展开。为此，我们的宏引用了 WWDCMacros 模块里的 SlopeSubsetMacro 类型。我们来创建那个类型，这样我们才能继续进入真正激动人心的部分：实际的宏实现。既然我们把 SlopeSubset 声明成了一个附加成员宏，对应的实现就需要遵循 MemberMacro 协议。这个协议只有一个要求：'expansion' 函数，和 ExpressionMacro 类似。

'expansion' 函数接收我们用来把这个宏应用到某个声明上的那个特性，以及这个宏被应用到的那个声明。在我们这个例子里，这会是 EasySlope 这个枚举声明。

然后这个宏会返回它想要添加到那个声明里的全部新成员的列表。

我知道现在就想直接开始实现这个变换真的很诱人，但我们说好了要先为它写一个测试用例。所以现在，我们先返回一个空数组，表示不添加任何新成员。

最后，我们需要让编译器能看到 SlopeSubset。为此，我把它加到了下面这里的 'providingMacros' 属性里。

在深入更多细节之前，我想先确保我们目前写的东西是可用的。虽然我可以试着在 Xcode 里应用这个宏，看看展开后的代码，但我更倾向于为它写一个测试用例，这样每当我对这个宏做改动时，我都可以重新运行它，以确保自己没有引入回归问题。

就像模板里的那个测试用例一样，我们用 'assertMacroExpansion' 函数来验证我们这个宏的行为。

我们想测试的是，这个宏应用到 EasySlope 类型上时会生成什么，所以我们把它作为测试用例的输入。

而且因为这个宏目前还什么都不做，我们只期望它移除这个特性，不添加任何新成员，所以期望展开出来的代码和输入是一样的，只是没有了 '@SlopeSubset'。

最后，我们需要让这个测试用例知道，它应该用 SlopeSubsetMacro 这个实现来展开 SlopeSubset 这个宏。为此，我们需要在 'testMacros' 这个字典里，把这个宏的名字映射到它的实现类型，再把这个字典传给断言函数。

现在我们运行一下测试，看看我们目前写的东西是不是真的能用。

确实可以，很好。但我们真正想要的是，检查这个宏是不是真的生成了那个初始化方法，而不只是移除了这个特性。所以我会把我之前手写的代码复制进这个测试用例里，因为那才是我们真正希望这个插件生成出来的东西。

如果我们再运行一次测试……它失败了，因为我们的宏其实还没有生成那个初始化方法。我们现在就来改这一点。

这个初始化方法要针对 EasySlopes 枚举里声明的所有枚举元素做 switch。所以我们首先要做的，是从这个声明里取出这些枚举元素。既然枚举元素只能在枚举声明内部声明，我们就先把 'declaration' 转型成一个枚举声明。

如果这个宏被附加到一个不是枚举的类型上，我们应该报出一个错误。我加了一个 TODO，这样我们就不会忘了以后处理它，现在先返回一个空数组。接下来，我们需要拿到这个枚举声明的所有元素。为了搞清楚该怎么做，我想看看我们这个枚举在 SwiftSyntax 树里的语法结构。

既然这个宏的实现只是一个普通的 Swift 程序，我就可以用你在 Xcode 里熟悉的所有工具来调试你的程序。举个例子，我可以在 expansion 函数里设一个断点，运行这些测试用例来命中这个断点。

现在，调试器暂停在了这个宏的实现内部，'enumDecl' 就是 EasySlopes 这个枚举。我们可以在调试器里输入 'po enumDecl' 来打印它。

我们来看看输出结果。这棵语法树最内层的节点代表的就是那些枚举元素——'beginnersParadise' 和 'practiceRun' 这两个坡道。要取出它们，我们需要按照语法树里展示给我们的结构来走。我们一步一步地走一遍这个结构，边走边写出访问代码。这个枚举声明有一个叫 'memberBlock' 的子节点，这个 member block 同时包含花括号和实际的成员。所以要访问这些成员，我们从 'enumDecl.memberBlock.members' 开始。

这些成员里包含实际的声明，以及一个可选的分号。我们关心的是这些声明，尤其是那些真正声明了枚举 case 的声明。我用 compact map 来取出所有是枚举 case 的成员声明的列表。每一个 case 声明都可以声明多个元素，这是因为，我不一定要在每个单独的 case 关键字之后另起一行来声明每个坡道，我完全可以把它们写在同一行，就像 'case beginnersParadise, practiceRun' 这样。

要取出它们全部，我们可以用 'flatMap'。

现在我们已经取出了所有的元素，我们就可以开始构造我们真正想添加到 EasySlope 里的那个初始化方法了。

这个初始化方法的声明只有一项内容：一个 switch 表达式。

这个 switch 表达式为枚举里的每个元素都包含一个 case，还包含一个返回 nil 的 default case。我们需要为所有这些创建语法节点。

找到该创建哪些语法节点，有两种很好的方式：要么像我们之前那样打印语法树，要么阅读 SwiftSyntax 的文档。我们先构造一个 InitializerDeclSyntax。

这个类型可以通过用一个结果构建器来构建方法体、并指定头部（也就是 'init' 关键字和所有参数）来构造出来。这样我们就可以在结果构建器内部用一个 for 循环来遍历所有元素，这正是我们需要的。

我直接把 init 的头部从我们的测试用例里复制过来。

在方法体内部，我们需要一个 switch 表达式。

这个类型同样有一个接收头部和结果构建器的初始化方法，我们再用一次。

现在我们可以用结果构建器的威力，遍历我们之前收集到的所有元素。

对于每一个元素，我们都想创建一个新的 case 项，我们可以像之前看到的 '#stringify' 那样，用字符串插值来构造它。

我们还需要添加一个返回 nil 的 default case。

最后，我们就可以返回这个初始化方法了。

我们运行一下测试，看看我们是不是真的生成了正确的初始化方法。

确实是这样。所以我们知道这个宏是可用的了，可以开始在我的 App 里用它了。

要把我们的宏包加到我的 Xcode 项目里，我可以右键点击它，选择 "Add Package Dependencies"，然后我就可以选择我们刚创建的这个本地包了。

要能够使用这个宏，我把 WWDC 这个 target 加为我 App 的依赖。

现在我们可以从这个包里导入 WWDC 模块，把 SlopeSubset 这个宏应用到 EasySlope 类型上了。

……如果我们编译……编译器会抱怨说，这个手写的初始化方法是一次无效的重复声明，这是因为现在这个宏替我们生成了它，所以我们可以直接把它删掉。

删代码总是很爽，对吧？所以如果我们想看看这个宏到底生成了什么，我们可以右键点击 SlopeSubset，点击 Expand Macro。

如果我忘了这个宏是做什么的，我还可以按住 Option 点击它，来读它的文档。

下一步应该是同样生成那个计算属性，不过我今天晚些时候再做这件事。通过使用宏，我们得以在不需要写重复代码的情况下，获得 EasySlopes 的类型安全性。我们是怎么做到的呢？我们从 Swift 宏包模板开始。为了探索语法树的结构，我们让宏的执行暂停下来，在调试器里打印语法节点，这让我们看清楚了，要取出所有的枚举元素，我们需要访问哪些属性。

而且，单独用一个测试用例来开发这个宏真的非常容易。在我们把它加到我的 App 里之后，它立刻就能正常运作。但如果你的宏被用在它不支持的场景里，会发生什么呢？就像你永远不希望带一个初学滑雪者去难度太高的坡道一样，你也永远不希望让你的宏执行意料之外的展开，或者生成编译不过的代码。如果你的宏被用在它不支持的方式里，一定要给出错误信息，告诉使用者到底出了什么问题，而不是让他们去读生成出来的代码来调试你的宏。

本着这种精神，我们来修一下我们代码库里留下的那个 TODO。当 SlopeSubset 被应用到一个不是枚举的类型上时，这个宏应该报出一个错误，说它只适用于枚举。就像之前一样，我们先加一个测试用例。

这次，我们把 SlopeSubset 宏应用到一个结构体上。

既然这个结构体里没有枚举元素，我们就不期望这个宏生成一个初始化方法。相反，它应该报出一个诊断信息，也就是一个错误，告诉我们 SlopeSubset 只能应用在枚举上。如果我们运行这个测试……它失败了，因为我们还没有输出这个错误信息。我们现在就去编译器插件那边处理这件事。

宏的错误可以用任何遵循 Swift Error 协议的类型来表示。我用一个只有一个 case 的枚举，来描述「SlopeSubset 被应用到一个不是枚举的类型上」这种情况对应的错误信息。

如果我们在 expansion 函数里抛出这个错误，它就会显示在调用这次宏展开的那个特性上。

如果你想在特性以外的其他位置显示错误信息、生成警告，甚至在 Xcode 里显示 Fix-It，context 这个参数上有一个 'addDiagnostic' 方法，可以让你生成丰富的诊断信息。但我认为在这个例子里，直接在这个特性上显示一条简单的错误信息就已经很高效了。现在，我们来看看我们是不是把一切都做对了，我们的测试是不是通过了。

很好，通过了。那如果我把 SlopeSubset 应用到一个结构体上，在 Xcode 里看起来是什么样的呢？为此，我把这个测试用例复制到一个文件里。

Xcode 会把这条自定义的错误信息和其他所有编译错误一起内联显示出来。这让使用我这个宏的人很容易看出自己哪里做错了。

你知道吗？既然我们现在已经有了良好的错误处理，我觉得这个宏对其他开发者指定枚举子集也可能有用，不只是对坡道有用。我们来把它泛化一下。

为了指定这个枚举的超集——目前我们把它硬编码成了 Slope——我们给这个宏声明加一个泛型参数。

而且既然这个宏现在不再专属于坡道了，我们右键点击 SlopeSubset，选择 Refactor、Rename，把它改名为 EnumSubset。

我还可以通过按住 Command 点击，选择把字符串字面量和注释里出现的所有内容也一并改名。

现在我们需要调整我们的宏实现，让它使用这个泛型参数，而不是硬编码的 Slope 类型。如果我们在调试器里打印这个特性、检查它的结构，就像我们对 'enumDecl' 做的那样，我们会看到，可以通过访问这个特性名字里 'genericArgumentClause' 的第一个参数的 'argumentType'，来取出这个泛型参数。所以既然我们已经取出了这个泛型参数，我们就可以把之前硬编码的 Slope 类型替换成变量 'supersetType'。

我还需要再做几处改动，比如给这个初始化方法的参数改名、改这个宏实现的类型名，以及更新文档，我晚点再做这些。现在，我们先确保我们的测试仍然是通过的。

既然我们让 EnumSubset 变成了泛型的，我们就需要通过把 slope 作为泛型参数传给 EnumSubset 宏，显式地指定 EasySlope 是 Slope 的一个子集。

我们来看看测试现在是不是通过了。

通过了。我真该考虑把这个宏作为 Swift 包发布给其他人用。今天我们讲了很多内容，我们来回顾一下我们都学了些什么。要创建一个宏，你可以从这个宏包模板开始，它自带了 stringify 宏，是一个很棒的起点。在开发你的宏的过程中，我们强烈建议你写测试用例，来确保你的宏生成出来的代码确实是有效的。如果你这样做的话，你可以通过在 expansion 函数里设一个断点、运行一个测试、在调试器里打印语法树，来检查这棵语法树的结构。最后，如果你的宏在某些场景下不适用，你应该始终给出自定义的错误信息，这样即使出了问题，你的宏依然能大放异彩。感谢观看，我很期待看到大家会创造出什么样的宏。♪ ♪
