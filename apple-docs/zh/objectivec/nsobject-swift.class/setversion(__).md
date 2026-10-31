---
title: 'setVersion(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setversion(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setversion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setversion%28_%3A%29.json'
content_hash: 'sha256:73b0a9d89a24fb28'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setVersion(_:)

<sub>类型方法</sub>

Sets the receiver’s version number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setVersion(_ aVersion: Int)
```

## 参数

- `aVersion` — The version number for the receiver.

## 讨论

当要归档类的实例并稍后重用时，版本号很有帮助。默认版本为 `0`。

### 特殊注意事项

版本号适用于 `NSArchiver`/`NSUnarchiver`，但不适用于 `NSKeyedArchiver`/`NSKeyedUnarchiver`。键控归档器不编码类版本号。

## 另请参阅

### 归档

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — 由子类重写，以便用另一个对象替换已解码并随后收到此消息的对象。
- [classForArchiver](classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — 重写以返回在对象的类不可用时可用于解码对象的类名。
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间替换为新类。
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。 _(已废弃)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ version](<version().md>) — 返回分配给该类的版本号。
