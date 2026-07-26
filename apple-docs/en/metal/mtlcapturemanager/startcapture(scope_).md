---
title: 'startCapture(scope:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.13+（10.15 起废弃）, tvOS 11.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlcapturemanager/startcapture(scope:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(scope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/startcapture%28scope%3A%29.json'
content_hash: 'sha256:12c4d2831e62ccb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# startCapture(scope:)

<sub>Instance Method</sub>

Starts capturing any of your app’s Metal commands that are in the specified capture scope.

> [!warning] Deprecated
> Use [- startCaptureWithDescriptor:error:](<startcapture(with_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startCapture(scope captureScope: any MTLCaptureScope)
```

## Parameters

- `captureScope` — The capture scope to use.

## See Also

### Starting capture

- [- startCaptureWithDescriptor:error:](<startcapture(with_).md>) — Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [- startCaptureWithDevice:](<startcapture(device_).md>) — Starts capturing any of your app’s Metal commands that are executed by the device object. _(deprecated)_
- [- startCaptureWithCommandQueue:](<startcapture(commandqueue_).md>) — Starts capturing any of your app’s Metal commands that are executed by the command queue. _(deprecated)_
