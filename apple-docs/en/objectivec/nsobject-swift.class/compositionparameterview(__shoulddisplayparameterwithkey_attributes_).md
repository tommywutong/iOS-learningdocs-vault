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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# compositionParameterView(_:shouldDisplayParameterWithKey:attributes:)

<sub>Instance Method</sub>

Allows you to define which composition parameters are visible in the user interface when the composition parameter view refreshes.

> [!warning] Deprecated
> QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

<sub>macOS</sub>

```swift
func compositionParameterView(_ parameterView: QCCompositionParameterView!, shouldDisplayParameterWithKey portKey: String!, attributes portAttributes: [AnyHashable : Any]! = [:]) -> Bool
```

## Parameters

- `parameterView` — The composition parameter view in which the selection changed.

- `portKey` — A key for one of the composition parameters, which is provided to you by the Quartz Composer engine.

- `portAttributes` — A dictionary of the attributes that you want to display in the user interface.

## Return Value

Return[YES](../yes.md) if the port attributes should be displayed; [NO](../no.md) otherwise.
