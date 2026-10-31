---
title: version()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/version()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/version()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/version%28%29.json'
content_hash: 'sha256:490dffe75d80b481'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# version()

<sub>类型方法</sub>

返回分配给该类的版本号。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func version() -> Int
```

## 返回值

The version number assigned to the class.

## 讨论

若未设置版本，则默认为 `0`。

解码或解档需要版本号，以便可以检测并正确解码对象的较旧版本。

在 `NSCoding` 协议或其他方法中获取版本时应谨慎。获取类版本号时请显式使用类名：

```objc
version = [MyClass version];
```

不要简单地向 class 的返回值发送 `version`——可能会返回子类版本号。

### 特殊注意事项

版本号适用于 `NSArchiver`/`NSUnarchiver`，但不适用于 `NSKeyedArchiver`/`NSKeyedUnarchiver`。键控归档器不编码类版本号。

## 另请参阅

### 相关文档

- [version(forClassName:)](<../../foundation/nscoder/version(forclassname_).md>) — 此方法因历史原因而存在，不与键控归档器一起使用。

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
- [+ setVersion:](<setversion(__).md>) — 设置接收者的版本号。
