---
title: 系统视频效果与麦克风模式
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/system-video-effects-and-microphone-modes
source_url: 'https://developer.apple.com/documentation/avfoundation/system-video-effects-and-microphone-modes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/system-video-effects-and-microphone-modes.json'
content_hash: 'sha256:34c2f54eb2096ee6'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# 系统视频效果与麦克风模式

<sub>API 集合</sub>

配置舞台居中等系统视频效果的状态，并检查系统对麦克风音频应用的增强。

## 主题

### 表演反应效果

- [reactionEffectsEnabled](avcapturedevice/reactioneffectsenabled.md) — 一个布尔值，指示 App 是否支持表演反应效果。
- [canPerformReactionEffects](avcapturedevice/canperformreactioneffects.md) — 一个布尔值，指示你能否在捕捉设备上表演反应效果。
- [availableReactionTypes](avcapturedevice/availablereactiontypes.md) — 设备支持表演的一组反应类型。
- [reactionEffectGesturesEnabled](avcapturedevice/reactioneffectgesturesenabled.md) — 一个布尔值，指示手势检测是否会在视频流上触发反应效果。
- [- performEffectForReaction:](<avcapturedevice/performeffect(for_).md>) — 在视频流上表演指定的反应类型。
- [reactionEffectsInProgress](avcapturedevice/reactioneffectsinprogress.md) — 设备当前正在表演的反应效果数组，按时间戳排序。
- [AVCaptureReactionEffectState](avcapturereactioneffectstate.md) — 一个报告在捕捉设备上表演的反应效果状态的对象。

### 配置舞台居中

- [centerStageActive](avcapturedevice/iscenterstageactive.md) — 一个布尔值，指示舞台居中在设备上是否处于活动状态。
- [centerStageEnabled](avcapturedevice/iscenterstageenabled.md) — 一个布尔值，指示用户或 App 是否在设备上启用了舞台居中。
- [centerStageRectOfInterest](avcapturedevice/centerstagerectofinterest.md) — 输出像素缓冲区内用于执行舞台居中取景的有效区域。
- [centerStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md) — 一个指示舞台居中控制当前模式的值。
- [CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.enum.md) — 指示当前舞台居中控制模式的常量。

### 配置录音室灯光

- [studioLightActive](avcapturedevice/isstudiolightactive.md) — 一个布尔值，指示录音室灯光在设备上是否处于活动状态。
- [studioLightEnabled](avcapturedevice/isstudiolightenabled.md) — 一个布尔值，指示用户是否在设备上启用了录音室灯光。

### 检查人像效果设置

- [portraitEffectActive](avcapturedevice/isportraiteffectactive.md) — 一个布尔值，指示人像视频效果在设备上是否处于活动状态。
- [portraitEffectEnabled](avcapturedevice/isportraiteffectenabled.md) — 一个布尔值，指示用户是否在控制中心启用了人像视频效果。

### 检查麦克风模式

- [activeMicrophoneMode](avcapturedevice/activemicrophonemode.md) — 设备当前活跃的麦克风模式。
- [preferredMicrophoneMode](avcapturedevice/preferredmicrophonemode.md) — 用户在控制中心选择的麦克风模式。
- [MicrophoneMode](avcapturedevice/microphonemode.md) — 定义可用麦克风模式的常量。

### 呈现配置用户界面

- [+ showSystemUserInterface:](<avcapturedevice/showsystemuserinterface(__).md>) — 显示系统用于配置视频效果或麦克风模式的用户界面。
- [SystemUserInterface](avcapturedevice/systemuserinterface.md) — 描述捕捉设备配置用户界面的常量。

### 配置背景替换

- [backgroundReplacementActive](avcapturedevice/isbackgroundreplacementactive.md) — 一个布尔值，指示背景替换当前是否在捕捉设备上处于活动状态。
- [backgroundReplacementEnabled](avcapturedevice/isbackgroundreplacementenabled.md) — 一个类属性，指示用户是否为该 App 启用了背景替换功能。
