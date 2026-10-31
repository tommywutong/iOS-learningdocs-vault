---
title: useStoredAccessor()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/usestoredaccessor()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/usestoredaccessor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/usestoredaccessor%28%29.json'
content_hash: 'sha256:4a6400e5d697bf06'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# useStoredAccessor()

<sub>类型方法</sub>

若存储值方法 [- storedValueForKey:](<storedvalue(forkey_).md>) 和 [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) 应优先使用私有访问器方法而非公共访问器，则返回 `true`。

> [!warning] 已废弃
> 此方法没有直接替代项，不过请参阅 [accessInstanceVariablesDirectly](accessinstancevariablesdirectly.md)。

<sub>tvOS, visionOS, watchOS</sub>

```swift
class func useStoredAccessor() -> Bool
```

## 讨论

返回 [NO](../no.md) 会使存储值方法使用与相应基本键值编码方法（[- valueForKey:](<value(forkey_).md>) 和 [- takeValue:forKey:](<takevalue(__forkey_).md>)）相同的访问器方法或实例变量搜索顺序。默认实现返回 [YES](../yes.md)。

应用应使用 `valueForKey:` 和 `setValue:forKey:` 方法，而不是 `storedValueForKey:` 和 `takeStoredValue:forKey:`。

## 另请参阅

### 已废弃的类方法

- [+ defaultPlaceholderForMarker:withBinding:](<defaultplaceholder(for_with_).md>) — 当接收类实例的符合键值编码的属性返回 `marker` 指定的值，且尚未指定其他占位符时，返回将用作 `binding` 占位符的对象。 _(已废弃)_
- [+ setDefaultPlaceholder:forMarker:withBinding:](<setdefaultplaceholder(__for_with_).md>) — 当接收类实例的符合键值编码的属性返回由 `marker` 指定的值，且尚未指定其他占位符时，将 `placeholder` 设为 `binding` 的默认占位符。 _(已废弃)_
