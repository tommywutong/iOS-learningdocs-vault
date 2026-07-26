---
title: Additional data capture
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/additional-data-capture
source_url: 'https://developer.apple.com/documentation/avfoundation/additional-data-capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/additional-data-capture.json'
content_hash: 'sha256:bfc9ffb3ee012bd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Additional data capture

<sub>API Collection</sub>

Capture additional data including depth and metadata, and synchronize capture from multiple outputs.

## Topics

### Depth data capture

- [Capturing photos with depth](capturing-photos-with-depth.md) — Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Creating auxiliary depth data manually](creating-auxiliary-depth-data-manually.md) — Generate a depth image and attach it to your own image.
- [Capturing depth using the LiDAR camera](capturing-depth-using-the-lidar-camera.md) — Access the LiDAR camera on supporting devices to capture precise depth data.
- [AVCamFilter: Applying filters to a capture stream](avcamfilter-applying-filters-to-a-capture-stream.md) — Render a capture stream with rose-colored filtering and depth effects.
- [Streaming depth data from the TrueDepth camera](streaming-depth-data-from-the-truedepth-camera.md) — Visualize depth data in 2D and 3D from the TrueDepth camera.
- [Enhancing live video by leveraging TrueDepth camera data](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — Apply your own background to a live capture feed streamed from the front-facing TrueDepth camera.
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — A capture output that records scene depth information on compatible camera devices.
- [AVDepthData](avdepthdata.md) — A container for per-pixel distance or disparity information captured by compatible camera devices.
- [AVCameraCalibrationData](avcameracalibrationdata.md) — Information about the camera characteristics used to capture images and depth data.

### Metadata capture

- [AVCaptureMetadataInput](avcapturemetadatainput.md) — A capture input for providing timed metadata to a capture session.
- [AVCaptureMetadataOutput](avcapturemetadataoutput.md) — A capture output for processing timed metadata produced by a capture session.
- [AVMetadataObject](avmetadataobject.md) — The abstract superclass for objects provided by a metadata capture output.
- [Metadata types](metadata-types.md) — Inspect the supported metadata object types that the framework supports.

### Synchronized capture

- [AVCaptureDataOutputSynchronizer](avcapturedataoutputsynchronizer.md) — An object that coordinates time-matched delivery of data from multiple capture outputs.
- [AVCaptureSynchronizedDataCollection](avcapturesynchronizeddatacollection.md) — A set of data samples collected simultaneously from multiple capture outputs.
- [AVCaptureSynchronizedSampleBufferData](avcapturesynchronizedsamplebufferdata.md) — A container for video or audio samples collected using synchronized capture.
- [AVCaptureSynchronizedMetadataObjectData](avcapturesynchronizedmetadataobjectdata.md) — A container for metadata objects collected using synchronized capture.
- [AVCaptureSynchronizedDepthData](avcapturesynchronizeddepthdata.md) — A container for scene depth information collected using synchronized capture.
- [AVCaptureSynchronizedData](avcapturesynchronizeddata.md) — The abstract superclass for media samples collected using synchronized capture.

## See Also

### Capture

- [Capture setup](capture-setup.md) — Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Photo capture](photo-capture.md) — Capture high-quality still images, Live Photos, and supporting photo data.
- [Audio and video capture](audio-and-video-capture.md) — Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.
