---
title: 'init(object:keyPath:options:)'
framework: Objective-C Runtime
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init(object:keypath:options:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init(object:keypath:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher/init%28object%3Akeypath%3Aoptions%3A%29.json'
content_hash: 'sha256:22972586fcd3daa7'
translated: true
---

> 导航： [技术](../../../technologies.md) · [Objective-C Runtime](../../../objectivec.md) · [NSObject](../../nsobject-swift.class.md) · [KeyValueObservingPublisher](../keyvalueobservingpublisher.md)

# init(object:keyPath:options:)

<sub>初始化方法</sub>

为给定的对象与键路径组合创建键值观察发布者，并使用你提供的发布行为选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(object: Subject, keyPath: KeyPath<Subject, Value>, options: NSKeyValueObservingOptions)
```

## 参数

- `object` — 包含要发布属性的对象。

- `keyPath` — 相对于接收此消息的对象、要发布属性的键路径。

- `options` — 决定发布者产生哪些元素的选项。将此参数设为 `[]`，可在观察到的属性更改时接收新元素。

## 讨论

每当观察到的属性更改时，此发布者都会产生一个新元素。
