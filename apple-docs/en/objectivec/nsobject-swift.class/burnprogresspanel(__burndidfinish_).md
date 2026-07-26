---
title: 'burnProgressPanel(_:burnDidFinish:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/burnprogresspanel(_:burndidfinish:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspanel(_:burndidfinish:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/burnprogresspanel%28_%3Aburndidfinish%3A%29.json'
content_hash: 'sha256:e13166c5ac6cbc9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# burnProgressPanel(_:burnDidFinish:)

<sub>Instance Method</sub>

Allows the delegate to handle the end-of-burn feedback.

<sub>macOS</sub>

```swift
func burnProgressPanel(_ theBurnPanel: DRBurnProgressPanel!, burnDidFinish burn: DRBurn!) -> Bool
```

## Parameters

- `theBurnPanel` — The progress panel

- `burn` — The object that performed the burn.

## Return Value

A `BOOL` indicating whether the normal end-of-burn feedback should occur.

## Discussion

This method allows the delegate to handle or modify the end-of-burn feedback performed by the progress panel. Return `YES` to indicate the delegate handled the burn completion and the standard feedback should be supressed. If this method returns `NO`, the normal end-of-burn handling is performed (displaying an error if appropriate, playing an “I’m done” sound, etc).

The delegate is messaged before the progress panel is ordered out so a sheet may be displayed on a progress panel displayed as a window.
