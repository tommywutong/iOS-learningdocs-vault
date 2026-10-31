---
title: 'keyPathsForValuesAffectingValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/keypathsforvaluesaffectingvalue%28forkey%3A%29.json'
content_hash: 'sha256:bac921ef751d15b0'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# keyPathsForValuesAffectingValue(forKey:)

<sub>类型方法</sub>

返回一组键路径，这些属性的值会影响指定键的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>
```

## 参数

- `key` — 其值受键路径影响的键。

## 讨论

当针对该键的观察者向接收类的实例注册时，键值观察本身会自动观察同一实例的所有键路径，并在那些键路径中任一值更改时向观察者发送该键的更改通知。

此方法的默认实现会在接收类中搜索名称匹配模式 `+keyPathsForValuesAffecting<Key>` 的方法，并在找到时返回调用该方法的结果。任何此类方法都必须返回 NSSet。若找不到此类方法，则为向后二进制兼容性，返回根据现已弃用的 [setKeys:triggerChangeNotificationsForDependentKey:](setkeys_triggerchangenotificationsfordependentkey_.md) 方法先前调用所提供信息计算得出的 NSSet。

当你的某个属性的 getter 方法使用其他属性（包括通过键路径定位的属性）的值来计算要返回的值时，可以重写此方法。你的重写通常应调用 `super`，并返回一个集合，其中包含这样做所得到的集合中的任何成员（以免干扰超类中对此方法的重写）。

> [!note] 注意
> 使用类别向现有类添加计算属性时，不得重写此方法；在类别中重写方法不受支持。在这种情况下，请实现匹配的 `+keyPathsForValuesAffecting<Key>` 以利用此机制。

## 另请参阅

### 观察自定义

- [+ automaticallyNotifiesObserversForKey:](<automaticallynotifiesobservers(forkey_).md>) — 返回一个布尔值，指示被观察对象是否支持给定键的自动键值观察。
- [NSKeyValueObservingCustomization](../../foundation/nskeyvalueobservingcustomization.md) — 使用键值观察并不要求遵循 NSKeyValueObservingCustomization。若需要为某个键禁用自动通知，或添加依赖键，请提供这些函数的实现
- [observationInfo](observationinfo.md) — 返回一个指针，用于标识向被观察对象注册的所有观察者的信息。
