---
title: 已废弃的符号
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller-deprecated-symbols.json'
content_hash: 'sha256:4390c7324fa2ec0a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UIViewController](uiviewcontroller.md)

# 已废弃的符号

<sub>API 集合</sub>

视图控制器不再支持的符号。

## 主题

### 已废弃的方法

- [- setOverrideTraitCollection:forChildViewController:](<uiviewcontroller/setoverridetraitcollection(__forchild_).md>) — 更改分配给指定子视图控制器的特性集合。_(已废弃)_
- [- overrideTraitCollectionForChildViewController:](<uiviewcontroller/overridetraitcollection(forchild_).md>) — 检索子视图控制器的特性集合。_(已废弃)_
- [+ attemptRotationToDeviceOrientation](<uiviewcontroller/attemptrotationtodeviceorientation().md>) — 尝试将所有窗口旋转到设备的方向。_(已废弃)_
- [- registerForPreviewingWithDelegate:sourceView:](<uiviewcontroller/registerforpreviewing(with_sourceview_).md>) — 注册视图控制器以参与 3D Touch 预览（peek）与提交（pop）。_(已废弃)_
- [- unregisterForPreviewingWithContext:](<uiviewcontroller/unregisterforpreviewing(withcontext_).md>) — 注销先前通过其上下文对象注册的视图控制器。_(已废弃)_
- [- canPerformUnwindSegueAction:fromViewController:withSender:](<uiviewcontroller/canperformunwindsegueaction(__from_withsender_).md>) — 在视图控制器上调用，以确定它是否想要响应某个 unwind 动作。_(已废弃)_
- [- didRotateFromInterfaceOrientation:](<uiviewcontroller/didrotate(from_).md>) — 在用户界面旋转后发送给视图控制器。_(已废弃)_
- [- dismissMoviePlayerViewControllerAnimated](<uiviewcontroller/dismissmovieplayerviewcontrolleranimated().md>) — 使用标准影片播放器过渡来关闭影片播放器视图控制器。_(已废弃)_
- [- viewControllerForUnwindSegueAction:fromViewController:withSender:](<uiviewcontroller/forunwindsegueaction(__from_withsender_).md>) — 当某个 unwind segue 动作想要在容器的子视图控制器中搜索处理该 unwind 动作的视图控制器时调用。_(已废弃)_
- [- presentMoviePlayerViewControllerAnimated:](<uiviewcontroller/presentmovieplayerviewcontrolleranimated(__).md>) — 使用标准影片播放器过渡来呈现影片播放器视图控制器。_(已废弃)_
- [- rotatingFooterView](<uiviewcontroller/rotatingfooterview().md>) — 返回界面方向更改期间要过渡的页脚视图。_(已废弃)_
- [- rotatingHeaderView](<uiviewcontroller/rotatingheaderview().md>) — 返回界面方向更改期间要过渡的页眉视图。_(已废弃)_
- [- segueForUnwindingToViewController:fromViewController:identifier:](<uiviewcontroller/segueforunwinding(to_from_identifier_).md>) — 当 unwind segue 动作需要在两个视图控制器之间进行过渡时调用。_(已废弃)_
- [- shouldAutomaticallyForwardRotationMethods](<uiviewcontroller/shouldautomaticallyforwardrotationmethods().md>) — 返回一个布尔值，指示旋转方法是否被转发给子视图控制器。_(已废弃)_
- [- willAnimateRotationToInterfaceOrientation:duration:](<uiviewcontroller/willanimaterotation(to_duration_).md>) — 在执行一步用户界面旋转之前发送给视图控制器。_(已废弃)_
- [- willRotateToInterfaceOrientation:duration:](<uiviewcontroller/willrotate(to_duration_).md>) — 在用户界面开始旋转之前立即发送给视图控制器。_(已废弃)_

### 已废弃的属性

- [shouldAutorotate](uiviewcontroller/shouldautorotate.md) — 一个布尔值，指示视图控制器的内容是否应自动旋转。_(已废弃)_
- [previewActionItems](uiviewcontroller/previewactionitems.md) — 用户在 3D Touch 预览上向上滑动时显示的快速操作。_(已废弃)_
- [automaticallyAdjustsScrollViewInsets](uiviewcontroller/automaticallyadjustsscrollviewinsets.md) — 一个布尔值，指示视图控制器是否应自动调整其滚动视图的内边距。_(已废弃)_
- [bottomLayoutGuide](uiviewcontroller/bottomlayoutguide.md) — 指示屏幕内容的最低垂直范围，供 Auto Layout 约束使用。_(已废弃)_
- [interfaceOrientation](uiviewcontroller/interfaceorientation.md) — 便捷属性，提供界面的当前方向，仅在视图控制器占据整个屏幕时有意义。_(已废弃)_
- [modalInPopover](uiviewcontroller/ismodalinpopover.md) — 一个布尔值，指示视图控制器是否应由弹出窗口模态呈现。_(已废弃)_
- [searchDisplayController](uiviewcontroller/searchdisplaycontroller.md) — 与视图控制器关联的搜索显示控制器。_(已废弃)_
- [topLayoutGuide](uiviewcontroller/toplayoutguide.md) — 指示屏幕内容的最高垂直范围，供 Auto Layout 约束使用。_(已废弃)_
