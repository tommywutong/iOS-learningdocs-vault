---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecodegenerator/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:ca20620e228ba564'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setDelegate(_ delegate: (any AVCaptureTimecodeGeneratorDelegate)?, queue callbackQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — An object conforming to the [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) protocol.

- `callbackQueue` — The dispatch queue on which the delegate methods are invoked. The `callbackQueue` parameter may not be `nil`, except when setting the [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) to `nil`, otherwise [- setDelegate:queue:](<setdelegate(__queue_).md>) throws an `NSInvalidArgumentException`.

## Discussion

Use this method to configure a delegate that handles timecode updates. The specified `queue` ensures thread-safe invocation of delegate methods.

## See Also

### Configuring the generator

- [synchronizationTimeout](synchronizationtimeout.md) — The maximum time interval allowed for source synchronization attempts before timing out.
- [timecodeAlignmentOffset](timecodealignmentoffset.md) — The time offset, in seconds, applied to the generated timecode.
- [timecodeFrameDuration](timecodeframeduration.md) — The frame duration that the generator will use to generate timecodes.
