---
title: copy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/copy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/copy%28%29.json'
content_hash: 'sha256:adf30273a116de64'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# copy()

<sub>实例方法</sub>

返回 `copy(with:)` 返回的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy() -> Any
```

## 返回值

由 [NSCopying](../../foundation/nscopying.md) 协议方法 [copy(with:)](<../../foundation/nscopying/copy(with_).md>) 返回的对象。

## 讨论

这是采用 [NSCopying](../../foundation/nscopying.md) 协议的类的便捷方法。若没有 [copy(with:)](<../../foundation/nscopying/copy(with_).md>) 的实现，则会引发异常。

`NSObject` 本身不支持 [NSCopying](../../foundation/nscopying.md) 协议。子类必须支持该协议并实现 [copy(with:)](<../../foundation/nscopying/copy(with_).md>) 方法。子类版本的 [copy(with:)](<../../foundation/nscopying/copy(with_).md>) 方法应先向 `super` 发送消息以纳入其实现，除非该子类直接继承自 `NSObject`。

## 另请参阅

### 创建、拷贝与释放对象

- [- init](<init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。
- [- mutableCopy](<mutablecopy().md>) — 返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。
