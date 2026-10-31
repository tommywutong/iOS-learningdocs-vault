---
title: 'newScriptingObject(of:forValueForKey:withContentsValue:properties:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/newscriptingobject(of:forvalueforkey:withcontentsvalue:properties:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/newscriptingobject(of:forvalueforkey:withcontentsvalue:properties:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/newscriptingobject%28of%3Aforvalueforkey%3Awithcontentsvalue%3Aproperties%3A%29.json'
content_hash: 'sha256:19988a270bf45e4d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# newScriptingObject(of:forValueForKey:withContentsValue:properties:)

<sub>实例方法</sub>

创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由该键标识的关系中。

<sub>macOS</sub>

```swift
func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties: [String : Any]) -> Any?
```

## 参数

- `objectClass` — 要创建的可脚本化对象的类。

- `key` — 标识要将新的类对象插入其中的关系的键。

- `contentsValue` — 指定要创建的对象的内容。可以为 `nil`。（另请参阅“讨论”部分。）

- `properties` — 要在新对象中设置的属性。（另请参阅“讨论”部分。）

## 返回值

新对象。若发生错误则返回 `nil`。

## 讨论

你可以重写 `newScriptingObjectOfClass` 方法，以便在应用程序收到 `make` 命令时获得更多控制。此方法在新对象的预期容器上调用。`contentsValue` 和 `properties` 派生自 `make` 命令的 `with contents` 和 `with properties` 参数。然后使用键值编码将返回的一个或多个对象插入容器。

当 Cocoa 调用此方法时，内容值和属性都尚未使用 `NSScriptKeyValueCoding` 方法 [- coerceValue:forKey:](<coercevalue(__forkey_).md>) 进行强制转换。不过，对于 sdef 声明的脚本能力，传入对象的类型会可靠地匹配相关的 sdef 声明。

此方法的默认实现通过向类发送 `alloc` 并向结果对象发送 `init` 来创建新的脚本对象。在这还不够的情况下（例如在 Core Data 应用程序中，新对象必须使用 `[NSManagedObject initWithEntity:insertIntoManagedObjectContext:]` 初始化），请重写此方法。

## 另请参阅

### 脚本

- [classCode](classcode.md) — 接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。
- [className](classname.md) — 包含类名的字符串。
- [- copyScriptingValue:forKey:withProperties:](<copyscriptingvalue(__forkey_withproperties_).md>) — 通过拷贝传入的值并设置拷贝对象中的属性，创建并返回一个或多个要插入到指定关系中的脚本对象。
- [scriptingProperties](scriptingproperties.md) — 以 `NSString` 为键的接收者可脚本化属性字典。
- [- scriptingValueForSpecifier:](<scriptingvalue(for_).md>) — 给定对象说明符，返回接收容器中指定的一个或多个对象。
