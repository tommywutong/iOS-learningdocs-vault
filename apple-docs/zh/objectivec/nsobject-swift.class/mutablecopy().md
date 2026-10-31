---
title: mutableCopy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/mutablecopy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablecopy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutablecopy%28%29.json'
content_hash: 'sha256:69f5342018b9500d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableCopy()

<sub>实例方法</sub>

返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableCopy() -> Any
```

## 返回值

由 [NSMutableCopying](../../foundation/nsmutablecopying.md) 协议方法 [mutableCopy(with:)](<../../foundation/nsmutablecopying/mutablecopy(with_).md>) 返回的对象，其中 zone 为 `nil`。

## 讨论

这是采用 [NSMutableCopying](../../foundation/nsmutablecopying.md) 协议的类的便捷方法。若没有 [mutableCopy(with:)](<../../foundation/nsmutablecopying/mutablecopy(with_).md>) 的实现，则会引发异常。

## 另请参阅

### 创建、拷贝与释放对象

- [- init](<init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。
- [- copy](<copy().md>) — 返回 `copy(with:)` 返回的对象。
