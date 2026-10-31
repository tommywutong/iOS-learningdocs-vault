---
title: 'bind(_:to:withKeyPath:options:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/bind(_:to:withkeypath:options:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/bind(_:to:withkeypath:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/bind%28_%3Ato%3Awithkeypath%3Aoptions%3A%29.json'
content_hash: 'sha256:156f10fcaf707c2f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# bind(_:to:withKeyPath:options:)

<sub>实例方法</sub>

在接收者的给定属性与由给定键路径指定的给定对象的属性之间建立绑定。

<sub>macOS</sub>

```swift
func bind(_ binding: NSBindingName, to observable: Any, withKeyPath keyPath: String, options: [NSBindingOption : Any]? = nil)
```

## 参数

- `binding` — 接收者先前使用 [+ exposeBinding:](<exposebinding(__).md>) 方法公开的属性的键路径。

- `observable` — 绑定到的对象。

- `keyPath` — 从 `observableController` 可达的属性的键路径。路径中的元素必须符合键值观察（参见 [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)）。

- `options` — 包含绑定选项的字典，例如占位符对象或如 Constants 中所述的 `NSValueTransformer` 标识符。此值可选——传入 `nil` 表示无选项。

## 另请参阅

### 管理绑定

- [- valueClassForBinding:](<valueclassforbinding(__).md>) — 返回将为指定绑定返回的值的类。
- [- optionDescriptionsForBinding:](<optiondescriptionsforbinding(__).md>) — 返回描述指定绑定选项的数组。
- [- infoForBinding:](<infoforbinding(__).md>) — 返回描述接收者 `binding` 的字典。
- [NSBindingInfoKey](../../appkit/nsbindinginfokey.md)
- [- unbind:](<unbind(__).md>) — 移除接收者与控制器之间的给定绑定。
- [NSIsControllerMarker(_:)](<../../appkit/nsiscontrollermarker(__).md>) — 测试给定对象是否为用于指示与键相关的选择状态的特殊标记对象。
