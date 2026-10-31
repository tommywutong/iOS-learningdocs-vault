---
title: 'fileManager(_:shouldProceedAfterError:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/filemanager(_:shouldproceedaftererror:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/filemanager(_:shouldproceedaftererror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/filemanager%28_%3Ashouldproceedaftererror%3A%29.json'
content_hash: 'sha256:51ad8a02f8dc2efc'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# fileManager(_:shouldProceedAfterError:)

<sub>实例方法</sub>

`NSFileManager` 对象在复制、移动、移除或链接文件或目录时遇到的每个错误都会向其处理程序发送此消息。

> [!warning] 已废弃
> 请参阅 copy、move、remove 和 link 方法的委托方法。

<sub>tvOS, visionOS, watchOS</sub>

```swift
func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool
```

## 参数

- `fm` — The file manager that sent this message.

- `errorInfo` — 包含与错误相关的两到三条信息（均为 [NSString](../../foundation/nsstring.md) 对象）的字典：| 键 | 值 | |---|---| | `@"Path"` | 与错误相关的路径（通常为源路径） | | `@"Error"` | 错误描述 | | `@"ToPath"` | 目标路径（并非所有错误都有） |

## 返回值

若操作（通常在循环内持续进行）应继续，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

每当 `NSFileManager` 对象 `manager` 在复制、移动、移除或链接文件或目录时遇到错误，都会发送此消息。返回值会回传给 [copyPath:toPath:handler:](../../foundation/nsfilemanager/copypath_topath_handler_.md)、[movePath:toPath:handler:](../../foundation/nsfilemanager/movepath_topath_handler_.md)、[removeFileAtPath:handler:](../../foundation/nsfilemanager/removefileatpath_handler_.md) 或 [linkPath:toPath:handler:](../../foundation/nsfilemanager/linkpath_topath_handler_.md) 的调用者。若发生错误且你的处理程序未实现此方法，则调用方法会自动返回 [NO](../no.md)。

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
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — `NSFileManager` 对象在尝试移动、复制、重命名或删除之前，或在尝试链接到给定路径之前，立即向处理程序发送此消息。 _(已废弃)_
