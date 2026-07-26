---
title: AVCaptureSceneMonitoringStatus
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescenemonitoringstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescenemonitoringstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescenemonitoringstatus.json'
content_hash: 'sha256:6c42eb7b10829927'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSceneMonitoringStatus

<sub>Structure</sub>

An informative status about the scene observed by the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct AVCaptureSceneMonitoringStatus
```

## Overview

Some features have certain requirements on the scene (lighting condition for Cinematic Video, for example) to produce optimal results; these [AVCaptureSceneMonitoringStatus](avcapturescenemonitoringstatus.md) string constants are used to represent such scene statuses for a given feature.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVCaptureSceneMonitoringStatusNotEnoughLight](avcapturescenemonitoringstatus/notenoughlight.md) — The light level of the current scene is insufficient for the current set of features to function optimally.

### Initializers

- [init(rawValue:)](<avcapturescenemonitoringstatus/init(rawvalue_).md>)

## See Also

### Configuring Cinematic video

- [- setCinematicVideoFixedFocusAtPoint:focusMode:](<avcapturedevice/setcinematicvideofixedfocus(at_focusmode_).md>) — Fix focus at a distance.
- [- setCinematicVideoTrackingFocusAtPoint:focusMode:](<avcapturedevice/setcinematicvideotrackingfocus(at_focusmode_).md>) — Focus on and start tracking an object if it can be detected at the region specified by the point.
- [- setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:](<avcapturedevice/setcinematicvideotrackingfocus(detectedobjectid_focusmode_).md>) — Focus on and start tracking a detected object.
- [CinematicVideoFocusMode](avcapturedevice/cinematicvideofocusmode.md) — Constants indicating the focus behavior when recording a Cinematic Video.
- [AVCaptureSceneMonitoringStatusNotEnoughLight](avcapturescenemonitoringstatus/notenoughlight.md) — The light level of the current scene is insufficient for the current set of features to function optimally.
- [cinematicVideoCaptureSceneMonitoringStatuses](avcapturedevice/cinematicvideocapturescenemonitoringstatuses.md) — The current scene monitoring statuses related to Cinematic Video capture.
