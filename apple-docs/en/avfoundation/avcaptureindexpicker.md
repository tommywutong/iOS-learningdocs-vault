---
title: AVCaptureIndexPicker
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureindexpicker
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureindexpicker.json'
content_hash: 'sha256:01bd2cd7ea278aea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureIndexPicker

<sub>Class</sub>

A control for selecting from a set of mutually exclusive values by index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureIndexPicker
```

## Overview

Index pickers are appropriate for controls that provide an indexed container of values.

## Relationships

- **Inherits From**: [AVCaptureControl](avcapturecontrol.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an index picker

- [- initWithLocalizedTitle:symbolName:numberOfIndexes:](<avcaptureindexpicker/init(__symbolname_numberofindexes_).md>) — Creates a control to pick a value from the specified number of indexes.
- [- initWithLocalizedTitle:symbolName:numberOfIndexes:localizedTitleTransform:](<avcaptureindexpicker/init(__symbolname_numberofindexes_localizedtitletransform_).md>) — Creates a control to pick a value from the specified number of indices.
- [- initWithLocalizedTitle:symbolName:localizedIndexTitles:](<avcaptureindexpicker/init(__symbolname_localizedindextitles_).md>) — Creates an object to select an index from a set of values.

### Handling interaction

- [setActionQueue(_:action:)](<avcaptureindexpicker/setactionqueue(__action_).md>) — Sets the action to perform on the specified dispatch queue when the control’s value changes.

### Accessing the control value

- [selectedIndex](avcaptureindexpicker/selectedindex.md) — The currently selected index.
- [numberOfIndexes](avcaptureindexpicker/numberofindexes.md) — The number of index values the control provides.

### Setting an accessibility identifier

- [accessibilityIdentifier](avcaptureindexpicker/accessibilityidentifier.md) — A string identifier for this control.

### Inspecting presentation attributes

- [symbolName](avcaptureindexpicker/symbolname.md) — The name of the SF Symbol that represents this control.
- [localizedTitle](avcaptureindexpicker/localizedtitle.md) — A localized title that describes the control’s action.
- [localizedIndexTitles](avcaptureindexpicker/localizedindextitles.md) — The titles to present for each index.

### Initializers

- [init(localizedTitle:symbolName:localizedIndexTitles:)](<avcaptureindexpicker/init(localizedtitle_symbolname_localizedindextitles_).md>)
- [init(localizedTitle:symbolName:numberOfIndexes:)](<avcaptureindexpicker/init(localizedtitle_symbolname_numberofindexes_).md>)
- [init(localizedTitle:symbolName:numberOfIndexes:localizedTitleTransform:)](<avcaptureindexpicker/init(localizedtitle_symbolname_numberofindexes_localizedtitletransform_).md>)

## See Also

### Capture controls

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md) — Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [AVCaptureControl](avcapturecontrol.md) — An abstract base class for controls that interact with the camera system.
- [AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md) — A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md) — A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [AVCaptureSlider](avcaptureslider.md) — A slider control that selects a value from a bounded range.
