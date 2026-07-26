---
title: Deprecated symbols
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput-deprecated-symbols.json'
content_hash: 'sha256:3fcdeb77b8d12d5f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Photo capture](photo-capture.md) · [AVCapturePhotoOutput](avcapturephotooutput.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Getting formatted output

- [+ JPEGPhotoDataRepresentationForJPEGSampleBuffer:previewPhotoSampleBuffer:](<avcapturephotooutput/jpegphotodatarepresentation(forjpegsamplebuffer_previewphotosamplebuffer_).md>) — Returns data in JPEG format corresponding to the captured photo in the specified sample buffer. _(deprecated)_
- [+ DNGPhotoDataRepresentationForRawSampleBuffer:previewPhotoSampleBuffer:](<avcapturephotooutput/dngphotodatarepresentation(forrawsamplebuffer_previewphotosamplebuffer_).md>) — Returns data in digital negative (DNG) format corresponding to the captured RAW photo in the specified sample buffer. _(deprecated)_

### Configuring dual camera capture

- [dualCameraFusionSupported](avcapturephotooutput/isdualcamerafusionsupported.md) — A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device. _(deprecated)_
- [dualCameraDualPhotoDeliverySupported](avcapturephotooutput/isdualcameradualphotodeliverysupported.md) — A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device. _(deprecated)_
- [dualCameraDualPhotoDeliveryEnabled](avcapturephotooutput/isdualcameradualphotodeliveryenabled.md) — A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device. _(deprecated)_

### Configuring high-resolution still capture

- [highResolutionCaptureEnabled](avcapturephotooutput/ishighresolutioncaptureenabled.md) — A Boolean value that specifies whether to configure the capture pipeline for high resolution still image capture. _(deprecated)_

### Monitoring the visible scene

- [isStillImageStabilizationScene](avcapturephotooutput/isstillimagestabilizationscene.md) — A Boolean value indicating whether the scene currently being previewed by the camera warrants image stabilization. _(deprecated)_

### Determining available settings

- [stillImageStabilizationSupported](avcapturephotooutput/isstillimagestabilizationsupported.md) — A Boolean value indicating whether the capture output currently supports automatic stabilization for still image capture. _(deprecated)_
