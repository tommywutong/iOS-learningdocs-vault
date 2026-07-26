---
title: isFastCapturePrioritizationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isfastcaptureprioritizationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isfastcaptureprioritizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isfastcaptureprioritizationenabled.json'
content_hash: 'sha256:0272431f52d50165'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isFastCapturePrioritizationEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the output enables fast capture prioritization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isFastCapturePrioritizationEnabled: Bool { get set }
```

## See Also

### Managing responsive capture

- [captureReadiness](capturereadiness-swift.property.md) — A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [CaptureReadiness](capturereadiness-swift.enum.md) — Constants that indicate whether the output is ready to receive capture requests.
- [autoDeferredPhotoDeliveryEnabled](isautodeferredphotodeliveryenabled.md) — A Boolean value that indicates the enabled state of automatic deferred photo delivery.
- [autoDeferredPhotoDeliverySupported](isautodeferredphotodeliverysupported.md) — A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [fastCapturePrioritizationSupported](isfastcaptureprioritizationsupported.md) — A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [responsiveCaptureSupported](isresponsivecapturesupported.md) — A Boolean value that indicates whether the photo output supports responsive capture.
- [responsiveCaptureEnabled](isresponsivecaptureenabled.md) — A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [zeroShutterLagSupported](iszeroshutterlagsupported.md) — A Boolean value that indicates whether the photo output supports zero shutter lag.
- [zeroShutterLagEnabled](iszeroshutterlagenabled.md) — A Boolean value that indicates whether the photo output configuration enables zero shutter lag.
