---
title: Quartz Window Services
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/quartz-window-services
source_url: 'https://developer.apple.com/documentation/coregraphics/quartz-window-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/quartz-window-services.json'
content_hash: 'sha256:e130ccb2b35e3523'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# Quartz Window Services

<sub>API Collection</sub>

Provides information about the windows managed by the macOS window server.

## Overview

This includes the onscreen windows seen on the user’s desktop and any offscreen windows used by the running applications. You can also use Quartz Window Services to generate images based on the contents of windows.

## Topics

### Getting Window Information

- [CGWindowListCopyWindowInfo](<cgwindowlistcopywindowinfo(____).md>) — Generates and returns information about the selected windows in the current user session.
- [CGWindowListCreateDescriptionFromArray](<cgwindowlistcreatedescriptionfromarray(__).md>) — Generates and returns information about windows with the specified window IDs.

### Data Types

- [CGWindowID](cgwindowid.md) — The data type used to store window identifiers.
- [CGWindowListOption](cgwindowlistoption.md) — The data type used to specify the options for gathering a list of windows.
- [CGWindowImageOption](cgwindowimageoption.md) — The data type to use to specify the type of image to be generated for a window.
- [CGWindowSharingType](cgwindowsharingtype.md) — The data type used to specify the sharing mode used by a window.
- [CGWindowBackingType](cgwindowbackingtype.md) — The data type used to specify the backing option for a given window.

### Constants

- [Window Sharing Constants](window-sharing-constants.md) — Specifies whether and how windows are shared between applications.
- [Backing Store Types](backing-store-types.md) — Specifies how the window device buffers drawing commands.
- [Window List Option Constants](window-list-option-constants.md) — Specifies which windows in the current user session to include in a generated list.
- [Window Image Types](window-image-types.md) — Specifies the options for capturing an image of a window.
- [CGWindowID Encoding Type](cgwindowid-encoding-type.md) — Defines the encoding type for window IDs.
- [Null Window](null-window.md) — Defines a guaranteed invalid window ID.
- [Window Sharing Encoding Type](window-sharing-encoding-type.md) — Defines the encoding type for window sharing values.
- [Window Backing Encoding Type](window-backing-encoding-type.md) — Defines the encoding type for window backing types.
- [Required Window List Keys](required-window-list-keys.md) — The keys that are guaranteed to be available in a window’s information dictionary.
- [Optional Window List Keys](optional-window-list-keys.md) — The keys that may optionally be available inside a window’s information dictionary.

## See Also

### Services

- [Quartz Display Services](quartz-display-services.md) — Provides direct access to features in the macOS window server for configuring and controlling display hardware.
- [Quartz Event Services](quartz-event-services.md) — Provides features for managing _event taps_—filters for observing and altering the stream of low-level user input events in macOS.
