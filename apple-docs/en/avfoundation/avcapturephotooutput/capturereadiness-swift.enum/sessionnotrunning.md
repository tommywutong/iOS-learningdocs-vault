---
title: AVCapturePhotoOutput.CaptureReadiness.sessionNotRunning
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/sessionnotrunning
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/sessionnotrunning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/sessionnotrunning.json'
content_hash: 'sha256:4e21fa75aa3da281'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCapturePhotoOutput](../../avcapturephotooutput.md) · [CaptureReadiness](../capturereadiness-swift.enum.md)

# AVCapturePhotoOutput.CaptureReadiness.sessionNotRunning

<sub>Case</sub>

Indicates that the session isn’t running and the output isn’t ready to receive requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case sessionNotRunning
```

## See Also

### Readiness states

- [AVCapturePhotoOutputCaptureReadinessNotReadyMomentarily](notreadymomentarily.md) — Indicates that the output isn’t ready to receive requests, but may be ready shortly.
- [AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForCapture](notreadywaitingforcapture.md) — Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForProcessing](notreadywaitingforprocessing.md) — Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.
- [AVCapturePhotoOutputCaptureReadinessReady](ready.md) — Indicates that the output is ready to receive new requests.
