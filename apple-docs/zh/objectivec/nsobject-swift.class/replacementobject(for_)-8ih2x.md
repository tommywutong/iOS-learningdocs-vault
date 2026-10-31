---
title: 'replacementObject(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-8ih2x'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-8ih2x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/replacementobject%28for%3A%29-8ih2x.json'
content_hash: 'sha256:7c7773488f144c62'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# replacementObject(for:)

<sub>实例方法</sub>

由子类重写，以便在归档期间用另一个对象替换自身。

<sub>Mac Catalyst, macOS</sub>

```swift
func replacementObject(for archiver: NSArchiver) -> Any?
```

## 参数

- `archiver` — The archiver creating an archive.

## 返回值

在归档期间用于替换接收者的对象。

## 讨论

此方法由 `NSArchiver` 调用。`NSObject` 的实现返回 [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) 返回的对象。

## 另请参阅

### 归档

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — 由子类重写，以便用另一个对象替换已解码并随后收到此消息的对象。
- [classForArchiver](classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — 重写以返回在对象的类不可用时可用于解码对象的类名。
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间替换为新类。
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ setVersion:](<setversion(__).md>) — 设置接收者的版本号。
- [+ version](<version().md>) — 返回分配给该类的版本号。
