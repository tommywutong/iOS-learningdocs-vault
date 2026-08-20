---
title: 自动释放的更多乐趣
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/more-fun-with-autorelease.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:232fc62df018d55d'
translated: true
---

> 原文：[More Fun With Autorelease](https://www.mikeash.com/pyblog/more-fun-with-autorelease.html)　·　mikeash.com Friday Q&A

发布于 2007-02-08 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[How To Shrink Your Source Code](https://www.mikeash.com/pyblog/how-to-shrink-your-source-code.html)  
上一篇：[Why CoreAudio is Hard](https://www.mikeash.com/pyblog/why-coreaudio-is-hard.html)  
标签：[autorelease](https://www.mikeash.com/pyblog/?tag=autorelease) [bug](https://www.mikeash.com/pyblog/?tag=bug) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

更多自动释放的乐趣

作者 [Mike Ash](https://www.mikeash.com/)

关键词是“事件循环”。在 Apple 无穷的智慧中，那些并非真正的 `NSEvent` 的东西不会触发自动释放池（autorelease pool）。

我当前正在开发一个 App，它在后台花费大量时间，在主线程上与 `NSStream` 进行黑暗、不可名状的操作。我遇到了一个 bug：在处理流事件的过程中，我的某个对象可能被销毁，导致它在被 dealloc 之后还能收到其他流事件。（显然，`NSStream` 在你关闭、释放它并将其委托（delegate）设为 `nil` 之后仍能发送流事件，但那是另一个完全不同的问题，留待日后处理。）

显而易见的修复方法是在调用问题方法之前简单地执行 `[[self retain] autorelease]`。这确实修复了问题，只不过现在我的 `dealloc` 不再发生在事件处理器的中途，而是*根本就不被调用了*。

直到我点击了 App 的 dock 图标。

至少解决方案很简单：在流事件处理器里投递一个 `NSApplicationDefined` 事件，自动释放的对象就会按计划销毁。

令人惊讶的是，据我所知，这个 bug 已经存在了很长时间。我虽然没用过，但 `CFRunLoopObserver` 似乎可以让你在这么低的层次轻松 hook 进 runloop，以至于任何微小的动静都能让你 drain 当前的自动释放池。而且我们都知道，[自动释放很快](http://www.mikeash.com/blog/pivot/entry.php?id=19)，所以这样做应该不会有性能损失。

我们有多少 App 在后台安静地滴答作响，积累着越来越大的自动释放池，却只有在我们把它们带到前台时才被 drain？这不禁让人深思。

希望这个问题能在 Leopard 中得到修复。我不敢提交 bug，生怕得到一个“行为正确”的回复。

喜欢这篇文章吗？我出了整本书！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/more-fun-with-autorelease.html)

添加你的想法，发表评论：

垃圾评论和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开处以羞辱。
