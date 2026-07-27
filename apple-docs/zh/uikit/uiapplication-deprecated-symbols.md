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
doc_path: /documentation/uikit/uiapplication-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication-deprecated-symbols.json'
content_hash: 'sha256:682b531b95a533fb'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [UIApplication](uiapplication.md)

# 已废弃符号

<sub>API 集合</sub>

查看不再受支持的符号及其替代方案。

## 主题

### 已废弃的方法

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — 请求系统激活一个现有场景，或创建一个新场景并将其与你的 App 关联。 _(已废弃)_
- [- beginIgnoringInteractionEvents](<uiapplication/beginignoringinteractionevents().md>) — 通知接收者暂停处理与触摸相关的事件。 _(已废弃)_
- [- endIgnoringInteractionEvents](<uiapplication/endignoringinteractionevents().md>) — 通知接收者恢复处理与触摸相关的事件。 _(已废弃)_
- [- setMinimumBackgroundFetchInterval:](<uiapplication/setminimumbackgroundfetchinterval(__).md>) — 指定两次后台获取操作之间必须间隔的最短时间。 _(已废弃)_
- [- scheduleLocalNotification:](<uiapplication/schedulelocalnotification(__).md>) — 安排一条本地通知在其封装的日期和时间送达。 _(已废弃)_
- [- presentLocalNotificationNow:](<uiapplication/presentlocalnotificationnow(__).md>) — 立即呈现一条本地通知。 _(已废弃)_
- [- cancelLocalNotification:](<uiapplication/cancellocalnotification(__).md>) — 取消指定的已排程本地通知的送达。 _(已废弃)_
- [- cancelAllLocalNotifications](<uiapplication/cancelalllocalnotifications().md>) — 取消所有已排程本地通知的送达。 _(已废弃)_
- [- setKeepAliveTimeout:handler:](<uiapplication/setkeepalivetimeout(__handler_).md>) — 为旧版本 iOS 中的 VoIP App 配置周期性处理程序。 _(已废弃)_
- [UIMinimumKeepAliveTimeout](uiminimumkeepalivetimeout.md) — App 在后台运行关键后台任务所允许的最短时间（以秒为单位）。 _(已废弃)_
- [- clearKeepAliveTimeout](<uiapplication/clearkeepalivetimeout().md>) — 移除此前安装的周期性处理程序代码块。 _(已废弃)_
- [- setStatusBarHidden:withAnimation:](<uiapplication/setstatusbarhidden(__with_).md>) — 隐藏或显示状态栏，可选择为过渡添加动画。 _(已废弃)_
- [- setStatusBarStyle:animated:](<uiapplication/setstatusbarstyle(__animated_).md>) — 设置状态栏的样式，可选择为过渡到新样式添加动画。 _(已废弃)_
- [- setStatusBarOrientation:animated:](<uiapplication/setstatusbarorientation(__animated_).md>) — 将 App 的状态栏设置为指定方向，可选择为过渡添加动画。 _(已废弃)_
- [- registerUserNotificationSettings:](<uiapplication/registerusernotificationsettings(__).md>) — 注册你偏好的通知用户的选项。 _(已废弃)_
- [- registerForRemoteNotificationTypes:](<uiapplication/registerforremotenotifications(matching_).md>) — 注册通过 Apple 推送通知服务接收指定类型的远程通知。 _(已废弃)_
- [- enabledRemoteNotificationTypes](<uiapplication/enabledremotenotificationtypes().md>) — 返回 App 接受的通知类型。 _(已废弃)_
- [UIRemoteNotificationType](uiremotenotificationtype.md) — 表示 App 可能向用户显示的通知类型的常量。 _(已废弃)_
- [- openURL:](<uiapplication/openurl(__).md>) — 尝试打开指定 URL 处的资源。 _(已废弃)_
- [- setNewsstandIconImage:](<uiapplication/setnewsstandiconimage(__).md>) — 将 Newsstand App 的图标设置为描绘某出版物当前期号的图像。 _(已废弃)_

### 已废弃的通知

- [UIApplicationWillChangeStatusBarFrameNotification](uiapplication/willchangestatusbarframenotification.md) — 当 App 即将改变状态栏的框架时发布。 _(已废弃)_
- [UIApplicationDidChangeStatusBarFrameNotification](uiapplication/didchangestatusbarframenotification.md) — 当状态栏的框架发生变化时发布。 _(已废弃)_
- [UIApplicationWillChangeStatusBarOrientationNotification](uiapplication/willchangestatusbarorientationnotification.md) — 当 App 即将改变其界面的方向时发布。 _(已废弃)_
- [UIApplicationDidChangeStatusBarOrientationNotification](uiapplication/didchangestatusbarorientationnotification.md) — 当 App 用户界面的方向发生变化时发布。 _(已废弃)_

### 已废弃的属性

- [applicationIconBadgeNumber](uiapplication/applicationiconbadgenumber.md) — 当前设置为主屏幕上 App 图标角标的数字。 _(已废弃)_
- [UIApplicationStatusBarFrameUserInfoKey](uiapplication/statusbarframeuserinfokey.md) — 一个键，其值表示新的状态栏框架。 _(已废弃)_
- [UIApplicationStatusBarOrientationUserInfoKey](uiapplication/statusbarorientationuserinfokey.md) — 一个键，其值表示当前的界面方向。 _(已废弃)_
- [currentUserNotificationSettings](uiapplication/currentusernotificationsettings.md) — 返回 App 的用户通知设置。 _(已废弃)_
- [ignoringInteractionEvents](uiapplication/isignoringinteractionevents.md) — 一个布尔值，表示接收者是否正在忽略由屏幕触摸引发的事件。 _(已废弃)_
- [networkActivityIndicatorVisible](uiapplication/isnetworkactivityindicatorvisible.md) — 一个布尔值，用于开启或关闭网络活动指示符。 _(已废弃)_
- [statusBarHidden](uiapplication/isstatusbarhidden.md) — 一个布尔值，决定状态栏是否隐藏。 _(已废弃)_
- [keyWindow](uiapplication/keywindow.md) — App 的关键窗口。 _(已废弃)_
- [scheduledLocalNotifications](uiapplication/scheduledlocalnotifications.md) — 所有当前已排程的本地通知。 _(已废弃)_
- [statusBarFrame](uiapplication/statusbarframe.md) — 定义状态栏区域的框架矩形。 _(已废弃)_
- [statusBarOrientation](uiapplication/statusbarorientation.md) — App 状态栏当前的方向。 _(已废弃)_
- [statusBarOrientationAnimationDuration](uiapplication/statusbarorientationanimationduration.md) — 状态栏在 90 度方向变化期间的动画持续时间（以秒为单位）。 _(已废弃)_
- [statusBarStyle](uiapplication/statusbarstyle.md) — 状态栏当前的样式。 _(已废弃)_
- [windows](uiapplication/windows.md) — App 可见和隐藏的窗口。 _(已废弃)_
