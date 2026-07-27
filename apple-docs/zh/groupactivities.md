---
title: Group Activities
framework: Group Activities
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/groupactivities
source_url: 'https://developer.apple.com/documentation/groupactivities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/groupactivities.json'
content_hash: 'sha256:a16db233d9784d1d'
translated: true
---

> 导航：[Technologies](technologies.md)

# Group Activities

<sub>框架</sub>

创建你的用户可以共同分享和体验的、特定于 App 的活动。

## 概述

借助 Group Activities 框架，你可以在 SharePlay 体验中提供 App 的内容，为用户带来联结感和临场感。例如，一款视频流媒体 App 可以提供参加观影派对的能力，让参与者在各自的个人设备上同步观看。App 负责处理每台设备上的播放，而 Group Activities 框架负责同步这些播放并促成设备之间的通信。

该框架利用 FaceTime 基础设施来同步你的 App 的活动，并邀请其他参与者加入这些活动。当你的 App 界面中包含可共享的活动时，请在用于表示这些活动的对象中采用 [GroupActivity](groupactivities/groupactivity.md) 协议。群组活动开始后，使用 [GroupSession](groupactivities/groupsession.md) 对象将你的 App 行为与其他参与设备同步。

> [!note] 注意
> Group Activities 框架会对 [GroupSession](groupactivities/groupsession.md) 对象在设备之间同步的所有会话数据使用端到端加密。Apple 没有解密这些数据的密钥。你使用 Group Activities 框架，并不会让 Apple 得以了解你的 App 所分享的内容，也不会让其获知与你的 App 中媒体内容播放相关的信息，例如用户从内容的何处开始、暂停或跳过某个会话。促成 Group Activities 会话的 Apple 服务器并不知道你的 App 的身份。偶尔，Apple 可能会请少数用户协助排查问题，例如[采集系统诊断报告或安装调试描述文件](https://developer.apple.com/bug-reporting/profiles-and-logs/)，这可能会附带导致 Apple 收集到与你的 App 中所分享内容相关的部分信息。

## 主题

### 基础

- [com.apple.developer.group-session](bundleresources/entitlements/com.apple.developer.group-session.md) — 一个布尔值，指示 App 是否可以实现共享的群组体验。

### 活动定义

- [定义你的 App 的 SharePlay 活动](groupactivities/defining-your-apps-shareplay-activities.md) — 配置你的 App 对 SharePlay 的支持，并定义人们可以从你的 App 中执行的活动。
- [支持协同媒体播放](avfoundation/supporting-coordinated-media-playback.md) — 创建同步的媒体体验，让用户可以跨设备观看和收听。
- [GroupActivity](groupactivities/groupactivity.md) — 一种类型，可以向其他参与者告知你的 App 的活动。
- [GroupActivityMetadata](groupactivities/groupactivitymetadata.md) — 向潜在参与者描述某项活动的文字和图片内容。
- [GroupActivityActivationResult](groupactivities/groupactivityactivationresult.md) — 准备开始自定义活动的结果。
- [GroupActivityTransferRepresentation](groupactivities/groupactivitytransferrepresentation.md) — 一种类型，让你可以从已知上下文开始一项群组活动。

### 界面呈现

- [从你的 App 界面呈现 SharePlay 活动](groupactivities/promoting-shareplay-activities-from-your-apps-ui.md) — 让人们能够轻松地从你的 App 界面、系统共享表单，或通过 AirDrop 上的 AirPlay 开始活动。
- [GroupActivitySharingController](groupactivities/groupactivitysharingcontroller-4gtfk.md) — 一个 macOS 视图控制器，用于显示开始某项活动的系统界面，并可以选择为该活动开始一通 FaceTime 通话。
- [GroupActivitySharingController](groupactivities/groupactivitysharingcontroller-ybcy.md) — 一个 iOS 视图控制器，用于显示开始某项活动的系统界面，并可以选择为该活动开始一通 FaceTime 通话。

### 会话管理

- [加入并管理共享活动](groupactivities/joining-and-managing-a-shared-activity.md) — 在 SharePlay 活动开始时配置会话，并处理活动生命周期内发生的事件。
- [在群组会话中绘制内容](groupactivities/drawing_content_in_a_group_session.md) — 邀请好友在 FaceTime 通话中于共享画布上绘图。
- [GroupSession](groupactivities/groupsession.md) — 一个正在进行的活动的会话，用于在参与设备之间同步内容。
- [CustomMessageIdentifiable](groupactivities/custommessageidentifiable.md) — 一种类型，为你发送给其他设备的消息分配自定义 ID 字符串。
- [Participant](groupactivities/participant.md) — 群组会话中的一名活跃参与者。

### 空间活动

- [为与附近的人共享配置你的 visionOS App](groupactivities/configure-your-app-for-sharing-with-people-nearby.md) — 为在同一房间佩戴 Vision Pro 的人以及正在通话的 FaceTime 参与者创建共享体验。
- [为某项活动添加空间 Persona 支持](groupactivities/adding-spatial-persona-support-to-an-activity.md) — 更新你的 SharePlay 活动，以在 visionOS 中运行时支持空间 Persona 和共享上下文。
- [SystemCoordinator](groupactivities/systemcoordinator.md) — 一种类型，当活跃的 SharePlay 会话支持内容的空间放置时，你可用它来协调界面的行为。
- [ParticipantState](groupactivities/systemcoordinator/participantstate.md) — 一个结构，告知你某个参与者是否支持当前活动的共享模拟空间。
- [groupActivityAssociation(_:)](<swiftui/view/groupactivityassociation(__).md>) — 指定某个视图应如何与当前的 SharePlay 群组活动相关联。
- [GroupActivityAssociationInteraction](groupactivities/groupactivityassociationinteraction.md) — 一种交互，配置某个视图与当前 SharePlay 群组活动的关联方式。
- [GroupActivityAssociationKind](groupactivities/groupactivityassociationkind.md) — 用户界面元素可以与某项 SharePlay 群组活动建立的一种关联。

### 自定义空间模板

- [为 visionOS 构建一款猜谜游戏](groupactivities/building-a-guessing-game-for-visionos.md) — 使用 Group Activities 为 visionOS 创建一款团队猜谜游戏。
- [SpatialTemplate](groupactivities/spatialtemplate.md) — 一个接口，你可以用它在某个场景中创建空间 Persona 的自定义排布方式。
- [SpatialTemplatePreference](groupactivities/spatialtemplatepreference.md) — 一个结构，指定共享模拟空间中参与者空间 Persona 的首选排布方式。
- [SpatialTemplateSeatElement](groupactivities/spatialtemplateseatelement.md) — 一个空间模板元素，表示活动中某位参与者的座位。
- [SpatialTemplateElement](groupactivities/spatialtemplateelement.md) — 一个接口，用于在你的空间模板中定义某个元素。
- [SpatialTemplateElementPosition](groupactivities/spatialtemplateelementposition.md) — 一种类型，定义某个元素在空间模板中的位置。
- [SpatialTemplateElementDirection](groupactivities/spatialtemplateelementdirection.md) — 活动开始时参与者最初面对的方向。
- [SpatialTemplateRole](groupactivities/spatialtemplaterole.md) — 一个接口，用于定义你分配给群组活动参与者的角色。

### 文件与数据传输

- [使用 SharePlay 创建协作式照片图库](groupactivities/creating-a-collaborative-photo-gallery-with-shareplay.md) — 通过使用 SharePlay 在参与者之间同步图片，构建一个共享照片图库。
- [在 SharePlay 活动期间同步数据](groupactivities/synchronizing-data-during-a-shareplay-activity.md) — 在设备之间发送自定义消息和数据，为你的活动同步内容，并处理你的 App 从其他参与者那里收到的消息。
- [GroupSessionMessenger](groupactivities/groupsessionmessenger.md) — 一个对象，在加入群组会话的设备之间传输特定于 App 的数据。
- [GroupSessionJournal](groupactivities/groupsessionjournal.md) — 一个对象，管理加入群组会话的参与者之间的文件和数据传输。

### 系统状态

- [GroupStateObserver](groupactivities/groupstateobserver.md) — 一个对象，包含有关系统能否启动 SharePlay 体验的信息。
