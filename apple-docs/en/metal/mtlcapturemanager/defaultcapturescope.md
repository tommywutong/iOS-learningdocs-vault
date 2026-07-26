---
title: defaultCaptureScope
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturemanager/defaultcapturescope
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturemanager/defaultcapturescope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturemanager/defaultcapturescope.json'
content_hash: 'sha256:2402d6bd1f3ebc82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureManager](../mtlcapturemanager.md)

# defaultCaptureScope

<sub>Instance Property</sub>

The capture scope to use when a capture is initiated in Xcode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var defaultCaptureScope: (any MTLCaptureScope)? { get set }
```

## Discussion

Use this property to specify a default capture scope for Xcode to use when the user presses the capture button. You can still long-press the button to select a different capture scope.

The default value is `nil.` When the value is `nil`, the capture scope is defined by drawable presentation boundaries; such as those created by calls to [- presentDrawable:](<../mtlcommandbuffer/present(__).md>) or [- present](<../mtldrawable/present().md>).

## See Also

### Creating a capture scope

- [- newCaptureScopeWithDevice:](<makecapturescope(device_).md>) — Creates a capture scope for commands submitted to a specific device object.
- [- newCaptureScopeWithCommandQueue:](<makecapturescope(commandqueue_)-1rozd.md>) — Creates a capture scope for commands submitted to a specific command queue.
