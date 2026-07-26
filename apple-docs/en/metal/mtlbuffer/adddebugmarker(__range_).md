---
title: 'addDebugMarker(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbuffer/adddebugmarker(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/adddebugmarker(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/adddebugmarker%28_%3Arange%3A%29.json'
content_hash: 'sha256:cf014862d44ac49a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# addDebugMarker(_:range:)

<sub>Instance Method</sub>

Adds a debug marker string to a specific buffer range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addDebugMarker(_ marker: String, range: Range<Int>)
```

## Parameters

- `marker` — A string that identifies the marked buffer range.

- `range` — The range of bytes that you want to identify.

## See Also

### Debugging buffers

- [- removeAllDebugMarkers](<removealldebugmarkers().md>) — Removes all debug marker strings from the buffer.
