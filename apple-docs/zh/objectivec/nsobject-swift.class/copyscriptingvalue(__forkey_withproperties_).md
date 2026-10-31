---
title: 'copyScriptingValue(_:forKey:withProperties:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/copyscriptingvalue(_:forkey:withproperties:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copyscriptingvalue(_:forkey:withproperties:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/copyscriptingvalue%28_%3Aforkey%3Awithproperties%3A%29.json'
content_hash: 'sha256:b2dca6349cfaf69a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# copyScriptingValue(_:forKey:withProperties:)

<sub>实例方法</sub>

通过复制传入的值并在复制的一个或多个对象中设置属性，创建并返回一个或多个要插入到指定关系中的脚本对象。

<sub>macOS</sub>

```swift
func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?
```

## 参数

- `value` — 要复制的一个或多个对象。类型必须与由 `key` 标识的属性的类型匹配。（另请参阅“讨论”部分。）例如，若属性是一对多关系，则 `value` 始终是要复制的对象数组，因此此方法也必须返回对象数组。

- `key` — 标识要将复制的一个或多个对象插入其中的关系的键。

- `properties` — 要在复制的一个或多个对象中设置的属性。派生自 `duplicate` 命令的 “with properties” 参数。（另请参阅“讨论”部分。）

## 返回值

复制的一个或多个对象。若发生错误则返回 `nil`。

## 讨论

你可以重写 `copyScriptingValue` 方法，以便在应用程序收到 `duplicate` 命令时获得更多控制。此方法在复制的一个或多个对象的预期容器上调用。`properties` 派生自 `duplicate` 命令的 `with properties` 参数。然后使用键值编码将返回的一个或多个对象插入容器。

当 Cocoa 调用此方法时，值和属性都尚未使用 `NSScriptKeyValueCoding` 方法 [- coerceValue:forKey:](<coercevalue(__forkey_).md>) 进行强制转换。不过，对于 sdef 声明的脚本能力，传入对象的类型会可靠地匹配相关的 sdef 声明。

此方法的默认实现通过向 `value` 指定的一个或多个对象发送 `copyWithZone:` 来复制脚本对象。在这还不够的情况下（例如在 Core Data 应用程序中，新对象必须使用 `[NSManagedObject initWithEntity:insertIntoManagedObjectContext:]` 初始化），请重写此方法。

## 另请参阅

### 脚本

- [classCode](classcode.md) — 接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。
- [className](classname.md) — 包含类名的字符串。
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — 创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由键标识的关系中。
- [scriptingProperties](scriptingproperties.md) — 以 `NSString` 为键的接收者可脚本化属性字典。
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — 给定对象说明符，返回接收容器中指定的一个或多个对象。
