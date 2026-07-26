---
title: presentedTime
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldrawable/presentedtime
source_url: 'https://developer.apple.com/documentation/metal/mtldrawable/presentedtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldrawable/presentedtime.json'
content_hash: 'sha256:88ac98fdc9a87fef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDrawable](../mtldrawable.md)

# presentedTime

<sub>Instance Property</sub>

The host time, in seconds, when the drawable was displayed onscreen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var presentedTime: CFTimeInterval { get }
```

## Discussion

Typically, you query this property in a callback method. See [- addPresentedHandler:](<addpresentedhandler(__).md>).

The property value is `0.0` if the drawable hasn’t been presented or if its associated frame was dropped.

## See Also

### Getting presentation information

- [- addPresentedHandler:](<addpresentedhandler(__).md>) — Registers a block of code to be called immediately after the drawable is presented.
