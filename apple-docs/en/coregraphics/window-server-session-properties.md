---
title: Window Server Session Properties
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/window-server-session-properties
source_url: 'https://developer.apple.com/documentation/coregraphics/window-server-session-properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/window-server-session-properties.json'
content_hash: 'sha256:83afd3a9aea40ead'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md) · [Quartz Display Services](quartz-display-services.md)

# Window Server Session Properties

<sub>API Collection</sub>

The keys for the standard properties in a window server session dictionary.

## Overview

To learn how to use these keys to access the values in a session dictionary, see [CFDictionary](../corefoundation/cfdictionary.md).

## Topics

### Constants

- [kCGSessionUserIDKey](kcgsessionuseridkey.md) — A `CFNumber` 32-bit unsigned integer value that encodes a user ID for the session’s current user.
- [kCGSessionUserNameKey](kcgsessionusernamekey.md) — A `CFString` value that encodes the session’s short user name as set by the login operation.
- [kCGSessionConsoleSetKey](kcgsessionconsolesetkey.md) — A `CFNumber` 32-bit unsigned integer value that represents a set of hardware composing a console.
- [kCGSessionOnConsoleKey](kcgsessiononconsolekey.md) — A `CFBoolean` value indicating whether the session is on a console.
- [kCGSessionLoginDoneKey](kcgsessionlogindonekey.md) — A `CFBoolean` value indicating whether the login operation has been done.

## See Also

### Constants

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [Display Fade Blend Fractions](display-fade-blend-fractions.md) — The lower and upper bounds for blend color fractions during a display fade operation.
- [Display Fade Constants](display-fade-constants.md) — Values relating to fade operations.
- [Display ID Defaults](display-id-defaults.md) — Default values for a display ID.
- [Display Mode Standard Properties](display-mode-standard-properties.md) — Keys for the standard properties in a display mode dictionary.
- [Display Mode Optional Properties](display-mode-optional-properties.md) — Keys for optional properties in a display mode dictionary.
- [Reserved Window Levels](reserved-window-levels.md) — Window level constants.
- [CGScreenUpdateOperation](cgscreenupdateoperation.md) — Types of screen-update operations.
- [CGWindowLevelKey](cgwindowlevelkey.md) — Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.
- [CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md) — Use these constants to determine which rectangles your app is interested in.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [Display Stream Optional Property Keys](display-stream-optional-property-keys.md) — These keys are used to populate the `properties` dictionary used when creating a new display stream.
- [Display Stream YCbCr to RGB conversion Matrix Options](display-stream-ycbcr-to-rgb-conversion-matrix-options.md) — These strings are used to specify a matrix for the `CGDisplayStream/yCbCrMatrix` option.
