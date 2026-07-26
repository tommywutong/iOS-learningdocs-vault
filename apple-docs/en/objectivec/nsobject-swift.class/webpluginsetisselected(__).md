---
title: 'webPlugInSetIsSelected(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webpluginsetisselected(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginsetisselected(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginsetisselected%28_%3A%29.json'
content_hash: 'sha256:6c0a89ba074dac46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInSetIsSelected(_:)

<sub>Instance Method</sub>

Controls plug-in behavior based on its selection.

<sub>macOS</sub>

```swift
func webPlugInSetIsSelected(_ isSelected: Bool)
```

## Parameters

- `isSelected` — If [YES](../yes.md), the plug-in is currently selected. Otherwise, it is not selected.

## Discussion

This may be used, for example, to change the plug-in’s appearance when it is selected by the user.
