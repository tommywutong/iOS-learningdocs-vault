---
title: Swift 泛型（扩展篇）
session_id: 406
collection: wwdc2018
year: 2018
duration: '56:55'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2018/406/'
content_hash: 'sha256:daee3bb6ffd44a96'
translated: true
---

# Swift 泛型（扩展篇）

<sub>WWDC2018 · 56:55 · Swift</sub>

泛型是 Swift 最强大的特性之一，让你能编写灵活、可重用的组件，同时保持静态……

> [!note] 归档理由
> 泛型的实现原理与特化，理解 Swift 编译期

## 相关资源

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2018/406z8wpyv2jdenet9rc/406/406_hd_swift_generics.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2018/406z8wpyv2jdenet9rc/406/406_sd_swift_generics.mp4?dl=1)
- [Presentation Slides (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2018/406z8wpyv2jdenet9rc/406/406_swift_generics.pdf?dl=1)
- [Embrace Swift type inference](https://developer.apple.com/videos/play/wwdc2020/10165)
- [Embracing Algorithms](https://developer.apple.com/videos/play/wwdc2018/223)
- [What's New in Swift](https://developer.apple.com/videos/play/wwdc2018/401)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Ben。我在 Swift 标准库工作。和我同事 Doug，来自编译器团队一起。我们要和你们聊聊 Swift 泛型。所以 Swift 最近的版本加入了一些重要的新特性。

包括条件一致性（conditional conformance）与递归协议约束。

而且，事实上，随着 Swift 的每一个版本，我们一直在精炼泛型系统，让它更富表现力。我们觉得 4.2 版本标志着一个重要节点。

这是我们可以最终完整实现一系列一直为标准库所设想的设计的节点。对我们实现 Swift API 稳定性的目标而言，这是至关重要的。

所以，我们过去给泛型讲过很多课，但已经有一段时间没有退一步。

也没有作为一个整体来聊聊泛型了。

所以今天，我们要带你们了解泛型系统的一些不同特性。包括新的和旧的，帮助理解它们如何组合在一起。我会简要回顾泛型的动机。

我们要讲到，给定一组具体类型，如何设计协议，例子取自标准库。

我们要回顾协议继承，并讲到条件一致性这一新特性。以及它如何与协议继承交互。

最后，我们要以类与泛型的讨论作为收尾。

那么为什么泛型是 Swift 如此重要的一部分？嗯，一种看到它们影响的方式，就是设计一个简单的集合类型。

我们把它叫做 buffer，它会和标准库的 array 类型类似。

现在，一个 buffer 读取部分最简单的可能 API，可能会包括元素个数的计数。以及按给定索引位置取每个元素的方式。但是，那个返回类型我们该作何处理？现在，如果没有泛型，我们就得让它成为某种能代表我们想放进 buffer 的任何东西的类型。

你可以把那个类型叫做 ID 或 object 或 void star。在 Swift 里我们把它叫做 Any，这是一个能代表 Swift 中任何不同类型的类型。

所以如果你想在 buffer 里处理任何东西，你可以让下标返回一个 Any。但当然，你可能知道这会导致非常不愉快的用户体验。在某个时刻，你得把那个类型从盒子里取出来。

才能真正使用它。

这不仅令人恼火，而且也容易出错。如果你的代码里某处，可能不小心把一个整数放进了本应是字符串 buffer 的地方怎么办？但这不只是易用性的问题。我们也想解决与这些值在内存中如何表示相关的问题。

现在，一个字符串 buffer 的理想表示，是一块连续的内存。每个元素紧挨着彼此排成一行。

但用无类型的方法，这不会很顺利。因为 buffer 事先不知道它要包含什么类型。所以它必须用像 Any 这样能涵盖所有可能性的类型。在跟踪、装箱与拆箱 Any 中的类型时，有大量开销。

这里，我可能只是想要一个整数 buffer，但我没有办法向编译器表达这一点。所以我在为灵活性付费，即使我不感兴趣。更进一步，因为 Any 必须涵盖任何不同类型的可能。包括太大而无法装进它自身内部存储的类型，它有时必须使用间接。它必须持有指向这些值的指针，而那个值可能散布在内存各处。

所以我们真的想解决这些问题，不仅为了易用性与正确性，也为了性能。我们用一种叫做参数多态的技术来做这件事。

这只不过是我们在 Swift 里称之为泛型的另一个术语。

用泛型的方法，我们给 buffer 放上更多信息，来表示 buffer 要包含的类型。

我们把它叫做 Element。

Element 是类型的泛型参数，因此有参数多态这个术语。你可以把它想成一个编译期参数，告诉 buffer 它要包含什么。

现在它有了引用那个元素类型的方式。它可以在之前使用 Any 的地方使用它。

这意味着在从 buffer 取出类型时不需要做转换。如果你做了把错误类型赋值这种意外，或者类似问题。编译器会抓住你。

现在，现在没有所谓不带关联元素类型的 buffer 这种类型。

如果你试图那样声明一个类型，你会得到编译错误。

你可能会觉得有点惊讶。因为有时你会看到你可以声明像 buffer 这样不带任何元素类型的类型。

但这只是因为编译器能够从上下文推断元素类型应该是什么。在这个例子里，从右边的字面量。

元素仍然在那里，只是隐式的。

这种 buffer 这样的类型包含什么类型的精确知识，会一路携带通过编译期与运行时。

这意味着我们可以实现目标：把所有元素保存在一块连续内存里，没有开销。

即使那些类型任意大。

而且因为编译器在所有时刻都直接知道 buffer 包含的确切元素类型。它拥有原本没有的优化机会。

所以，在这个例子里，我声明了一个整数 buffer。

这样的循环应该被编译成仅仅几条非常高效的 CPU 指令。

现在，如果你经常写这样的循环。来求一个整数 buffer 的和，把它们提取到一个方法里可能更有意义。一个 buffer 上的扩展，更可单元测试，调用时也更可读。

但你可能知道，如果你写过这样的代码，你会得到编译问题，因为不是所有元素类型都能像这样求和。我们需要告诉编译器更多关于元素需要具备的能力，才能让这个方法对 buffer 可用。

现在，最简单的做法是把元素类型约束为某个具体类型，比如我们原始循环里的 Int。

如果你采取这种简单的做法来快速上手你的扩展，以后很容易泛化它。当你发现需要做别的事情时。比如求 double buffer 或 float buffer 的和。

只需看你约束到的类型。看它遵循的协议。一直向上跟到给你做工作所需一切的最通用协议。

在这个例子里，numeric 协议，它给我们这里依赖的两样东西。

创建一个值为零的新元素的能力，以及把元素加到它上面的能力。这些都作为 numeric 协议的一部分。

现在，让我们聊聊从各种类型中提取协议的过程。

我们一直在谈这个 buffer 类型，我们可以让它在不同元素上泛型。但关于编写在不同方向上泛型的代码呢？或者编写在任何不同种类的集合上都能工作的代码？比如一个和我们 buffer 类型非常相似的 array。

但也有更多样化的类型，比如作为键值对集合的 dictionary。或者不是泛型、元素类型不同的类型，比如 data 或 string，它们返回特定的元素类型。我们想创建一个协议，捕捉它们所有的共同能力。我们打算创建一个，一个精简的、简化的标准库自己的 collection 协议版本。

注意我们先考虑了各种不同的具体类型。然后现在我们想的是一个能 Join 它们所有类型的协议。而且，按这个顺序思考很重要。从一些具体类型开始，然后试图用协议统一它们。

这些类型有什么共同点？它们没有共同点的是什么？当你设计这样一个协议时，你可以把它想成一种契约谈判。

这里有一种自然的拉锯，一边是遵循类型，想要在履行契约时有尽可能多的灵活性。

另一边是协议的用户，想要一个真正好、紧、简单的协议来做他们的扩展。

这就是为什么在设计协议时，同时拥有一系列不同的可能遵循类型。和一些不同的用例在 mente 是非常重要的。

因为这是一个平衡。

所以，让我们开始 flesh out collection 协议。首先我们需要表示元素类型。现在，在协议里，我们用关联类型来做这个。每个遵循类型需要把 element 设置成合适的东西。在 buffer 或 array 的例子里，从 Swift 4.2 开始，这会自动发生。

因为我们也把它们的泛型参数命名为 element。

这是给泛型参数有意义的、遵循常见约定如单词 element 的名字的不错副作用。

而不是给它们一个任意的 T，你得另外声明那是元素类型。

对于其他数据类型，你可能需要做稍微更具体的事。比如，dictionary 需要把元素类型设置为它的键与值类型的 pair。接下来，让我们谈添加下标操作。

现在，如果我们说的是像 array 这样的类型，我们可能会倾向于让下标把 Int 作为它的参数。

但让下标把 Int 作为参数意味着一个非常强的契约。每个遵循类型都必须提供按用整数表示的位置取元素的能力。这对像 array 这样的类型很好。

对协议用户来说也绝对容易理解。

但它对稍微更复杂的类型，比如 dictionary，是否足够灵活？现在无论你怎么建模，dictionary 可能都会被某个相当复杂的内部数据结构支撑。它有特定的逻辑来从一个元素移动到下一个。

比如，它可能被某种内部 buffer 支撑，它可能用一个 index 类型来存储到那个 buffer 的偏移量。它随后可以把它作为下标的参数，来按那个偏移量取位置上的元素。

但 dictionary 的 index 类型必须是一个不透明类型，只有 dictionary 能控制。

你不会想让某人给你的偏移量加一。那不一定移动到 dictionary 的下一个元素。它可能移动到 dictionary 内部存储的某个任意、可能未初始化的部分。

所以相反我们想让 dictionary 通过推进 index 来控制向前遍历集合。

所以为了做到这一点，我们添加另一个方法。

给定一个 index，给你标记它之后位置的 index。一旦你采取这一步，你需要几样更多的东西。你需要一个 startIndex 属性和一个 endIndex 属性。因为简单的 count 不再能工作，来告诉我们已经到达末尾。既然我们不再用 Ints 作为 index 类型。

所以让我们把它们带回到 collection 协议。

所以我们有一个取某个 index 类型来表示位置、在那里给出一个元素的下标。以及一种把那个位置向前移动的方式。

但我们还需要类型提供它们要用于 index 的什么类型。我们用另一个关联类型来做这个。

遵循类型会提供合适的类型。所以 array 或 data 会给出 Int 作为它们的 index 类型。

而 dictionary 会给出它自己的自定义实现，处理它自己的内部逻辑。

所以让我们回到一分钟前为了泛化索引模型而丢掉的 count。它仍然是一个非常有用的属性。所以我们可能想把它作为 collection 上的一个扩展加回来。

某种遍历集合的东西，把 index 向前移动，累加一个计数器，最后返回它。现在，如果我们试图实现这个，我们会遇到另一个缺失的要求。

既然我们从 Int 移到了通用 index 类型，我们不能再假设 index 类型是可相等的。

Ints 是，但任意的 index 类型不一定。而且，我们需要它来知道我们已经到达末尾。

现在，我们可以像之前那样，通过约束我们的扩展来解决。说它只在 index 类型是可相等的时候工作。

但这感觉不对。

我们希望协议易于使用。如果每次写扩展都必须把这个约束放在那里，会变得非常恼人。因为我们几乎总是需要能够比较两个 index。

相反，它可能更好地表达为协议的要求。作为我们 index 关联类型上的约束。

把这个约束放在协议上意味着所有遵循协议的类型都需要为它们的 index 提供一个可相等的类型。

这样你每次写扩展时就不必指定它。

这是契约谈判的另一个例子。

协议的用户有一个他们真的需要能够比较 index 的要求。

而遵循类型，它们检查它们可以在不放弃太多灵活性的情况下合理地满足这个要求。

在这个例子里，它们绝对可以。

array 和 data 用的 Ints 已经是可相等的。而且，随着 Swift 4.2 新的可相等一致性自动合成。

dictionary 要让它的 index 类型可相等也很容易。

接下来，让我们谈用 customization point 优化这个 count 操作。

所以，我们写了一个版本的 count，通过遍历整个集合来计算集合中的元素个数。但显然很多集合可能能做得快得多。比如，假设 dictionary 内部保留一个它所持有元素个数的计数，为了它自己的目的。

如果它有这个信息，它就可以在它自己的 count 实现里直接提供。

这意味着当人们在 dictionary 上调用 count 时，他们得到的是快速的常数时间。而不是我们原始版本在任何集合上工作的线性时间。

但在添加这样的优化时，有件事你需要意识到。那就是 fulfilled protocol requirements 与只是在特定类型上添加大量重载之间的区别。

到目前为止，dictionary 上这个新版本的 count 只是一个重载。这意味着当你有一个 dictionary，并且你知道它是 dictionary。

你会得到更新、更好的版本的 count。

但如果你在泛型算法内调用它呢？所以假设我们想，例如，写一个版本的标准库的 map？如果你还不熟悉，它是一个非常有用的 operation，转换集合中的每个元素。并作为新 array 给回你。

实现相当简单。它只是创建一个新 array，遍历集合，转换每个元素。然后把它 append 到 array。现在，当你像这样 append 元素到 array 时，array 会自动增长。

而且当它增长时，它有时需要重新分配它的内部存储。以腾出更多空间来容纳新元素。

在这样的循环里，取决于它长到多大，它可能需要多次做这件事。而做这个需要时间。分配内存可能相当昂贵。有一个不错的优化技巧可以用在这个实现里。

我们已经确切知道最终 array 会有多大。它会恰好和我们原始集合一样大。

所以我们可以预先在 array 里 reserve 恰好正确数量的空间，在开始 append 之前，这是一个不错的加速。为了做到这个，我们调用 count。

但我们是在这里调用 count，所谓的泛型上下文里。也就是集合类型完全泛型、不具体的上下文。它可能是 array，或 dictionary，或链表，或任何东西。

所以，我们不能知道它是否必然有更好实现的 count 可用。当编译器编译这个代码时。

所以，在这种情况下，实际调用的 count 版本是通用的 count 版本。它在任何集合上工作并遍历整个集合。

如果你在 dictionary 上调用 map，它不会调用我们刚写的 count 的更好版本。

为了让像这样的自定义方法或属性在泛--在泛型上下文中被调用。它需要被声明为协议本身的要求。我们已经确定某些集合绝对有一种提供优化版 count 的方式，所以把它作为协议的要求是有意义的。

现在，即使我们把它作为要求来实现，所有集合也不必提供自己的实现。因为我们已经通过扩展提供了一个在任何集合上都工作的实现。

把要求添加到协议上，同时通过扩展提供默认实现，这就是我们所称的 customization point。

有了 customization point，编译器可以知道可能有更好的方法或属性实现可用。所以，在泛型上下文中，它通过协议动态分派到那个实现。

所以现在，如果你在 dictionary 上调用 map，即使它是一个完全泛型的函数。

你也会得到 count 的更好实现。

添加这样的 customization points，连同通过扩展的默认实现。
是获得与类、实现继承与方法重写所能做到相同益处的真正强大方式。

但这种技术在 struct 和 enum 上也工作，和类一样。

不是每个方法都能这样优化。customization points 对你的二进制大小、编译器运行时性能有很小但非零的影响。所以只有当绝对有定制的机会时，添加 customization points 才有意义。

比如，我们刚写的 map 操作。没有任何不同种类的集合能合理地提供更好的实现。所以把它作为 customization point 没有意义。它只是作为扩展保留。

所以，我们创建了这个 collection 类型，现在它相当功能完备了。它有很多不同的可能遵循类型。以及各种不同的有用的算法你可以为它写。但有时你需要的不止一个协议来对你的类型家族进行分类。

你需要协议继承。关于这个，让我同事 Doug 来和你们谈。

谢谢，Ben。

所以，协议继承从 Swift 一开始就在。

而为了思考我们在哪里需要协议继承。让我们回看我们一直在构建的这个 collection 协议。

它是一个不错的协议。设计得很好。

它描述了一组遵循类型，并给你写出有趣的泛型算法的能力。

但我们不必走很远就能找到其他 collection-like 算法，我们无法用迄今为止的 collection 协议实现。

比如，如果我们想找到集合中最后一个匹配某个 predicate 的元素的 index。最好的方式是从末尾开始，向后走。

collection 协议不允许我们这么做。

或者说我们想构建一个 shuffle 操作，随机打乱集合中的元素。嗯，这需要 mutation，而 collection 不做这个。不是 collection 协议错了。

而是我们需要更多的东西来描述这些额外的泛型算法，那就是协议继承的意义。所以这里 bidirectionalCollection 协议继承自，或者说是一个 collection。

这意味着任何遵循 bidirectionalCollection 协议的类型也遵循 collection，并且你可以使用那些 collection 算法。

但 bidirectionalCollection 添加了这个额外的要求，能够向后步进集合。需要注意的重要一点是，并非每个集合都能真正实现这个特定的要求。想想 singlyLinkedList，你只有这些指针从一个位置跳到下一个。没有高效的方式向后遍历这个 sequence，所以它不能是 bidirectionalCollection。所以一旦引入继承，你就限制了遵循类型的集合。但你允许自己实现更有趣的算法。所以这是 last index where 操作背后的代码。它相当简单。我们只是向后遍历集合，使用 bidirectionalCollection 协议的这个新要求。

让我们看一个更有趣的算法。所以这是为，为 Swift 4.2 中的集合引入的 shuffle 操作。你不必自己实现它，但我们要看算法本身，看它引入了什么要求，来弄清楚如何有意义地把那些分类进协议。

所以 Fisher-Yates shuffle 算法是个相当老的算法。它也相当简单。你从集合中第一个元素的 index 开始。

然后，你随机选择集合中的某个其他元素，交换这两个。

在下一次迭代，你把左 index 向前移动一。

随机选择那里与末尾之间，交换那些元素。所以算法相当简单。它只是线性地遍历集合，随机选择另一个元素来与之交换。最后，你得到一个 nicely shuffled 的集合。

所以，我们实际上可以看这里的代码。它有点 involved。别担心。我们要在某种集合上实现它。所以我们会看其中的核心操作。首先我们需要能够抓取一个随机数，在我们集合中的当前位置与末尾之间，使用这个 random facility。但那是整数。而我们需要的是集合中的 index。我们知道它们不同。所以我们需要某种操作。我们称之为 index offsetBy。

从 startIndex 快速跳到我们选中的位置。

另一个我们需要的操作是交换两个元素。

很好。我们有两个需要添加到 collection 概念上的操作来实现 shuffle。因此，我们有一个新的 shuffleCollection 协议。

请别这么做。所以这是我们看到的一种反面模式。这里的反面模式是，我们有一个算法。我们找到了它的要求，然后把它打包成一个协议，只是描述那个一个--只是描述那个一个算法。如果你这么做，你会有大量大量大量描述不了任何有趣意义的协议。你从那些协议里学不到任何东西。所以你应该做的是注意，我们实际上这里有 distinct capabilities。所以 shuffle 使用随机访问，并且使用 mutation。但这些是，这些是分开的，我们可以把它们分类进单独的协议。比如，randomAccessCollection 协议是允许我们跳转集合，快速移动 index 的地方。

还有像 unsafeBufferPointer 这样的类型可以给你随机访问。但不允许任何 mutation。那是单独的能力。

所以我们也有 mutableCollection 协议在这里。

我们可以想到这里允许 mutation 但不是随机访问的类型，比如我们早先谈过的 singlyLinkedList。

现在，你会注意到我们基本上把继承层级 split 了。

我们有随机访问、双向等的访问侧。然后我们有这个 mutation 侧。这完全没问题，因为客户端自己可以组合多个协议来实现他们正在做的任何泛型算法。所以，我们回到 shuffle 算法。它可以写成 randomAccessCollection 上的一个扩展，带一个 self-type。所以这个类型遵循 randomAccessCollection 也遵循 mutableCollection 协议。现在我们把这两个的能力拉到了一起。

现在，当你有一堆遵循类型和一堆泛型算法时，你往往得到协议层级形成。现在，这些层级，它们不应该太大。它们不应该太细粒度。

因为你真的想要少量的协议，真正描述出在领域里出现的类型种类，对吧？现在，当你构建这些协议层级时，你会注意到一些事。所以，当你从层级底部向上移动时，你会到有更少要求的协议。因此，有更多遵循类型能实现那些要求。

另一方面，当你向下移动层级，并从层级组合不同的协议。你得到实现更 intricate、更 specialized 的算法，需要更高级的能力。但自然地和更少的遵循类型工作。

好的。所以让我们谈条件一致性。这当然是，Swift 中一个较新的特性。让我们先从 slices 再看一遍开始。所以对于你拥有的任何 collection，你可以通过用某个 index 范围下标来形成那个 collection 的 slice。而那个 slice 本质上是集合某部分的视图。

现在这些是从 slicing 一个 collection 得到的默认类型，叫做 slice。

而且 slice 是一个泛型 adaptor 类型。

所以它参数化在一个 base collection 类型上，并且它本身是一个 collection。

所以我们的 slice 期望是，你能在 slice 上做任何你能对底层 collection 做的事。这是合理想要的事。

所以当然我们可以去用前向搜索操作如 indexwhere，去找到匹配 predicate 的东西。这在 collection 和它的任何 slice 上都工作。

所以，我们想要对向后搜索做同样的事，但这里我们会遇到一个问题。即使 buffer 是 bidirectionalCollection，也没有任何东西说 slice 是 bidirectionalCollection。

我们可以修这个。让我们扩展 slice 让它遵循 bidirectionalCollection 协议。

我们需要实现这个 index before 操作，我们可以在底层 base collection 的基础上实现它。

除了编译器会在这里抱怨。

我们对那个 base collection 唯一知道的是它是一个 collection。它在上面没有 index before 操作。

我们知道怎么修。我们所要做的就是给这个扩展引入一个要求，说 base 需要是 bidirectionalCollection。

这就是条件一致性。

它只是声明对协议的 conformance 的扩展。然后是那个 conformance 实际有意义的约束。

而条件一致性的美妙之处是，当你有这些协议层级时，它会 nicely stack。所以我们也可以说 slice 是 randomAccessCollection。当它的底层 base 类型是 randomAccessCollection 时。

现在，注意我这里写了两个不同的扩展。

现在，通常好的 Swift 风格。写一个扩展，让它遵循一个协议，这样你就知道那个扩展是干什么的，你知道它的 meaning。这在条件要求、conformances 中特别重要，因为你对这些扩展有不同的要求。这允许 composability。底层 base collection 能做什么，slice 类型也能做。

所以让我们看条件一致性的另一个应用，也在标准库里，这些是 ranges。所以，ranges 在 Swift 里一直存在。你可以用，比如，这些 dot-dot less than 操作来形成 range。所以你可以形成 double 的 range，你可以形成整数的 range。但有些 range 比其他更强大。所以，你可以迭代一个整数 range 中的元素。嗯，为什么你能这么做？因为一个 intRange 遵循 collection。

现在，如果你实际看类型，它是由那个 dot-dot-less-than 运算符 reduce 的。它恰当的叫做 range 类型。

再次，它在底层 bound 类型上是泛型的。所以在这个例子里，我们有一个 double 的 range，它仅仅存储 lower 和 upper bounds。相当简单。

但，在 Swift 4.2 之前，你会从一个整数 range 得到一个实际上不同的类型。这是 countableRange 类型。

现在，注意它在结构上和 range 类型相同。它有一个类型参数。它有 lower 和 upperBound。但它在那个 bound 类型上添加了几个额外的要求。那就是 bound 是 stridable 的，对吧？意味着你可以 walk through 并 enumerate 所有元素。现在那是你需要的能力，以便你能让 countableRange 遵循 randomAccessCollection。

这启用了 forEach、forEach 迭代循环以及其他东西。

但有了条件一致性，当然，我们可以做得更好。

所以让我们把基本的 range 类型变成 collection，当 bound 类型遵循这个--在这个 stridable 要求上。这是条件一致性的一个简单应用。但当与更好的类型参数一起使用时，它让 range 类型更强大。

现在，注意我只遵循 randomAccessCollection。我并没有真正提到 collection 或 bidirectionalCollection。

对于无条件的 performances，这是可以的。声明遵循 randomAccessCollection 暗示遵循它继承的任何协议。在这个例子里，bidirectionalCollection 和 collection。

然而，对于条件一致性，这实际上是一个错误。

现在，如果你回想 slice 例子，我们需要为 collection 对比 bidirectionalCollection 对比 randomAccessCollection 的这些不同层级有不同的约束。所以编译器强制你思考过这个，并确保你对条件一致性有正确的要求集合。

在这个例子里，整个层级的要求是相同的。所以我们可以显式写出 collection 和 bidirectionalCollection。来断言这就是所有这些 conformance 所在。或者我们可以做 stylistically 更好的事，把不同的 conformance 拆分出来。

现在到这个点，我们的 range 类型相当强大了。它做 countableRange 做的一切。那么我们该对 countableRange 做什么？我们可以扔掉它。在这个例子里我们在谈标准库，有很多代码实际使用 countableRange。所以我们可以把它保留为一个泛型类型别名。

这是一个真的很 nice 的解决方案。所以这个泛型类型别名添加了你需要让 range 可计数的所有额外要求。你需要把它变成 collection 的要求，但它只是底层 range 类型的另一个名字。

再次，这对源码兼容性很棒，因为代码仍然可以使用 countableRange。另一方面，给那些有额外能力成为 randomAccessCollection 的 range 一个名字也很 nice。事实上，我们可以用这个来清理其他代码。说，嗯，我们知道 countableRange 是什么。它是带这个额外 striding 能力的 range，所以我们可以去扩展 countableRanges。而那就是我们有 randomAccessCollection conformance 的情况。

所以，我们在 Swift 4.2 引入了这个，来帮助简化我们处理的类型集合。并让现有的核心类型如 range 更可组合、更灵活。

递归约束描述协议与它们的关联类型之间的关系。这个主题在 WWDC 版本的这个 talk 中没有覆盖。但它是在标准库使用 Swift 泛型系统的重要部分。让我们直接跳进去。

递归约束只不过是协议内提到那个相同协议的约束。

这里，collection 有一个叫做 subsequence 的关联类型。它本身是一个 collection。为什么你需要这个？嗯，让我们看一个依赖它的泛型算法。所以给定一个已排序的集合。我们想找到应该插入一个新值的 index。以维持那个排序顺序。我们要计算值 11 的 sorted insertion point。

当我们把 11 在那个 index 插入时，结果仍然是一个已排序的 array。sorted insertion point of 函数是用二分搜索实现的。

二分搜索是一个经典的 divide-and-conquer 算法。意味着在每一步，它做一个决定，允许它显著减少问题大小。供下一步考虑。对于二分搜索，我们首先看中间元素，8。并把它与我们想插入的值比较。那是 11。

而且因为 11 大于 8，我们知道 11 需要被插入到 8 之后的某处。在集合的后半部分。所以我们把搜索空间减半。

在下一步，我们找到新的中间，14，并与我们想插入的值比较。

十一小于 14，所以 insertion point 必须在中间之前。把剩余集合再减半。

继续把我们看的集合减半。直到我们指向正确的 insertion point。那是我们的 solution。

像这样的 divide-and-conquer 算法 fantastic。因为它们 extremely 快。二分搜索取对数时间。这意味着把你的输入大小加倍不会让算法运行速度减半，像线性算法那样。对于像二分搜索这样的对数算法，它只需要执行一个额外的步骤来再次把问题大小减半。所以让我们把它变成代码。第一件事我们需要做的是找到中间元素的 index。我们可以用 randomAccessCollections 的 index offset by 函数来做。

接下来，我们检查我们的值是否在中间元素之前。这样我们就知道集合的哪一半包含我们的 insertion point。

现在在我们的例子里，要插入的值大于中间元素。所以我们从中间之后的 index 取一个 slice。一直到末尾。并递归地在那个 slice 上调用 sort and insertion point of。这是 divide-and-conquer 算法的常见模式。你减少问题空间然后递归。现在要让这个 work，我们需要那个 slicing 语法。提供一个合适的 collection 的 slice。

我们可以通过引入一个通用操作来为所有 collection 做到这个，它取一个 index 范围并产生一个 slice。像这样。

现在记住我们早先讨论的 slice adaptor 对任何 collection 都 work。提供对底层 collection 元素的视图，它本身是一个 collection。

这让我们 divide-and-conquer 算法对任何 collection work。同时给所有 collection 提供 slicing 语法。那 great，但只有一个问题。

有些 collection 不想要这个特定的 slice 类型。它们真的想提供自己的 slicing 操作，产生不同的类型。String 是最常见的例子。当你 slice 一个 string 时，你得到一个 substring。

所以如果你把我们的 divide-and-conquer 算法应用到 string collection。你真的想要那些以 substring 为单位。而不是 string 的 slice 这样的其他类型。

Range 是另一个有趣的例子。因为它的 slicing 操作返回一个具有新 bounds 的完全相同 range 类型的实例。

所以为了捕捉遵循 collection 的不同类型之间的这种变化，我们可以把新的要求引入 collection 协议。具体来说是 slicing。

所以这里我们把 slicing subscript 拉进 collection 协议本身作为要求。

现在注意这个 subscript 的 result type 由一个新的关联类型描述：subsequence。

现在 string 和 range 都满足 collection 的这些新要求。

对于 string，subsequence 类型是 substring。

对于 range，subsequence 类型将是 range 本身。现在这对 string 和 range 工作良好。但对所有其他 collection 类型，它们不想定制实际的 subsequence 类型。我们可以提供默认的 slicing 限制。

所以这些 collection 类型的作者实际上不必做任何额外工作来遵循 collection。他们免费得到所有 slicing 行为。

所以我们要从 subsequence 开始。

关联类型本身可以有默认值。写在等号之后。对于 subsequence，slice adaptor 类型是一个完美的默认，因为它对所有 collection 都 work。所以这个默认会被任何不提供自己的 subsequence 类型的遵循类型使用。

这与我们早先开始的 slicing subscript 实现配对得很好。写在 collection 协议的扩展里。它可以作为默认实现，提供返回 slice 的 slicing subscript 操作。

我们可以更进一步，把我们默认 slicing subscript 实现的适用性限制在那些我们选择了默认 subsequence 类型的情况。

所以这个模式防止默认实现作为重载出现在那些定制了它们 subsequence 的 collection 类型上。比如 string 和 range。所以对遵循类型来说这都 great。他们免费得到 slicing，或者如果他们想可以定制它。

但记住我们的 goal 在这里。我们试图把我们的 divide-and-conquer 算法写在 collection 协议上。所以我们必须回答一个非常重要的问题。subsequence 做什么？我们对 subsequence 目前所知只是它是 slicing subscript 操作的 result type。但我们需要更多来实际使用它。所以要回答这个问题，我们必须回到我们想要用 subsequence 写的算法。我们的算法是递归的。它形成一个 slice，现在是 subsequence 类型的值。然后递归地在那个 slice 上调用 sort insertion point of。现在这只有当得到的 subsequence 类型本身是一个 collection 时才有意义。

现在当它执行那个调用时，我们要传递一个 collection 的 element 类型的值。但递归调用本身期望的是这个 subsequence 的 element 类型的值。

唯一可能 make sense 的方式是那些 element 类型相同。现在同样的问题出现在从递归调用返回 index 时。它将以 subsequence 为单位计算。但那个返回的 index 也需要是当前 collection 的有效 index。所以我们可以把所有这些要求捕捉在 collection 协议本身。现在第一件事我们想做的是说 collection 的 subsequence 本身是一个 collection。这叫做递归约束。因为关联类型遵循它自己的 enclosing 协议。

然后我们可以用关联类型 where 子句进一步约束我们的 subsequence。正如我们早先谈过的，它有一个 element 类型。而且那个 element 类型需要和原始 collection 的相同。所以我们可以在这里用 same type constraint 来表达。Subsequent element 与 element 相同。

我们可以对 index 类型做完全相同的事。

现在，这些覆盖了我们通过查看 sorted insertion point of 算法的实现所发现的所有 properties。

这引出一个有趣的问题。你能 slice 一个 subsequence 吗？嗯，每个 subsequence 是一个 collection，每个 collection 都有 slice 操作。所以当然你能 slice 一个 subsequence。结果将是 subsequence 的 subsequence。

现在你可以再做一次，得到 subsequence 的 subsequence 的 subsequence。并继续下去 on and on and on。

现在有趣的是，在每一点我们可能有一个 brand-new 类型。所以我们在潜在上有一个无限的类型塔。那 actually okay。

我们的泛型算法中的每个递归步骤可能创建一个新类型。

基于当前 collection 类型。所以只要递归最终在运行时终止，就没有问题。

然而，divide-and-conquer 算法通常可以通过使它们 nonrecursive 来更高效地实现。

所以这是 sort and insertion point of 算法的 nonrecursive 实现。我们要 walk through 它。因为核心算法相同。但它用 while 循环而不是递归地 iteratively 表达。

所以第一件事我们要做的是取整个 collection 的 slice。

这个 slice 变量将代表我们在每次迭代中看的 collection 部分。

现在我们看到熟悉的 divide-and-conquer 模式。找到 slice 的中间。然后把要插入的值与 slice 中的中间元素比较。

然后我们在再次 loop 之前通过 slicing the slice 来缩小搜索基准。

然而，这里我们有问题。我们正在对 slice 变量进行赋值。它是 subsequence 类型。

另一方面，右边是 slice of a slice。正如我们早先谈过的，这是 subsequence 的 subsequence，可能是一个完全不同的类型。所以我们会得到编译器错误，告诉我们这两个类型不一定相同。这 really inconvenient，因为它阻止我们写这个 nonrecursive 算法。而且它并不真正反映特定 collection 类型的行为。想想 string。如果你 slice 一个 string，你得到一个 substring。如果你 slice 一个 substring，你不会得到 sub-substring。

你只是得到 substring 类型的另一个实例。

所以让我们回到这个 slice adaptor 如何 work，来泛化这个 notion。我们有一个 collection。我们把它叫做 Self，我们从 I slice 到 J。

现在那会构建一个 slice of Self 类型的东西。只是对底层 Self collection 的视图。如果我们随后 slice the slice，我们得到 slice of slice of self。这是对那个相同底层 Self collection 的视图的视图。

所以这是我们实践中的无限类型塔。然而，它不必是这样。记住 slice 类型使用与它们底层 collection 相同的 index。而且它们也了解它们底层的基本 collection。所以当我们 slice the slice 时，我们可以取那些新的 index，I2 和 J2。把它们带回原始 base collection，并从那里形成新 slice。而这样做的结果是，当你 slice 一个 slice 时，你得到相同 slice 类型的东西。有效地 tying off the recursion。这 exactly 是我们与 substring 看到的相同行为。而且完全 reasonable 期望所有 subsequence 类型都这样行为。所以让我们把它建模为 collection 协议要求的 explicit 部分。

所以这里我们说 subsequence 的 subsequence 是与 subsequence 相同的类型。换句话说，当你 slice 一个 slice 时，你得到回相同的 slice。

这让我们 nonrecursive divide-and-conquer 算法 work。并简化了 collection 协议的使用。不再需要推理无限类型塔。现在还有这里涉及 subsequence 的一个 last issue。我们说它 required 是 collection。但我们需要 subsequence 类型是 random access collection 来执行这个 index offset by 操作。

为了描述这个，我们可以用 protocol where 子句。所以当 bidirectionalCollection 继承自 collection。它可以对 subsequence 添加一个新约束，要求它遵循那个 bidirectionalCollection 协议。这 again 是递归约束，但现在它在 bidirectionalCollection 协议上表达。我们可以对 randomAccessCollections 做完全相同的事。比如 random access collection 的 subsequence 本身遵循 randomAccessCollection。注意 subsequence 上的约束跟随 enclosing 协议。这可能听起来有点熟悉。

递归约束与条件一致性都倾向于 tracking 协议层级像这样。而且特性支持彼此。这特别重要，因为我们希望 subsequence 的默认关联类型，slice of Self，能在 collection 层级的每个 level 工作。Slice 总是一个 collection。

当我们继续创建 bidirectionalCollection 协议。它现在要求 subsequence 类型也遵循 bidirectionalCollection。

slice adaptor 对 bidirectionalCollection 的条件一致性，当它自身已知是 bidirectionalCollection 时 kick in。满足那个要求。randomAccessCollection work the same way。Subsequence 获得一个 randomAccessCollection 要求。slice 对 randomAccessCollection 的条件一致性满足那个要求。现在 itself 已知是 randomAccessCollection。这种 associated type default 在 hierarchy 内的每个 protocol 都 work 的行为，是 cohesive design 的 good indicator。

如果你发现自己在 collection 层级的不同点需要不同的 associated type defaults。你可能在 design 上有问题。Recursive restraints 是一个 powerful tool。与 associated type 和 protocol where 子句一起使用，它们帮助我们自然地在泛型代码中写出我们需要的 protocol requirements 来表达 divide-and-conquer 算法。现在我们回到 WWDC talk 的最后部分。

所以，Swift 是一门多范式语言。我们刚才一直在只谈泛型。但当然，Swift 也支持面向对象编程。

所以，我想花几分钟谈这两个特性之间的交互。它们在 Swift 语言中如何一起 work。所以有了类继承，我们知道类继承怎么 work。它相当简单。你可以声明一个超类，比如 Vehicle。你可以声明一些子类，比如 Taxi 和 PoliceCar，它们都继承自 Vehicle。

而且，一旦你这么做，你就有了这个面向对象的层级。你对在哪里能使用那些子类有某些期望。所以如果我扩展 Vehicle 用一个新方法，让它 drive，我完全期望我可以在我的子类之一 Taxi 上调用那个方法。

所以，这是面向对象编程的一个 fundamental aspect。而且，Barbara Liskov 实际上在 80 年代的一个 lecture 中很好地描述了这个。

从那以后，我们把这称为 Liskov 替换原则。而且 idea 实际上相当简单。所以，如果你的程序某处引用了一个 supertype，或 superclass，比如 Vehicle。

你应该能够取它任何一个 subtype、或 subclass 的实例，比如 Taxi 或 PoliceCar，并用那个 instead。程序应该仍然继续 type check 并正确运行。

所以，这里的 substitution 是子类的实例应该能够去到任何期望超类的地方并被 tested。而且，这是一个 really simple principle。我们都 internalized 它，但它 also really powerful。如果你想想它。在程序的任何 point 想想 well，如果我得到一个不同的 subclass，也许是一个我在这里没想过 of subclass。

所以，回到泛型，当把 Liskov 替换原则应用到泛型系统时，我们的期望是什么？嗯，也许我们添加一个新协议，Drivable。Whatever。并扩展 Vehicle 让它 Drivable。我们期望发生什么？嗯，我们期望你可以使用 Vehicle 对 Drivable 的 protocol conformance，给它的一些子类 as well。

说，你给 Drivable 协议添加一个简单的泛型算法，去进行 sundayDrive。嗯，现在你应该能够在一个 PoliceCar 上使用那个 API，即使那可能不是最好的 idea。

所以，这里的 protocol conformance effectively 被子类继承。

而且这给 conformance 施加了一个约束。你写的那个 conformance，让 Vehicle Drivable 的东西。现在必须为 Vehicle 的所有子类 work，以及任何后来出现的。

大多数时候，那 just works。

然而，有些情况这 actually 给子类添加了新要求。最常见的一个是处理 initializer requirements。

所以，如果你看过 decodable 协议，它有一个有趣的 require。那就是 initializer requirement，从 decoder 创建 conforming type 的新实例。我们怎么用这个？嗯，让我们给 decodable 协议添加一个便捷方法。它是一个 static 方法 decode，从 decoder 创建新实例，本质上是一个 wrapper for the initializer，让它更容易使用。

而且，有两件 interesting 的事要注意这个 particular 方法。第一，它返回 Self，大写 S。记住这是 conforming type。它与你调用 static 方法的类型相同。

现在，第二件 interesting 的事是，我们怎么实现这个？嗯，我们调用上面的 initializer 来创建 whatever decodable type 我们有的 brand-new 实例，然后返回它。

Fair enough。

我们可以继续把我们的 Vehicle 类型做成 Decodable。

然后，我们期望，应用 Liskov 替换原则，我们可以使用 Vehicle 的任何 subclass。

用我们通过 protocol conformance 构建的这些 new API。所以，我们可以在 Taxi 上调用 Decode。

而我们得到的不是 Vehicle 不是 some arbitrary Vehicle 实例，而是 Taxi，一个 Taxi 的实例。

这 great，但它 how does it work？所以让我们看 Taxi 可能有什么。也许这里有个 hourly rate，当我们从调用 Taxi.decode，我们通过 protocol，通过 protocol initializer requirement。

实际上只能调用一个 initializer，那就是在 Vehicle 类里、在 superclass 里声明的 initializer。

所以那个 initializer，它知道怎么 decode Vehicle 的所有 state。但它对 Taxi subclass 一无所知。

所以，如果我们直接用这个 initializer，我们 actually 会有问题，hourly rate 完全 uninitialized，这可能导致当你收到 bill 时一些 rather unfortunate misunderstandings。

所以，我们怎么 address 这个？嗯，事实证明 Swift 不让你进入这个问题。

它会在你试图让 Vehicle 遵循 decodable 协议的 point 诊断，there's actually a problem with this initializer。它需要被标记 required。

现在，required initializer 必须在所有子类中实现。不仅直接子类，还有它们的子类，任何你还不知道的未来子类。

现在通过添加那个 requirement，它意味着当 Taxi 继承自 Vehicle 时，它 also 需要引入一个同名的 initializer。

现在，这 important，因为这个 initializer 负责 decode hourly rate。然后 chaining up to superclass initializer 来 decode Vehicle 类型的其余部分。

好的。现在，如果你 very quickly 读那些 red boxes，你可能注意到了 subphrase non-final。

所以，根据定义，final classes 没有子类。所以它 essentially 豁免它们 later 被 substituted。

这意味着没有 sense 有 required initializer，因为你知道没有子类。所以 final classes 在 sense 上，与 decodable 或其他 initializer requirements 交互时，a little easier to work with。因为它们被 exempt from 这些 having required initializers 的规则。

所以当你使用类，for reference semantics，consider using final when you no longer need to customize your class through the inheritance mechanism。现在，这 doesn't mean 你不能 later customize 你的类。你仍然可以写一个 extension on it。就像你可以 extend struct 或 enum 一样。

你也可以给它添加 conformances，来获得 more dynamic dispatch。

但 final 可以简化与泛型系统的交互，also unlock optimization opportunities for 编译器 in runtime。

所以今天我们谈了一点 Swift 泛型。Swift 泛型背后的 idea 是提供复用代码的能力，同时 maintain static type information。让写出 correct programs 更容易，并把它们 compile down into efficient、efficiently executing programs。

当你设计协议时，让这个 generic algorithms 你想要写在协议上的 push and pull。和需要实现那个协议的 conforming types 指导你的 design to meaningful extractions。

当你需要一些更 specialized 的 capabilities 来实现只在遵循类型子集上 supportable 的新泛型算法时，引入协议继承。

以及当你写泛型类型时，条件一致性，以便它们能 nicely compose，特别是在与协议层级工作时。

最后，当你 reasoning about 类继承与泛型系统之间 tricky interaction 时。回到 Liskov 替换原则，想想 if I introduce a subclass rather than a superclass at which I wrote the conformance 会发生什么。

嗯，谢谢大家。有几个相关的 session 关于 embracing algorithms 以及它们如何帮助你构建 better code。以及在 everyday programming 中 effectively 使用 Swift collections。

谢谢。

[ Applause ]
