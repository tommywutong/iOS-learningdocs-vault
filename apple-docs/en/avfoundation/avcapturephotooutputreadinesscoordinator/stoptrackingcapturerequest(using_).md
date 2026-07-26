---
title: 'stopTrackingCaptureRequest(using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/stoptrackingcapturerequest(using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/stoptrackingcapturerequest(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/stoptrackingcapturerequest%28using%3A%29.json'
content_hash: 'sha256:1f0cdba8172b77e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutputReadinessCoordinator](../avcapturephotooutputreadinesscoordinator.md)

# stopTrackingCaptureRequest(using:)

<sub>Instance Method</sub>

Stop tracking the capture request represented by the specified photo setting’s unique identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func stopTrackingCaptureRequest(using settingsUniqueID: Int64)
```

## Parameters

- `settingsUniqueID` — The [uniqueID](../avcapturephotosettings/uniqueid.md) value of the related photo settings object.

## See Also

### Performing tracking requests

- [- startTrackingCaptureRequestUsingPhotoSettings:](<starttrackingcapturerequest(using_).md>) — Tracks a capture request that uses the specified photo settings.
