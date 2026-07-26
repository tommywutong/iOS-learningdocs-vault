---
title: MTLColorWriteMask
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcolorwritemask
source_url: 'https://developer.apple.com/documentation/metal/mtlcolorwritemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcolorwritemask.json'
content_hash: 'sha256:97186d7a6d1e7511'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLColorWriteMask

<sub>Structure</sub>

Values used to specify a mask to permit or restrict writing to color channels of a color value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLColorWriteMask
```

## Overview

The values [MTLColorWriteMaskRed](mtlcolorwritemask/red.md), [MTLColorWriteMaskGreen](mtlcolorwritemask/green.md), [MTLColorWriteMaskBlue](mtlcolorwritemask/blue.md), and [MTLColorWriteMaskAlpha](mtlcolorwritemask/alpha.md) select one color channel each, and they can be bitwise combined.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<mtlcolorwritemask/init(rawvalue_).md>) — Returns a new color write mask from a specified raw value.

### Type Properties

- [MTLColorWriteMaskAll](mtlcolorwritemask/all.md) — All color channels are enabled.
- [MTLColorWriteMaskAlpha](mtlcolorwritemask/alpha.md) — The alpha color channel is enabled.
- [MTLColorWriteMaskBlue](mtlcolorwritemask/blue.md) — The blue color channel is enabled.
- [MTLColorWriteMaskGreen](mtlcolorwritemask/green.md) — The green color channel is enabled.
- [MTLColorWriteMaskRed](mtlcolorwritemask/red.md) — The red color channel is enabled.
- [MTLColorWriteMaskUnspecialized](mtlcolorwritemask/unspecialized.md) — Defers assigning the color write mask.

## See Also

### Configuring render pipeline states

- [pixelFormat](mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md) — The pixel format of the color attachment’s texture.
- [writeMask](mtlrenderpipelinecolorattachmentdescriptor/writemask.md) — A bitmask that restricts which color channels are written into the texture.
