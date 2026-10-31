---
title: 'didChangeValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/didchangevalue%28forkey%3A%29.json'
content_hash: 'sha256:5f70925a9980106e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# didChangeValue(forKey:)

<sub>实例方法</sub>

通知被观察对象给定属性的值已更改。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didChangeValue(forKey key: String)
```

## 参数

- `key` — 已更改的属性的名称。

## 讨论

在手动实现键值观察合规性时使用此方法，以通知被观察对象 `key` 处的值刚刚更改。对此方法的调用始终与对 [- willChangeValueForKey:](<willchangevalue(forkey_).md>) 的匹配调用成对出现。

### 特殊注意事项

很少需要在子类中重写此方法；若重写，请务必调用 `super`。

## 另请参阅

### Notifying Observers of Changes

- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — 告知被观察对象，某给定属性的值即将变化。
- [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化即将在给定索引处执行。
- [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化已在给定索引处发生。
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，即将对指定的无序一对多关系做出指定变化。
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，已对指定的无序一对多关系做出指定变化。
