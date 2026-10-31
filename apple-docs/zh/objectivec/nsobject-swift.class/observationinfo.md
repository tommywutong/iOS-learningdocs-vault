---
title: observationInfo
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/observationinfo
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observationinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/observationinfo.json'
content_hash: 'sha256:ad538dc355b74aa1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# observationInfo

<sub>实例属性</sub>

返回一个指针，用于标识向被观察对象注册的所有观察者的信息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var observationInfo: UnsafeMutableRawPointer? { get set }
```

## 返回值

标识向被观察对象注册的所有观察者的信息、注册时使用的选项等的指针。

## 讨论

此方法的默认实现从按内存地址键控的被观察对象全局字典中检索信息。

为提高性能，可重写此属性以及 [observationInfo](observationinfo.md)，以将不透明数据指针存储在实例变量中。对此属性的重写不得尝试向所存储的数据发送消息。

## 另请参阅

### 观察自定义

- [+ automaticallyNotifiesObserversForKey:](<automaticallynotifiesobservers(forkey_).md>) — 返回一个布尔值，指示被观察对象是否支持给定键的自动键值观察。
- [+ keyPathsForValuesAffectingValueForKey:](<keypathsforvaluesaffectingvalue(forkey_).md>) — 返回一组键路径，这些键路径对应的属性值会影响指定键的值。
- [NSKeyValueObservingCustomization](../../foundation/nskeyvalueobservingcustomization.md) — 使用键值观察并不要求遵循 NSKeyValueObservingCustomization。若需要为某个键禁用自动通知，或添加依赖键，请提供这些函数的实现
