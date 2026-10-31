---
title: 'objc_copyClassNamesForImage(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_copyclassnamesforimage(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyclassnamesforimage(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyclassnamesforimage%28_%3A_%3A%29.json'
content_hash: 'sha256:ebe95600a7e2fe97'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyClassNamesForImage(_:_:)

<sub>函数</sub>

返回指定库或框架中所有类的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyClassNamesForImage(_ image: UnsafePointer<CChar>, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>?
```

## 参数

- `image` — 你正在查询的库或框架。

- `outCount` — 返回数组中的类名数量。

## 返回值

由表示指定库或框架中所有类名的 C 字符串组成的数组。

## 另请参阅

### 处理库

- [objc_copyImageNames](<objc_copyimagenames(__).md>) — 返回所有已加载的 Objective-C 框架和动态库的名称。
- [class_getImageName](<class_getimagename(__).md>) — 返回类所源自的动态库的名称。
