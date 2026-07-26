---
title: 理解 anchorPoint，position，frame 的关系
source_url: 'https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/'
source_domain: joeshang.github.io
source_group: single-site
original_language: zh
published: 2014-12-19
archived_at: 2026-07-27
content_hash: 'sha256:9341c4ceaeee1524'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08）
container: '//*[contains(@class,''post-body'')]'
container_source: guess
---

> 原文：[理解 anchorPoint，position，frame 的关系](https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/)

对于 UIView 的 `frame`，`bounds`，`center` 都比较熟悉：

- `bounds`指定 UIView 自身坐标系。
- `center`指定 UIView 在 superview 中的位置坐标。
- `frame`由互不影响（正交）的 `bounds` 跟 `center` 生成。

但是我一直有这样的疑问：为什么要使用 UIView 中心位置的 `center` 来指定坐标，为什么不用其他位置？

后来学习了 CALayer，发现 UIView 的主要任务其实是响应事件（这就是为什么从 UIResponser 继承的原因），而将显示委托给 CALayer 处理。一个成功的 UIView 背后总有一个默默贡献的 CALayer，CALayer 作为 GPU/OpenGL 纹理的一种高层封装，处理显示的方方面面，UIView 则将 CALayer 一些功能再次封装，提供简洁好用的接口。像 UIView 中的 `frame`，`bounds` 就是直接使用 CALayer 中的 `frame`，`bounds`。

但是对于 `center`，CALayer 对应项是 `position`，为什么不同名了呢？因为 `position` 更灵活，谁规定“指定 UIView 在 superview 中的位置坐标”一定要在 UIView 的中心位置呢？！而 `position` 默认在中心位置的目的我觉得是为了方便 Rotation，因为一般 Rotation 都是绕着中心旋转，UIView 为了简化使用，满足大部分情况即可，所以就将默认在中心的 `position` 封装成了 `center`。

由于 CALayer 的 `position` 并没有限制一定要在 `bounds` 的中心位置，所以就需要一个属性来描述 `position` 在 `bounds` 中的位置，这样才能推算出 `frame` 的 origin 点位置。于是 `anchorPoint` 出现了，**CALayer 用 `anchorPoint` 指定 `position` 在 `bounds` 中的位置**，有如下特点：

- 为了可以任意指定位置，因此 `anchorPoint` 就不使用绝对值，而是比例值。
- 由于 Rotation 总是围绕 `position` 旋转，因此指定 `position` 在 Layer 中位置的 `anchorPoint` 就被命名为**锚点**（像船的锚一样固定位置）。

总之，`frame` 是由 `position`，`bounds`，`anchorPoint` 共同生成（其实还有 `transform`，这就需要了解 Current Transform Matrix 的概念，为了减少复杂性，这里就不涉及了），公式如下：

- frame.origin.x = position.x - bounds.size.width * anchorPoint.x
- frame.origin.y = position.y - bounds.size.height * anchorPoint.y

这就解释了：

1. 为什么 anchorPoint 改变会导致 frame 改变，而 position 却没变？
2. 为什么 anchorPoint 要使用比例而不是具体值？

豁然开朗。

PS. 多思考，保持好奇心，多从设计者角度想想为什么这样设计，即使是简单的概念，也会有收获。Stay Hungry，Stay Foolish。
