---
title: Display Fade Blend Fractions
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/display-fade-blend-fractions
source_url: 'https://developer.apple.com/documentation/coregraphics/display-fade-blend-fractions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/display-fade-blend-fractions.json'
content_hash: 'sha256:efd6a90db8d8239b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md) · [Quartz Display Services](quartz-display-services.md)

# Display Fade Blend Fractions

<sub>API Collection</sub>

The lower and upper bounds for blend color fractions during a display fade operation.

## Overview

For general information about blend fractions, see the data type [CGDisplayBlendFraction](cgdisplayblendfraction.md). For information about how these constants are used, see the function [CGDisplayFade](<cgdisplayfade(________________).md>).

## Topics

### Constants

- [kCGDisplayBlendNormal](kcgdisplayblendnormal.md) — The blend color is not applied at the start or end of a fade operation.
- [kCGDisplayBlendSolidColor](kcgdisplayblendsolidcolor.md) — The user sees only the blend color at the start or end of a fade operation.

## See Also

### Constants

- [CGCaptureOptions](cgcaptureoptions.md) — Configuration parameters that are used when capturing displays.
- [CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md) — The configuration parameters that are passed to a display reconfiguration callback function.
- [CGConfigureOption](cgconfigureoption.md) — The scope of the changes in a display configuration transaction.
- [Display Fade Constants](display-fade-constants.md) — Values relating to fade operations.
- [Display ID Defaults](display-id-defaults.md) — Default values for a display ID.
- [Display Mode Standard Properties](display-mode-standard-properties.md) — Keys for the standard properties in a display mode dictionary.
- [Display Mode Optional Properties](display-mode-optional-properties.md) — Keys for optional properties in a display mode dictionary.
- [Reserved Window Levels](reserved-window-levels.md) — Window level constants.
- [CGScreenUpdateOperation](cgscreenupdateoperation.md) — Types of screen-update operations.
- [CGWindowLevelKey](cgwindowlevelkey.md) — Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.
- [Window Server Session Properties](window-server-session-properties.md) — The keys for the standard properties in a window server session dictionary.
- [CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md) — Use these constants to determine which rectangles your app is interested in.
- [CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md) — Describes a frame update event.
- [Display Stream Optional Property Keys](display-stream-optional-property-keys.md) — These keys are used to populate the `properties` dictionary used when creating a new display stream.
- [Display Stream YCbCr to RGB conversion Matrix Options](display-stream-ycbcr-to-rgb-conversion-matrix-options.md) — These strings are used to specify a matrix for the `CGDisplayStream/yCbCrMatrix` option.
