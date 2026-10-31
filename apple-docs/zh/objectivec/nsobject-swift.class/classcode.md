---
title: classCode
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classcode
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classcode.json'
content_hash: 'sha256:321f9f1284fbb5e1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classCode

<sub>实例属性</sub>

接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。

<sub>Mac Catalyst, macOS</sub>

```swift
var classCode: FourCharCode { get }
```

## 讨论

Cocoa 的脚本支持类使用此属性。

## 另请参阅

### 脚本

- [className](classname.md) — 包含类名的字符串。
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — 通过拷贝传入的值并设置可选属性字典中的属性，创建并返回一个或多个要插入到指定关系中的脚本对象。
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — 创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由键标识的关系中。
- [scriptingProperties](scriptingproperties.md) — 以 `NSString` 为键的接收者可脚本化属性字典。
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — 给定对象说明符，返回接收容器中指定的一个或多个对象。
