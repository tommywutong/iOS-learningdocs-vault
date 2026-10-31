---
title: 'scriptingValue(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/scriptingvalue(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingvalue(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/scriptingvalue%28for%3A%29.json'
content_hash: 'sha256:9af75f6339bdb279'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# scriptingValue(for:)

<sub>实例方法</sub>

给定对象说明符，返回接收容器中的指定一个或多个对象。

<sub>macOS</sub>

```swift
func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?
```

## 参数

- `objectSpecifier` — An object specifier to be evaluated.

## 返回值

接收容器中的指定一个或多个对象。

## 讨论

根据对象说明符的类型，此方法可能成功返回对象、对象数组或 `nil`。由于 `nil` 是有效的返回值，失败通过在返回前调用对象说明符的 `setEvaluationError:` 方法来发出信号。

## 讨论

你可以重写此方法以自定义对象说明符的求值，而无需要求脚本容器为本身没有自然索引的所含对象编造索引（若你改为实现 [- indicesOfObjectsByEvaluatingObjectSpecifier:](<indicesofobjects(byevaluatingobjectspecifier_).md>)，则可能出现这种情况）。

你对此方法的重写不需要同时调用任何 `NSScriptCommand` 错误信号方法，不过可以调用以记录非常具体的信息。`NSUnknownKeySpecifierError` 和 `NSInvalidIndexSpecifierError` 编号很特殊，因为若遇到它们，Cocoa 可能会继续求值外部说明符，以便为脚本编写者提供便利。

## 另请参阅

### 脚本

- [classCode](classcode.md) — 接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。
- [className](classname.md) — 包含类名的字符串。
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — 通过拷贝传入的值并设置拷贝对象中的属性，创建并返回一个或多个要插入到指定关系中的脚本对象。
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — 创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由键标识的关系中。
- [scriptingProperties](scriptingproperties.md) — 以 `NSString` 为键的接收者可脚本化属性字典。
