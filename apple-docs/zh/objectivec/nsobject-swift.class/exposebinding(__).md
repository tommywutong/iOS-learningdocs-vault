---
title: 'exposeBinding(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/exposebinding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposebinding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/exposebinding%28_%3A%29.json'
content_hash: 'sha256:0152f5ede78b518d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# exposeBinding(_:)

<sub>类型方法</sub>

公开指定的 `binding`，宣告其可用性。

<sub>macOS</sub>

```swift
class func exposeBinding(_ binding: NSBindingName)
```

## 参数

- `binding` — 要公开的属性的键路径。

## 讨论

将使用符合键值编码的方法访问绑定属性。此方法通常在类的 `initialize` 实现中调用。

使用 `exposeBinding` 公开的绑定会自动在 [exposedBindings](exposedbindings.md) 中公开，除非该方法显式将其过滤掉（例如在子类中）。

## 另请参阅

### 公开绑定

- [exposedBindings](exposedbindings.md) — 返回包含接收者所公开绑定的数组。
