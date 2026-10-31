---
title: 'accessibilityIsAttributeSettable(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.1+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilityisattributesettable(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityisattributesettable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityisattributesettable%28_%3A%29.json'
content_hash: 'sha256:a76c4140f2dfdbf1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityIsAttributeSettable(_:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者中指定属性的值是否可设置。

> [!warning] 已废弃
> 请改用 [NSAccessibilityProtocol](../../appkit/nsaccessibilityprotocol.md)。

<sub>macOS</sub>

```swift
func accessibilityIsAttributeSettable(_ attribute: NSAccessibility.Attribute) -> Bool
```

## 参数

- `attribute` — 属性名称。属性名称列表参见 [NSAccessibility](../../appkit/nsaccessibility.md) 常量。

## 返回值

如果指定属性可设置，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

用户界面类必须实现此方法。若子类未实现 `attribute`，应在超类实现存在时调用它。

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
- [- accessibilityIsIgnored](<accessibilityisignored().md>) — 返回一个布尔值，指示在父子辅助功能层次结构中是否应忽略接收者。 _(已废弃)_
- [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>) — 返回接收者支持的参数化属性名称列表。 _(已废弃)_
- [- accessibilityPerformAction:](<accessibilityperformaction(__).md>) — 执行与指定操作关联的操作。 _(已废弃)_
- [- accessibilitySetOverrideValue:forAttribute:](<accessibilitysetoverridevalue(__forattribute_).md>) — 覆盖接收者中的指定属性（若不存在则添加），并将其值设置为指定值。 _(已废弃)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — 将接收者中指定属性的值设置为指定值。 _(已废弃)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — 当复制、移动、移除或链接文件或目录时，`NSFileManager` 对象每遇到一个错误就会向其处理程序发送此消息。 _(已废弃)_
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — `NSFileManager` 对象在尝试移动、复制、重命名或删除之前，或在尝试链接到给定路径之前，立即向处理程序发送此消息。 _(已废弃)_
