---
title: Shared with You
framework: Shared with You
symbol_kind: module
role: collection
role_heading: Technology
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/sharedwithyou
source_url: 'https://developer.apple.com/documentation/sharedwithyou'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sharedwithyou.json'
content_hash: 'sha256:b99e5b09148eb3c0'
translated: true
---

> 导航：[Technologies](technologies.md)

# Shared with You

<sub>技术</sub>

在你的 App 中呈现共享内容并支持协作。

## 概述

访问并查看从 Messages 共享到系统各处的内容，无需离开你的 App 即可继续这段信息交流体验。集成 Shared with You，让人们更方便地访问通过对话或通知共享的内容。

![](../../attachments/cbf165ab43e7dff75cbc6c588785e19f/media-4301694@2x.png)

<sub>一张 iPhone 的图片。屏幕中间是一个 Shared with You 分享栏，垂直排列着三个列表项。每个列表项都有一个灰色矩形，旁边配有文字。三行都以「Title」作为标题、「Subtitle」作为副标题。副标题下方，三行都有一个椭圆形按钮，标题为「From Juan」。</sub>

在你的 App 中支持 Shared with You 分享栏，使用系统渲染的 [SWAttributionView](sharedwithyou/swattributionview.md) 直观呈现共享项目。使用 [SWHighlight](sharedwithyou/swhighlight.md) 类安全共享你的 App 所访问的通用链接。要了解入门信息，请参阅 [Making your app content shareable](sharedwithyou/making-your-app-content-shareable.md)。

> [!note] 来自 WWDC22 的相关场次
> 场次 10094：[Add Shared with You to your app](https://developer.apple.com/videos/play/wwdc2022/10094)

## 主题

### 框架

- [Shared with You Core](sharedwithyoucore.md) — 将自定义协作与 Messages、Mail 和 FaceTime 集成。

### 共享内容

- [Making your app content shareable](sharedwithyou/making-your-app-content-shareable.md) — 为你的 App 添加对通用链接和 Shared with You 分享栏的支持，以支持共享内容。
- [Shared content interactions](sharedwithyou/shared-content-interactions.md) — 使用高亮内容和归属视图来管理参与者，并为共享内容触发事件。

### 协作

- [Adding shared content collaboration to your app](sharedwithyou/adding-shared-content-collaboration-to-your-app.md) — 使用 CloudKit 和 iCloud Drive 在你的 App 中管理共享内容协作。
- [Adding custom collaboration to your app](sharedwithyou/adding-custom-collaboration-to-your-app.md) — 将你的自定义协作 App 与 Messages 集成。
- [Collaboration views](sharedwithyou/collaboration-views.md) — 创建并自定义协作视图，以管理共享内容操作。

### 框架版本

- [Version number](sharedwithyou/version-number.md)
- [Version string](sharedwithyou/version-string.md)

### 宏

- [Macros](sharedwithyou/macros.md)

### 变量

- [SWCopyRepresentationTypeIdentifier](sharedwithyou/swcopyrepresentationtypeidentifier.md) _(beta)_
