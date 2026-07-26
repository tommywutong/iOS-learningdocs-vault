---
title: 'MTLSamplePositionMake(_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlsamplepositionmake(_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplepositionmake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplepositionmake%28_%3A_%3A%29.json'
content_hash: 'sha256:5dea5a9dfac8f261'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplePositionMake(_:_:)

<sub>Function</sub>

Returns a new sample position on a subpixel grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLSamplePositionMake(_ x: Float, _ y: Float) -> MTLSamplePosition
```

## Parameters

- `x` — The x coordinate.

- `y` — The y coordinate.

## Return Value

The new sample position.

## See Also

### Using programmable sample positions

- [setSamplePositions(_:)](<mtlrenderpassdescriptor/setsamplepositions(__).md>) — Sets the programmable sample positions for a render pass.
- [getSamplePositions()](<mtlrenderpassdescriptor/getsamplepositions().md>) — Returns the programmable sample positions set for a render pass.
