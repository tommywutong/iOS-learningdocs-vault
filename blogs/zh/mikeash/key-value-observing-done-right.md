---
title: 正确使用键值观察
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/key-value-observing-done-right.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c7d5ca4dd7ae0b8e'
translated: true
---

> 原文：[正确使用键值观察](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)　·　mikeash.com Friday Q&A

发布于 2008-10-22 21:47 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)）| [博客索引](https://www.mikeash.com/pyblog/)<br>
下一篇：[不要使用 NSOperationQueue](https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html)<br>
上一篇：[Cocoa 初始化方法的原理与原因](https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html)<br>
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [kvo](https://www.mikeash.com/pyblog/?tag=kvo) [源代码](https://www.mikeash.com/pyblog/?tag=sourcecode)

正确使用键值观察

作者：[Mike Ash](https://www.mikeash.com/)

**哪里出了问题**<br>
KVO API 存在三个主要问题，都与类层次中多个层级注册观察者有关。这很重要，因为即使是 NSObject（作为其 `-bind:toObject:withKeyPath:options:` 实现的一部分）也会观察对象。

1. **`-addObserver:forKeyPath:options:context:` 不允许传入要调用的自定义 selector。**<br>
   查看 NSNotificationCenter 等类似 API 会发现，注册观察者总要传入指定事件发生时调用的 selector。这样很容易与超类分离，因为只要将消息指向自己的方法即可。KVO 则要求你重写 `-observeValueForKeyPath:ofObject:change:context:`，然后自行处理消息或调用 super。由于 super 可能为完全相同的键路径和对象注册过观察，决定处理消息还是将其沿链上交就变得复杂。
2. **上下文指针没有实际用处。**<br>
   这是问题 1 的后果。因为不能指定要调用的自定义方法，也无法通过检查键路径或对象得知超类是否关心该通知，所以需要别的方法判断通知是发给自己还是超类。上下文指针就是这样做的。你必须创建一个超类不可能使用的唯一指针，并将它传给 `addObserver:...`。随后在 `-observeValueForKeyPath:...` 的实现中检查上下文指针是否为该唯一指针。因此，不能使用上下文指针实际保存上下文。
3. **`-removeObserver:forKeyPath:` 的参数不足。**<br>
   此方法不接受上下文指针。这意味着，若你与超类为同一对象/键路径组合注册了观察、但生命周期不同，就无法只停用自己的观察者。调用该方法可能停用你的观察者、超类的观察者，甚至两者都会停用。

这样强大的工具竟然如此残缺，实在遗憾。尤其是 Apple 开始在新 API 中省略传统的 NSNotification 和委托回调，转而只支持 KVO。NSOperation 就是很好的例子：要在 NSOperation 完成时收到通知，唯一办法是通过 KVO 观察其 `isFinished` 属性。

那可以怎么办？我不想只抱怨却不提供帮助，所以写了一个类解决这个问题。可以像这样从我的[公开 svn 仓库](http://www.mikeash.com/svn/)取得：

`svn co http://www.mikeash.com/svn/MAKVONotificationCenter/`

也可以直接点击上面的链接浏览。

它如何工作？它利用了一个可保证唯一的指针：`self` 指针。它不让目标对象注册通知，而是为每项通知创建唯一的辅助对象，并注册该对象。辅助对象收到通知后，再将其转发给原始观察者。每个观察都有唯一的辅助对象，因此它可以用简单的实例变量保存观察的元数据，无须依赖必须唯一的上下文指针。辅助对象只监听 KVO 通知，因此观察会持续到对象生命周期结束；我们可以假定其超类 NSObject 不观察任何对象，或者也会在对象的整个生命周期内观察。

MAKVONotificationCenter 因而绕过了以上三项缺陷：

1. `-addObserver:...` 方法提供自定义 selector，在被观察的键路径变化时调用。超类会使用不同 selector，问题便解决了。（Cocoa 超类会直接观察，而 MAKVONotificationCenter 经由辅助对象观察，因此它们不会相互干扰。）
2. 提供 `userInfo` 参数，并传入观察者方法。它可以是包含观察所需信息的任意对象。
3. `-removeObserver:...` 方法除目标和键路径外还接受 selector。因此，子类和超类若为同一对象上的同一键路径注册观察，可通过指定各自唯一的 selector 注销，而不影响对方。

还有几个有趣的特性值得注意。

`+defaultCenter` 使用[简单的无锁原子调用](https://www.mikeash.com/pyblog/late-night-cocoa.html)，在不为每次访问加锁和解锁的情况下使单例线程安全。这是个很好的技巧：不必预先安排初始化，也不必每次都承担锁的开销，就能得到安全的单例。

它还通过 NSObject 上的分类暴露了更简洁的 API。这比显式访问 MAKVONotificationCenter 单例更好。极端情况下甚至可将 MAKVONotificationCenter 完全从头文件中移除，只保留 NSObject 扩展。

这份代码基本没有经过测试。我只写了 `Tester.m` 中那一小段测试代码。在亲自验证前不要信任它。实际代码约 150 行，并不多，但仍请自行承担风险。

只要适当署名，就可以在自己的项目中使用此代码。若发现缺陷，也非常欢迎补丁。

如对代码有任何意见，请在下方留言。

喜欢这篇文章吗？我在售卖整本收录这类文章的书！第二、三卷已经出版，提供 ePub、PDF、印刷版、iBooks 和 Kindle。[点击这里了解更多](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/key-value-observing-done-right.html)

留下你的想法，发表一条评论：

垃圾信息和离题帖子会不经通知删除；发帖人可能会由我全权决定公开羞辱。
