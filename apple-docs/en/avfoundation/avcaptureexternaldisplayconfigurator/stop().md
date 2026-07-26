---
title: stop()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator/stop()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/stop()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator/stop%28%29.json'
content_hash: 'sha256:5114391e2543e91e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)

# stop()

<sub>Instance Method</sub>

Forces the external display configurator to asynchronously stop configuring the external display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func stop()
```

## Discussion

Call [- stop](<stop().md>) to force the [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md) to asynchronously stop configuring the external display. Once stopped, the [active](isactive.md) property changes to `false` and the [activeExternalDisplayFrameRate](activeexternaldisplayframerate.md) becomes 0.
