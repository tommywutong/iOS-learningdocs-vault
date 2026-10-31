---
title: 'defaultPlaceholder(for:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/defaultplaceholder(for:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/defaultplaceholder(for:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/defaultplaceholder%28for%3Awith%3A%29.json'
content_hash: 'sha256:682d86e4273eab3b'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# defaultPlaceholder(for:with:)

<sub>类型方法</sub>

当接收类实例的符合键值编码的属性返回 `marker` 指定的值，且尚未指定其他占位符时，返回将用作 `binding` 占位符的对象。

<sub>macOS</sub>

```swift
class func defaultPlaceholder(for marker: Any?, with binding: NSBindingName) -> Any?
```

## 讨论

`marker` 可以为 `nil`，或为 [Selection Markers](../../appkit/selection-markers.md) 中描述的常量之一。

## 另请参阅

### 已废弃的类方法

- [+ setDefaultPlaceholder:forMarker:withBinding:](<setdefaultplaceholder(__for_with_).md>) — 当接收类实例的符合键值编码的属性返回 `marker` 指定的值，且尚未指定其他占位符时，将 `placeholder` 设为 `binding` 的默认占位符。（已废弃）
- [+ useStoredAccessor](<usestoredaccessor().md>) — 如果存储值方法 [- storedValueForKey:](<storedvalue(forkey_).md>) 和 [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) 应优先使用私有访问器方法而非公共访问器，则返回 `true`。（已废弃）
