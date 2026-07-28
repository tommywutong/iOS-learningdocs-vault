---
title: 'Friday Q&A 2009-11-06：链接与安装名称'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5a532e2cef965e9d'
translated: true
---

> 原文：[Friday Q&A 2009-11-06: Linking and Install Names](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html)　·　mikeash.com Friday Q&A

发布于 2009-11-07 00:18 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-11-13: 危险的 Cocoa 调用](https://www.mikeash.com/pyblog/friday-qa-2009-11-13-dangerous-cocoa-calls.html)  
上一篇：[Friday Q&A 2009-10-30: Objective-C 中的生成器](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html)  
标签：[frameworks](https://www.mikeash.com/pyblog/?tag=frameworks) [libraries](https://www.mikeash.com/pyblog/?tag=libraries) [linking](https://www.mikeash.com/pyblog/?tag=linking)

Friday Q&A 2009-11-06：链接与安装名称

作者：[Mike Ash](https://www.mikeash.com/)

**静态库（Static Libraries）**  
这些简单到几乎无需讨论。当你链接一个静态库时，该库的内容会在构建时被复制到你的 App 中。从那时起，这些代码的行为就如同你自己编写的代码一样。

**动态库（Dynamic Libraries）**  
当你链接一个动态库时，事情就没那么简单了。链接器基本上只是做一条记录：你对各种符号的引用将在这个库中找到，并且你的二进制文件依赖于该库。然后在运行时，当你的 App 被加载时，动态链接器（dynamic linker）也会加载那个库。

今天的大问题是，动态链接器如何知道在哪里找到它？

**安装名称（Install Name）**  
这个问题的答案在不同操作系统上差异很大，但在 Mac 上，答案是 **安装名称（install name）**。

安装名称就是一个嵌入在动态库中的路径名，它告诉链接器在运行时可以在哪里找到这个库。例如，`libfoo.dylib` 可能有一个安装名称为 `/usr/lib/libfoo.dylib`。这个安装名称会在链接时被复制到 App 中。当动态链接器在运行时查找 `libfoo.dylib` 时，它会从 App 中取出这个安装名称，并知道要在 `/usr/lib` 中查找该库。

框架（Frameworks）本质上就是带了一层包装的动态库，所以它们的工作方式相同。`Foo.framework` 可能有一个安装名称为 `/Library/Frameworks/Foo.framework/Versions/A/Foo`，这就是动态链接器查找它的地方。

**`@executable_path`**  
绝对路径很烦人。有时你想将框架直接嵌入到 App 中，而不是将其安装到 `/Library` 或类似位置。

Mac 对此的解决方案是 `@executable_path`。这是一个魔法令牌，当它被放在库的安装名称的开头时，会被扩展为正在加载它的可执行文件的路径（去掉末尾的组件）。例如，假设 `Bar.app` 链接了 `Foo.framework`。如果 `Bar.app` 安装在 `/Applications`，那么 `@executable_path` 会被扩展为 `/Applications/Bar.app/Contents/MacOS`。如果你打算将框架嵌入到 `Contents/Frameworks` 中，那么你只需将 `Foo.framework` 的安装名称设置为 `@executable_path/../Frameworks/Foo.framework/Versions/A/Foo`。动态链接器会将其扩展为 `/Applications/Bar.app/Contents/MacOS/../Frameworks/Foo.framework/Versions/A/Foo`，并能够在那里找到该框架。

**`@loader_path`**  
仅仅能找到可执行文件并不总是足够。想象一下，你发布了一个插件或一个框架，其中又嵌入了另一个框架。例如，`Foo.framework` 嵌入了 `Baz.framework`。即使 `Foo.framework` 是发起加载请求的一方，动态链接器在计算 `@executable_path` 所指的位置时，仍然会以 `Bar.app` 的位置为准，这会导致错误。

从 10.4 开始，Apple 提供了 `@loader_path`，它能满足你的这种需求。它会扩展为实际导致目标库被加载的那个文件的全路径（去掉末尾组件）。如果是 App，那么它与 `@executable_path` 相同。但如果是一个框架或插件，那么它就会相对于那个框架或插件，这要有用得多。

**`@rpath`**  
虽然上述方法在理论上足以应对任何情况，但在实践中可能会很麻烦。问题在于，一份库的副本只能以一种方式使用。如果你希望 `Foo.framework` 既能嵌入到 App 中工作，又能安装到 `/Library/Frameworks` 中工作，你就必须提供两份副本，并设置不同的安装名称。（或者之后使用 `install_name_tool` 手动调整安装名称。）这是可行的，但很烦人。

从 10.5 开始，Apple 提供了 `@rpath`，这是对此的解决方案。当它被放在安装名称的开头时，它会要求动态链接器搜索一个位置列表来查找该库。这个列表嵌入在 App 中，因此可以由 App 的构建过程来控制，而不是由框架来控制。因此，一份框架的副本就可以满足多种用途。

为了实现这一点，`Foo.framework` 的安装名称会被设置为 `@rpath/Foo.framework/Versions/A/Foo`。一个打算嵌入 `Foo.framework` 的 App，需要在构建时向链接器传递 `-rpath @executable_path/../Frameworks`，这告诉动态链接器在那里搜索 `@rpath` 框架。一个打算安装该框架的 App，则会传递 `-rpath /Library/Frameworks`，告诉动态链接器在那里搜索。一个出于某种原因不想在构建时做出单一选择的 App，可以同时传递这两组参数，这将使动态链接器尝试这两个位置。

**结论**  
现在，希望你对 Mac OS X 上动态链接的工作方式以及动态链接器如何找到你的库有了更多了解，包括如何将框架嵌入到 App、插件以及其他框架中。

下周请回来继续关注另一期精彩内容。Friday Q&A 由你的投稿驱动，所以如果你有想在这里看到的主题想法，请[发送进来！](mailto:mike@mikeash.com)

喜欢这篇文章吗？我正在销售包含所有文章的整本书！第二卷和第三卷现已发售！它们有 ePub、PDF、印刷版，也支持 iBooks 和 Kindle。 [点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-11-06-linking-and-install-names.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。
