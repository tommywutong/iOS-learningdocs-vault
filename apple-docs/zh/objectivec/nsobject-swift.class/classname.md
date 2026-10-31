---
title: className
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classname
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classname.json'
content_hash: 'sha256:0a9801ecc819005f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# className

<sub>实例属性</sub>

包含类名的字符串。

<sub>Mac Catalyst, macOS</sub>

```swift
var className: String { get }
```

## 另请参阅

### 脚本

- [classCode](classcode.md) — 接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — 通过拷贝传入的值并设置可选属性字典中的属性，创建并返回一个或多个要插入到指定关系中的脚本对象。
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — 创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由键标识的关系中。
- [scriptingProperties](scriptingproperties.md) — 以 `NSString` 为键的接收者可脚本化属性字典。
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — 给定对象说明符，返回接收容器中指定的一个或多个对象。
