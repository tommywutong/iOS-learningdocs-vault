---
title: 'compositionParameterView(_:didChangeParameterWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/compositionparameterview(_:didchangeparameterwithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionparameterview(_:didchangeparameterwithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/compositionparameterview%28_%3Adidchangeparameterwithkey%3A%29.json'
content_hash: 'sha256:aec8f5a05004a5e8'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionParameterView(_:didChangeParameterWithKey:)

<sub>实例方法</sub>

在合成参数视图中的输入参数被编辑后调用。

> [!warning] 已废弃
> QuartzComposer API 已废弃。（定义 QC_SILENCE_DEPRECATION 可消除这些警告）

<sub>macOS</sub>

```swift
func compositionParameterView(_ parameterView: QCCompositionParameterView!, didChangeParameterWithKey portKey: String!)
```

## 参数

- `parameterView` — 发生参数更改的合成参数视图。

- `portKey` — 其中一个合成参数的键，由 Quartz Composer 引擎提供给你。
