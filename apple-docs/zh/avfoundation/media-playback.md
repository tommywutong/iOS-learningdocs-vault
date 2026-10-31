---
title: 媒体播放
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/media-playback
source_url: 'https://developer.apple.com/documentation/avfoundation/media-playback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/media-playback.json'
content_hash: 'sha256:3fc6e211feeccfe3'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 媒体播放

<sub>API 集合</sub>

管理媒体资产和插播内容的播放，与你在界面中呈现这些内容的方式无关。

## 概述

你使用播放器来管理媒体资产的播放和计时，例如开始和停止播放，以及跳转到特定时间。一个播放器一次管理单个媒体资产的播放。该框架还提供一个队列播放器，可将媒体资产排队依次播放。

> [!note] 注意
> 当你使用 AVFoundation 时，Apple 可能会收集指标以帮助改进该框架。

你创建一个 [AVPlayerItem](avplayeritem.md) 实例来播放媒体资产。播放器条目管理由播放器播放的资产的计时和呈现状态。播放器条目还包含与资产中的轨道相对应的播放器条目轨道。你可以将播放器的输出定向到专用的 Core Animation 图层——播放器图层或同步图层。

> [!important] 重要
> 如果你的 App 需要对 ProRes 和 ProRes RAW 视频文件进行 Afterburner 加速播放和解码，则必须调用 [VTRegisterProfessionalVideoWorkflowVideoDecoders()](<../videotoolbox/vtregisterprofessionalvideoworkflowvideodecoders().md>) 函数。

## 主题

### 基础

- [为媒体播放配置你的 App](configuring-your-app-for-media-playback.md) — 配置 App 以启用标准媒体播放行为。

### 播放控制

- [在 SwiftUI 中观察播放状态](observing-playback-state-in-swiftui.md) — 让你的用户界面与播放对象的状态变化保持同步。
- [控制播放器的传输行为](controlling-the-transport-behavior-of-a-player.md) — 在媒体呈现中播放、暂停和跳转。
- [创建无缝的多视图播放体验](creating-a-seamless-multiview-playback-experience.md) — 使用 AVFoundation 和 AVRouting 框架构建高级的多视图播放体验。
- [AVPlayer](avplayer.md) — 一个提供控制播放器传输行为接口的对象。
- [AVPlayerItem](avplayeritem.md) — 一个为播放期间资产的时间安排和呈现状态建模的对象。
- [AVPlayerItemTrack](avplayeritemtrack.md) — 一个表示播放期间资产轨道呈现状态的对象。
- [AVQueuePlayer](avqueueplayer.md) — 一个依次播放一系列播放器条目的对象。
- [AVPlayerLooper](avplayerlooper.md) — 一个使用队列播放器循环播放媒体内容的对象。

### SharePlay

- [Destination Video](../visionos/destination-video.md) — 利用 SwiftUI 在多平台 App 中构建沉浸式媒体体验。
- [支持协调媒体播放](supporting-coordinated-media-playback.md) — 创建同步的媒体体验，让用户能够跨设备观看和收听。
- [AVPlaybackCoordinator](avplaybackcoordinator.md) — 一个协调已连接群组中各播放器播放的对象。
- [AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md) — 一种播放协调器子类，协调已连接群组中各播放器对象的播放。
- [AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md) — 一种播放协调器子类，协调已连接群组中各自定播放器对象的播放。
- [AVPlaybackCoordinationMedium](avplaybackcoordinationmedium.md) — AVPlaybackCoordinationMedium 在其连接的各播放协调器之间传递状态和消息。

### 呈现

- [在 App 中监测播放进度](monitoring-playback-progress-in-your-app.md) — 观察媒体资产的播放以更新 App 的用户界面状态。
- [使用带 alpha 通道的 HEVC 视频](using-hevc-video-with-alpha.md) — 播放、写入和导出带 alpha 通道的 HEVC 视频，为你的视频处理添加叠层效果。
- [AVPlayerLayer](avplayerlayer.md) — 一个呈现播放器对象视觉内容的对象。
- [AVSynchronizedLayer](avsynchronizedlayer.md) — 一种 Core Animation 图层，其计时派生自播放器条目，使你可以将图层动画与媒体播放同步。

### 媒体选择

- [选择字幕和备选音轨](selecting-subtitles-and-alternative-audio-tracks.md) — 通过添加用户母语的字幕和备选音轨来增强 App 对用户的吸引力。
- [AVMediaSelection](avmediaselection.md) — 一个表示资产上媒体选择选项完整呈现方式的对象。
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — 一个表示资产内媒体呈现的一组互斥选项的对象。
- [AVMediaSelectionOption](avmediaselectionoption.md) — 一个表示选项组内媒体呈现的某个特定选项的对象。
- [AVMutableMediaSelection](avmutablemediaselection.md) — 一个可变对象，表示资产上媒体选择选项完整呈现方式。
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — 一个为播放器指定首选语言和媒体特性的对象。
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — 对于以明确意图提供 AVMediaSelectionOptions 备选选择界面而制作的内容，AVCustomMediaSelectionScheme 提供一组用于控制媒体呈现的自定设置。
- [AVMediaPresentationSelector](avmediapresentationselector.md) — 对于以明确意图提供 AVMediaSelectionOptions 备选选择界面而制作的内容，AVMediaPresentationSelector 表示一组互斥的设置。
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — 对于以明确意图提供 AVMediaSelectionOptions 备选选择界面而制作的内容，AVMediaPresentationSetting 表示用于控制媒体呈现的一个可选设置。

### 插播内容

- [播放 HLS 插播内容时提供时间线的整合视图](providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.md) — 通过点播（point）和填充占用（fill occupancy）的 HLS 插播内容，超越简单的广告插入。
- [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) — 一个提供播放器呈现插播内容方式指示的对象。
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) — 一个为主播放器播放的条目安排插播事件的对象。
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — 一个监测插播事件安排与进度的对象。
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification 的 userInfo 字典键。值为 NSError。请求成功时不存在。
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](avplayerinterstitialeventmonitorschedulerequestidentifierkey.md) — AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification 的 userInfo 字典键。值为 NSString。
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification 的 userInfo 字典键。值为 NSData。请求失败时不存在。
- [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) — 一个为主播放器条目和已安排的插播事件的时间线和播放序列建模的对象。

### 指标

- [AVMetrics](avmetrics.md) — 一个异步的指标信息流。
- [AVMergedMetrics](avmergedmetrics.md) — 一个来自不同发布者的异步指标信息流。
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — 一个提供与视频播放质量相关指标的对象。
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — 一种用于向事件流发布指标事件的对象的类型。
- [AVMetricEvent](avmetricevent.md) — 表示指标事件的基类。
- [AVMetricErrorEvent](avmetricerrorevent.md) — 一个表示错误发生时的指标事件的对象。
- [指标事件类型](metric-event-types.md)

### 遥控器

- [在 tvOS 中支持远程交互](supporting-remote-interactions-in-tvos.md) — 使用相关方法，让你的 App 在多种场景下支持远程命令和事件。

### 定时元数据

- [呈现章节标记](presenting-chapter-markers.md) — 添加章节标记，让用户能够快速导览你的内容。
- [AVMetadataGroup](avmetadatagroup.md) — 与时间线片段关联的元数据项集合。
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — 在特定时间范围内有效可用的元数据项集合。
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — 在特定时间范围内有效可用的可变元数据项集合。
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — 在特定日期范围内有效可用的元数据项集合。
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — 在特定日期范围内有效可用的可变元数据项集合。
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — 媒体数据收集器的抽象基类。
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — 一个用于捕获为 HTTP Live Streaming 资产定义的日期范围元数据的对象。

### 媒体输出

- [AVPlayerVideoOutput](avplayervideooutput.md) — 一个从播放器对象接收视频数据的对象。
- [AVVideoOutputSpecification](avvideooutputspecification.md) — 一个指定播放器视频输出所处理的像素缓冲区属性和标签集合的对象。
- [AVPlayerItemOutput](avplayeritemoutput.md) — 一个抽象类，定义从播放器条目输出媒体数据的通用接口。
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) — 一个从播放器条目输出视频帧的对象。
- [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md) — 一个为具有可读（legible）特性的媒体提供属性字符串的对象。
- [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md) — 一种播放器条目输出，将具有可读特性的媒体以渲染后的像素缓冲区形式提供。
- [AVRenderedCaptionImage](avrenderedcaptionimage.md) — 一个提供渲染后的像素缓冲区及其像素位置的对象。
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md) — 一个提供播放器条目轨道所载元数据项集合的对象。
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) — 一个协议，定义了为响应媒体数据序列变化而需实现的方法。
- [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) — [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) 为 [AVPlayerItem](avplayeritem.md) 的播放提供 `CMSampleBuffers`。_(beta)_
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — 创建 [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) 时指定的配置选项。_(beta)_
- [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) — 创建 [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) 时指定的音频专属配置选项。_(beta)_

### 实用工具

- [AVAssetPlaybackAssistant](avassetplaybackassistant.md) — 一个为资产提供播放信息的对象。
- [AVAssetPlaybackConfigurationOption](avassetplaybackconfigurationoption.md) — 一个为资产定义播放配置选项的结构体。

## 另请参阅

### 播放

- [离线播放与存储](offline-playback-and-storage.md) — 将流媒体内容下载到磁盘以支持离线播放，并定义自动移除已下载资产的策略。
- [流媒体与隔空播放](streaming-and-airplay.md) — 使用隔空播放（AirPlay）将内容无线串流到其他设备，并处理涉及 FairPlay 保护资产的请求。
- [样本缓冲区播放](sample-buffer-playback.md) — 创建自定控制器来播放样本缓冲区流并同步其计时。
