---
title: NSObject.KeyValueObservingPublisher
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keyvalueobservingpublisher.json'
content_hash: 'sha256:ec9973cc81f67040'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# NSObject.KeyValueObservingPublisher

<sub>结构体</sub>

每当观察值更改时生成新元素的 Combine 发布者。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct KeyValueObservingPublisher<Subject, Value> where Subject : NSObject
```

## 概述

使用此发布者将符合键值观察的属性集成到 Combine 发布链中。你可以使用 [NSObject](../nsobject-swift.class.md) 实例方法 `publisher(for:options:)`，传入键路径和一组 [NSKeyValueObservingOptions](../../foundation/nskeyvalueobservingoptions.md) 来创建此类型的发布者。

## 关系

- **符合**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Publisher](../../combine/publisher.md)

## 主题

### Creating a KVO Publisher

- [init(object:keyPath:options:)](<keyvalueobservingpublisher/init(object_keypath_options_).md>) — 为给定的对象与键路径组合创建键值观察发布者，并使用你提供的发布行为选项。

### 检查 KVO 发布者属性

- [object](keyvalueobservingpublisher/object.md) — 包含要发布属性的对象。
- [keyPath](keyvalueobservingpublisher/keypath.md) — 相对于接收此消息的对象、要发布属性的键路径。
- [options](keyvalueobservingpublisher/options.md) — 决定发布者生成哪些元素的选项。

### 实例方法

- [didChange()](<keyvalueobservingpublisher/didchange().md>) — 返回在符合 KVO 的属性更改时发出值的发布者。
