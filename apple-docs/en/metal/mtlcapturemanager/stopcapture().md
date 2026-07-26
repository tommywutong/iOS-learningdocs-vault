---
title: stopCapture()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturemanager/stopcapture()
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/stopcapture()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/stopcapture%28%29.json'
content_hash: 'sha256:bbd84ae6eb876332'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# stopCapture()

<sub>Instance Method</sub>

Stops capturing Metal commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stopCapture()
```

## Discussion

Calling this method stops a capture that was started manually in Xcode or programmatically by calling one of the methods on [MTLCaptureManager](../mtlcapturemanager.md).

When using a custom capture scope, calling this function preempts any [- endScope](<../mtlcapturescope/end().md>) demarcations of the capture scope.
