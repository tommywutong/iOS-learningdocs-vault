---
title: 'compositionParameterView(_:shouldDisplayParameterWithKey:attributes:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/compositionparameterview(_:shoulddisplayparameterwithkey:attributes:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionparameterview(_:shoulddisplayparameterwithkey:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/compositionparameterview%28_%3Ashoulddisplayparameterwithkey%3Aattributes%3A%29.json'
content_hash: 'sha256:ec60574b3aa30d30'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionParameterView(_:shouldDisplayParameterWithKey:attributes:)

<sub>实例方法</sub>

允许你定义在合成参数视图刷新时，哪些合成参数在用户界面中可见。

> [!warning] 已废弃
> QuartzComposer API 已废弃。（定义 QC_SILENCE_DEPRECATION 可消除这些警告）

<sub>macOS</sub>

```swift
func compositionParameterView(_ parameterView: QCCompositionParameterView!, shouldDisplayParameterWithKey portKey: String!, attributes portAttributes: [AnyHashable : Any]! = [:]) -> Bool
```

## 参数

- `parameterView` — 选择发生更改的合成参数视图。

- `portKey` — 其中一个合成参数的键，由 Quartz Composer 引擎提供给你。

- `portAttributes` — 要在用户界面中显示的属性字典。

## 返回值

若应显示端口属性则返回[YES](../yes.md)；否则返回 [NO](../no.md)。
