---
title: Push to Talk
framework: Push to Talk
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/pushtotalk
source_url: 'https://developer.apple.com/documentation/pushtotalk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/pushtotalk.json'
content_hash: 'sha256:815983957efcf56b'
translated: true
---

> 导航：[Technologies](technologies.md)

# Push to Talk

<sub>框架</sub>

为你 App 的 Push to Talk 服务显示系统用户界面。

## 概述

Push to Talk 框架是一套省电、易用且注重隐私的 API。它让你的 App 能够提供用户界面控制，让用户可以随时随地传输音频。它提供一个临时的 Apple 推送通知服务令牌，以便系统在会话进行期间于后台唤醒你的 App 来处理传入的音频。

> [!note] 注意
> 在 visionOS 中运行的兼容 iPad 和 iPhone App 无法使用 Push to Talk 服务。

## 主题

### 要点

- [Creating a Push to Talk app](pushtotalk/creating-a-push-to-talk-app.md) — 使用系统用户界面控制构建一款对讲机风格的 App。
- [PTChannelManager](pushtotalk/ptchannelmanager.md) — 表示 push-to-talk 频道管理器的对象。

### 频道管理

- [PTChannelManagerDelegate](pushtotalk/ptchannelmanagerdelegate.md) — 表示频道管理器生命周期的类型。
- [PTTransmissionMode](pushtotalk/pttransmissionmode.md) — 标识音频传输模式类型。
- [PTServiceStatus](pushtotalk/ptservicestatus.md) — 标识指示服务状态的类型。
- [PTChannelJoinReason](pushtotalk/ptchanneljoinreason.md) — 标识指示加入原因的类型。
- [PTChannelLeaveReason](pushtotalk/ptchannelleavereason.md) — 标识指示离开原因的类型。
- [PTChannelTransmitRequestSource](pushtotalk/ptchanneltransmitrequestsource.md) — 标识指示传输请求来源的类型。

### 频道恢复

- [PTChannelDescriptor](pushtotalk/ptchanneldescriptor.md) — 描述频道的对象。
- [PTChannelRestorationDelegate](pushtotalk/ptchannelrestorationdelegate.md) — 表示频道恢复行为的类型。

### 频道参与者

- [PTParticipant](pushtotalk/ptparticipant.md) — 表示参与者的对象。

### 推送通知结果

- [PTPushResult](pushtotalk/ptpushresult.md) — 表示推送结果的对象。

### Push to Talk 错误

- [PTChannelError](pushtotalk/ptchannelerror-swift.struct.md) — 表示频道错误的结构体。
- [Code](pushtotalk/ptchannelerror-swift.struct/code.md) — 频道操作的错误代码。
- [PTInstantiationError](pushtotalk/ptinstantiationerror-swift.struct.md) — 表示实例化错误的结构体。
- [Code](pushtotalk/ptinstantiationerror-swift.struct/code.md) — 实例化操作的错误代码。
- [PTChannelErrorDomain](pushtotalk/ptchannelerrordomain.md) — 频道错误域的字符串表示。
- [PTInstantiationErrorDomain](pushtotalk/ptinstantiationerrordomain.md) — 实例化错误域的字符串表示。
