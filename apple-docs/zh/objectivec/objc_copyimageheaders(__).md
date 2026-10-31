---
title: 'objc_copyImageHeaders(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/objectivec/objc_copyimageheaders(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyimageheaders(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyimageheaders%28_%3A%29.json'
content_hash: 'sha256:98749b45eab57c54'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyImageHeaders(_:)

<sub>函数</sub>

返回当前进程中已加载且包含 Objective-C 或 Swift 代码的所有映像的 Mach 头。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyImageHeaders(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<OpaquePointer>
```

<sub>Mac Catalyst, macOS</sub>

```swift
func objc_copyImageHeaders(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<mach_header>>
```

## 参数

- `outCount` — 返回的映像头数量。

## 返回值

由 @c mach_header 指针组成的数组。该数组包含 @c *outCount 个指针，后跟 @c NULL 终止符。你必须使用以下方式释放该数组
