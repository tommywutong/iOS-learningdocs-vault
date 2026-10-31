---
title: classFallbacksForKeyedArchiver()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classfallbacksforkeyedarchiver()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classfallbacksforkeyedarchiver()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classfallbacksforkeyedarchiver%28%29.json'
content_hash: 'sha256:78cb7d0511bc2ad3'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classFallbacksForKeyedArchiver()

<sub>类型方法</sub>

重写以返回在其类不可用时可用来解码对象的类的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func classFallbacksForKeyedArchiver() -> [String]
```

## 返回值

指定解档时按首选顺序排列的类名称的字符串对象数组

## 讨论

[NSKeyedArchiver](../../foundation/nskeyedarchiver.md) 会调用此方法并将结果存储在归档中。若对象的实际类在解档时不存在，[NSKeyedUnarchiver](../../foundation/nskeyedunarchiver.md) 会遍历存储的类列表，并使用第一个确实存在的类作为解码该对象的替代类。此方法的默认实现返回空数组。

若你在应用程序中引入新类，可使用此方法提供某种向后兼容性，以防归档会在没有该类的系统上读取。有时可能有另一个类几乎同样适合作为新类的替代，并且可以为新类仔细选择归档键和归档状态（或写出兼容性数据），以便在必要时将该对象作为替代类解档。

## 另请参阅

### 归档

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — 由子类重写，以便用另一对象替代已解码并随后收到此消息的对象。
- [classForArchiver](classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间替换为新类。
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。 _(已废弃)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ setVersion:](<setversion(__).md>) — 设置接收者的版本号。
- [+ version](<version().md>) — 返回分配给该类的版本号。
