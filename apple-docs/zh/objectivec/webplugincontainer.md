---
title: WebPlugInContainer
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/webplugincontainer
source_url: 'https://developer.apple.com/documentation/objectivec/webplugincontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/webplugincontainer.json'
content_hash: 'sha256:e325b0296eb17c12'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# WebPlugInContainer

<sub>API 集合</sub>

`WebPlugInContainer` 是一个非正式协议，使插件能够向应用程序发送消息。

## 主题

### Performing actions on the enclosing container

- [- webPlugInContainerLoadRequest:inFrame:](<nsobject-swift.class/webplugincontainerload(__inframe_).md>) — 将一个 URL 加载到某个网页框架中。
- [- webPlugInContainerShowStatus:](<nsobject-swift.class/webplugincontainershowstatus(__).md>) — 告知容器显示一条状态消息。

### Obtaining information about the container

- [webFrame](nsobject-swift.class/webframe.md) — 返回包含该插件的 `WebFrame`。
- [webPlugInContainerSelectionColor](nsobject-swift.class/webplugincontainerselectioncolor.md) — 返回插件的选中颜色。

## 另请参阅

### 相关文档

- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)

### Interacting with Web Plug-ins

- [WebPlugIn](webplugin.md) — `WebPlugIn` 这个非正式协议定义了一些方法，使得使用 WebKit 框架的应用程序与其可能使用的任何基于 WebKit 的插件之间能够进行交互。
