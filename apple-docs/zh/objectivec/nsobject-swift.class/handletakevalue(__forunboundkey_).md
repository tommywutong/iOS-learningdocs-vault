---
title: 'handleTakeValue(_:forUnboundKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/handletakevalue(_:forunboundkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handletakevalue(_:forunboundkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/handletakevalue%28_%3Aforunboundkey%3A%29.json'
content_hash: 'sha256:01002aac8638401b'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# handleTakeValue(_:forUnboundKey:)

<sub>实例方法</sub>

当 [- takeValue:forKey:](<takevalue(__forkey_).md>) 找不到 `key` 的属性绑定时调用。

> [!warning] 已废弃
> 请改用 [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>)。

<sub>tvOS, visionOS, watchOS</sub>

```swift
func handleTakeValue(_ value: Any?, forUnboundKey key: String)
```

## 另请参阅

### 已废弃的方法

- [+ useStoredAccessor](<usestoredaccessor().md>) — 如果存储值方法 [- storedValueForKey:](<storedvalue(forkey_).md>) 和 [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) 应优先使用私有访问器方法而非公共访问器，则返回 `true`。（已废弃）
- [- handleQueryWithUnboundKey:](<handlequery(withunboundkey_).md>) — 当 [- valueForKey:](<value(forkey_).md>) 找不到与 `key` 对应的属性时调用。（已废弃）
- [- storedValueForKey:](<storedvalue(forkey_).md>) — 返回由给定键标识的属性。（已废弃）
- [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) — 设置由给定键标识的属性的值。（已废弃）
- [- takeValuesFromDictionary:](<takevalues(from_).md>) — 使用给定字典中的值设置接收者的属性，并用其键标识属性（已废弃）
- [- takeValue:forKeyPath:](<takevalue(__forkeypath_).md>) — 将由 `keyPath` 标识的属性的值设置为 `value`。（已废弃）
- [- takeValue:forKey:](<takevalue(__forkey_).md>) — 将由 `key` 标识的属性的值设置为 `value`。（已废弃）
- [- unableToSetNilForKey:](<unabletosetnil(forkey_).md>) — 如果 `key` 由标量属性表示，则调用。（已废弃）
- [- valuesForKeys:](<values(forkeys_).md>) — 返回一个字典，其键为 `keys` 中的属性名，对应值为相应的属性值。（已废弃）
