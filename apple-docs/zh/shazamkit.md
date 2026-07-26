---
title: ShazamKit
framework: ShazamKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/shazamkit
source_url: 'https://developer.apple.com/documentation/shazamkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/shazamkit.json'
content_hash: 'sha256:c7c7c2cfafe2af6a'
translated: true
---

> 导航：[Technologies](technologies.md)

# ShazamKit

<sub>框架</sub>

当一段音频是 Shazam 目录或你自定义目录中已捕获声音的一部分时，查找该音频录音的相关信息。

## 概述

ShazamKit 使用音频录音独有的声学*签名*来查找匹配项。这个签名捕捉了音频信号能量的时频分布，体积远小于原始音频。它同时也是一种单向转换，因此无法将签名还原回录音本身。

ShazamKit 会为每段可供搜索的完整音频录音生成一个*参考签名*。*目录*用于存储参考签名及其关联的元数据，即*媒体项*。

查找匹配项时，会将 ShazamKit 为捕获音频生成的*查询签名*与目录中的参考签名进行比对。当查询签名与某个参考签名的一部分充分匹配时，即视为匹配成功。即使捕获的音频存在噪声，例如餐厅里播放的背景音乐的部分录音，也可能出现匹配。

下图展示了将查询签名与目录中参考签名进行匹配的过程。匹配结果中的信息包括参考录音中与查询起点相匹配的时间码。

![一张频谱图，展示了查询签名与参考签名在某一特定时间点的签名匹配情况。](../../attachments/685947e963164829076ac3ec0fe3bbc1/media-3807548@2x.png)

例如，Shazam App 会将设备麦克风采集的声音流转换为查询签名，并在 Shazam 音乐目录中查找匹配项。匹配结果包含参考签名的元数据，例如歌曲名、艺人名和其他详情。

你可以使用自己的参考签名及其关联元数据创建自定义目录。例如，一款虚拟学习 App 的目录可能包含教学视频的参考签名，以及关联的元数据（其中包括问题对应的时间码）。借助 ShazamKit，该 App 可以根据匹配的时间码识别出当前问题，并给出可能的答案选项。如果学生在视频中前进或后退，App 会根据学生当前观看内容的声音更新状态。

## 主题

### 匹配音频

- [SHSession](shazamkit/shsession.md) — 当一段录音是 Shazam 目录或你自定义目录中已捕获声音的一部分时，用于匹配该特定音频录音的对象。
- [SHManagedSession](shazamkit/shmanagedsession.md) — 用于将一段录音与 Shazam 目录或你自定义目录中已捕获的声音进行录制和匹配的对象。
- [SHSessionDelegate](shazamkit/shsessiondelegate.md) — 会话调用这些方法来返回匹配请求的结果。
- [SHMatch](shazamkit/shmatch.md) — 表示与某次查询匹配的目录媒体项的对象。
- [SHMatchedMediaItem](shazamkit/shmatchedmediaitem.md) — 表示某个已匹配参考签名的元数据的对象。
- [SHMediaItem](shazamkit/shmediaitem.md) — 表示某个参考签名的元数据的对象。

### 从音频创建签名

- [SHSignature](shazamkit/shsignature.md) — 包含签名的不透明数据及其他信息的对象。
- [SHSignatureGenerator](shazamkit/shsignaturegenerator.md) — 用于将音频数据转换为签名的对象。

### 创建自定义音频目录

- [Building a Custom Catalog and Matching Audio](shazamkit/building-a-custom-catalog-and-matching-audio.md) — 通过将音频与自定义参考签名及其关联元数据进行匹配，显示与教学视频同步的课程内容。
- [ShazamKit Dance Finder with Managed Session](shazamkit/shazamkit-dance-finder-with-managed-session.md) — 通过将音频与自定义目录进行匹配，查找某首歌曲对应的舞蹈动作视频，并显示已识别歌曲的历史记录。
- [SHCustomCatalog](shazamkit/shcustomcatalog.md) — 用于存储自定义音频录音的参考签名及其关联元数据的对象。
- [SHCatalog](shazamkit/shcatalog.md) — 用于存储参考签名及其关联元数据的抽象基类。

### 更新用户的 Shazam 资料库

- [SHLibrary](shazamkit/shlibrary.md) — 表示用户已同步的 Shazam 资料库的对象。
- [SHMediaLibrary](shazamkit/shmedialibrary.md) — 表示用户 Shazam 资料库的对象。 _(已废弃)_

### Shazam 错误

- [SHError](shazamkit/sherror.md) — 一种错误类型，由你创建或由系统创建，用于指示目录、匹配尝试、签名或保存到用户 Shazam 资料库过程中出现的问题。

### 参考

- [ShazamKit Enumerations](shazamkit/shazamkit-enumerations.md)
- [ShazamKit Constants](shazamkit/shazamkit-constants.md)
