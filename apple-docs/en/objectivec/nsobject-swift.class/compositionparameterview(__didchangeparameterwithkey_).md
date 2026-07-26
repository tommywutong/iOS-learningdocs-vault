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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionParameterView(_:didChangeParameterWithKey:)

<sub>Instance Method</sub>

Called after an input parameter in the composition parameter view has been edited.

> [!warning] Deprecated
> QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
func compositionParameterView(_ parameterView: QCCompositionParameterView!, didChangeParameterWithKey portKey: String!)
```

## Parameters

- `parameterView` — The composition parameter view in which the parameter changed.

- `portKey` — A key for one of the composition parameters, which is provided to you by the Quartz Composer engine.
