---
title: 'accessibilitySetOverrideValue(_:forAttribute:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.1+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue%28_%3Aforattribute%3A%29.json'
content_hash: 'sha256:08bdacb981f2eb4a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilitySetOverrideValue(_:forAttribute:)

<sub>实例方法</sub>

覆盖接收者中的指定属性（若不存在则添加），并将其值设置为指定值。

> [!warning] 已废弃
> 请改用 [NSAccessibilityProtocol](../../appkit/nsaccessibilityprotocol.md)。

<sub>macOS</sub>

```swift
func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: NSAccessibility.Attribute) -> Bool
```

## 参数

- `value` — 要设置的属性值。

- `attribute` — 属性名称。属性名称列表参见 [NSAccessibility](../../appkit/nsaccessibility.md) 常量。

## 返回值

如果覆盖成功，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

此方法用于更改实例上的属性集，可作为子类化的替代方案。

此方法仅适用于其类已实现 `NSAccessibility` 协议的对象。如果对象已支持指定属性，则此方法指定的值优先。

如果指定属性不存在，则会在 `NSAccessibility` 协议之外创建它，因此 `accessibilityAttributeNames` 仍返回不包含新属性的旧列表。同样，`accessibilityAttributeValue` 不会返回覆盖过程创建的属性，也不会返回它们被覆盖后的值。

被覆盖属性的值不能由辅助功能客户端设置。

如果需要撤销使用此方法的效果，请再次调用它，并为 value 传入 `nil`。

确保在表示用户界面元素的实际对象上调用此方法。例如，对于 `NSButton`，应使用底层的 `NSButtonCell` 对象。`NSButton` 本身会被辅助功能忽略。

此方法仅适用于表示单个用户界面元素的对象。例如，当单个对象表示多个用户界面元素时不能使用它，例如 `NSSegmentedCell` 只有一个对象，却为每个分段提供用户界面元素。

## 另请参阅

### 已废弃的方法

- [- accessibilityAttributeNames](<accessibilityattributenames().md>) — 返回接收者支持的属性名称数组。 _(已废弃)_
- [- accessibilityAttributeValue:](<accessibilityattributevalue(__).md>) — 返回接收者中指定属性的值。 _(已废弃)_
- [- accessibilityAttributeValue:forParameter:](<accessibilityattributevalue(__forparameter_).md>) — 返回接收者中与指定属性名和参数对应的参数化属性值。 _(已废弃)_
- [- accessibilityActionDescription:](<accessibilityactiondescription(__).md>) — 返回指定操作的本地化描述。 _(已废弃)_
- [- accessibilityActionNames](<accessibilityactionnames().md>) — 返回辅助功能元素支持的操作名称数组。 _(已废弃)_
- [- accessibilityArrayAttributeCount:](<accessibilityarrayattributecount(__).md>) — 返回指定辅助功能数组属性的计数。 _(已废弃)_
- [- accessibilityArrayAttributeValues:index:maxCount:](<accessibilityarrayattributevalues(__index_maxcount_).md>) — 返回辅助功能数组属性的值的子数组。 _(已废弃)_
- [- accessibilityIndexOfChild:](<accessibilityindex(ofchild_).md>) — 返回指定辅助功能子项在父项中的索引。 _(已废弃)_
- [- accessibilityIsAttributeSettable:](<accessibilityisattributesettable(__).md>) — 返回一个布尔值，指示接收者中指定属性的值是否可设置。 _(已废弃)_
- [- accessibilityIsIgnored](<accessibilityisignored().md>) — 返回一个布尔值，指示在父子辅助功能层次结构中是否应忽略接收者。 _(已废弃)_
- [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>) — 返回接收者支持的参数化属性名称列表。 _(已废弃)_
- [- accessibilityPerformAction:](<accessibilityperformaction(__).md>) — 执行与指定操作关联的操作。 _(已废弃)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — 将接收者中指定属性的值设置为指定值。 _(已废弃)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — 当复制、移动、移除或链接文件或目录时，`NSFileManager` 对象每遇到一个错误就会向其处理程序发送此消息。 _(已废弃)_
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — `NSFileManager` 对象在尝试移动、复制、重命名或删除之前，或在尝试链接到给定路径之前，立即向处理程序发送此消息。 _(已废弃)_
