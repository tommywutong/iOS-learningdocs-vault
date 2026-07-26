---
title: isAutoDeferredPhotoDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isautodeferredphotodeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isautodeferredphotodeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isautodeferredphotodeliveryenabled.json'
content_hash: 'sha256:724f778b1c51fb08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isAutoDeferredPhotoDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that indicates the enabled state of automatic deferred photo delivery.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isAutoDeferredPhotoDeliveryEnabled: Bool { get set }
```

## Discussion

Changing this value requires a lengthy reconfiguration of the capture pipeline, so you should set this property before calling [- startRunning](<../avcapturesession/startrunning().md>) on the capture session.

Setting this property to [true](../../swift/true.md) throws an invalid argument exception the value of [autoDeferredPhotoDeliverySupported](isautodeferredphotodeliverysupported.md) is [false](../../swift/false.md).

## See Also

### Managing responsive capture

- [captureReadiness](capturereadiness-swift.property.md) — A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [CaptureReadiness](capturereadiness-swift.enum.md) — Constants that indicate whether the output is ready to receive capture requests.
- [autoDeferredPhotoDeliverySupported](isautodeferredphotodeliverysupported.md) — A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [fastCapturePrioritizationSupported](isfastcaptureprioritizationsupported.md) — A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [fastCapturePrioritizationEnabled](isfastcaptureprioritizationenabled.md) — A Boolean value that indicates whether the output enables fast capture prioritization.
- [responsiveCaptureSupported](isresponsivecapturesupported.md) — A Boolean value that indicates whether the photo output supports responsive capture.
- [responsiveCaptureEnabled](isresponsivecaptureenabled.md) — A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [zeroShutterLagSupported](iszeroshutterlagsupported.md) — A Boolean value that indicates whether the photo output supports zero shutter lag.
- [zeroShutterLagEnabled](iszeroshutterlagenabled.md) — A Boolean value that indicates whether the photo output configuration enables zero shutter lag.
