---
title: 'awakeAfter(using:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/awakeafter(using:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/awakeafter(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/awakeafter%28using%3A%29.json'
content_hash: 'sha256:25c4c794cf1a794d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# awakeAfter(using:)

<sub>实例方法</sub>

由子类重写，以便用另一个对象替换已解码并随后收到此消息的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func awakeAfter(using coder: NSCoder) -> Any?
```

## 参数

- `coder` — The decoder used to decode the receiver.

## 返回值

接收者，或用于替换已解码并随后收到此消息的对象的另一个对象。

## 讨论

你可以使用此方法消除由编码器创建的冗余对象。例如，若在解码对象后发现已存在等效对象，则可以返回现有对象。若返回替换对象，则你的重写方法负责释放接收者。

此方法由 `NSCoder` 调用。`NSObject` 的实现仅返回 `self`。

## 另请参阅

### 相关文档

- [init(coder:)](<../../foundation/nscoding/init(coder_).md>) — 根据给定解档器中的数据初始化接收者。

### 归档

- [classForArchiver](classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — 重写以返回在对象的类不可用时可用于解码对象的类名。
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间替换为新类。
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。 _(已废弃)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ setVersion:](<setversion(__).md>) — 设置接收者的版本号。
- [+ version](<version().md>) — 返回分配给该类的版本号。
