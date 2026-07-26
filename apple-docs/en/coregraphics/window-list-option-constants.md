---
title: Window List Option Constants
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/window-list-option-constants
source_url: 'https://developer.apple.com/documentation/coregraphics/window-list-option-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/window-list-option-constants.json'
content_hash: 'sha256:197ecd8b638b231f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md) · [Quartz Window Services](quartz-window-services.md)

# Window List Option Constants

<sub>API Collection</sub>

Specifies which windows in the current user session to include in a generated list.

## Overview

The [kCGWindowListOptionIncludingWindow](cgwindowlistoption/optionincludingwindow.md) and [kCGWindowListExcludeDesktopElements](cgwindowlistoption/excludedesktopelements.md) constants may be combined with the other constants by adding (or ORing) them together and passing the resulting value to the appropriate function.

These constants let you retrieve windows in the current user session only. You cannot use them to retrieve windows from other active user sessions running on the system.

## Topics

### Constants

- [kCGWindowListOptionAll](cgwindowlistoption/optionall.md)
- [kCGWindowListOptionOnScreenOnly](cgwindowlistoption/optiononscreenonly.md)
- [kCGWindowListOptionOnScreenAboveWindow](cgwindowlistoption/optiononscreenabovewindow.md)
- [kCGWindowListOptionOnScreenBelowWindow](cgwindowlistoption/optiononscreenbelowwindow.md)
- [kCGWindowListOptionIncludingWindow](cgwindowlistoption/optionincludingwindow.md)
- [kCGWindowListExcludeDesktopElements](cgwindowlistoption/excludedesktopelements.md)

## See Also

### Constants

- [Window Sharing Constants](window-sharing-constants.md) — Specifies whether and how windows are shared between applications.
- [Backing Store Types](backing-store-types.md) — Specifies how the window device buffers drawing commands.
- [Window Image Types](window-image-types.md) — Specifies the options for capturing an image of a window.
- [CGWindowID Encoding Type](cgwindowid-encoding-type.md) — Defines the encoding type for window IDs.
- [Null Window](null-window.md) — Defines a guaranteed invalid window ID.
- [Window Sharing Encoding Type](window-sharing-encoding-type.md) — Defines the encoding type for window sharing values.
- [Window Backing Encoding Type](window-backing-encoding-type.md) — Defines the encoding type for window backing types.
- [Required Window List Keys](required-window-list-keys.md) — The keys that are guaranteed to be available in a window’s information dictionary.
- [Optional Window List Keys](optional-window-list-keys.md) — The keys that may optionally be available inside a window’s information dictionary.
