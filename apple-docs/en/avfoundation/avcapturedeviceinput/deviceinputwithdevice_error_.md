---
title: 'deviceInputWithDevice:error:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedeviceinput/deviceinputwithdevice:error:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/deviceinputwithdevice:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/deviceinputwithdevice%3Aerror%3A.json'
content_hash: 'sha256:29a87ddbd2eb810a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# deviceInputWithDevice:error:

<sub>Type Method</sub>

Returns a new input for the specified capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) deviceInputWithDevice:(AVCaptureDevice *) device error:(NSError **) outError;
```

## Parameters

- `device` — The device from which to capture input.

- `outError` — If an error occurs during initialization, upon return contains an `NSError` object describing the problem.

## Return Value

A new capture input.

## See Also

### Creating an input

- [- initWithDevice:error:](<init(device_).md>) — Creates an input for the specified capture device.
