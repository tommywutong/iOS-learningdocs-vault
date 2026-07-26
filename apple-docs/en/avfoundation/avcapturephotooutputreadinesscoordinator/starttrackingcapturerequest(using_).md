---
title: 'startTrackingCaptureRequest(using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest%28using%3A%29.json'
content_hash: 'sha256:fee2496c280b7b76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutputReadinessCoordinator](../avcapturephotooutputreadinesscoordinator.md)

# startTrackingCaptureRequest(using:)

<sub>Instance Method</sub>

Tracks a capture request that uses the specified photo settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func startTrackingCaptureRequest(using settings: AVCapturePhotoSettings)
```

## Parameters

- `settings` — A settings object that the system passes [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) for this capture request.

## See Also

### Performing tracking requests

- [- stopTrackingCaptureRequestUsingPhotoSettingsUniqueID:](<stoptrackingcapturerequest(using_).md>) — Stop tracking the capture request represented by the specified photo setting’s unique identifier.
