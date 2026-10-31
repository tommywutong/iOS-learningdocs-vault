---
title: 'unbind(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/unbind(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/unbind(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/unbind%28_%3A%29.json'
content_hash: 'sha256:cef5734e54ec1fd3'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# unbind(_:)

<sub>实例方法</sub>

移除接收者与控制器之间的给定绑定。

<sub>macOS</sub>

```swift
func unbind(_ binding: NSBindingName)
```

## 参数

- `binding` — 绑定的名称。

## 另请参阅

### 管理绑定

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — 返回将为指定绑定返回的值的类。
- [- bind:toObject:withKeyPath:options:](<bind(__to_withkeypath_options_).md>) — 在接收者的给定属性与由给定键路径指定的给定对象的属性之间建立绑定。
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — 返回描述指定绑定选项的数组。
- [- infoForBinding:](<infoforbinding(__).md>) — 返回描述接收者 `binding` 的字典。
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — 测试给定对象是否为用于指示与键相关的选择状态的特殊标记对象。
