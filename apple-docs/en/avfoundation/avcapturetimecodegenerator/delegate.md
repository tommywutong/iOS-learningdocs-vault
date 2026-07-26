---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/delegate.json'
content_hash: 'sha256:20dc1ad0110b41f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# delegate

<sub>Instance Property</sub>

The delegate that receives timecode updates from the timecode generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var delegate: (any AVCaptureTimecodeGeneratorDelegate)? { get }
```

## Discussion

You can use your [delegate](delegate.md) to receive real-time timecode updates. Implement the `timecodeGenerator:didReceiveUpdate:` method in your delegate to handle updates.

## See Also

### Handling delegate callbacks

- [delegateCallbackQueue](delegatecallbackqueue.md) — The dispatch queue on which delegate callbacks are invoked.
