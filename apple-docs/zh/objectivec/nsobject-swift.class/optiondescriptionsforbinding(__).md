---
title: 'optionDescriptionsForBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/optiondescriptionsforbinding%28_%3A%29.json'
content_hash: 'sha256:f4099ae0f68c7369'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# optionDescriptionsForBinding(_:)

<sub>实例方法</sub>

返回描述指定绑定选项的数组。

<sub>macOS</sub>

```swift
func optionDescriptionsForBinding(_ binding: NSBindingName) -> [NSAttributeDescription]
```

## 参数

- `binding` — The name of a binding

## 返回值

返回描述 `binding` 选项的 [NSAttributeDescription](../../coredata/nsattributedescription.md) 数组。

## 讨论

数组中的 [NSAttributeDescription](../../coredata/nsattributedescription.md) 实例由 Interface Builder 用于构建绑定检查器的选项编辑器用户界面。

- 绑定检查器中为选项显示的选项名称基于 [NSAttributeDescription](../../coredata/nsattributedescription.md) 方法 [name](../../coredata/nspropertydescription/name.md) 的值。
- 绑定检查器中为选项显示的编辑器类型基于 [NSAttributeDescription](../../coredata/nsattributedescription.md) 方法 [attributeType](../../coredata/nsattributedescription/attributetype-swift.property.md) 的值。
- 绑定检查器中为选项显示的默认值基于 [NSAttributeDescription](../../coredata/nsattributedescription.md) 方法 [defaultValue](../../coredata/nsattributedescription/defaultvalue.md) 的值。

## 另请参阅

### 管理绑定

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — 返回将为指定绑定返回的值的类。
- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — 在接收者的给定属性与由给定键路径指定的给定对象的属性之间建立绑定。
- [- infoForBinding:](<infoforbinding(__).md>) — 返回描述接收者 `binding` 的字典。
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — 移除接收者与控制器之间的给定绑定。
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — 测试给定对象是否为用于指示与键相关的选择状态的特殊标记对象。
