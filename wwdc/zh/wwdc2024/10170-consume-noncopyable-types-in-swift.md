---
title: 在 Swift 中使用 noncopyable 类型
session_id: 10170
collection: wwdc2024
year: 2024
duration: '22:21'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10170/'
content_hash: 'sha256:94920201c8b1cc60'
translated: true
---

# 在 Swift 中使用 noncopyable 类型

<sub>WWDC2024 · 22:21 · Swift</sub>

开始了解 Swift 中的 noncopyable 类型。了解复制在 Swift 中意味着什么、什么时候你可能想用一个 noncopyable 类型，以及……

> [!note] 归档理由
> noncopyable 类型与所有权模型

## 章节

- [Introduction](/videos/play/wwdc2024/10170/?time=0)
- [Agenda](/videos/play/wwdc2024/10170/?time=30)
- [Copying](/videos/play/wwdc2024/10170/?time=50)
- [Noncopyable Types](/videos/play/wwdc2024/10170/?time=425)
- [Generics](/videos/play/wwdc2024/10170/?time=710)
- [Extensions](/videos/play/wwdc2024/10170/?time=1152)
- [Wrap up](/videos/play/wwdc2024/10170/?time=1284)

## 相关资源

- [Introduction](https://developer.apple.com/videos/play/wwdc2024/10170/?time=0)
- [Agenda](https://developer.apple.com/videos/play/wwdc2024/10170/?time=30)
- [Copying](https://developer.apple.com/videos/play/wwdc2024/10170/?time=50)
- [Noncopyable Types](https://developer.apple.com/videos/play/wwdc2024/10170/?time=425)
- [Generics](https://developer.apple.com/videos/play/wwdc2024/10170/?time=710)
- [Extensions](https://developer.apple.com/videos/play/wwdc2024/10170/?time=1152)
- [Wrap up](https://developer.apple.com/videos/play/wwdc2024/10170/?time=1284)
- [Copyable](https://developer.apple.com/documentation/Swift/Copyable)
- [Swift Evolution: Noncopyable Standard Library Primitives](https://github.com/apple/swift-evolution/blob/main/proposals/0437-noncopyable-stdlib-primitives.md)
- [Swift Evolution：针对 noncopyable 类型的 borrowing 与 consuming 模式匹配](https://github.com/apple/swift-evolution/blob/main/proposals/0432-noncopyable-switch.md)
- [Swift Evolution: Noncopyable Generics](https://github.com/apple/swift-evolution/blob/main/proposals/0427-noncopyable-generics.md)
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10170/4/993789F1-AF44-4E20-8C66-BF59DAC6C1F6/downloads/wwdc2024-10170_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10170/4/993789F1-AF44-4E20-8C66-BF59DAC6C1F6/downloads/wwdc2024-10170_sd.mp4?dl=1)
- [Modern Swift API Design](https://developer.apple.com/videos/play/wwdc2019/415)
- [Player as a struct](https://developer.apple.com/videos/play/wwdc2024/10170/?time=52)
- [Player as a class](https://developer.apple.com/videos/play/wwdc2024/10170/?time=115)
- [Deeply copying a PlayerClass](https://developer.apple.com/videos/play/wwdc2024/10170/?time=180)
- [Copyable BankTransfer](https://developer.apple.com/videos/play/wwdc2024/10170/?time=310)
- [Copying FloppyDisk](https://developer.apple.com/videos/play/wwdc2024/10170/?time=466)
- [Missing ownership for FloppyDisk](https://developer.apple.com/videos/play/wwdc2024/10170/?time=498)
- [Consuming ownership](https://developer.apple.com/videos/play/wwdc2024/10170/?time=540)
- [Borrowing ownership](https://developer.apple.com/videos/play/wwdc2024/10170/?time=566)
- [Inout ownership](https://developer.apple.com/videos/play/wwdc2024/10170/?time=595)
- [Noncopyable BankTransfer](https://developer.apple.com/videos/play/wwdc2024/10170/?time=628)
- [Schedule function for noncopyable BankTransfer](https://developer.apple.com/videos/play/wwdc2024/10170/?time=670)
- [Overview of conformance constraints](https://developer.apple.com/videos/play/wwdc2024/10170/?time=732)
- [Noncopyable generics: 'execute' function](https://developer.apple.com/videos/play/wwdc2024/10170/?time=950)
- [Conditionally Copyable](https://developer.apple.com/videos/play/wwdc2024/10170/?time=1085)
- [Extensions of types with noncopyable generic parameters](https://developer.apple.com/videos/play/wwdc2024/10170/?time=1167)
- [Cancellable for Jobs with Copyable actions](https://developer.apple.com/videos/play/wwdc2024/10170/?time=1214)
- [Cancellable for all Jobs](https://developer.apple.com/videos/play/wwdc2024/10170/?time=1260)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Swift 团队的 Kavon！欢迎来到"在 Swift 中使用 noncopyable 类型"！你和我都是独一无二的，但 Swift 中的值却不是这样。这是因为值是可以被复制的。在编程时，能保证一个值是独一无二的，可以是一个很强大的概念。所以，我很高兴地告诉大家，我们最近在 Swift 中引入了 noncopyable 类型！今天有很多精彩的内容要讲。首先我会回顾一下复制是如何工作的。然后我们会讲讲所有权和 noncopyable 类型，最后我会讲一些更进阶的主题，比如如何在泛型代码中使用 noncopyable 类型，以及如何为这些类型编写扩展。那我们开始讲复制吧！我正在开发一个新游戏，所以我定义了一个 Player 类型，用一个 emoji 来表示玩家的图标。

我们来创建两个 player。到目前为止，它们是一样的。

凭直觉，我知道改变一个 player 的图标不会影响另一个。我们来一步步examine一下这种直觉背后的原理。从第一行开始，player1 是一只青蛙。

这个变量的内容,就是构成一个 Player 的实际数据。这是因为它是一个结构体，而结构体是一种值类型。接着看 player2，我让它和 player1 一样。但这到底意味着什么呢？这意味着我是在复制 player1。当你复制一个变量时，你复制的是它的内容。

所以，当我改变 player2 的图标时，我改变的是一个和 player1 相互独立的 Player。

我甚至都不需要去考虑复制或销毁值的问题。Swift 会替我处理好。

好，但如果 Player 是一个引用类型呢？这仅仅意味着我把它从一个结构体改成了一个类。

用和之前一样的代码，会发生什么呢？我们来拆解一下第一条语句。

在构造一个 PlayerClass 时，会单独分配一个对象来存储它的数据。

player1 的内容,变成了对那个对象的一个自动管理的引用。

这就是"引用类型"的含义。

在下一条语句里，player2 和 player1 相同，也就是说，被复制的是这个引用，而不是对象本身！这有时被称为浅拷贝（shallow copy），速度非常快。

因为两个 player 都指向同一个对象，改变图标会同时影响到它们两个。

所以，这个断言并不成立。

注意，在这两种情况下，复制的工作方式是一样的。唯一的区别在于你复制的是一个值，还是一个引用。你可以通过定义一个执行深拷贝的初始化方法，让一个引用类型表现得像一个值类型。

这个初始化方法就是一个例子。它会递归地重新创建一个对象，以及这个对象所指向的一切。

它的做法是调用 Icon 的初始化方法，用另一个 Player 的 icon 来重新创建它。这有助于确保这个新的 player 不会和另一个共享引用。

我们回到之前的程序状态，也就是在我们让 player2 和 player1 相同之后，来看看深拷贝是如何改变这个行为的。

现在，两个 player 都是指向同一个对象的引用。

在我给 player 的字段写入之前，我现在会先对它调用初始化方法本身，做一次深拷贝。

这会分配一个独立的、但内容相同的对象，从而确保这次变更不会影响到其他任何变量。

事实上，这正是写时复制（copy-on-write）的本质。

它让你在变更时拥有独立性，从而获得和值类型一样的行为。

在设计一个新类型时，你已经能控制别人是否可以对它的值做深拷贝了。而你之前无法控制的，是 Swift 能不能对它做自动复制。Copyable 是一个新协议，描述的是一个类型是否具有被自动复制的能力。和 Sendable 一样，它没有成员要求。

在 Swift 中，默认情况下，一切都被推断为 Copyable。我说的是真的一切。

每个类型都会尝试自动遵循 Copyable。

每个泛型参数都会自动要求你放进去的那个类型是 Copyable 的。

每个协议和关联类型，都会自动要求对应的具体类型遵循 Copyable。

而且，每个装箱的协议类型，也都自动和 Copyable 组合在一起。

你不需要像我这样，自己手动写出 Copyable。它已经在那里了，即便你看不见它。

Swift 假定你想要复制的能力，因为处理 Copyable 类型要容易得多。

但是，也有一些情况下，复制会让你的代码容易出错。假设我正在为我的后端开发一个类型，用来给一次银行转账建模。在现实生活中，这次转账要么处于待处理状态，要么被取消，要么已完成。

我们给这个类型一个 run 方法，用来完成这次转账。我需要安排这些转账的执行，所以这里有一个用来做这件事的函数。显然，如果我不小心把一次转账运行了两次，我的用户不会高兴的，所以我们来做个双重检查。如果延迟小于一秒，我宁愿立刻执行它，但我忘了写 return。所以代码会继续往下执行，再次运行它。像这样一个简单的失误可能代价很高，那我该怎么防范它呢？我可以加一个变量来追踪这次转账的状态。这样，一个断言就能捕获到再次运行它的企图。但是，除非我写了一个能触发它的测试，否则一个断言是发现不了 bug 的。所以，我可能仍然会有这样一个 bug，而它可能会导致我的后端服务瘫痪。事实上，在这个 schedule 函数里还有另一个 bug！想想看，如果这个 sleep 的任务被取消了，会发生什么。如果调用方没有仔细检查抛出的错误，他们可能会忘记取消这次转账。

我可以在我的 BankTransfer 里引入一个 deinit，用来记得去取消它。但这在实践中其实没什么用。

仔细看看 startPayment 函数。它保留了一份这次转账的副本，以便追踪它已经被安排执行了。这就是个问题，因为除非这次转账的所有副本都被销毁，否则它的 deinit 不会执行。这正是我这个问题的根源：我没法控制我这个程序里到底漂浮着多少份这次转账的副本。

所以，虽然能够复制值，对你的类型来说通常是正确的默认选择，但在某些情况下，如果这个类型是 noncopyable 的会更好。

我们先把 BankTransfer 的问题放到一边，来了解一下 noncopyable 类型。

假设我想给一个 FloppyDisk（软盘）建模。像这样写的话，这个类型会有一个默认的 Copyable 一致性。

但是，如果在你声明一致性的地方，我在 Copyable 这个词前面加上一个波浪号，那我就是在抑制它默认对 Copyable 的一致性。现在，FloppyDisk 完全没有 Copyable 一致性了！把 tilde-Copyable（波浪号 Copyable）想象成是在为你标注的这个类型声明"没有 Copyable"。那么，当你试图复制这块软盘时，会发生什么呢？复制是不被支持的，所以 Swift 会转而消耗（consume）它。

我可以通过写 consume 来把这一点显式表达出来，但不管我写不写，这件事都会发生。

消耗（consuming）一个变量会取走它的值，让这个变量处于未初始化状态。

所以，在这次 consume 之前，只有 system disk 是已初始化的。

这次 consume 会把 system disk 的内容移出来，放进 backup disk 里。

之后再去读取 system disk 就是一个错误了，它里面已经什么都没有了。

现在，来看看这个用来创建新磁盘的函数。

当它调用 format 时，变量 result 会发生什么呢？这很难说清楚，因为这个函数的签名并没有声明它对这个磁盘需要什么样的所有权。对于 copyable 的参数，你不需要考虑这个问题：format 实际上会收到这个磁盘的一份副本。但是，对于 noncopyable 的参数，你必须声明这个函数对这个值拥有什么样的所有权，因为我们没法复制它。

第一种所有权叫做 consuming（消耗）。它意味着这个函数会把这个参数从它的调用方那里拿走。它会归你所有，所以你甚至可以变更它。

但是，在这里使用 consuming 会有问题，因为 format 并不会把这块磁盘还回去；它什么都不返回。

不过，仔细想想，格式化一块磁盘只需要临时访问它就行了。

当你对某样东西拥有临时访问权时，你是在借用（borrowing）它。借用会给你对这个参数的只读访问权，就像一个 let 绑定一样。

在底层，几乎所有 Copyable 类型的参数和方法都是这样工作的。

区别在于，你不能消耗或变更一个显式借用的参数。你只能复制它。因为我们的 format 函数最终需要变更这块磁盘，所以我们也不能对它使用 borrowing。

最后一种所有权，你已经很熟悉了，那就是 inout！对于方法来说，等价的写法是 mutating。

inout 会给你对调用方那个变量的临时写访问权。因为你拥有写访问权，你可以消耗这个参数。但是，你必须在函数结束之前的某个时刻，重新初始化这个 inout 参数。因为调用方期望在你返回时，那里已经有了一个值。好，我们回到 BankTransfer 这个例子，因为现在我们可以把它建模成一种可消耗的资源了。首先，我把 BankTransfer 变成了一个 noncopyable 的结构体，并把它的 run 方法标记为 consuming，这会把 self 的值从调用方那里拿走。仅凭这两处改动，我就不再需要断言了。Swift 保证了我不能对同一次转账调用两次 run 方法。事实上，它的所有权被追踪得如此精确，以至于我可以给这个结构体加一个 deinit，如果它被销毁（而不是被"运行"）,就触发一个动作。因为我这个 'run' 方法结束时也会自动销毁 self，我会在那里写上 discard self。那会销毁它，但不会调用 deinit。我们来看看我这个 schedule 函数里的那些 bug 会怎么样。首先，我得为 transfer 这个参数加上所有权标注。因为 'schedule' 本来就是要作为最后一次使用，所以用 consuming 是合理的。现在，当我尝试编译这段代码时，我会看到 Swift 精准地定位到了我的 bug。因为这个 if 语句会继续往下执行，所以这次转账有可能被消耗两次。

而加上 return 就能防止这种情况。那另一个 bug 呢？它也被彻底消除了。schedule 是这次转账的最后一个持有者，所以如果 Sleep 抛出错误，它的 deinit 就会执行，从而取消这次转账。

noncopyable 类型是提升程序正确性的一个很好的工具。你可能希望在任何地方都用上它们，包括在泛型代码里。好消息是，在 Swift 6 中，你现在就可以做到了，借助 noncopyable 泛型！这并不是什么全新的泛型系统。它是建立在 Swift 现有的泛型模型之上的。所以，我们先来重新认识一下泛型。

作为铺垫，我们来考虑一下 Swift 中类型的整个"宇宙"。

每个类型都愉快地共存在这里，不管它是一个 String，还是我自己定义的一个叫 Command 的类型。

我的协议 Runnable 在这个宇宙里定义了一个子空间，里面包含了遵循它的那些类型。目前，还没有任何类型遵循它，所以它是空的。但是，如果我给 Command 扩展一个 Runnable 一致性，那它的位置就会移动到 Runnable 这个空间里。

泛型背后的一个核心理念是：一致性约束描述的是泛型类型。我们借助这个叫做 execute 的泛型函数来思考一下这一点。

注意这里尖括号里的这个 T。它声明了一个新的泛型类型参数，代表这个宇宙里的某个类型，但我们不知道具体是哪一个。还记得我说过 Copyable 无处不在吗？对这个 T 是有一个默认约束的。它要求传入的类型遵循 Copyable。

Command 默认遵循 Copyable；而 Runnable 也继承自 Copyable。事实上，直到最近，Swift 里整个类型的宇宙其实都只是披着不同外衣的 Copyable 而已。

这意味着，这个空间里的所有类型都可以传给我的 execute 函数。因为唯一的约束就是 T 遵循 Copyable。

所以，即便 Command 同时也遵循 Runnable，它仍然存在于这个更广阔的 Copyable 空间里，在这个空间中，某个具体的类型可能是 Runnable 的，但也可能不是。我的泛型参数 T 并不排斥那些拥有额外一致性的类型。按目前的写法，execute 函数承诺，除了 Copyable 之外，不需要任何其他一致性也能正常工作。

不过，要实现我的 execute 函数，我其实是希望 T 是 Runnable 的，因为我需要调用一个 run 方法。所以，我会用一个 where 子句，给 T 加上一个 Runnable 约束。

这样一来，我就进一步收窄了允许用作 T 的类型的空间。现在它变成了一个更窄的空间：Runnable & Copyable。这包含了 Command，但现在排除了 String，因为 String 没有 Runnable 一致性。

从 Swift 5.9 开始，我们的这个宇宙已经扩展了。因为，出现了一些不遵循 Copyable 的类型。

举例来说，我们那个闪亮的新类型 BankTransfer 并不遵循它，所以它的位置在这个空间之外。

因为我们只能通过写波浪号 Copyable 来抑制对 Copyable 的一致性，所以我就把这个更广阔的空间称为这个。

Swift 里你熟悉的大多数类型确实都遵循 Copyable。

那么，它们是怎么被包含在 tilde Copyable（波浪号 Copyable）里的呢？和之前一样，在这个更广阔的空间里，你不能假设某个特定的类型一定遵循 Copyable。它可能是 Copyable 的，但也可能不是。这就是你应该如何理解 tilde Copyable 的方式。

那 Any 类型呢？它一直都是 Copyable 的；而且理应如此。当你想到几乎任何编程语言里的 any 类型时，它都是 Copyable 的。

现在，我们准备好来聊聊 noncopyable 泛型了。

我们先从前面那个 Runnable 协议开始。

我们目前类型的宇宙看起来是这样的。所有 Runnable 的值都是 Copyable 的。

BankTransfer 不是 Copyable 的，所以它也不能是 Runnable 的。但是，我希望 BankTransfer 能遵循这个协议，这样我就可以在泛型代码里使用它了。能不能复制一个 Runnable 类型，这一点对这个协议来说并不是根本性的，所以，我会通过加上波浪号 Copyable，把 Copyable 约束从 Runnable 上移除。

这改变了这个层级结构，所以现在 Copyable 这个空间只是和 Runnable 有重叠，而不是包含它。Command 是 Runnable & Copyable 的，所以它就位于这个重叠区域里。

接下来，如果我给 BankTransfer 扩展一个 Runnable 一致性，它的位置就会移动到 Runnable 里面，但不属于 Copyable。

我们再来看看我们那个泛型函数 execute。

泛型参数 T 上仍然有一个默认约束。所以，只有像 Command 这样，同时是 Runnable 和 Copyable 的类型，才被允许用在 execute 里。

我们用波浪号 Copyable，把 Copyable 约束从 T 上移除。

移除这个约束会扩大允许使用的类型范围，扩大到所有 Runnable 的类型。execute 函数这样写就是在表明：T 可能不是 Copyable 的。这是关键所在：一个普通的约束会通过变得更具体，来收窄允许使用的类型；而一个波浪号约束则会通过变得不那么具体，来扩大范围。

好。现在，我们把所有这些理论付诸实践。我这里有一些 Runnable 类型，我想把它们包装进一个叫做 Job 的新结构体里。我把 Job 定义为带有一个泛型参数 Action，这个 Action 是 Runnable 的，可能不是 Copyable 的。但按我目前写的这样，我会得到一个错误。结构体 Job 默认遵循 Copyable，所以它只能包含 Copyable 的数据。要在另一个类型里存储 noncopyable 的值，有两种方式。要么它必须放在一个类里面，因为复制一个类只会复制一个引用；要么你必须在容器类型本身上抑制 Copyable。我会选择第二种方式，让 Job 变成 noncopyable 的。

我仍然可以把 Command 这个类型用作 Action，因为 Action 并不会阻止 Copyable 的类型出现在这里。Job 承诺它不需要复制一个 Action，所以 noncopyable 类型同样也能用。但是，如果我知道我用作 Action 的类型是 Copyable 的呢？那么 Job 应该是可以被复制的，因为它只是一个 action 的容器而已。

作为这个 API 的作者，我可以通过声明 Job 是有条件地 Copyable 的，来允许这一点。这个扩展的意思是：当 Job 的 Action 是 Copyable 时，Job 也是 Copyable 的。

这在我们的宇宙里看起来是什么样的呢？在我们为 Action 填入一个具体类型之前，我们并不知道一个 Job 是不是 Copyable 的。那我们来填入 Command。

我们知道 Command 是 Copyable 的，所以一个 Command-Job 也是 Copyable 的。

但是，如果我把 Action 换成 BankTransfer，这个条件一致性就不满足了，所以一个 BankTransfer-Job 就不是 Copyable 的。

所以，noncopyable 泛型背后的整个理念，就是移除默认的 Copyable 约束。

你已经看到了如何定义一个带有 noncopyable 泛型参数的类型。我们再来仔细看看这个类型的扩展。

假设我想为 Action 定义一个 getter 方法。

我会用一个普通的 Job 扩展来添加它。

调用它是完全没问题的……但这不是在给我一份 Action 的副本吗？没错。返回这个 action 确实会复制它。而这在这个扩展里并不是一个错误。

因为这个普通的扩展默认会被约束为：只适用于 Action 是 Copyable 的那些 Job。

所以，这个 getter 是正确的，因为它单纯地就不能被调用，比如说，不能在一个 BankTransfer 的 job 上调用。

所有的扩展都是这样工作的：被扩展类型作用域内的任何泛型参数，都会被约束为 Copyable。这也包括协议里的 Self。

让扩展以这种方式工作，有一个非常好的优势。假设 Job 其实是我没有写的某个 JobKit 模块的一部分。

我这里有一个协议，用来描述 Cancellable（可取消）的类型。假设我完全不知道什么是 noncopyable 类型，但我还是想让 Job 遵循它。

这没问题，因为我可以写出这个扩展，它就是能正常工作。

这是因为，这个一致性默认是有条件的，条件是 Action 是 Copyable 的，因为一般来说，Action 可能并不是。而当 Action 是 Copyable 时，Job 也是，也就是说它遵循 Cancellable。

所以，你可以把这个 Job 类型发布出去，那些只处理 Copyable 类型的程序员也能使用它。那现在，如果我确实想让这个扩展适用于所有的 job，不管它是不是 Copyable 的呢？

那我只需要把这个扩展里 Action 上的 Copyable 约束去掉就行了。现在，Job 遵循 Cancellable，而不再假设 Action 是 Copyable 的。

今天，我们了解了复制在 Swift 中是如何工作的，以及它在哪些地方会带来挑战。noncopyable 类型是提升程序正确性的一个有用工具，代价是你需要去考虑所有权问题。我们已经在标准库里迈出了采用 noncopyable 泛型的第一步，涉及 Optional、UnsafePointer 和 Result。你可以阅读关于以下内容的 Swift Evolution 提案来了解更多：noncopyable 泛型、针对 noncopyable 类型的 borrowing 和 consuming 模式匹配，以及 noncopyable 标准库原语。你也可以在《The Swift Programming Language》这本书里了解更多。更广泛地说，如果你想了解写时复制,以及设计泛型类型的最佳实践，可以看看 WWDC 2019 的"Modern Swift API Design"。

谢谢大家，祝 WWDC 愉快！
