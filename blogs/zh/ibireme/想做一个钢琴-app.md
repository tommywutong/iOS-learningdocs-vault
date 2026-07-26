---
title: 想做一个钢琴 App~
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2013/04/25/wang-to-make-a-piano-app/'
original_language: zh
published: 2013-04-25
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ab49e621b1f25e1e'
translated: n/a
---

> 原文：[想做一个钢琴 App~](https://blog.ibireme.com/2013/04/25/wang-to-make-a-piano-app/)　·　ibireme (郭曜源)

Appstore有几个非常棒的钢琴类软件:

- 音色方面表现最贴近现实的自然是苹果的GarageBand,体积不小但乐器库非常棒,钢琴的采样应该是隔3采1,每个音有3个力度的样本,通过感应敲击震动幅度来模拟力度,形式和电钢琴差不多。编辑功能自然是同样的强大，当然那些功能我也玩不转。。
- 可玩性比较高的是Music Studio,这家伙的音色库很全,可以选各种乐器来玩,缺点是声音有些呆板。
- 平时最喜欢的还是FingerPiano。体积很小巧,启动飞快,音色也不错~ 操作起来比上面两个App要舒服很多

虽然这些App都很棒，但我还是一直想自己做一个钢琴的App。

最开始接触iOS的时候,做的第一个成型一点的App就是一个小钢琴。用几个wav合成一下，没有延长音，体积很大，效果也不好，之后就没再折腾。

随后一直在关注FingerPiano。这个App最开始也是用的wav合成,只有一个钢琴音色。但直到有一版更新,体积一下变得好小,而且还增加了几种乐器。仔细研究了下发现它改用了Soundfont,挺有意思～～ 最开始貌似是用fluidsynth 库来加载sf2文件的,sf2也是它自己生成的; 但后来貌似就自己实现了一套,同时sf2也换用了经典的[GeneralUser GS](http://www.schristiancollins.com/generaluser.php).于是我也手痒想试着做一下。。

嗯。。折腾了两晚上。。看苹果的AU文档。。做了一个简单的[Demo](https://github.com/ibireme/SF2Piano) 倒是能切换声音,但效果好差啊。。。比FingerPiano差远了。。

同样的Soundfont文件，在电脑里和FingerPiano里都表现的不错,用AU的API就感觉差很多。。 看来是我打开姿势不对=_= 有时间仔细学学CoreAudio…

2013-04-26更新: 终于发现FingerPiano用的什么样的技术了：[crimsontech.jp](http://www.crimsontech.jp/eng/softsynth/index.html)。 这家公司应该是从2002年起始的，开发出来的东西都是要license的。。

唉～～果然没那么容易啊～回头恶补一下吧。。

# ╮(￣▽￣)╭
