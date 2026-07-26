---
title: AVCapturePhotoOutput.CaptureReadiness
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/capturereadiness-swift.enum.json'
content_hash: 'sha256:e6d7d5025d84e61e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# AVCapturePhotoOutput.CaptureReadiness

<sub>Enumeration</sub>

Constants that indicate whether the output is ready to receive capture requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum CaptureReadiness
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Readiness states

- [AVCapturePhotoOutputCaptureReadinessSessionNotRunning](capturereadiness-swift.enum/sessionnotrunning.md) — Indicates that the session isn’t running and the output isn’t ready to receive requests.
- [AVCapturePhotoOutputCaptureReadinessNotReadyMomentarily](capturereadiness-swift.enum/notreadymomentarily.md) — Indicates that the output isn’t ready to receive requests, but may be ready shortly.
- [AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForCapture](capturereadiness-swift.enum/notreadywaitingforcapture.md) — Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy capturing.
- [AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForProcessing](capturereadiness-swift.enum/notreadywaitingforprocessing.md) — Indicates that the output isn’t ready to receive requests for a longer duration because it’s busy processing.
- [AVCapturePhotoOutputCaptureReadinessReady](capturereadiness-swift.enum/ready.md) — Indicates that the output is ready to receive new requests.

### Initializers

- [init(rawValue:)](<capturereadiness-swift.enum/init(rawvalue_).md>)

## See Also

### Managing responsive capture

- [captureReadiness](capturereadiness-swift.property.md) — A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [autoDeferredPhotoDeliveryEnabled](isautodeferredphotodeliveryenabled.md) — A Boolean value that indicates the enabled state of automatic deferred photo delivery.
- [autoDeferredPhotoDeliverySupported](isautodeferredphotodeliverysupported.md) — A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [fastCapturePrioritizationSupported](isfastcaptureprioritizationsupported.md) — A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [fastCapturePrioritizationEnabled](isfastcaptureprioritizationenabled.md) — A Boolean value that indicates whether the output enables fast capture prioritization.
- [responsiveCaptureSupported](isresponsivecapturesupported.md) — A Boolean value that indicates whether the photo output supports responsive capture.
- [responsiveCaptureEnabled](isresponsivecaptureenabled.md) — A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [zeroShutterLagSupported](iszeroshutterlagsupported.md) — A Boolean value that indicates whether the photo output supports zero shutter lag.
- [zeroShutterLagEnabled](iszeroshutterlagenabled.md) — A Boolean value that indicates whether the photo output configuration enables zero shutter lag.
