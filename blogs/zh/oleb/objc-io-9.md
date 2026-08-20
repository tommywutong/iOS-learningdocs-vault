---
title: 'objc.io 第 9 期'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/02/objc-io-issue-9/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:034f5252cac731e3'
translated: true
---

> 原文：[objc.io 第 9 期](https://oleb.net/blog/2014/02/objc-io-issue-9/)　·　Ole Begemann

# objc.io 第 9 期

我为[本月 objc.io 第 9 期](http://www.objc.io/issue-9/)撰写了一篇关于 [Unicode 和 NSString](http://www.objc.io/issue-9/unicode.html) 的文章，该期全篇聚焦 Cocoa 中的字符串。这是一个复杂的主题，光我这一篇文章就超过 5000 字，因此提前感谢你花时间阅读。我希望你能学到新东西，因为我在写作过程中确实受益匪浅。

尽管 Unicode 距今已有二十多年且已是一项成熟标准，我仍然在 App 和网站中遇到看似简单的文本处理错误。作为开发者，我们有责任为全世界的用户彻底做好字符串处理例程的单元测试——这意味着要使用英文以外的文字进行测试。

[![我在 objc.io 第 9 期上关于 Unicode 和 NSString 的文章截图](https://oleb.net/media/objc-io-9-screenshot-nsstring-unicode-1280px.jpg)](http://www.objc.io/issue-9/unicode.html)
