---
title: 'valueClassForBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/valueclassforbinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/valueclassforbinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/valueclassforbinding%28_%3A%29.json'
content_hash: 'sha256:575494828fd222df'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# valueClassForBinding(_:)

<sub>实例方法</sub>

返回将为指定绑定返回的值的类。

<sub>macOS</sub>

```swift
func valueClassForBinding(_ binding: NSBindingName) -> AnyClass?
```

## 参数

- `binding` — 绑定的名称。

## 返回值

将为 `binding` 返回的值的类。

## 讨论

Interface Builder 使用此方法来确定绑定的适当转换器。

Implementation of this method is optional.

## 另请参阅

### 管理绑定

- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — 在接收者的给定属性与由给定键路径指定的给定对象的属性之间建立绑定。
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — 返回描述指定绑定选项的数组。
- [- infoForBinding:](<infoforbinding(__).md>) — 返回描述接收者 `binding` 的字典。
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — 移除接收者与控制器之间的给定绑定。
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — 测试给定对象是否为用于指示与键相关的选择状态的特殊标记对象。
