---
title: 'startCapture(commandQueue:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.13+（10.15 起废弃）, tvOS 11.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlcapturemanager/startcapture(commandqueue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/startcapture(commandqueue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/startcapture%28commandqueue%3A%29.json'
content_hash: 'sha256:fc825138ee8b0dc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# startCapture(commandQueue:)

<sub>Instance Method</sub>

Starts capturing any of your app’s Metal commands that are executed by the command queue.

> [!warning] Deprecated
> Use [- startCaptureWithDescriptor:error:](<startcapture(with_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startCapture(commandQueue: any MTLCommandQueue)
```

## Parameters

- `commandQueue` — The command queue whose commands you want to capture.

## See Also

### Starting capture

- [- startCaptureWithDescriptor:error:](<startcapture(with_).md>) — Starts capturing any of your app’s Metal commands, with the capture session defined by a descriptor object.
- [- startCaptureWithDevice:](<startcapture(device_).md>) — Starts capturing any of your app’s Metal commands that are executed by the device object. _(deprecated)_
- [- startCaptureWithScope:](<startcapture(scope_).md>) — Starts capturing any of your app’s Metal commands that are in the specified capture scope. _(deprecated)_
