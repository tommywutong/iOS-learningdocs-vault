---
title: 'objc_copyClassList(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_copyclasslist(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_copyclasslist(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_copyclasslist%28_%3A%29.json'
content_hash: 'sha256:0a1bcc30c935ccea'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_copyClassList(_:)

<sub>函数</sub>

创建并返回指向所有已注册类定义的指针列表。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_copyClassList(_ outCount: UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<AnyClass>?
```

## 参数

- `outCount` — 用于存储此函数在列表中返回的类数量的整数指针。此参数可以为 `nil`。

## 返回值

以 `nil` 结尾的类数组。必须使用 `free()` 释放该数组。

## 另请参阅

### 获取类定义

- [objc_getClassList](<objc_getclasslist(____).md>) — 获取已注册的类定义列表。
- [objc_lookUpClass](<objc_lookupclass(__).md>) — 返回指定类的类定义。
- [objc_getClass](<objc_getclass(__).md>) — 返回指定类的类定义。
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — 返回指定类的类定义。
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — 返回指定类的元类定义。
