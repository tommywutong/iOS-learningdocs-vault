---
title: Audio and video capture
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/audio-and-video-capture
source_url: 'https://developer.apple.com/documentation/avfoundation/audio-and-video-capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/audio-and-video-capture.json'
content_hash: 'sha256:651c6645091338df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Audio and video capture

<sub>API Collection</sub>

Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.

## Topics

### File capture

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md) — Change the default format for capturing movie files.
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — A capture output that records video and audio to a QuickTime movie file.
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — A capture output that records audio and saves the recorded audio to a file.
- [AVCaptureFileOutput](avcapturefileoutput.md) — The abstract superclass for capture outputs that can record captured data to a file.
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — Methods for monitoring or controlling the output of a media file capture.
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — Methods for responding to events that occur while recording captured media to a file.

### Stream capture

- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md) — Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) — A capture output that records video and provides access to video frames for processing.
- [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md) — A capture output that records audio and provides access to audio sample buffers as they are recorded.
- [AVCaptureSpatialAudioMetadataSampleGenerator](avcapturespatialaudiometadatasamplegenerator.md) — An interface for generating a spatial audio timed metadata sample.

### Mac screen capture

- [AVCaptureScreenInput](avcapturescreeninput.md) — A capture input for recording from a screen in macOS.

### Broadcast video output

- [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) — [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) is a subclass of [AVCaptureOutput](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode) _(beta)_
- [AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md) — Protocol for receiving broadcast video output events and data. _(beta)_

## See Also

### Capture

- [Capture setup](capture-setup.md) — Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Photo capture](photo-capture.md) — Capture high-quality still images, Live Photos, and supporting photo data.
- [Additional data capture](additional-data-capture.md) — Capture additional data including depth and metadata, and synchronize capture from multiple outputs.
