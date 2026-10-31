---
title: 'fontManager(_:willIncludeFont:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/fontmanager(_:willincludefont:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/fontmanager(_:willincludefont:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/fontmanager%28_%3Awillincludefont%3A%29.json'
content_hash: 'sha256:8bc80208113e50c6'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# fontManager(_:willIncludeFont:)

<sub>实例方法</sub>

请求“字体”面板委托允许在“字体”面板中显示给定字体名称。

> [!warning] 已废弃
> 使用 [NSFontCollection](../../appkit/nsfontcollection.md) 提供过滤后的字体列表。

<sub>macOS</sub>

```swift
func fontManager(_ sender: Any, willIncludeFont fontName: String) -> Bool
```

## 参数

- `sender` — The font manager making the request.

- `fontName` — 要显示的字体的完整 PostScript 名称，例如 Helvetica-BoldOblique 或 Helvetica-Narrow-Bold。

## 返回值

若“字体”面板委托返回 [YES](../yes.md)，则列出 `fontName`；若委托返回 [NO](../no.md)，则不列出。

## 讨论

在 macOS 10.2 及更早版本中，每当“字体”面板需要更新时（例如首次加载“字体”面板时，以及用户选择系列名称以查看该系列中有哪些可用字样时），都会根据需要反复调用此方法。你的实现应相当快速地执行，以确保“字体”面板的响应性。

> [!important] 重要
> 在 macOS 10.3 及更高版本中不会调用此委托方法。

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
- [- accessibilitySetOverrideValue:forAttribute:](<accessibilitysetoverridevalue(__forattribute_).md>) — 覆盖接收者中的指定属性（若不存在则添加），并将其值设置为指定值。 _(已废弃)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — 将接收者中指定属性的值设置为指定值。 _(已废弃)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — 当复制、移动、移除或链接文件或目录时，`NSFileManager` 对象每遇到一个错误就会向其处理程序发送此消息。 _(已废弃)_
