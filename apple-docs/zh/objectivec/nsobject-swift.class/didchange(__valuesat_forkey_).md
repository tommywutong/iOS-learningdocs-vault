---
title: 'didChange(_:valuesAt:forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/didchange(_:valuesat:forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didchange(_:valuesat:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/didchange%28_%3Avaluesat%3Aforkey%3A%29.json'
content_hash: 'sha256:80a74ce8f0b2da10'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# didChange(_:valuesAt:forKey:)

<sub>实例方法</sub>

通知被观察对象，指定的有序一对多关系的索引上已发生指定更改。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)
```

## 参数

- `changeKind` — The type of change that was made.

- `indexes` — 受更改影响的一对多关系的索引。

- `key` — 作为有序一对多关系的属性的名称。

## 讨论

在手动实现键值观察合规性时使用此方法。

### 特殊注意事项

很少需要在子类中重写此方法；若重写，请务必调用 `super`。对此方法的调用始终与对 [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) 的匹配调用成对出现。

## 另请参阅

### Notifying Observers of Changes

- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — 告知被观察对象，某给定属性的值即将变化。
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — 通知被观察对象给定属性的值已更改。
- [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化即将在给定索引处执行。
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，即将对指定的无序一对多关系做出指定变化。
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，已对指定的无序一对多关系做出指定变化。
