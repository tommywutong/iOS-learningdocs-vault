---
title: Window Image Types
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/window-image-types
source_url: 'https://developer.apple.com/documentation/coregraphics/window-image-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/window-image-types.json'
content_hash: 'sha256:9ab0607157a5cce3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md) · [Quartz Window Services](quartz-window-services.md)

# Window Image Types

<sub>API Collection</sub>

Specifies the options for capturing an image of a window.

## Topics

### Constants

- [kCGWindowImageBoundsIgnoreFraming](cgwindowimageoption/boundsignoreframing.md)
- [kCGWindowImageShouldBeOpaque](cgwindowimageoption/shouldbeopaque.md)
- [kCGWindowImageOnlyShadows](cgwindowimageoption/onlyshadows.md)
- [kCGWindowImageBestResolution](cgwindowimageoption/bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageNominalResolution](cgwindowimageoption/nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.

## See Also

### Constants

- [Window Sharing Constants](window-sharing-constants.md) — Specifies whether and how windows are shared between applications.
- [Backing Store Types](backing-store-types.md) — Specifies how the window device buffers drawing commands.
- [Window List Option Constants](window-list-option-constants.md) — Specifies which windows in the current user session to include in a generated list.
- [CGWindowID Encoding Type](cgwindowid-encoding-type.md) — Defines the encoding type for window IDs.
- [Null Window](null-window.md) — Defines a guaranteed invalid window ID.
- [Window Sharing Encoding Type](window-sharing-encoding-type.md) — Defines the encoding type for window sharing values.
- [Window Backing Encoding Type](window-backing-encoding-type.md) — Defines the encoding type for window backing types.
- [Required Window List Keys](required-window-list-keys.md) — The keys that are guaranteed to be available in a window’s information dictionary.
- [Optional Window List Keys](optional-window-list-keys.md) — The keys that may optionally be available inside a window’s information dictionary.
