---
title: 通知名称
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/notification-names
source_url: 'https://developer.apple.com/documentation/uikit/notification-names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/notification-names.json'
content_hash: 'sha256:4bf564bd10a90714'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [UIKit 辅助功能](accessibility-for-uikit.md)

# 通知名称

<sub>API 集合</sub>

辅助功能系统生成的通知名称。

## 主题

### UI 变化

- [UIAccessibilityScreenChangedNotification](uiaccessibility/notification/screenchanged.md) — 当出现占据屏幕主要部分的新视图时，App 发布的通知。
- [UIAccessibilityLayoutChangedNotification](uiaccessibility/notification/layoutchanged.md) — 当屏幕布局发生变化时，App 发布的通知。
- [UIAccessibilityPageScrolledNotification](uiaccessibility/notification/pagescrolled.md) — 当滚动操作完成时，App 发布的通知。
- [UIAccessibilitySwitchControlStatusDidChangeNotification](uiaccessibility/switchcontrolstatusdidchangenotification.md) — 当系统的“切换控制”设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityElementFocusedNotification](uiaccessibility/elementfocusednotification.md) — 当辅助 App 聚焦于辅助功能元素时，UIKit 发布的通知。
- [UIAccessibilityReduceTransparencyStatusDidChangeNotification](uiaccessibility/reducetransparencystatusdidchangenotification.md) — 当系统的 Reduce Transparency 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityButtonShapesEnabledStatusDidChangeNotification](uiaccessibility/buttonshapesenabledstatusdidchangenotification.md) — 当系统的 Button Shapes 设置发生变化时，UIKit 发布的通知。_（已废弃）_

### 「旁白」

- [UIAccessibilityAnnouncementNotification](uiaccessibility/notification/announcement.md) — 当 App 需要向辅助 App 传达播报时发布的通知。
- [UIAccessibilityVoiceOverStatusDidChangeNotification](uiaccessibility/voiceoverstatusdidchangenotification.md) — 当「旁白」启动或停止时，UIKit 发布的通知。
- [UIAccessibilityAnnouncementDidFinishNotification](uiaccessibility/announcementdidfinishnotification.md) — 当系统读完播报时，UIKit 发布的通知。
- [UIAccessibilityVoiceOverStatusChanged](uiaccessibilityvoiceoverstatuschanged.md) — 当「旁白」启动或停止时，UIKit 发布的通知。_（已废弃）_

### 文本

- [UIAccessibilityBoldTextStatusDidChangeNotification](uiaccessibility/boldtextstatusdidchangenotification.md) — 当系统的 Bold Text 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityClosedCaptioningStatusDidChangeNotification](uiaccessibility/closedcaptioningstatusdidchangenotification.md) — 当 Closed Captions + SDH 设置发生变化时，UIKit 发布的通知。

### 颜色

- [UIAccessibilityDarkerSystemColorsStatusDidChangeNotification](uiaccessibility/darkersystemcolorsstatusdidchangenotification.md) — 当系统的 Increase Contrast 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityGrayscaleStatusDidChangeNotification](uiaccessibility/grayscalestatusdidchangenotification.md) — 当系统的 Grayscale 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityInvertColorsStatusDidChangeNotification](uiaccessibility/invertcolorsstatusdidchangenotification.md) — 当反色设置发生变化时，UIKit 发布的通知。

### 辅助 App

- [UIAccessibilityAssistiveTouchStatusDidChangeNotification](uiaccessibility/assistivetouchstatusdidchangenotification.md) — 指示 AssistiveTouch 状态发生变化的通知。
- [UIAccessibilityGuidedAccessStatusDidChangeNotification](uiaccessibility/guidedaccessstatusdidchangenotification.md) — 指示 Guided Access 会话何时开始或结束的通知。
- [UIAccessibilityPauseAssistiveTechnologyNotification](uiaccessibility/notification/pauseassistivetechnology.md) — 暂时暂停辅助 App 操作的通知。
- [UIAccessibilityResumeAssistiveTechnologyNotification](uiaccessibility/notification/resumeassistivetechnology.md) — 暂时恢复辅助 App 操作的通知。
- [AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md) — 辅助 App 的标识符。

### 音频与语音

- [UIAccessibilityMonoAudioStatusDidChangeNotification](uiaccessibility/monoaudiostatusdidchangenotification.md) — 当系统音频从立体声变为单声道时，UIKit 发布的通知。
- [UIAccessibilitySpeakScreenStatusDidChangeNotification](uiaccessibility/speakscreenstatusdidchangenotification.md) — 当系统的 Speak Screen 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilitySpeakSelectionStatusDidChangeNotification](uiaccessibility/speakselectionstatusdidchangenotification.md) — 当系统的 Speak Selection 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityHearingDevicePairedEarDidChangeNotification](uiaccessibility/hearingdevicepairedeardidchangenotification.md) — 当当前配对的助听设备发生变化时，UIKit 发布的通知。

### 动态效果

- [UIAccessibilityReduceMotionStatusDidChangeNotification](uiaccessibility/reducemotionstatusdidchangenotification.md) — 当系统的 Reduce Motion 设置发生变化时，UIKit 发布的通知。
- [UIAccessibilityShakeToUndoDidChangeNotification](uiaccessibility/shaketoundodidchangenotification.md) — 当系统的 Shake to Undo 设置发生变化时，UIKit 发布的通知。

## 另请参阅

### 通知

- [通知字典键](notification-dictionary-keys.md) — 使用用户信息字典中的键处理通知。
- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — 向辅助 App 发布通知。
