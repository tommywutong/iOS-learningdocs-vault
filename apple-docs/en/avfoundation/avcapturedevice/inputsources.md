---
title: inputSources
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/inputsources
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/inputsources.json'
content_hash: 'sha256:de2182899e82c591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# inputSources

<sub>Instance Property</sub>

An array of input sources that the device supports.

<sub>macOS</sub>

```swift
var inputSources: [AVCaptureDevice.InputSource] { get }
```

## Discussion

Some devices can capture data from one of multiple data sources (different input jacks on the same audio device, for example). For devices with multiple possible data sources, you can use this property to enumerate the possible choices.

This value is key-value observable.

## See Also

### Configuring input sources

- [activeInputSource](activeinputsource.md) — The currently active input source of the device.
- [InputSource](inputsource.md) — A distinct input source on a capture device.
