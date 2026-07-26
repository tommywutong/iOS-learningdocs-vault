---
title: Photo capture
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/photo-capture
source_url: 'https://developer.apple.com/documentation/avfoundation/photo-capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/photo-capture.json'
content_hash: 'sha256:35c5337625d69daa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Photo capture

<sub>API Collection</sub>

Capture high-quality still images, Live Photos, and supporting photo data.

## Topics

### Photo capture

- [Capturing consistent color images](capturing-consistent-color-images.md) — Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md) — Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md) — Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../appkit/supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [AVCapturePhoto](avcapturephoto.md) — A container for image data from a photo capture output.
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [AVCapturePhotoOutput](avcapturephotooutput.md) — A capture output for still image, Live Photos, and other photography workflows.
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — Methods for monitoring progress and receiving results from a photo capture output.
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — An object that monitors changes to a photo output’s capture readiness.
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — A delegate protocol to receive updates about a photo output’s capture readiness.
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — A capture output for capturing still photos. _(deprecated)_

### Photo settings

- [AVCapturePhotoSettings](avcapturephotosettings.md) — A specification of the features and settings to use for a single photo capture request.
- [AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md) — A specification of the features and settings to use for a photo capture request that captures multiple images with varied settings.
- [AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md) — A description of the features and settings in use for an in-progress or complete photo capture request.

### Matte data

- [AVPortraitEffectsMatte](avportraiteffectsmatte.md) — An auxiliary image used to separate foreground from background with high resolution.
- [AVSemanticSegmentationMatte](avsemanticsegmentationmatte.md) — An object that wraps a matting image for a particular semantic segmentation.

## See Also

### Capture

- [Capture setup](capture-setup.md) — Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Audio and video capture](audio-and-video-capture.md) — Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.
- [Additional data capture](additional-data-capture.md) — Capture additional data including depth and metadata, and synchronize capture from multiple outputs.
