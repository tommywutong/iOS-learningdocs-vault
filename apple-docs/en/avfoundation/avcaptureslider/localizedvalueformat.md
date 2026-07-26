---
title: localizedValueFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureslider/localizedvalueformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/localizedvalueformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/localizedvalueformat.json'
content_hash: 'sha256:023fadf5f54130a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# localizedValueFormat

<sub>Instance Property</sub>

A localized string that defines the presentation of the slider’s value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var localizedValueFormat: String? { get set }
```

## Discussion

Specify a format string to modify the presentation of a slider’s value. The format string may only contain `%@` and no other placeholders like `%d`, `%s`, and so on. Setting an Invalid format string results in the value’s default presentation.

Examples of valid format strings are:

- “%@%” for “40%”
- “%@ fps” for “60 fps”
- “+ %@” for “+ 20”

## See Also

### Accessing the control value

- [value](value.md) — The current value of the slider.
- [prominentValues](prominentvalues-199dz.md) — Values in this array may receive unique visual representations or behaviors.
