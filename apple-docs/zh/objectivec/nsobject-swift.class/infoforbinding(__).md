---
title: 'infoForBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/infoforbinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/infoforbinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/infoforbinding%28_%3A%29.json'
content_hash: 'sha256:ebfaa4055bb4e67a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# infoForBinding(_:)

<sub>实例方法</sub>

返回描述接收者 `binding` 的字典。

<sub>macOS</sub>

```swift
func infoForBinding(_ binding: NSBindingName) -> [NSBindingInfoKey : Any]?
```

## 参数

- `binding` — 绑定的名称。

## 返回值

包含有关 `binding` 信息的字典；若绑定未绑定则为 `nil`。该字典包含三个键/值对：`NSObservedObjectKey`：绑定的对象，`NSObservedKeyPathKey`：绑定的键路径，`NSOptionsKey`：绑定的选项字典。

## 讨论

此方法主要供想要分析对象现有绑定的子类使用。

## 另请参阅

### 管理绑定

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — 返回将为指定绑定返回的值的类。
- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — 在接收者的给定属性与由给定键路径指定的给定对象的属性之间建立绑定。
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — 返回描述指定绑定选项的数组。
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — 移除接收者与控制器之间的给定绑定。
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — 测试给定对象是否为用于指示与键相关的选择状态的特殊标记对象。
