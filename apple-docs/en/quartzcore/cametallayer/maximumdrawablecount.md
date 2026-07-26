---
title: maximumDrawableCount
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/maximumdrawablecount
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/maximumdrawablecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/maximumdrawablecount.json'
content_hash: 'sha256:5e4554eb8acf25de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# maximumDrawableCount

<sub>Instance Property</sub>

The number of Metal drawables in the resource pool managed by Core Animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maximumDrawableCount: Int { get set }
```

## Discussion

You can set this value to `2` or `3` only; if you pass a different value, Core Animation ignores the value and throws an exception.

The default value is `3`.

## See Also

### Obtaining a Metal Drawable

- [- nextDrawable](<nextdrawable().md>) — Waits until a Metal drawable is available, and then returns it.
- [allowsNextDrawableTimeout](allowsnextdrawabletimeout.md) — A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.
