---
title: accessibilityIsIgnored()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.1+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityisignored()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityisignored()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityisignored%28%29.json'
content_hash: 'sha256:313df10133cdd8c4'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityIsIgnored()

<sub>实例方法</sub>

返回一个布尔值，指示在父子辅助功能层次结构中是否应忽略接收者。

> [!warning] 已废弃
> 请改用 [NSAccessibilityProtocol](../../appkit/nsaccessibilityprotocol.md)。

<sub>macOS</sub>

```swift
func accessibilityIsIgnored() -> Bool
```

## 返回值

如果应忽略接收者，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

在请求对象的子项时，不要包含被忽略的子项；而是用它们自己未被忽略的子项替换被忽略的子项。在请求对象的父项时同样适用：跳过被忽略的父项，并将第一个未被忽略的祖先视为真正的父项。同样，当命中测试或焦点测试由被忽略的元素满足时，应改用该元素的第一个未被忽略的祖先（在某些情况下也可能是后代，例如单单元格控件）。

被忽略的元素可让你提供视图与对象所有权层次结构的简化版本。辅助功能客户端可以绕过中间对象，从而让用户更快访问真正的用户界面对象。例如，单单元格的 `NSControl` 对象会被忽略；可见的父子关系存在于该控件的父项（如果父项也被忽略，则为更高的祖先）与该控件的单元格之间。

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
- [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>) — 返回接收者支持的参数化属性名称列表。 _(已废弃)_
- [- accessibilityPerformAction:](<accessibilityperformaction(__).md>) — 执行与指定操作关联的操作。 _(已废弃)_
- [- accessibilitySetOverrideValue:forAttribute:](<accessibilitysetoverridevalue(__forattribute_).md>) — 覆盖接收者中的指定属性（若不存在则添加），并将其值设置为指定值。 _(已废弃)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — 将接收者中指定属性的值设置为指定值。 _(已废弃)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — 当复制、移动、移除或链接文件或目录时，`NSFileManager` 对象每遇到一个错误就会向其处理程序发送此消息。 _(已废弃)_
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — `NSFileManager` 对象在尝试移动、复制、重命名或删除之前，或在尝试链接到给定路径之前，立即向处理程序发送此消息。 _(已废弃)_
