---
title: 'eraseProgressPanel(_:eraseDidFinish:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/eraseprogresspanel(_:erasedidfinish:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspanel(_:erasedidfinish:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/eraseprogresspanel%28_%3Aerasedidfinish%3A%29.json'
content_hash: 'sha256:fadc1e63aae91d11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# eraseProgressPanel(_:eraseDidFinish:)

<sub>Instance Method</sub>

Notification sent by the panel before display.

<sub>macOS</sub>

```swift
func eraseProgressPanel(_ theErasePanel: DREraseProgressPanel!, eraseDidFinish erase: DRErase!) -> Bool
```

## Parameters

- `theErasePanel` — The progress panel

- `erase` — The object that performed the erase.

## Discussion

This method allows the delegate to handle or modify the end-of-burn feedback performed by the progress panel. Return `YES` to indicate the delegate handled the burn completion and the standard feedback should be supressed. If this method returns `NO`, the normal end-of-burn handling is performed (displaying an error if appropriate, playing an “I’m done” sound, etc).

The delegate is messaged before the progress panel is ordered out so a sheet may be displayed on a progress panel displayed as a window.
