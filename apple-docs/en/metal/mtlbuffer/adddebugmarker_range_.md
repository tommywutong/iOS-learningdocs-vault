---
title: 'addDebugMarker:range:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbuffer/adddebugmarker:range:'
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/adddebugmarker:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/adddebugmarker%3Arange%3A.json'
content_hash: 'sha256:b6e2eb01621456ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# addDebugMarker:range:

<sub>Instance Method</sub>

Adds a debug marker string to a specific buffer range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) addDebugMarker:(NSString *) marker range:(NSRange) range;
```

## Parameters

- `marker` — A string that identifies the marked buffer range.

- `range` — The range of bytes that you want to identify.

## See Also

### Debugging buffers

- [- removeAllDebugMarkers](<removealldebugmarkers().md>) — Removes all debug marker strings from the buffer.
