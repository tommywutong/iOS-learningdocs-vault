---
title: 'namesOfPromisedFilesDropped(atDestination:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped(atdestination:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped(atdestination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped%28atdestination%3A%29.json'
content_hash: 'sha256:ea8a6658fa9c1fb4'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# namesOfPromisedFilesDropped(atDestination:)

<sub>实例方法</sub>

返回接收者承诺在指定位置创建的文件的名称。

> [!warning] 已废弃
> Use NSFilePromiseProvider objects instead

<sub>macOS</sub>

```swift
func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?
```

## 参数

- `dropDestination` — 标识将创建承诺文件的位置的 URL 对象。

## 返回值

接收者承诺在 `dropDestination` 创建的文件名称（非完整路径）的数组。

## 讨论

当放置已被目标接受，并且目标（对于另一个 Cocoa 应用程序）调用 NSDraggingInfo 方法 [namesOfPromisedFilesDropped(atDestination:)](<../../appkit/nsdragginginfo/namesofpromisedfilesdropped(atdestination_).md>) 时，会调用此方法。对于长时间操作，你可以缓存 `dropDestination` 并将文件创建推迟到 `draggedImage:endedAt:operation:` 方法，以避免阻塞目标应用程序。

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
