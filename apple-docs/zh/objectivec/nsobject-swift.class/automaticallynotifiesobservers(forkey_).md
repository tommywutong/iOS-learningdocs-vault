---
title: 'automaticallyNotifiesObservers(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/automaticallynotifiesobservers%28forkey%3A%29.json'
content_hash: 'sha256:4aebb3522bdc7028'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# automaticallyNotifiesObservers(forKey:)

<sub>类型方法</sub>

返回一个布尔值，指示被观察对象是否支持给定键的自动键值观察。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func automaticallyNotifiesObservers(forKey key: String) -> Bool
```

## 返回值

若键值观察机制应在该类的实例收到针对 `key` 的键值编码消息，或针对 `key` 的符合键值编码的变更方法被调用时，自动调用 [- willChangeValueForKey:](<willchangevalue(forkey_).md>)/[- didChangeValueForKey:](<didchangevalue(forkey_).md>) 以及 [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>)/[- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>)，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

默认实现返回 [YES](../yes.md)。从 OS X 10.5 起，此方法的默认实现会在接收类中搜索名称匹配模式 `+automaticallyNotifiesObserversOf<Key>` 的方法，若找到则返回调用该方法的结果。找到的任何方法都必须返回 `BOOL`。若未找到此类方法，则返回 [YES](../yes.md)。

## 另请参阅

### 观察自定义

- [+ keyPathsForValuesAffectingValueForKey:](<keypathsforvaluesaffectingvalue(forkey_).md>) — 返回一组键路径，这些键路径对应的属性值会影响指定键的值。
- [NSKeyValueObservingCustomization](../../foundation/nskeyvalueobservingcustomization.md) — 使用键值观察并不要求遵循 NSKeyValueObservingCustomization。若需要为某个键禁用自动通知，或添加依赖键，请提供这些函数的实现
- [observationInfo](observationinfo.md) — 返回一个指针，用于标识向被观察对象注册的所有观察者的信息。
