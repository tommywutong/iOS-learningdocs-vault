---
title: 在 Swift 中设计协议接口
session_id: 110353
collection: wwdc2022
year: 2022
duration: '25:31'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2022/110353/'
content_hash: 'sha256:0629907c009fd216'
translated: true
---

# 在 Swift 中设计协议接口

<sub>WWDC2022 · 25:31 · Swift</sub>

学习如何利用 Swift 5.7 通过协议来设计高级抽象。我们将向你展示如何使用既存类型（existential type），以及探索如何……

> [!note] 归档理由
> 协议接口设计与主关联类型（primary associated type）

## 相关资源

- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110353/4/518CFD38-CEE9-4052-8DB9-6692741930F2/downloads/wwdc2022-110353_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110353/4/518CFD38-CEE9-4052-8DB9-6692741930F2/downloads/wwdc2022-110353_sd.mp4?dl=1)
- [使用参数包泛化 API](https://developer.apple.com/videos/play/wwdc2023/10168)
- [拥抱 Swift 泛型](https://developer.apple.com/videos/play/wwdc2022/110352)
- [Swift 新功能](https://developer.apple.com/videos/play/wwdc2022/110354)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ 大家好，我是来自 Swift 编译器团队的 Slava。欢迎观看“在 Swift 中设计协议接口”。

我将接着“拥抱 Swift 泛型”的话题继续讲解，向你展示一些高级技术，用于抽象具体类型（concrete type）以及使用协议来对类型关系建模。本讲座将涵盖已有的语言特性以及 Swift 5.7 中引入的一些新能力。

本讲座包含三大主题：首先，我会通过解释“结果类型擦除（result type erasure）”的工作方式，向你展示带有关联类型（associated type）的协议如何与既存 `any` 类型交互。接着，我会讲解如何使用不透明结果类型（opaque result type）将接口与实现分离，从而改善封装。最后，你会看到协议中的相同类型要求（same-type requirement）如何在多个不同的具体类型集合之间建立关系。

让我们先来学习带有关联类型的协议如何与既存类型（existential type）交互。这里，我们有一个数据模型，包含一对协议和四个具体类型。有两种动物类型：小鸡和奶牛；以及两种食物类型：鸡蛋和牛奶。小鸡产鸡蛋，奶牛产牛奶。为了在食物生产上进行抽象，我将在 Animal 协议中添加一个 `produce()` 方法。你可能还记得“拥抱 Swift 泛型”讲座中提到，对 Cow 和 Chicken 上 `produce()` 的不同返回类型进行抽象，最佳方式是使用关联类型。通过使用关联类型，我们声明：对于某个具体的 Animal 类型，调用 `produce()` 会返回某种具体的 Food 类型，该类型取决于具体的 Animal 类型。我们可以用示意图来展示这种关系。协议 `Self` 类型代表符合 Animal 协议的实际具体类型。`Self` 类型有一个关联的 `Commodity` 类型，该类型符合 Food 协议。让我们看看具体类型 Chicken 和 Cow 与 Animal 协议的关联类型示意图之间的关系。

Chicken 类型符合 Animal 协议，其 CommodityType 为 `Egg`。Cow 类型符合 Animal 协议，其 CommodityType 为 `Milk`。现在，假设我们有一个农场，农场里有很多动物。Farm 上的存储属性 `animals` 是一个 `any Animal` 的异质数组。在“拥抱 Swift 泛型”中，我们看到了 `any Animal` 类型使用了一种容器表示（box representation），能够动态存储任何具体类型的动物。这种为不同具体类型使用相同表示方式的策略被称为类型擦除（type erasure）。

`produceCommodities()` 方法遍历动物数组，对每只动物调用 `produce()` 方法。这个方法看起来很简单，但我们知道类型擦除会消除与底层动物类型之间的静态类型关系，因此值得深入理解为什么这段代码能通过类型检查。

`map()` 闭包中的 `animal` 参数类型为 `any Animal`。`produce()` 的返回类型是一个关联类型。当你在既存类型上调用一个返回关联类型的方法时，编译器会使用类型擦除来确定该调用的结果类型。类型擦除会将这些关联类型替换为具有等效约束的对应既存类型。我们通过将它们替换为 `any Animal` 和 `any Food`，擦除了具体 Animal 类型与关联 CommodityType 之间的关系。`any Food` 类型被称为关联 CommodityType 的上界（upper bound）。由于 `produce()` 方法是在 `any Animal` 上调用的，返回值的类型被擦除，从而得到一个类型为 `any Food` 的值。这正是我们期望的类型。

让我们更仔细地看一下关联类型擦除的工作方式，这是 Swift 5.7 的新特性。出现在协议方法结果类型中（箭头右侧）的关联类型，被称为处于“生产位置（producing position）”，因为调用该方法会生成该类型的值。当我们在 `any Animal` 上调用这个方法时，我们在编译时并不知道具体的结果类型，但我们知道它是上界的一个子类型。在这个例子中，我们在一个运行时持有 Cow 的 `any Animal` 上调用 `produce()`。在我们的例子中，Cow 上的 `produce()` 方法返回 Milk。Milk 可以存储在 `any Food` 内部，`any Food` 是 Animal 协议的关联 CommodityType 的上界。

这对于所有符合 Animal 协议的具体类型来说都是安全的。

另一方面，让我们思考一下，如果关联类型出现在方法或初始化方法的参数列表中会发生什么。这里，Animal 协议上的 `eat()` 方法拥有处于消费位置（consuming position）的关联类型 FeedType。我们需要传入一个该类型的值才能调用该方法。由于转换方向相反，我们不能进行类型擦除。关联类型的上界既存类型无法安全地转换为实际的具体类型，因为我们不知道具体类型。让我们看一个例子。同样，我们有一个存储了 Cow 的 `any Animal`。假设 Cow 上的 `eat` 方法接受 Hay。Animal 协议的关联 `FeedType` 的上界是 `any AnimalFeed`。但对于任意一个 `any AnimalFeed`，我们无法静态保证它存储的是 `Hay` 这个具体类型。类型擦除不允许我们对处于消费位置的关联类型进行操作。相反，你必须将既存 `any` 类型解封（unbox），并传递给一个接受 opaque `some` 类型的函数。

这种带有关联类型的类型擦除行为，实际上与你可能在 Swift 5.6 中见过的已有语言特性类似。考虑一个用于克隆引用类型的协议。该协议定义了一个单独的 `clone()` 方法，返回 Self。当你在一个类型为 `any Cloneable` 的值上调用 `clone()` 时，结果类型 `Self` 会被类型擦除到它的上界。Self 类型的上界总是协议本身，因此我们得到一个新的 `any Cloneable` 类型的值。总结一下：你可以使用 `any` 来声明一个值的类型是一个既存类型（existential type），它存储了某个符合某协议的具体类型。这甚至适用于带有关联类型的协议。当调用一个协议方法，且该方法在生产位置有关联类型时，该关联类型会被类型擦除到它的上界，即另一个携带该关联类型约束的既存类型。对具体类型进行抽象不仅对函数输入有用——对函数输出也很有用，这样具体类型只在实现中可见。让我们看看如何抽象具体的结果类型，以将一段代码的核心接口与其实现细节分离，从而使静态类型分配在面对变化时更具模块性和健壮性。让我们泛化 Animal 协议，使其能够喂养动物。动物会饿，饿了就需要吃东西。让我们在 Animal 协议中添加一个 `isHungry` 属性。Farm 上的 `feedAnimals()` 方法将只喂养那些饥饿的动物。我将计算饥饿动物子集的过程拆分到了 `hungryAnimals` 属性中。`hungryAnimals()` 的初始实现使用了 `filter()` 方法，选择出 `isHungry` 属性为 true 的动物子集。对一个 `any Animal` 数组调用 `filter()` 会返回一个新的 `any Animal` 数组。现在你可能会注意到 `feedAnimals()` 只遍历了一次 `hungryAnimals` 的结果，然后立即丢弃了这个临时数组。如果农场有大量饥饿的动物，这种做法的效率就很低。避免这种临时分配的一种方法是使用标准库的惰性集合（lazy collection）功能。通过将对 `filter` 的调用替换为 `lazy.filter`，我们得到了所谓的惰性集合。惰性集合包含的元素与直接调用 `filter` 返回的数组相同，但它避免了临时分配。然而，现在 `hungryAnimals` 属性的类型必须声明为相当复杂的具体类型 `LazyFilterSequence of Array of any Animal`。这暴露了一个不必要的实现细节。客户端 `feedAnimals()` 并不关心我们在 `hungryAnimals` 的实现中使用了 `lazy.filter`；它只需要知道它得到的是某个可以遍历的集合。不透明结果类型（opaque result type）可以用来将复杂的具体类型隐藏在 Collection 的抽象接口之后。现在，调用 `hungryAnimals` 的客户端只知道他们得到的是某个符合 Collection 协议的具体类型，但不知道该集合的具体类型。

然而，按这样写，实际上对客户端隐藏了过多的静态类型信息。我们声明 `hungryAnimals` 输出某个符合 Collection 的具体类型，但我们不知道这个 Collection 的 `Element` 类型。由于不知道元素类型是 `any Animal`，我们只能传递元素类型，而不能调用 Animal 协议的任何方法。让我们专注于不透明结果类型 `some Collection`。通过使用受限不透明结果类型（constrained opaque result type），我们可以在隐藏实现细节和暴露足够丰富的接口之间取得恰当的平衡。受限不透明结果类型是 Swift 5.7 的新特性。受限不透明结果类型的写法是在协议名称后的尖括号中应用类型参数。Collection 协议有一个类型参数，即 Element 类型。一旦 `hungryAnimals` 被声明为受限不透明结果类型，它实际上是 `LazyFilterSequence of an array of any Animal` 这一事实就对客户端隐藏了；但客户端仍然知道它是某个符合 Collection 的具体类型，其 Element 关联类型等于 `any Animal`。这正是我们想要的接口。在 `feedAnimals()` 的 for 循环内部，`animal` 变量的类型是 `any Animal`，允许对每只饥饿的动物调用 Animal 协议的方法。这一切之所以能工作，是因为 Collection 协议声明 Element 关联类型是一个主关联类型（primary associated type）。你可以通过将一个或多个关联类型放在协议名称后的尖括号中来声明你自己的带有主关联类型的协议，就像这样。最适合作为主关联类型的，是那些通常由调用者提供的关联类型，例如集合的 Element 类型，而不是实现细节，例如集合的 Iterator 类型。你通常会看到协议的主关联类型与符合该协议的具体类型的泛型参数之间存在对应关系。这里，你可以看到 `Collection` 的 Element 主关联类型是由 Array 和 Set 的 `Element` 泛型参数实现的，这两个具体类型都由标准库定义，并且都符合 Collection。`some Collection of Element` 可以与 `some` 关键字一起用于不透明结果类型，也可以与 `any` 关键字一起用于受限既存类型（constrained existential type）。在 Swift 5.7 之前，你需要编写自己的数据类型来表示具有特定泛型参数的既存类型。Swift 5.7 通过受限既存类型将这个概念内建到了语言中。

如果我们希望 `hungryAnimals` 可以选择是惰性还是急切地计算饥饿动物，那么使用 `some Collection of any Animal` 会导致错误，因为函数返回了两种不同的底层类型。我们可以通过返回 `any Collection of any Animal` 来解决这个问题，这表示该 API 可以在不同的调用中返回不同的类型。约束主关联类型的能力为不透明类型和既存类型带来了新的表现力。这可以与各种标准库协议（如 Collection）一起使用；你也可以声明自己的协议拥有主关联类型。

使用不透明类型编写泛型代码必须依赖于抽象的类型关系。让我们讨论如何识别和保证多个抽象类型之间必要的类型关系，使用相关协议来实现。

我们将在 Animal 协议中添加一个新的关联类型，表示该动物所吃的具体动物饲料类型，以及一个 `eat()` 方法，指示动物消耗这种饲料。为了让事情更有趣，我将引入一个额外的复杂性：在喂养动物之前，我们必须先种植合适的作物，然后收获作物以产生饲料。这是第一组具体类型。牛吃干草，所以给一头牛，我们首先需要种植一些干草。这会得到苜蓿，将苜蓿收获并加工成干草，牛才能吃。这是第二组具体类型。鸡吃混合饲料，所以如果你给我一只鸡，我们首先需要种植一种叫做小米的谷物，收获并加工成鸡的混合饲料，然后喂养我们的鸡。我想对这两组相关的具体类型进行抽象，这样我就可以实现 `feedAnimal()` 方法一次，并且它既能喂牛也能喂鸡，还能喂我将来可能收养的任何新类型的动物。由于 `feedAnimal()` 需要处理 Animal 协议的 `eat()` 方法，而该方法在消费位置有一个关联类型，我将通过声明 `feedAnimal()` 方法接受 `some Animal` 作为参数类型来解封既存类型。首先，我将使用到目前为止我们对协议和关联类型的了解，定义一对协议：AnimalFeed 和 Crop。AnimalFeed 有一个关联的 CropType，该类型符合 Crop；Crop 有一个关联的 FeedType，该类型符合 AnimalFeed。和之前一样，我们可以查看每个协议的类型参数示意图。首先，让我们看看 AnimalFeed。每个协议都有一个 `Self` 类型，代表具体的符合类型。我们的协议有一个关联的 `CropType`，该类型符合 Crop。关联的 `CropType` 有一个嵌套的关联 `FeedType`，该类型符合 AnimalFeed，而 AnimalFeed 又有一个嵌套的关联 `CropType` 符合 Crop，以此类推。实际上，这种来回往复会永远持续下去，形成无限嵌套的关联类型，在符合 AnimalFeed 和 Crop 之间交替。

对于 Crop 协议，我们有类似的情况，只是偏移了一位。我们从符合 `Crop` 的 `Self` 类型开始，它有一个关联的 `FeedType`，符合 AnimalFeed。这又有一个嵌套的关联 `CropType`，符合 Crop，以此类推……

直到无穷。让我们看看这些协议是否正确地建模了具体类型之间的关系。回想一下，在喂养动物之前，我们需要种植作物，然后将作物加工成正确的动物饲料类型。`grow()` 是 AnimalFeed 协议中的一个静态方法，这意味着它必须直接在符合 AnimalFeed 的类型上调用，而不能在某个值上调用，即使该值的类型符合 AnimalFeed。我们需要写下符合 AnimalFeed 的类型名称，但我们拥有的只是一个特定值，其类型符合某个不同的协议 Animal。嗯，我们可以获取这个值的类型，我们知道它是某个符合 Animal 的类型，而 Animal 有一个关联的 FeedType，该类型符合 AnimalFeed。

这个类型可以用作方法调用 `grow()` 的基类型。AnimalFeed 上的 `grow()` 方法返回一个值，其类型是 AnimalFeed 的嵌套关联类型 CropType。我们知道 CropType 符合 Crop，因此我可以在它上面调用 `harvest()`。但我能得到什么呢？`harvest()` 被声明为返回 Crop 协议的关联 FeedType。在我们的例子中，由于调用的基类型是 `(some Animal).FeedType.CropType`，`harvest()` 将输出一个类型为 `(some Animal).FeedType.CropType.FeedType` 的值。不幸的是，这是错误的类型。`(some Animal)` 上的 `eat()` 方法期望 `(some Animal).FeedType`，而不是 `(some Animal).FeedType.CropType.FeedType`。程序类型不正确。这些协议定义，按目前这样写，实际上并不能保证如果我们从一种动物饲料类型开始，然后种植并收获这个作物，我们会得到与开始时相同的动物饲料类型，而这正是我们的动物期望吃的。另一种思考方式是，这些协议定义过于宽泛——它们没有准确地建模我们具体类型之间的期望关系。为了理解原因，让我们看看我们的 Hay 和 Alfalfa 类型。当我种植干草时，我得到苜蓿，当我收获苜蓿时，我得到干草，以此类推。现在想象我在重构代码，不小心将 Alfalfa 上 `harvest()` 方法的返回类型改成了 Scratch 而不是 Hay。在这个意外更改之后，具体类型仍然满足 AnimalFeed 和 Crop 协议的要求，尽管我们违反了种植和收获作物会产生与开始时相同的动物饲料类型这一期望的不变量。让我们再看一次 AnimalFeed 协议。真正的问题在于，在某种意义上，我们有太多不同的关联类型。我们需要写下来，这些关联类型中的两个实际上是相同的具体类型。这将防止编写错误的具体类型符合我们的协议；它还将为 `feedAnimal()` 方法提供所需的保证。我们可以使用一个相同类型要求（same-type requirement），以 `where` 子句的形式来表达这些关联类型之间的关系。相同类型要求表达了一种静态保证，即两个不同的、可能嵌套的关联类型实际上必须是相同的具体类型。在这里添加一个相同类型要求，对符合 AnimalFeed 协议的具体类型施加了一个限制。在这个相同类型要求中，我们声明 `Self dot CropType dot FeedType` 与 `Self` 是相同的类型。这在我们的示意图中看起来是什么样的呢？这样来可视化：每个符合 AnimalFeed 的具体类型都有一个 CropType，该类型符合 Crop。然而，这个 CropType 的 FeedType，不仅仅是一些其他符合 AnimalFeed 的类型，它实际上是与原始 AnimalFeed 相同的具体类型。我没有建立一个无限高的嵌套关联类型塔，而是将所有关系折叠到一对相关的关联类型上。那 Crop 协议呢？这里，Crop 的 FeedType 被折叠成了一对类型，但我们仍然多了一个关联类型。我们想说，Crop 的 FeedType 的 Crop Type 与我们最初开始的 Crop 是相同的类型。

现在这两个协议都配备了相同类型要求，我们可以重新审视 `feedAnimal()` 方法。和之前一样，我们从某个 Animal 的类型开始。然后我们得到动物的饲料类型，我们知道它符合 AnimalFeed 协议。当我们种植这个作物时，我们得到某个动物的饲料类型的作物类型。但现在，当我们收获这个作物时，我们得到的不是另一个嵌套的关联类型，而正是我们的动物期望的饲料类型，快乐的动物现在可以保证吃到我们刚刚种植的正确类型的动物饲料了。最后，让我们看一下 Animal 协议的关联类型示意图，它把我们到目前为止看到的所有内容整合到了一起。

这是两组符合类型：首先，我们有 Cow、Hay 和 Alfalfa。其次，我们有 Chicken、Scratch 和 Millet。注意我们的三个协议如何精确地建模了每组三个具体类型之间的关系。通过理解你的数据模型，你可以使用相同类型要求来定义这些不同嵌套关联类型之间的等价关系。泛型代码在进行多个协议要求的链式调用时，就可以依赖这些关系。在本讲座中，我们探讨了何时类型擦除是安全的，以及何时我们需要在类型关系得到保证的上下文中工作。接着，我们讨论了如何使用主关联类型在保留丰富类型信息和隐藏实现细节之间取得恰当的平衡，主关联类型可以同时用于不透明结果类型和既存类型。最后，我们看到了如何使用跨协议（这些协议代表了那些相关的类型集合）的相同类型要求来识别和保证具体类型集合之间的类型关系。感谢你的参与。祝你 WWDC 愉快。
