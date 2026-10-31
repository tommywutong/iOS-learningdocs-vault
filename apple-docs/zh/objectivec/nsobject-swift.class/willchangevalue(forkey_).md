---
title: 'willChangeValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/willchangevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/willchangevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/willchangevalue%28forkey%3A%29.json'
content_hash: 'sha256:95138835e5971048'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# willChangeValue(forKey:)

<sub>实例方法</sub>

通知被观察对象给定属性的值即将更改。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willChangeValue(forKey key: String)
```

## 参数

- `key` — 将更改的属性的名称。

## 讨论

在手动实现键值观察合规性时使用此方法，以通知被观察对象 `key` 处的值即将更改。

The change type of this method is `NSKeyValueChangeSetting`.

> [!important] 重要
> 值更改后，必须使用相同参数调用相应的 [- didChangeValueForKey:](<didchangevalue(forkey_).md>)。

### 特殊注意事项

很少需要在子类中重写此方法；若重写，请务必调用 `super`。

## 另请参阅

### Notifying Observers of Changes

- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — 通知被观察对象给定属性的值已更改。
- [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化即将在给定索引处执行。
- [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化已在给定索引处发生。
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，即将对指定的无序一对多关系做出指定变化。
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — 通知被观察对象，已对指定的无序一对多关系进行了指定更改。
