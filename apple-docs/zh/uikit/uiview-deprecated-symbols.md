---
title: 已废弃符号
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/uiview-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview-deprecated-symbols.json'
content_hash: 'sha256:22f111944a9b9da8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [UIView](uiview.md)

# 已废弃符号

<sub>API 集合</sub>

视图不再支持的符号。

## 主题

### 已废弃方法

- [+ beginAnimations:context:](<uiview/beginanimations(__context_).md>) — 标记 begin/commit 动画 block 的开始。_(已废弃)_
- [+ commitAnimations](<uiview/commitanimations().md>) — 标记 begin/commit 动画 block 的结束，并调度动画执行。_(已废弃)_
- [+ setAnimationStartDate:](<uiview/setanimationstart(__).md>) — 设置当前动画 block 的开始时间。_(已废弃)_
- [+ setAnimationsEnabled:](<uiview/setanimationsenabled(__).md>) — 设置是否启用动画。
- [+ setAnimationDelegate:](<uiview/setanimationdelegate(__).md>) — 为所有动画消息设置委托（delegate）。_(已废弃)_
- [+ setAnimationWillStartSelector:](<uiview/setanimationwillstart(__).md>) — 设置动画开始时发送给动画委托的消息。_(已废弃)_
- [+ setAnimationDidStopSelector:](<uiview/setanimationdidstop(__).md>) — 设置动画停止时发送给动画委托的消息。_(已废弃)_
- [+ setAnimationDuration:](<uiview/setanimationduration(__).md>) — 设置动画 block 中动画的持续时间（以秒为单位）。_(已废弃)_
- [+ setAnimationDelay:](<uiview/setanimationdelay(__).md>) — 设置动画 block 中属性更改开始动画之前的等待时间（以秒为单位）。_(已废弃)_
- [+ setAnimationCurve:](<uiview/setanimationcurve(__).md>) — 设置动画 block 中属性更改动画所使用的曲线。_(已废弃)_
- [+ setAnimationRepeatCount:](<uiview/setanimationrepeatcount(__).md>) — 设置动画 block 中动画的重复次数。_(已废弃)_
- [+ setAnimationRepeatAutoreverses:](<uiview/setanimationrepeatautoreverses(__).md>) — 设置动画 block 中的动画是否自动反向播放。_(已废弃)_
- [+ setAnimationBeginsFromCurrentState:](<uiview/setanimationbeginsfromcurrentstate(__).md>) — 设置动画是否应从当前状态开始播放。_(已废弃)_
- [+ setAnimationTransition:forView:cache:](<uiview/setanimationtransition(__for_cache_).md>) — 设置在动画 block 期间应用于视图的过渡效果。_(已废弃)_
- [areAnimationsEnabled](uiview/areanimationsenabled.md) — 返回一个布尔值，指示是否启用动画。
- [- viewForBaselineLayout](<uiview/forbaselinelayout().md>) — 返回用于满足基线约束的视图。_(已废弃)_
