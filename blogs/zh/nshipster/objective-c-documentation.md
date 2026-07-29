---
title: Objective-C 文档
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/objective-c-documentation/'
original_language: en
published: 2013-08-05
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:7d486832e57cf79e'
translated: true
---

> 原文：[Objective-C Documentation](https://nshipster.com/objective-c-documentation/)　·　NSHipster (Mattt)

# [Objective-C 文档](https://nshipster.com/objective-c-documentation/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2013 年 8 月 5 日

Cocoa 开发者中流传着一句俗语：Objective-C 的冗长性使得其代码实质上能够自我文档化。从 `longMethodNamesWithNamedParameters:` 到这些参数的显式类型声明，Objective-C 方法几乎不需要任何想象力就能理解。

但即使是自我文档化的代码，也可以通过文档得到改进，只需付出少量努力就能为他人带来显著的益处。

**听着**——我知道程序员不喜欢被命令，那些「你应当」和「你不应当」的说教式论调，其修辞效果就像 [拉长号一样](https://www.youtube.com/watch?v=ss2hULhXf04)，所以我直截了当地说：

你喜欢 Apple 的文档吗？你难道不想 [为你自己的库](http://cocoadocs.org/docsets/AFNetworking/1.3.1/Classes/AFHTTPClient.html) 也拥有这样的文档吗？只需遵循几个简单的约定，你的代码就能获得它应得的文档。

---

每种现代编程语言都有注释：由特殊字符序列（如 `//`、`/* */`、`#` 和 `--`）标记的不可执行的自然语言注解。文档通过使用特殊格式的注释提供辅助说明和上下文，这些注释可以被构建工具提取和解析。

在 Objective-C 中，首选的文档工具是 [`appledoc`](https://github.com/tomaz/appledoc)。`appledoc` 使用类似 [Javadoc](https://en.wikipedia.org/wiki/Javadoc) 的语法，能够从 `.h` 文件生成 HTML 和 Xcode 兼容的 `.docset` 文档，这些文档 [看起来几乎与](http://cocoadocs.org/docsets/AFNetworking/1.3.1/Classes/AFHTTPClient.html) [Apple 的官方文档](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html) 一模一样。

> [Doxygen](http://www.stack.nl/~dimitri/doxygen/) 主要用于 C++，是 Objective-C 的另一个可行选项，但通常不被 iOS/OS X 开发者社区普遍采用。

以下是一些文档写得好的 Objective-C 项目的示例：

- [`AFHTTPSessionManager.h`](https://github.com/AFNetworking/AFNetworking/blob/master/AFNetworking/AFHTTPSessionManager.h)
- [`MRBrew.h`](https://github.com/marcransome/MRBrew/blob/master/MRBrew/MRBrew.h)
- [`GRMustache.h`](https://github.com/groue/GRMustache/blob/master/src/classes/GRMustache.h)
- [`TTTAddressFormatter.h`](https://github.com/mattt/FormatterKit/blob/master/FormatterKit/TTTAddressFormatter.h)

## 编写 Objective-C 文档的指南

Objective-C 文档由 `/** */` 注释块（注意额外的起始星号）标识，它位于任何 `@interface` 或 `@protocol` 以及任何方法或 `@property` 声明之前。

对于类、类别（category）和协议（protocol），文档应描述该特定组件的用途，并提供关于如何使用它的建议和指南。像新闻文章一样组织它：从顶层的「推文长度（tweet-sized）」概述开始，然后根据需要深入探讨更多主题。像类应该如何（或不应该）被子类化，或标准协议（如 `NSCopying`）行为中的任何注意事项，都应始终被记录在文档中。

每个方法同样应以对其功能的简洁描述开头，然后跟上任何注意事项或额外细节。方法文档还包含 Javadoc 风格的 `@` 标签，用于常见字段，如参数和返回值：

- `@param [param] [Description]`：描述应为该参数传递什么值
- `@return [Description]`：描述方法的返回值
- `@see [selector]`：提供对相关方法的「另请参阅」参考
- `@warning [description]`：指出异常或潜在的危险行为

属性（property）通常用一句话描述，并应包括其默认值是什么。

相关的属性和方法应通过 `@name` 声明进行分组，其功能类似于 [`#pragma mark`](https://nshipster.com/pragma/)，并且可以与三斜线（`///`）注释变体一起使用。

在自行编写文档之前，不妨先阅读其他文档，以便对正确的语气和风格有所了解。当对术语或措辞有疑问时，遵循你能在 Apple 官方文档中找到的最接近的用法。

> 为了加快项目的文档编写过程，你可能想查看 [VVDocumenter-Xcode](https://github.com/onevcat/VVDocumenter-Xcode) 项目，它可以根据方法的签名 [自动添加 `@param` 和 `@return` 标签](https://raw.github.com/onevcat/VVDocumenter-Xcode/master/ScreenShot.gif)。

---

只需遵循这些简单的指南，你就可以为你自己的项目添加外观精美、信息丰富的文档。一旦你掌握了窍门，你会发现编写文档毫不费力。

> 感谢 [@orta](https://github.com/orta) 建议本周的话题，以及他目前在 [CocoaDocs](http://cocoadocs.org) 上的持续工作，该项目为发布在 [CocoaPods](http://cocoapods.org) 上的项目提供了自动生成的文档。
