---
title: 'init(_:symbolName:in:step:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureslider/init(_:symbolname:in:step:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/init(_:symbolname:in:step:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/init%28_%3Asymbolname%3Ain%3Astep%3A%29.json'
content_hash: 'sha256:067579e2cf4c2a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# init(_:symbolName:in:step:)

<sub>Initializer</sub>

Creates a discrete slider control that selects a stepped value from a bounded range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc convenience init(_ localizedTitle: String, symbolName: String, in range: ClosedRange<Float>, step: Float)
```

## Parameters

- `localizedTitle` — A localized title that describes the slider’s action.

- `symbolName` — A symbol name from the SF Symbols library.

- `range` — A bounded range of floating point values.

- `step` — The distance between each valid value. This specified value must be greater than `0` or the system throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md).

## Discussion

Use discrete sliders when your use case supports selecting stepped values within the specified range.

## See Also

### Creating a slider

- [init(_:symbolName:in:)](<init(__symbolname_in_).md>) — Creates a continuous slider control that selects a value from a bounded range.
- [init(_:symbolName:values:)](<init(__symbolname_values_).md>) — Creates a discrete slider control that selects a value from a list.
