---
title: scriptingProperties
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/scriptingproperties
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/scriptingproperties.json'
content_hash: 'sha256:05969da5ad5b9a94'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# scriptingProperties

<sub>实例属性</sub>

以 `NSString` 为键的接收者可脚本化属性字典。

<sub>Mac Catalyst, macOS</sub>

```swift
var scriptingProperties: [String : Any]? { get set }
```

## 讨论

以 `NSString` 为键的接收者可脚本化属性字典，包括在该类及其脚本超类的 `.scriptSuite` 属性列表条目中声明为 Attributes 和 ToOneRelationships 的全部属性，但以“scriptingProperties”为键的除外。字典中的每个键必须与 Attribute 或 ToOneRelationship 的键相同。字典的值必须是可转换为 `NSAppleEventDescriptor` 对象的 Objective-C 对象。

## 另请参阅

### 脚本

- [classCode](classcode.md) — 接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。
- [className](classname.md) — 包含类名的字符串。
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — 通过拷贝传入的值并设置拷贝对象中的属性，创建并返回一个或多个要插入到指定关系中的脚本对象。
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — 创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由键标识的关系中。
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — 给定对象说明符，返回接收容器中指定的一个或多个对象。
