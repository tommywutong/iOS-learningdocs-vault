---
title: 'objc_copyImageNames(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_copyimagenames(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyimagenames(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyimagenames%28_%3A%29.json'
content_hash: 'sha256:3cdec85ef4b4e845'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyImageNames(_:)

<sub>函数</sub>

返回所有已加载的 Objective-C 框架和动态库的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyImageNames(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>
```

## 参数

- `outCount` — 返回数组中的名称数量。

## 返回值

由表示所有已加载的 Objective-C 框架和动态库名称的 C 字符串组成的数组。

## 另请参阅

### 处理库

- [class_getImageName](<class_getimagename(__).md>) — 返回类所源自的动态库的名称。
- [objc_copyClassNamesForImage](<objc_copyclassnamesforimage(____).md>) — 返回指定库或框架中所有类的名称。
