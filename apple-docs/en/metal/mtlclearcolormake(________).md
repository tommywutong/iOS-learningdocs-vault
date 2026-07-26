---
title: 'MTLClearColorMake(_:_:_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlclearcolormake(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlclearcolormake(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlclearcolormake%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2ce2aa4e362370c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLClearColorMake(_:_:_:_:)

<sub>Function</sub>

Returns a color value used to clear a color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLClearColorMake(_ red: Double, _ green: Double, _ blue: Double, _ alpha: Double) -> MTLClearColor
```

## Parameters

- `red` — The red color channel.

- `green` — The green color channel.

- `blue` — The blue color channel.

- `alpha` — The alpha channel.

## Return Value

A value for clearing a color attachment.

## See Also

### Specifying clearing value

- [clearColor](mtlrenderpasscolorattachmentdescriptor/clearcolor.md) — The color to use when clearing the color attachment.
