---
title: 0代码隐藏GroupedTableView上边多余的间隔 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/04/15/ios-hide-grouped-tableview-header/'
original_language: zh
published: 2015-04-15
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:cfab664262dea1bb'
translated: n/a
---

> 原文：[0代码隐藏GroupedTableView上边多余的间隔 · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/04/15/ios-hide-grouped-tableview-header/)　·　sunnyxx (孙源)

# 0代码隐藏GroupedTableView上边多余的间隔

2015年4月15日

实现诸如支付宝的 “探索” 页面时，最简单的方案是在 Storyboard 中来一个静态 Grouped UITableViewController，把各个 Cell 中的元素摆好就行了

![](http://ww1.sinaimg.cn/mw690/51530583jw1er6hby1sp0j20nq0tk768.jpg)

不过会有下面的问题，第一个 Section 距离屏幕顶端有间隔

![](http://ww1.sinaimg.cn/mw690/51530583jw1er6hbxkv2xj20k80oota0.jpg)

### [#一行代码搞定](#一行代码搞定)一行代码搞定

研究发现，这里其实是一个被 UITableView 默认填充的 HeaderView。而且，当试图将它的高度设置为 0 时，完全不起效果。但我们用下面的代码创建一个高度特别小的 HeaderView 时，上面的边距就不见了：

![](http://ww2.sinaimg.cn/large/51530583jw1er6jpgw0ndj20u40600ud.jpg)

`CGFLOAT_MIN` 这个宏表示 CGFloat 能代表的最接近 0 的浮点数，64 位下大概是 0.00(300左右个)0225 这个样子  
这样写单纯的为了避免一个魔法数字，这里用 `0.1` 效果是一样的，后面再讲。

### [#在-Storyboard-中-0-代码搞定](#在-Storyboard-中-0-代码搞定)在 Storyboard 中 0 代码搞定

没用 Storyboard 的同学使用上面的代码就 OK 了； 而在 Storyboard 中可以 0 代码搞定这个事：

首先，在第一个 Section 的上面拖进来一个空 UIView

![](http://ww3.sinaimg.cn/mw690/51530583jw1er6jd7na5uj20aw07cwfi.jpg)

然后选中这个 UIView 的 Runtime Attributes 栏，添加一个 `frame` 的 KeyPath

![](http://ww3.sinaimg.cn/mw690/51530583jw1er6jd7wt02j20f6064wf8.jpg)

这样头部的间隔就乖乖的不见了：

![](http://ww2.sinaimg.cn/mw690/51530583jw1er6jj5n61fj20ju0lidgi.jpg
)

### [#刨根问底-UITableViewHeader-的猫腻](#刨根问底-UITableViewHeader-的猫腻)刨根问底 UITableViewHeader 的猫腻

为什么刚才说 0.1 和 CGFLOAT_MIN 是等效的呢？经过研究，这个高度值的影响大概是这样的：

1. 若传入的 height == 0，则 height 被设置成默认值
2. 若 height 小于屏幕半像素对应的高度，这个 header 不在另一个像素渲染

半像素也就是 `1.0 / scale / 2.0`，如在 @2x 屏上是 0.25  
直观的感受下，假如这个 height 被设置成 0.5 的样子：  
![](http://ww3.sinaimg.cn/mw690/51530583jw1er6kdmuz21j20ju0de0u4.jpg
)

身患强迫症的我是绝对不能容忍导航栏下面的阴影线看上去宽了 0.5 像素的，Done。
