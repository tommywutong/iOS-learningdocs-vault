---
title: 'init(_:symbolName:in:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureslider/init(_:symbolname:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/init(_:symbolname:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/init%28_%3Asymbolname%3Ain%3A%29.json'
content_hash: 'sha256:e980b7f81ed71d43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# init(_:symbolName:in:)

<sub>Initializer</sub>

Creates a continuous slider control that selects a value from a bounded range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc convenience init(_ localizedTitle: String, symbolName: String, in range: ClosedRange<Float>)
```

## Parameters

- `localizedTitle` — A localized title that describes the slider’s action.

- `symbolName` — A symbol name from the SF Symbols library.

- `range` — A bounded range of floating point values.

## Discussion

Use continuous sliders when your use case supports selecting any value in the specified range.

## See Also

### Creating a slider

- [init(_:symbolName:in:step:)](<init(__symbolname_in_step_).md>) — Creates a discrete slider control that selects a stepped value from a bounded range.
- [init(_:symbolName:values:)](<init(__symbolname_values_).md>) — Creates a discrete slider control that selects a value from a list.
