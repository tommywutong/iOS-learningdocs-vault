---
title: Cocoa 初始化方法的原理与缘由
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3e6eb5c9306bde78'
translated: true
---

> 原文：[The How and Why of Cocoa Initializers](https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html)　·　mikeash.com Friday Q&A

发表于 2008-10-09 23:43 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[正确使用键值观察](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)  
上一篇：[拙匠才怪工具不好，或者：Xcode 又烂了一次](https://www.mikeash.com/pyblog/its-a-poor-carpenter-who-blames-his-tools-or-xcode-sucks-again.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [init](https://www.mikeash.com/pyblog/?tag=init) [initializer](https://www.mikeash.com/pyblog/?tag=initializer) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [super](https://www.mikeash.com/pyblog/?tag=super)

Cocoa 初始化方法的原理与缘由

作者：[Mike Ash](https://www.mikeash.com/)

**必须怎么写**  
初始化方法的正确写法就是 Apple 的标准做法，对读这篇文章的人来说应该都不陌生：

```
- init {
    if((self = [super init])) {
        // 在这里设置实例变量以及其他内容
    }
    return self;
}
```

细微的变体当然也没问题，只要它们等价就行。比如，有人喜欢先检查 self 是否为 nil，是的话就直接返回 nil，以免把初始化放进单独的代码块里；也有人喜欢把赋值单独拿出来，然后在 if 语句里只检查普通的 `self`。这些写法做的事都一样，纯粹是口味问题。

**调用 `super` 还是 `self`？**  
为完整起见，先讲讲这个方法里比较显而易见的部分：对 `[super init]` 的调用。如果你刚接触 Objective-C、之前用的是 C++ 或 Java 这类语言，这里可能会让你感到困惑。之所以要有这一句，是因为 Objective-C 的初始化方法和其他方法一样，只是普通的方法。如果你想让超类的初始化方法得到调用，就必须自己去调用它。这里你还有一个选择：调用 `super` 还是调用 `self`。用哪个取决于具体情况。拿不准的话，可以套用下面这些经验法则：

1. 当且仅当方法名匹配时，调用 super。
2. 当且仅当你在实现本类的[指定初始化器（designated initializer）](http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/CocoaObjects/chapter_3_section_6.html#//apple_ref/doc/uid/TP40002974-CH4-SW3)时，调用 super。（这条规则更准确，但有时更难套用。）

**检查 `nil`**  
还是为完整起见：有些人可能会纳闷，为什么这里非要有一个 if 语句。原因在于你的超类可能初始化失败（例如参数前后不一致），而表示这种情况的标准做法是释放对象、从初始化方法返回 `nil`。如果这之后你还继续初始化自己的状态，就会崩溃。if 语句让你在超类失败时能够得体地失败。

**赋值**  
现在进入争议的核心。上面这些相当显而易见，我想不会有人反对。但对 `self` 的那个赋值却经常引来质疑。我们把这些误解（myth）逐一过一遍，从最显而易见的到最不显而易见的。

**误解：** 超类的初始化方法只可能返回 nil 或 self。  
**事实：** 许多 Cocoa 类会从它们的初始化方法返回一个不同的指针。

**误解：** 好吧，但那只发生在类簇（class cluster）身上，而且只有当你不派生它们的子类时才会发生。  
**事实：** 类簇确实不会对它们的子类这么做，但_其他_类可以，而且确实会。

**误解：** 但那些其他的类反正是你绝不会想去派生子类的，比如 NSColorPanel；或者说只有你做错了什么时才会发生，比如派生了单例（singleton）的子类，却没有让那个子类成为单例。  
**事实：** 这些确实是可以发生这种情况的场景，但并不限于这些场景。

**误解：** 超类的初始化方法必须返回 `self`，因为我的初始化方法只能处理我的类的实例。  
**事实：** 超类的初始化方法可能返回你的类的一个_不同的_实例。

**误解：** 它不可能返回不同的实例，因为不允许对实例重新初始化。  
**事实：** 关于重新初始化这一点没说错，但它可以分配一个_新的_实例。

**误解：** 但它没有理由这么做。它手头_已经_有一个新实例了。  
**事实：** 如果它想在实例末尾多要一些_额外的_存储，它就有充分的理由这么做——比如它创建了你的类的一个动态子类，想改用那个子类的实例。

这正是标准初始化模式成为唯一可行做法的原因。Cocoa 类_可以_，而且_确实会_释放原始实例（deallocate），然后分配一个同类（或其子类）的新实例，并从初始化方法里返回它。诚然这种情况罕见，但它是合法的，也确实会发生。简而言之，这就是为什么 Apple 的标准初始化模式是唯一正确的做法。

**结论**  
总结一下：超类的初始化方法可能返回三种东西之一，而 Apple 的标准模式对这三种情况都能正确处理：

1. `self`（绝大多数、绝大多数情况下你得到的就是它。）
2. `nil`（失败时。）
3. 你的类的一个新实例（罕见但合法。）

很多人喜欢省掉赋值，只检查是不是 nil。对情况 1 和 2 这么做没问题，但对情况 3 会以非常令人费解的方式出错。

实际上还有另外两种东西有可能被返回：

1. 另一个类的实例
2. 你的类的一个已有实例

情况 4 只在你做错了什么时才会发生，所以它不是你该去处理的东西。情况 5 只在你做错了什么、或者派生了单例的子类时才会发生。如果你派生了单例的子类，就应当确保你的初始化方法能处理对已有单例实例的重新初始化。不管怎样，这本来就是使用单例的良好实践。

（顺带一提：如果你直接派生 NSObject 的子类，标准模式_并非_必需。因为文档写明 `-[NSObject init]` 什么都不做、总是返回 self。不过，本着「我们写的代码应当始终对变化保持健壮」的原则——这里的变化指的是你所继承的类发生变化——我非常建议即使是 NSObject 的直接子类也使用标准模式。）

就是这些。这就是初始化方法的写法，以及为什么要这么写。希望它足够清楚，不至于引发争论；但如果你非要争论，请尽管留言。

**参考资料**

1. [re: self = [super init] debate.](http://www.cocoabuilder.com/archive/message/cocoa/2008/2/11/198591) - Ben Trumbull 在 [cocoa-dev](http://lists.apple.com/mailman/listinfo/cocoa-dev) 上发帖，解释了这个主题的一些关键点。
2. [NSManagedObject 类参考](http://developer.apple.com/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObject_Class/Reference/NSManagedObject.html#//apple_ref/occ/instm/NSManagedObject/initWithEntity:insertIntoManagedObjectContext:) - 这个类就是一个例子：它会返回一个与正在初始化的类不同的新实例。

喜欢这篇文章吗？我正在销售收录这些文章的整套书！第二卷和第三卷现已出版，提供 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/the-how-and-why-of-cocoa-initializers.html)

分享你的想法，发表评论：

垃圾评论和离题内容将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
