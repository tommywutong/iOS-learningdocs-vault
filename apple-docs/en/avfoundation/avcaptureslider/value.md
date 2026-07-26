---
title: value
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureslider/value
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider/value.json'
content_hash: 'sha256:e3e023383a1952f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSlider](../avcaptureslider.md)

# value

<sub>Instance Property</sub>

The current value of the slider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var value: Float { get set }
```

## Discussion

The default value is the slider’s minimum value. You may set a value only if it’s within the slider’s minimum and maximum values, otherwise the system throws an exception.

> [!important] Important
> Only modify a slider’s value from the same dispatch queue that you specified in the control’s [setActionQueue:action:](setactionqueue_action_.md) method.

## See Also

### Accessing the control value

- [prominentValues](prominentvalues-199dz.md) — Values in this array may receive unique visual representations or behaviors.
- [localizedValueFormat](localizedvalueformat.md) — A localized string that defines the presentation of the slider’s value.
