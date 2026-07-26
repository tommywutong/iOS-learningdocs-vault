---
title: getSamplePositions()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/getsamplepositions()
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/getsamplepositions()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/getsamplepositions%28%29.json'
content_hash: 'sha256:62ad50d9731a16bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# getSamplePositions()

<sub>Instance Method</sub>

Returns the programmable sample positions set for a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func getSamplePositions() -> [MTLSamplePosition]
```

## Return Value

An array of programmable sample positions.

## See Also

### Using programmable sample positions

- [MTLSamplePositionMake](<../mtlsamplepositionmake(____).md>) — Returns a new sample position on a subpixel grid.
- [setSamplePositions(_:)](<setsamplepositions(__).md>) — Sets the programmable sample positions for a render pass.
