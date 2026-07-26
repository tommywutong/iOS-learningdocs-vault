---
title: PencilKit updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/pencilkit
source_url: 'https://developer.apple.com/documentation/updates/pencilkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/pencilkit.json'
content_hash: 'sha256:09ca911ad96f2024'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# PencilKit updates

<sub>Article</sub>

Learn about important changes to PencilKit.

## Overview

Browse notable changes in [PencilKit](../pencilkit.md).

## June 2026

### Strokes

- Access and assign a stable identity to strokes and stroke paths using the `id` property on [PKStroke](../pencilkit/pkstroke-swift.struct.md) and [PKStrokePath](../pencilkit/pkstrokepath-swift.struct.md), which conform to `Identifiable`.
- Select strokes programmatically and respond to selection changes using the [selection](../pencilkit/pkcanvasview/selection.md) property and the [canvasViewSelectionDidChange(_:)](<../pencilkit/pkcanvasviewdelegate/canvasviewselectiondidchange(__).md>) delegate method.
- Erase portions of a drawing along a path using [erasePath(_:mask:transform:)](<../pencilkit/pkdrawing-swift.struct/erasepath(__mask_transform_)-shn.md>), or get a new drawing with the erasure applied using [erasingPath(_:mask:transform:)](<../pencilkit/pkdrawing-swift.struct/erasingpath(__mask_transform_)-9dpi9.md>).
- Convert a stroke path to a `CGPath` using the [bezierRepresentation](../pencilkit/pkstrokepathreference/bezierrepresentation.md) property, or create a stroke path from a bezier path using [init(bezierPath:creationDate:pointProvider:)](<../pencilkit/pkstrokepath-swift.struct/init(bezierpath_creationdate_pointprovider_).md>).

### Handwriting recognition

- Recognize handwritten text, search within ink, and generate indexable string content using [PKStrokeRecognizer](../pencilkit/pkstrokerecognizer.md).

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
