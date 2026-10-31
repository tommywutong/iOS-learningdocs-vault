---
title: 'didChangeValue(forKey:withSetMutation:using:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:withsetmutation:using:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:withsetmutation:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/didchangevalue%28forkey%3Awithsetmutation%3Ausing%3A%29.json'
content_hash: 'sha256:d80fb8b5f09e88dc'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# didChangeValue(forKey:withSetMutation:using:)

<sub>实例方法</sub>

通知被观察对象，已对指定的无序一对多关系进行了指定更改。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)
```

## 参数

- `key` — 作为无序一对多关系的属性的名称

- `mutationKind` — The type of change that was made.

- `objects` — 参与更改的对象（请参阅 [NSKeyValueSetMutationKind](../../foundation/nskeyvaluesetmutationkind.md)）。

## 讨论

在手动实现键值观察合规性时使用此方法。对此方法的调用始终与对 [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) 的匹配调用成对出现。

### 特殊注意事项

很少需要在子类中重写此方法；若重写，请务必调用 `super`。

## 另请参阅

### Notifying Observers of Changes

- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — 告知被观察对象，某给定属性的值即将变化。
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — 通知被观察对象给定属性的值已更改。
- [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化即将在给定索引处执行。
- [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化已在给定索引处发生。
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，即将对指定的无序一对多关系做出指定变化。
