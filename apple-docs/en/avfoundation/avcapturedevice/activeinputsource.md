---
title: activeInputSource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activeinputsource
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeinputsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activeinputsource.json'
content_hash: 'sha256:700fe090b33b9048'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeInputSource

<sub>Instance Property</sub>

The currently active input source of the device.

<sub>macOS</sub>

```swift
var activeInputSource: AVCaptureDevice.InputSource? { get set }
```

## Discussion

You must call [- lockForConfiguration:](<lockforconfiguration().md>) before attempting to set a format. Setting a format that isn’t present in the [inputSources](inputsources.md) array results in an exception.

This property is key-value observable.

## See Also

### Configuring input sources

- [inputSources](inputsources.md) — An array of input sources that the device supports.
- [InputSource](inputsource.md) — A distinct input source on a capture device.
