---
title: 'replacementObject(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-2l8ox'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacementobject(for:)-2l8ox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/replacementobject%28for%3A%29-2l8ox.json'
content_hash: 'sha256:577d3c52ecec8a17'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# replacementObject(for:)

<sub>实例方法</sub>

由子类重写，以便在编码期间用另一个对象替换自身。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacementObject(for coder: NSCoder) -> Any?
```

## 参数

- `coder` — The coder encoding the receiver.

## 返回值

代替接收者进行编码的对象（若不同）。

## 讨论

对象可能会将自身编码到归档中，但若为分发而编码，则编码自身的代理。此方法由 `NSCoder` 调用。`NSObject` 的实现返回 `self`。

## 另请参阅

### 归档

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — 由子类重写，以便用另一个对象替换已解码并随后收到此消息的对象。
- [classForArchiver](classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — 重写以返回在对象的类不可用时可用于解码对象的类名。
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间替换为新类。
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。 _(已废弃)_
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ setVersion:](<setversion(__).md>) — 设置接收者的版本号。
- [+ version](<version().md>) — 返回分配给该类的版本号。
