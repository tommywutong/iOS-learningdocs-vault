---
title: 误导性指标与 UX 权衡
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/04/Misleading-Metrics/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a43495adb7477590'
translated: true
---

> 原文：[Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [“FIXME”并不总是意味着“Fix Me”](https://belkadan.com/blog/2018/04/FIXME/)

[一个闪亮的魔法数字](https://belkadan.com/blog/2019/02/A-Shiny-Magic-Number/) »

« [Webmailer 的更新栏](https://belkadan.com/blog/2016/05/Webmailer-Update-Bar/?tag=user-experience)

[软数量级](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/?tag=user-experience) »

## [误导性指标与 UX 权衡](#)

假设你有一个搜索功能，然后发现几乎没人用它。也就是说，专用搜索页面的加载次数非常少。你对自己的用户界面做了一点小调整，突然就有更多人访问搜索页面了！听起来是胜利，对吧？

不过……那个界面调整是这样的：以前搜索结果会内联显示在搜索栏里，但现在只做**自动补全**。而你的产品是 Facebook，这意味着大多数搜索都是搜索者已经认识的人或页面；他们只是用搜索栏来做快速导航（就像[「聚焦」](https://en.wikipedia.org/wiki/Spotlight_(software))或开始菜单）。这个改变发生在一两年前，但每次使用还是让我很恼火。

当我在 Facebook 上搜索 "mark" 时，我**以前**可以直接跳转到某个名叫 Mark 的朋友。现在，Facebook 仍然会补全他们的名字，但如果我**选择**了那个补全结果，它会先把我带到搜索页面。我必须点击第一个结果才能真正到达那个朋友那里。

![（看起来是这样的）](https://belkadan.com/blog/2018/04/Misleading-Metrics/mark.jpg)

更糟的是，他们显然还保留了旧界面——可以直接跳转到某人或页面——因为他们把旧界面用在了“最近搜索”上。（你可以点击搜索栏并删除所有文字来看到这一点；这里没有图片是因为如果涂黑就基本没什么意义了。）

我把这篇帖子叫做“误导性指标”，是因为我觉得这**肯定是**基于指标的决策。**[结果我错了](https://medium.com/@justahl/simplifying-facebook-search-8a555dbef4ad)。** Facebook 在做出这个改变的过程中确实做了定性用户研究。但他们最终确定的设计，与我实际使用 Facebook 的方式——并且很可能与许多其他人使用 Facebook 的方式——严重冲突。

我最初的心得是：指标能给你数字，但它们不能给你**原因**，而且你应该总是试着想出多个可能解释这些数字的原因——甚至要把指标与面对面的用户研究和定性反馈结合起来。这仍然是一个好教训，但也许我需要一个更好的例子。

（我拿 Facebook 说事，是因为我用 Facebook^[1](#fn:me) 并且他们体量够大，经得起这种批评，但这种事任何公司都可能做。另外，反馈可以通过 [https://www.facebook.com/help/feedback](https://www.facebook.com/help/feedback) 提交。）

1. 除非我们线下是朋友或同事，或者至少是 Twitter 互相关注，否则请不要试图在 Facebook 上找我。这是另一个身份。 [↩︎](#fnref:me)

这篇文章发布于 [2018](https://belkadan.com/blog/2018) 年 [4月](https://belkadan.com/blog/2018/04) 29 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[用户体验](https://belkadan.com/blog/tags/user-experience)，[吐槽](https://belkadan.com/blog/tags/rant)
