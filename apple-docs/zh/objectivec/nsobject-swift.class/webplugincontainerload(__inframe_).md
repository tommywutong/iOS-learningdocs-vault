---
title: 'webPlugInContainerLoad(_:inFrame:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webplugincontainerload(_:inframe:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugincontainerload(_:inframe:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webplugincontainerload%28_%3Ainframe%3A%29.json'
content_hash: 'sha256:08f034e46eb7157c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInContainerLoad(_:inFrame:)

<sub>实例方法</sub>

将 URL 载入 web 帧。

<sub>macOS</sub>

```swift
func webPlugInContainerLoad(_ request: URLRequest!, inFrame target: String!)
```

## 参数

- `request` — 指定 URL 的请求。

- `target` — 将载入该 URL 的帧。

## 讨论

若找不到 `target` 指定的帧，则会打开新窗口，载入该 URL 请求，并赋予指定的帧名称。若 `target` 为 `nil`，则将 URL 请求载入包围插件的帧。

## 另请参阅

### 对包围容器执行操作

- [- webPlugInContainerShowStatus:](<webplugincontainershowstatus(__).md>) — 告知容器显示状态消息。
