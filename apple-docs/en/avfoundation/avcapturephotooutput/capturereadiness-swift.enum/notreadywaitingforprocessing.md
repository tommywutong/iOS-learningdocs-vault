---
title: AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForProcessing
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforprocessing
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforprocessing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum/notreadywaitingforprocessing.json'
content_hash: 'sha256:4ac2bae94ec0886e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCapturePhotoOutput](../../avcapturephotooutput.md) · [CaptureReadiness](../capturereadiness-swift.enum.md)

# AVCapturePhotoOutput.CaptureReadiness.notReadyWaitingForProcessing

<sub>Case</sub>

Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case notReadyWaitingForProcessing
```

## See Also

### Readiness states

- [AVCapturePhotoOutputCaptureReadinessSessionNotRunning](sessionnotrunning.md) — Indicates that the session isn’t running and the output isn’t ready to receive requests.
- [AVCapturePhotoOutputCaptureReadinessNotReadyMomentarily](notreadymomentarily.md) — Indicates that the output isn’t ready to receive requests, but may be ready shortly.
- [AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForCapture](notreadywaitingforcapture.md) — Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutputCaptureReadinessReady](ready.md) — Indicates that the output is ready to receive new requests.
