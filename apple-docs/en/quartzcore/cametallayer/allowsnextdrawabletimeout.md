---
title: allowsNextDrawableTimeout
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/allowsnextdrawabletimeout
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/allowsnextdrawabletimeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/allowsnextdrawabletimeout.json'
content_hash: 'sha256:c9de742ed0e1953b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# allowsNextDrawableTimeout

<sub>Instance Property</sub>

A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowsNextDrawableTimeout: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the [- nextDrawable](<nextdrawable().md>) method returns [nil](../../objectivec/nil-227m0.md) if it can’t provide a drawable object within one second. If [false](../../swift/false.md), the [- nextDrawable](<nextdrawable().md>) method waits indefinitely for a drawable to become available.

The default value is [true](../../swift/true.md).

## See Also

### Obtaining a Metal Drawable

- [- nextDrawable](<nextdrawable().md>) — Waits until a Metal drawable is available, and then returns it.
- [maximumDrawableCount](maximumdrawablecount.md) — The number of Metal drawables in the resource pool managed by Core Animation.
