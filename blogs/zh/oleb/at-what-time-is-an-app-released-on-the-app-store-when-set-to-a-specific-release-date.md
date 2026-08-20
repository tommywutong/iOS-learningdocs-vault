---
title: 将 App Store 上的 App 设置为特定发布日期时，它会在什么时间发布？
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/at-what-time-is-an-app-released-on-the-app-store-when-set-to-specific-release-date/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1668c0d61b5b7665'
translated: true
---

> 原文：[At What Time Is an App Released on the App Store When Set to a Specific Release Date?](https://oleb.net/blog/2011/05/at-what-time-is-an-app-released-on-the-app-store-when-set-to-specific-release-date/)　·　Ole Begemann

# 将 App Store 上的 App 设置为特定发布日期时，它会在什么时间发布？

当你向 Apple 提交 App 进行审核时，可以选择设置一个特定的发布日期。不过，你只能指定某一天，而不能指定具体时间。那么，在这个特定日期的什么时间，App 才会真正发布呢？是午夜 GMT 时间？是 Cupertino 的员工上班时间？是一天中的某个随机时间？App 会在所有时区的所有 App Store 上同时出现吗？

事实证明，一个设置了可用日期的 App 大约会在相应 App Store 当地时区的午夜时分出现在该地区的国际 App Store 上。因此，新西兰将比美国提前 16 个小时。

为了说明这一点，让我记录一下 [Tapbots](http://tapbots.com/) 最近发布 [Tweetbot](http://tapbots.com/software/tweetbot/) 那天的一些推文。

午夜（当地时间），Tweetbot 出现在新西兰的 App Store 上。Tweetbot 开发者 Paul Haddad 开始疑惑发生了什么。Federico Viticci 给出了解释：

> 该死的时区。它们是怎么运作的？
> 
> [@tapbot_paul](https://twitter.com/tapbot_paul)
> 
> tapbot_paul
> 
> [2011年4月13日 13:00 GMT](https://twitter.com/tapbot_paul/status/58182894492975105)

> [@tapbot_paul](https://twitter.com/tapbot_paul/status/58182894492975105) App Store 的时区系统很糟糕。App 会在全球午夜时分开始发布。
> 
> [@viticci](https://twitter.com/viticci)
> 
> Federico Viticci
> 
> [2011年4月13日 15:01 GMT](https://twitter.com/viticci/status/58183093101658114)

> [@viticci](https://twitter.com/viticci/status/58183093101658114) 我猜到可能会这样，但出于某种原因，我以为它会从午夜 GMT 开始。
> 
> [@tapbot_paul](https://twitter.com/tapbot_paul)
> 
> tapbot_paul
> 
> [2011年4月13日 15:03 GMT](https://twitter.com/tapbot_paul/status/58183489949929472)

> [@tapbot_paul](https://twitter.com/tapbot_paul/status/58183489949929472) 不对。它总是从日本和新西兰开始，然后根据时区缓慢推出。
> 
> [@viticci](https://twitter.com/viticci)
> 
> Federico Viticci
> 
> [2011年4月13日 15:04 GMT](https://twitter.com/viticci/status/58183686411124737)

几个小时后，Tweetbot 在日本 App Store 上架，向日本用户问好。与此同时，Paul 不得不回答许多用户的提问，这些用户暂时还无法使用 Tweetbot：

> Konichiwa！
> 
> [@tweetbot](https://twitter.com/tweetbot)
> 
> Tweetbot for iPhone
> 
> [2011年4月13日 15:43 GMT](https://twitter.com/tweetbot/status/58193686219063296)

> 对于那些因为 Tweetbot 在你们那里的商店里还无法获取而不高兴的人，请怪 Sandford Fleming 和国际日期变更线。或者，我想，也可以怪 Apple。
> 
> [@tapbot_paul](https://twitter.com/tapbot_paul)
> 
> tapbot_paul
> 
> [2011年4月13日 17:02 GMT](https://twitter.com/tapbot_paul/status/58213409308680192)

刚过晚上 11 点 GMT（英国午夜，西欧凌晨 1 点），Tweetbot 出现在欧洲的 App Store 上。

> 看来欧洲和英国的商店已是午夜。只剩下美国/加拿大/世界其他地区了。
> 
> [@tapbot_paul](https://twitter.com/tapbot_paul)
> 
> tapbot_paul
> 
> [2011年4月13日 23:08 GMT](https://twitter.com/tapbot_paul/status/58305646835138561)

美国用户仍需等待：

> [fwdr.org/yu8v](http://fwdr.org/yu8v) 有人能告诉我，他妈的为什么我怎么做都找不到 Tweetbots 吗？谢谢。抄送：[@tapbot_paul](https://twitter.com/tapbot_paul)
> 
> [@rockets](https://twitter.com/rockets)
> 
> Buzz Bellamonté
> 
> [2011年4月14日 00:17 GMT](https://twitter.com/rockets/status/58323067927150592)

> [@rockets](https://twitter.com/rockets/status/58323067927150592) 美国还没有发布，你得再等几个小时。
> 
> [@tapbot_paul](https://twitter.com/tapbot_paul)
> 
> tapbot_paul
> 
> [2011年4月14日 00:20 GMT](https://twitter.com/tapbot_paul/status/58323755197399040)

最后，在新西兰发布 16 小时后，Tweetbot 在美国 App Store 上线：

> Tweetbot 在美国 App Store 上线了，我们的评测也发布了！ [mcstr.net/fkW2Vn](http://mcstr.net/fkW2Vn)
> 
> [@viticci](https://twitter.com/viticci)
> 
> Federico Viticci
> 
> [2011年4月14日 03:02 GMT](https://twitter.com/viticci/status/58364488155537408)

**更新 #1 2011年5月6日：** Ben Zotto [想知道这项政策是否也适用于 App Store 的其他日期，比如价格变更或节假日暂停截止日期](https://twitter.com/bzotto/status/66284027589566464)。我不知道，不过我相信至少每日销售数据也是基于每个国际 App Store 的当地时间计算的。我想这也是 Apple 通常在第二天下午 1:00–2:00 GMT 左右（当天在“最后一个”App Store 结束后几小时）才发布每日销售数据的原因之一。

**更新 #2 2011年5月6日：** Bob Koon 在 Twitter 上通知我，他[早在2010年10月就已经写过关于这个问题的博客](http://www.appsizematters.com/2010/10/track-your-appstore-launch-across-the-globe/)。在他的文章中，Bob 还提供了一个方便的电子表格，可以告诉你，你的 App 在全部 90 个国际 App Store 中分别会在什么时间上线。
