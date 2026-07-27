---
title: 《App Architecture》一书
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/05/app-architecture-book/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d453db772ff35856'
translated: true
---

> 原文：[App Architecture book](https://oleb.net/blog/2018/05/app-architecture-book/)　·　Ole Begemann

# 《App Architecture》一书

[![书籍封面：App Architecture: iOS Application Design Patterns in Swift，作者 Chris Eidhof、Matt Gallagher 和 Florian Kugler](https://oleb.net/media/app-architecture-book-cover-900px.jpg)](https://oleb.net/media/app-architecture-book-cover-900px.jpg)

由 Chris Eidhof、[Matt Gallagher](https://www.cocoawithlove.com) 和 Florian Kugler 撰写的新书 [_App Architecture: iOS Application Design Patterns in Swift_](https://www.objc.io/books/app-architecture/) 终于出了正式版。和之前的 [objc.io](https://www.objc.io) 系列书籍一样，我在这本书的创作过程中担任了技术审校，出了点小力——这份工作[我非常享受](https://twitter.com/olebegemann/status/993152885390274560)。

我显然带有偏见，但如果你在写 iOS App，我真心推荐这本书。虽然书中讨论的一些架构模式你可能已经很熟悉了，但我敢肯定你在每一章都会学到一些新东西——我自己就是如此。作者们即便是对 MVC 这种耳熟能详的模式，也能带来全新的视角。读这本书的过程中，我好几次都有那种恍然大悟的时刻：这些概念事后看来显而易见，但我从来没有像书中呈现的那种方式去真正思考过它们。

这本书还讨论了另外三种更具实验性的架构。要用这几种模式之一写出一整个 iOS App，需要更坚定地偏离典型的 UIKit 代码写法（你有时会感觉是在跟 Apple 的框架对着干）。不过好消息是，你并不需要把整个 App 都切换到一种新架构，才能从中受益。大多数模式都建立在相对精简的一套核心理念之上，而这些理念往往可以单独应用到现有的基于 MVC 或 MVVM 的 App 中。

不管怎样，如果你还没机会尝试过声明式 UI 编程（比如 [React](https://reactjs.org)），这本书是个很好的学习机会。UIKit 的命令式风格已经显得有些过时了，如果 Apple [传闻中的跨平台 UI 项目](https://daringfireball.net/2018/04/scuttlebutt_regarding_ui_project)也从 [Elm](https://guide.elm-lang.org/architecture/)/React 中汲取了灵感，我一点也不会感到意外。

还有一个加分项：这本书篇幅刚过 200 页，读起来相对轻松快捷。如果这还不够，你还可以选择额外购买 7 个小时的配套视频内容。
