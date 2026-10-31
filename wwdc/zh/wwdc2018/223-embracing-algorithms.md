---
title: 拥抱算法
session_id: 223
collection: wwdc2018
year: 2018
duration: '40:13'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2018/223/'
content_hash: 'sha256:796880010fb5f3bc'
translated: true
---

# 拥抱算法

<sub>WWDC2018 · 40:13 · Swift</sub>

当你想象构建一个新 App 时，你在想什么？模型、视图和控制器在设计中理应占据突出的位置……

> [!note] 归档理由
> 算法与集合抽象的思维方式

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2018/223plbqb0sfpv80/223/223_hd_embracing_algorithms.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2018/223plbqb0sfpv80/223/223_sd_embracing_algorithms.mp4?dl=1)
- [演示文稿幻灯片（PDF）](https://devstreaming-cdn.apple.com/videos/wwdc/2018/223plbqb0sfpv80/223/223_embracing_algorithms.pdf?dl=1)
- [认识 Swift Algorithms 和 Collections 包](https://developer.apple.com/videos/play/wwdc2021/10256)
- [Swift 泛型（扩展版）](https://developer.apple.com/videos/play/wwdc2018/406)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好。今天见到各位真高兴。我是 Dave，接下来的 40 分钟关于理解并尊重让我们的程序真正工作的根本。

会有实用建议，但这不是关于技巧与技术的讲座，也不是关于任何特定算法的讲座，尽管我们会看几个。

这是关于揭示某种根本性的东西，而它的潜力已经存在于你的代码中。我希望对至少几位听众来说，这标志着与编程实践建立新关系的开始。

就个人而言，当我发现这种方法时，它改变了我人生和职业的轨迹。这就是我如此关心软件库的原因，但也是此后我写过的每一段具体代码的可靠性、可维护性和性能的来源。

但在进入正题之前，让我介绍一位朋友。

这是 Crusty。

Crusty 是老派的。他不信任调试器，也不折腾集成开发环境。不，他喜欢 80×24 的终端窗口配纯文本，谢谢。

Crusty 对最新的编程潮流持怀疑态度，所以有时要把他拖进 21 世纪需要费点劲。他只是想得不同。

但如果你仔细听，你能学到一两件事。有时他晦涩的格言，比如"编程揭示真实"，几乎带有神秘色彩。为了理解他，我发现实际写代码很有帮助。

所以，最近我一直在开发一个名为 Shapes 的小程序。

我希望把它做成一个全功能的矢量绘图程序，但目前它只允许你在无限画布上排列形状。

现在我想讲讲删除选中项命令的故事，因为实现这个单一功能让我学到了很多。

我想我们作为程序员在学习如何从数组中移除东西时，可能都经历过部分这个过程。每个人都从类似这样开始。

这就是删除选中项命令。

我们从 0 循环到 count，找到要删除的东西就移除它，然后继续循环，直到，哎哟，我们越界了。

数组变短了，但我们在循环开始时就选定了迭代次数。幸运的是，如果你使用 Swift 并测试代码，你不会错过这个 bug，因为它会 trap。但如果你像我一样作为 C 程序员学到这个教训，可能就没那么幸运了。好的。我们可以通过用一个稍微丑一点的 while 循环替换 for 循环来修复它，这样就能在每次迭代检查 count。但这个也有一个微妙的 bug。

如果两个连续元素都被选中，它会移除第一个，然后立刻跳过下一个。这个 bug 更阴险，因为它隐藏起来，除非你的测试恰好覆盖到它。但如果我们幸运地注意到了，就继续修正实现，通过在 else 块中守护 increment。那么，我们现在完成了吗？我们确定这个是对的吗？我想我可以向自己证明它能工作。

Anyway，经历了这次 ordeal，我们怎么办？当然，我们把这个九行模式锁进大脑，以便每次需要删除东西时都能拿出来。我确定你们很多人一直在忍着别对我大喊，因为有更优雅的方式。我记得自己发现这个技巧的那天，因为一旦找到，你就再也不会做这个九行舞蹈。迭代限制和下一个要检查的项的索引不断在我们脚下移动，因为 remove(at: i) 会改变 i 之后数组的部分。

但如果你倒着来，你只迭代你还没有改变的数组部分。

很酷，对吧？这就是我从那以后一直使用的模式，因为它简洁，从不失败，直到几个月前。一天早上，我刚吃完牛油果吐司，闲来无事摆弄 App，试图从一个非常复杂的画布中删除大约一半的形状。

我的 iPad 冻结了大约三秒。所以我抿了一口半咖啡因三份浓缩的拿铁，装在竹制保温通勤杯里，开始考虑我的选项。

这令人不安。我是说，这是相当直接的操作，我的代码那么干净，怎么可能错了？性能分析显示热点就在这里，但除此之外，我一筹莫展。就在这时，Crusty 走到我身后，手里拿着从本地超市买的便宜咖啡粉，准备他的每日冲泡。

"卡住了？"他说。"嗯，"我叹了口气，解释了情况。"嗯，你看过那个的文档吗？"我还没看过，所以我弹出 Remove At 的 Quick Help，Crusty 凑过来。"问题就在这里，"他说，留下一个污迹在我 gorgeous 的 retina 显示屏上。

现在我用手工制作的意大利超细纤维布小心擦掉指纹，Crusty 说："这告诉你什么，孩子？" "嗯，"我说，"这意味着移除一个元素需要的步数与数组长度成正比。"这有点道理，因为数组必须把后面的所有元素滑动到新位置。

"那这对你的删除选中项命令意味着什么？"他问。

"呃，"我说。就在这时他掏出一包薄荷锭，把它们排在我的桌上。"你自己试试。"所以我按照过程回答他的问题。"嗯，因为删除选中项要执行 n 步，每个被选中的元素一次，而且你可以选多达 n 个元素，总步数与 n 的平方成正比。"Crusty 补充："那是二次的，孩子，无论你用丑陋的正向方式还是花哨的反向方式。"我那时意识到，对于我 10 到 20 个元素的小测试用例，我们只在说几百步，而且步数相当快，看起来很棒。

但问题在于它扩展性不好。50 的平方是 2500，100 的平方是 10000。所以如果你在这个小区域里做所有测试，你可能永远看不到它，但可扩展性很重要，因为人们越来越多地使用手机和平板管理数据，我们不断出货内存更大的设备来帮助他们。

你关心这个，因为可扩展性是用户可预测性。所以，现在我理解了问题，但仍然不确定该做什么。"现在怎么办？"我问 Crusty。

"你知道，孩子，"他说，弹着一个锭，"有一个算法可以做到。"我告诉他："听着，Crusty，我是 App 开发者。

你说你不做面向对象。嗯，我也不'做'算法。"你在算法课上注意数据结构，因为你知道求职时面试官会问你。但在真实编程世界里，把精英和新手区分开的是把控制器、委托和响应者连在一起构建工作系统的能力。"Bonkey，"他说；我不知道他为什么这么叫我，"计算机做什么？" "它们计算。" "所有这些里计算在哪里？" "嗯，"我答，"我猜我的代码里没看到任何看起来像算法的东西。"但 Crusty 不接受。"哦，你的 App 里全是算法，"他说，把一本老死树字典拍到我桌上，"查一下。"我恢复镇定后，小心地把书滑到一边，输入 Define Algorithm 到 Spotlight，Crusty 认为这是个 neat trick。

嗯。计算或其他问题求解操作中遵循的过程或规则集合。

嗯，仔细想想，这听起来像大多数代码，但我仍然不确定。

"你做过长除法吗？"Crusty 问。"那就是算法。"我开始在 Spotlight 里输入，但他 snaps："在纸上。"不想让自己尴尬，我把话题转回我的代码。

"嗯。"我问："那么，这个能治愈我性能问题的魔法算法是什么？" "嗯，如果你让我用你那 TTY 一分钟，"他说，"这东西怎么用？哦，是 track pad。我会尽量不碰它。所以，首先，你去掉这些 foolishness。

现在，shapes.removeAll(where: shape is selected)。嗯。试试看。"现在 Crusty 去洗咖啡壶的罐子了，留我搞清楚代码里刚发生了什么。首先，我检查发现性能问题已修复。不错。

我不想再听 Crusty 关于查看文档的耳语，所以我弹出 Quick Help for removeAll(where:，看到它的复杂度与集合长度成正比，就像 removeAt 一样。但因为我不必把它放在循环里，这成了整个操作的复杂度。

现在我想给你一些直观感受这种差异的大小。n 是什么意思：算法运行时间随问题规模线性缩放。图是一条直线。

现在橙色线是 order n squared 的形状。

如你所见，线性算法在小问题上可能更差，但它最终比二次算法更快。

酷的是，不管你把线性算法的步骤做多贵，只要你继续看更大的问题规模，总会找到一个点，线性算法获胜并永远继续获胜。

所以我们在说可扩展性，不是绝对性能。

我的可扩展性问题已修复，但我真的想看看标准库如何改进我的反向删除方案。

Crusty 提醒我 Swift 是开源的，所以我可以在他称为"hipster web"的东西上 pull up，但我们都叫它 GitHub。

我首先注意到的是 dot comment，它是所有 Quick Help 的来源，描述算法做什么以及其复杂度。其次，原来 removeAll(where) 不仅仅是 reg 上的某个方法；它是一个通用算法，意味着它在多种不同集合上工作。

它依赖几件事：重新排列元素的能力，来自 mutable collection；改变长度和结构的能力，来自 range-replaceable collection。它由几个其他 order n 算法构建。第一个是 half stable partition，它把满足某个 predicate 的所有元素移动到末尾，并告诉我们 suffix 从哪里开始。

half stable 名字中的 "half stable"，表示它保留不移动元素的顺序，但可能打乱移动到末尾的元素顺序。有时这不重要；第二个算法 removeSubrange。 anyway 它们只是要被删除。

我们见过这个 partial range notation 吗？这只是写 extend 到集合末尾的 range 的 convenient way。

好的。removeSubrange 是库的 public API 的一部分，所以你可以在 online 找到其文档，但 halfStablePartition 是实现细节。现在我们不会 walkthrough 全部，但有几件事值得注意。

首先，它开始时调用另一个算法 firstIndex(where:)，找到属于 suffix 的第一个元素的位置。

接下来，它设置循环变量 j，只有一个循环，循环索引 j 每次迭代向前移动一。

所以可以确定 j 对元素只做一次 pass。你几乎可以从这点看到 order 和 complexity。最后，因为这个方法需要重新排列元素但不改变集合的长度或结构，它只依赖 mutable collection conformance。所以这是我学到的第一课。

熟悉 Swift Standard Library 里有什么。

它包含一套具有 documented meanings and performance characteristics 的算法。

虽然我们碰巧 peeked at implementation，你可以从中学到很多，但它设计成你不必这样做。

官方文档应该告诉你有效使用库所需的一切。你甚至会找到 playground tutorial。

现在我意识到 Swift 里有很多东西，看起来 daunting，但你不必记住一切。对有什么在那里以及如何找到它有概念，将带你走得很远。

在我们继续之前，我想指出 Crusty 做出这个改变时代码里还发生了另一件事。这些哪一个最直接描述其 meaning？现在我实际上必须 read and think through 第一个才知道它在做什么。嗯。也许我最好 add a comment。好的。看起来怎么样？哦，即使有那个 comment，reverse iteration 也有点 tricky，我不想有人因为不理解而破坏这段代码。所以我最好解释一下。好的，我们澄清事情时，After code with trailing closure syntax 读起来更好。现在深呼吸再看一遍。

哪一个更明显正确？即使有所有这些 comments，我仍然需要 read through 第一个才能看到它 inefficiently 做与第二个相同的事。

使用算法让代码在各方面都更好。所以这是 guideline，Shawn Perin 首先提出的 aspiration for your code。

每次你写一个 loop，用 call to an algorithm 替换它。如果你找不到，就自己 make that algorithm，并把 loop 移入其实现。

真正 follow 这个现在对你可能看起来 unrealistic，但到 talk 结束时，我希望不会。

为了稍微激励一下，想想上次你看 spaghetti code。它充满了 loops 吗？我打赌是的。All right. Done and done. 我刚刚让代码更短、更快、在各方面都更好。我准备 call it a day。"谢谢你的帮助，Crusty，"我说，扣上 bespoke leather messenger bag 上的 titanium carabiners，但他 suspiciously 看着我，说："你 Suppose 你可能在别处也犯了这个 mistake？"我叹了口气，放下包，开始 hunting down 代码里的 loops。

文件里有很多。Bring to front、send it back、bring forward，它 sort of hops selected shape over the one in front。

让我们再做几次。Send backward with hops，under the shape，below selected shape，最后是在左侧 shape list 中 dragging。这些听起来 really simple，直到你意识到它们都要在可能不 contiguous 的多个 selected shapes 上操作。

所以 turns out 合理的行为是操作完成后所有 selected elements 保持 next to each other。所以当你 bring shapes forward 时，你 hop front most selected shape 到其 neighbor 前面，然后把其他 ones group 在它后面。

当你 send shapes backward 时，你 hop bottom most selected shape backward 到其 neighbor 后面，并把其他 ones group 在它前面。

所以如果你没完全 follow，别担心。我们会回来。但 suffice it to say 我有一些相当 carefully worked out 的 code 来把所有细节 right。

例如，这是 bringToFront，当我 look at it 时，sure enough，有一个 order n loop over shapes，包含两个 order n operations，remove(at:) 和 insert(at:)，这使它，你猜对了，n squared。

事实上，同样的 problem 出现在我其他四个命令中。

所有这些 implementations 都 loop over an array，执行 insertions and removals，这意味着它们都是 quadratic。现在我有点 discouraged，所以我问 Crusty 是否愿意和我一起看。

他说："不能太晚 stay，"他说，"我今晚有 ballroom dancing，但我想我们 better get a move on。"所以我 pull up bringToFront，Crusty 的第一个问题是："它实际上做什么？" "嗯，"我说，"有一个 while loop，j tracks insertion point，i tracks 我们正在看的 element。" "用 words，not in codes，"Crusty 说。

"描述它。" "好的。Let's see。它把 selected shapes 移到前面，maintaining their relative order。" "Write that down in a dot comment 并 read it back to me。"我是 superfast typist。

"Moves the selected shapes to the front, maintaining their relative order。" "Sound familiar？"Crusty 说。

就在这时我意识到这很像 half stable partition，除了它是 fully stable。我开始 excited。你认为这个叫什么？所以我猜："Stable partition？" "That's right。One of my old favorites，你可以在 Swift Open Source project 的这个 file 中找到 implementation。"所以我把文件 pull into 我的 project，Crusty mumbled something about 我们添加的 comment 应该一直都在，我开始 coding，到 about this far before I had a problem。

你看，stable partition takes a predicate，说是否把 element 移入 collection 的 suffix。所以我必须用 moving things to the back 来表达 bring to front。

我 look at Crusty。

"Visualize it，"他说。所以我 close eyes，watch as unselected shapes gathered at the back，这给了我 answer。现在我觉得 sendToBack 甚至更 easy，因为我们只需 invert the predicate。我们把 selected ones 送到 back。现在我 just about to attack bring forward command，我 figured Crusty 会和我一样 eager to move on，given 他 evening 的 plans，但他 stopped me。"Hold your horses, Snuffy。

我不想错过 opening tango，但 aren't you going to check whether it'll scale？"他有道理，所以我 pop up Quick Help for stable partition，看到它有 (n log n) complexity。所以要 think about (n log n)，look at log n。它开始 level off really quickly，越大 grow 越慢，越接近 constant。所以当你 multiply by n，你得到 something that doesn't scale quite as well as order n but gets closer and closer to linear as it grows。

所以 order n login 通常被 rightly treated as being almost the same as order n。我相当 happy。所以我们 moved on to bring forward。现在如我们 earlier 所说，bring forward bumps front most selected shape forward by one position 并 gathers other selected shapes behind it。

但 Crusty 一点也不喜欢这种 thinking。"开头那个 little do-si-do 让 line dance 看起来像 Fox Trot。"他说，"你不需要它。"我 blankly 看着他，他 broke out lozenges again，用他的五根 free digits 执行 bringForward command。

"See it again？"他问。

我有点像 Three-card Monte 里的 mark，但我 played along。"Look familiar？" "No。"他 threw a hanky over the first few。

"How about now？"就在这时我意识到这不过是另一个 stable partition。

Okay。我 got this，我想。

如果我们找到 front most selected shape，然后 move to its predecessor，并 isolate 从那里开始的 array section，我们就可以 partition 那部分。

"但你怎么 modify just part of a collection？"我问 Crusty。

"Ain't you never heard of a slice？"他说，taking over keyboard。

"Shapes, starting with predecessor。

There。Stick that in your algorithm and mutate it。"我 promptly did。

所以人类关于如何正确高效计算的知识比计算机早几千年，至少可追溯到古埃及，自从计算机发明以来，这个领域的工作爆炸式增长。

如果 standard library 没有你需要的，你需要的东西 probably out there with tests，with documentation，often with a proof of correctness。学习如何 search the web for research that applies to your problem domain。

Okay。回到代码。我对这个 slice thing intrigued，当我 check out its type 时，我看到它 wasn't an array。既然我们在 array 和 bringToFront、sendToBack 上用过 stable partition，现在又在 array slice 上用，我猜 out loud 它 must be generic。"Of course it is。What's stable partition got to do with the specifics of array？" "That's right, nothing。Speaking of which, Blonkey，just what does bringForward have to do with shapes and selection？" "嗯，"我说，"它 operates on shapes，并 bring forward the selected ones。" "That's right, nothing，"他继续 without listening。

"Can you run bring forward on a row of lozenges？Of course you can。So it's got nothing to do with shapes。" Hmm。"Are you suggesting we make it generic？"我问。"Isn't that premature generalization？"Crusty 用问题回答问题："Well, just how do you plan to test this method？" "Okay，"我说，"I'll create a canvas。I'll add a bunch of random shapes。I'll select some of them，and then finally..."但我没 finish sentence，因为我知道那是 bad idea。如果我做所有这些，我真的在测试我的 function，还是在测试 Canvas 和 various shapes 的 initializers、addShape method、various shapes 的 isSelected property（如果 computed）？我肯定要 build test cases，但 ideally，那段代码不应该 depend on other code that I also have to test。

如果我能 bring lozenges forward，就应该可以在 playground 里 casual 做到，像这样，把能被 3 整除的数字 bring forward。

在 spectrum 的另一端，我应该能 throw vast quantities of randomly generated test data at it，并 ensure algorithm scales。只要代码 tied to Canvas and shapes，这两者都不 easy。

于是我对 Crusty 承认他是对的，开始把 non-generic bringForward 变成 generic。

第一步是 decouple from Canvas 并 move to arrays of shapes。

当然这个 array 就是 shape，所以我必须 replace shapes with self，然后 decouple from selection，通过传入 predicate 指示给定 shape 是否应被 bring forward。

一切继续 compile。Awesome！那时我很 pleased 地发现没有对 shape 的依赖，我可以 just delete where clause。Pretty cool，我想。现在我可以 bring forward on any array。

我 look over at Crusty，他 quietly 在 corner 练 cha-cha-cha，但他似乎不 think 我 finished。

"bring forward 和 arrays 有什么关系？"他问。"嗯，nothing，"我 sighed，开始想如何 remove this dependency。

Let's see，这里有一个 stable partition，需要 mutable collection conformance。所以 maybe 我 just move it to mutable collection。Hmm。我 thought，clearly index type doesn't match Int。Okay。所以 there's a simple fix，right？你做过这个吗？别这样做。

它 compiled，但 Crusty 突然 stopped dancing，我知道 something was wrong。"What？"我说。"Rookies always do that，"Crusty 说，shaking his head。

"First，你 got that comparison with 0，which is going to be wrong for array slice。So，did you know that array slices，their indices don't start at 0？所有 slices 的 indices 从它们被 slice from 的 underlying collection 对应的 index 开始。这个 relationship 对于能够 compose generic algorithms using slices 至关重要，所以 really important。"这个 problem，我知道怎么 fix。Just compare with start index。

但 real problem 是"bringForward 和 having integer indices 有什么关系？"我打断。"Yeah, I know。" "Well, I do have to get the index before i，which I can do with subtraction。"Crusty 只是 sighed 并 broke out lozenges again。

然后，他 laid two fingers down on desk，walked them across，直到右手指向第一个 green lozenge。"Not a backwards step in the whole dance，"他说。我意识到 Crusty 刚刚 showed me 一个 new algorithm。

Let's call that one indexBeforeFirst。

"Now, the trick here is to keep your focus by assuming somebody already wrote it for you。"他 proceeded to hack away all code we didn't need，like that and that。

"Predecessor 就是满足该谓词的第一个索引的前一个位置。

Now, just look how pretty that reads。"现在如果你 look at it，you can see that he's right。

Taking away all irrelevant detail about shapes、selections、arrays、and integers had left me with clearer code because it only traffics in essentials of the problem。"I already showed you how indexBeforeFirst works。See if you could write it，"他说。所以我想我开始 catch on 了，因为我 first time got it right。我告诉过你，我是 superfast typist。All right。So return the first index whose successor matches the predicate。我相当 excited about how well this was going。

"All right, Crusty，"我说，"let's do the next one。" "Ain't you forgetting something, Bonkey？"他问。我不知道他在说什么。Code was clean，and it worked。

"Semantics, son。如果我不知道它们 mean，我 how am I supposed to use these from other code？"就在这时我意识到每次我们使用 new algorithm，我们都 leaned on his documentation 来 draw conclusions about meaning and efficiency of our own code。

因为大多数 algorithms built out of other algorithms，它们 lean on the same thing。最近我面试一个 perspective intern，问他关于 documentation 的 role，他开始用一个我不会忘记的 phrase。"Oh, it's incredibly important，"他说。

"我们正在构建这些 towers of abstraction，"现在我 paraphrasing，"我们能 build without constantly inspecting layers below us 的 reason 是我们 build on 的 parts 是 documented。"现在作为 App developer，你工作在 stretches through 你的 system frameworks、DOS、into hardware 的 tower 顶端，而 hardware rests on laws of physics。

但只要你调用一个你自己的 method，它就成为你 foundation 的一部分；所以 document your code。The intern was hired，by the way，他正坐在那里。所以我 took the hint 并 documented Crusty's new algorithm，这意味着我们可以 forget about implementation 并 just use it，knowing Quick Help had everything we needed。

我也 documented bringForward。

Cool！现在，因为似乎解决了我所有 problems，此时我 really curious to see what was going on inside stablePartition。

事实证明我 well rewarded，因为 it's a really beautiful and instructive algorithm。

Public method gets collection's count 并 passes it on to this helper，which uses divide and conquer strategy。

所以，first，它处理 base cases：当 count less than 2，we're done。我们只需要 figure out whether partition point is at beginning or end of collection。Next，我们 divide collection in two。

现在此时你必须 temporarily take it on faith that algorithm works，因为我们要 stable partition left half 和 right half。现在如果你 look at these two ends，you can see everything is exactly in right place，但 center section has two parts that need to be exchanged。

它们不会 always have same length as they do in this example，fortunately there's an algorithm for that。我们 call it rotate。Okay。

我不会 go into rotate here，但它 actually quite beautiful，如果你 interested，你可以在 same file as stable partitions 找到 implementation。Okay。

回到 shapes。

现在这个 mess implemented dragging in shapes list，它一直是我最 complicated and buggy 的 operations 之一。

策略是 allocate temporary buffer；然后 loop over shapes before insertion point，extracting selected ones 并 adjusting insertion point；然后 separately loop over rest of shapes without adjusting insertion point，extracting selected ones。最后 reinsert them。

Honestly，我有点 scared to touch code because I thought I finally had it right。几乎一周没有发现 new bug 了。但我现在相当 good at this process，所以我 tried visualizing operation happening all at once。Hey，that looks familiar。Let's see it again。Hmm。

Suppose we do this first，然后 take care of parts separately。

That's right。This is just two stable partitions with inverted predicates。所以 generic algorithm collapsed down to this two-liner，这里是 canvas 里剩下的。现在 let's just see that next to old code。

That's not bad，但我们 got a reusable efficient documented general purpose algorithm out of it，which is spectacular。Okay。

所以这是 learned skill：look past details specific to your application domain，see what your code is doing fundamentally，and capture that in reusable generic code。It takes practice。

所以 why bother？Well，practical answer 是因为它们 decoupled from those irrelevant details，generic algorithms are more reusable、testable、and even clearer than their non-generic counterparts。但我也认为这对 anyone that really loves programming 来说 just deeply rewarding。

这是对真理与美的追寻，但并非某种抽象不可触及的真理，因为真实硬件的约束会让你保持诚实。

As Crusty likes to say，"Programming reveals the real。"所以 treat your computation as a first class citizen with all rights and obligations that you take seriously for types and application architecture。Identify it，give it a name，unit test it，and document its semantics and performance。现在我想把 Shawn Perin 的 advice 放在 full context 中 close。"If you want to improve the code quality in your organization, replace all of your coding standards with one goal, No Raw Loops。" Thank you。[ Applause ]
