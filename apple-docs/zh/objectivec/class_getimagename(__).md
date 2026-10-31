---
title: 'class_getImageName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_getimagename(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_getimagename(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_getimagename%28_%3A%29.json'
content_hash: 'sha256:72d67619cddd8a5a'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_getImageName(_:)

<sub>函数</sub>

返回某个类源自的动态库的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_getImageName(_ cls: AnyClass?) -> UnsafePointer<CChar>?
```

## 参数

- `cls` — 你要查询的类。

## 返回值

一个 C 字符串，表示包含 `cls` 类所在库的名称。

## 另请参阅

### 使用库

- [objc_copyImageNames](<objc_copyimagenames(__).md>) — 返回所有已加载的 Objective-C 框架和动态库的名称。
- [objc_copyClassNamesForImage](<objc_copyclassnamesforimage(____).md>) — 返回指定库或框架内所有类的名称。
