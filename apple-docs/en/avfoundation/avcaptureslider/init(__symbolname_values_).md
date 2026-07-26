---
title: 'init(_:symbolName:values:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureslider/init(_:symbolname:values:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/init(_:symbolname:values:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/init%28_%3Asymbolname%3Avalues%3A%29.json'
content_hash: 'sha256:93856bc0503d7add'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# init(_:symbolName:values:)

<sub>Initializer</sub>

Creates a discrete slider control that selects a value from a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc convenience init(_ localizedTitle: String, symbolName: String, values: [Float])
```

## Parameters

- `localizedTitle` — A localized title that describes the slider’s action.

- `symbolName` — A symbol name from the SF Symbols library.

- `values` — An array of floating-point values.

## Discussion

Use discrete sliders when your app supports selecting from a specific list of values.

## See Also

### Creating a slider

- [init(_:symbolName:in:)](<init(__symbolname_in_).md>) — Creates a continuous slider control that selects a value from a bounded range.
- [init(_:symbolName:in:step:)](<init(__symbolname_in_step_).md>) — Creates a discrete slider control that selects a stepped value from a bounded range.
