---
title: 播放 HLS 插播内容时提供时间线的整合视图
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials
source_url: 'https://developer.apple.com/documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.json'
content_hash: 'sha256:d15090eacec402ff'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体播放](media-playback.md)

# 播放 HLS 插播内容时提供时间线的整合视图

<sub>示例代码</sub>

通过点播（point）和填充占用（fill occupancy）的 HLS 插播内容，超越简单的广告插入。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC24 场次 10114：[Enhance ad experiences with HLS Interstitials](https://developer.apple.com/wwdc24/10114/)

### 配置示例代码项目

使用 App 的 Live stream examples 部分下的示例需要运行一个本地测试流。项目中包含一个 Go 脚本，它会启动一个托管此示例流的本地 Web 服务器。你必须安装 [Go](https://go.dev/doc/install) 才能运行此脚本。

打开一个终端窗口，切换到 `/Source/LiveStreamExample/` 目录，并运行以下命令来启动流：

```
go run liveStreamGenerator.go --http :8443 map.mp4 segment0.m4s segment1.m4s segment2.m4s
```

流启动后，复制它的 URL，其格式如下：`http://<hostname>:8443/media.m3u8`。在 Xcode 项目中，打开 `Menu.json` 文件，并将占位 URL（http://livestreamserver.url:8443/media.m3u8）替换为你的本地流 URL。重新启动 App 以查看直播示例。

## 另请参阅

### 插播内容

- [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) — 一个提供播放器呈现插播内容方式指示的对象。
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) — 一个为主播放器播放的条目安排插播事件的对象。
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — 一个监测插播事件安排与进度的对象。
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification 的 userInfo 字典键。值为 NSError。请求成功时不存在。
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](avplayerinterstitialeventmonitorschedulerequestidentifierkey.md) — AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification 的 userInfo 字典键。值为 NSString。
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification 的 userInfo 字典键。值为 NSData。请求失败时不存在。
- [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) — 一个为主播放器条目和已安排的插播事件的时间线和播放序列建模的对象。

## 下载

- [ProvidingAnIntegratedViewOfYourTimelineWhenPlayingHLSInterstitials.zip](https://docs-assets.developer.apple.com/published/f879c5e639a6/ProvidingAnIntegratedViewOfYourTimelineWhenPlayingHLSInterstitials.zip)
