---
title: classForPortCoder
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/classforportcoder
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classforportcoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classforportcoder.json'
content_hash: 'sha256:87357ec71e1959cb'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classForPortCoder

<sub>实例属性</sub>

在分布式编码中用于替代接收者的类。

<sub>Mac Catalyst, macOS</sub>

```objc
@property (readonly) Class classForPortCoder;
```

## 讨论

此属性允许针对分布式对象的专用行为——请重写 [classForCoder](classforcoder.md) 以添加通用编码行为。

## 另请参阅

### 相关文档

- [replacementObjectForPortCoder:](replacementobjectforportcoder_.md) — 由子类重写，以便在分布式编码期间用另一对象或其副本替代自身。（已废弃） _(已废弃)_

### 归档

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — 由子类重写，以便用另一对象替代已解码并随后收到此消息的对象。
- [classForArchiver](classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classFallbacksForKeyedArchiver](<classfallbacksforkeyedarchiver().md>) — 重写以返回在对象的类不可用时可用于解码对象的类名。
- [+ classForKeyedUnarchiver](<classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间用新类替代。
- [- replacementObjectForArchiver:](<replacementobject(for_)-8ih2x.md>) — 由子类重写，以便在归档期间用另一对象替代自身。（已废弃） _(已废弃)_
- [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) — 由子类重写，以便在编码期间用另一对象替代自身。
- [- replacementObjectForKeyedArchiver:](<replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ setVersion:](<setversion(__).md>) — 设置接收者的版本号。
- [+ version](<version().md>) — 返回分配给该类的版本号。
