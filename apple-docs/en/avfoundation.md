---
title: AVFoundation
framework: AVFoundation
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.2+, iPadOS 13.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation
source_url: 'https://developer.apple.com/documentation/avfoundation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation.json'
content_hash: 'sha256:135f88661d56ad84'
translated: false
---

> Navigation: [Technologies](technologies.md)

# AVFoundation

<sub>Framework</sub>

Work with audiovisual assets, control device cameras, process audio, and configure system audio interactions.

## Overview

AVFoundation combines several major technology areas that together encompass a wide range of tasks for inspecting, playing, capturing, and processing audiovisual media on Apple platforms.

## Topics

### Essentials

- [AVFoundation updates](updates/avfoundation.md) — Learn about important changes to AVFoundation.

### Common

- [Media assets](avfoundation/media-assets.md) — Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.
- [Media reading and writing](avfoundation/media-reading-and-writing.md) — Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- [Media types and utilities](avfoundation/media-types-and-utilities.md) — Identify the types of content and file formats that AVFoundation supports.
- [Video settings](avfoundation/video-settings.md) — Configure video processing settings using standard key and value constants.
- [Audio settings](avfoundation/audio-settings.md) — Configure audio processing settings using standard key and value constants.

### Playback

- [Media playback](avfoundation/media-playback.md) — Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Offline playback and storage](avfoundation/offline-playback-and-storage.md) — Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.
- [Streaming and AirPlay](avfoundation/streaming-and-airplay.md) — Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.
- [Sample buffer playback](avfoundation/sample-buffer-playback.md) — Create custom controllers to play and synchronize the timing of sample buffer streams.

### Capture

- [Capture setup](avfoundation/capture-setup.md) — Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Photo capture](avfoundation/photo-capture.md) — Capture high-quality still images, Live Photos, and supporting photo data.
- [Audio and video capture](avfoundation/audio-and-video-capture.md) — Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.
- [Additional data capture](avfoundation/additional-data-capture.md) — Capture additional data including depth and metadata, and synchronize capture from multiple outputs.

### Editing

- [Composite assets](avfoundation/composite-assets.md) — Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- [QuickTime movies](avfoundation/quicktime-movies.md) — Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.
- [Video effects](avfoundation/video-effects.md) — Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.
- [Audio mixing](avfoundation/audio-mixing.md) — Define how to mix the audio levels from multiple audio tracks over an asset’s duration.

### Audio

- [Audio playback, recording, and processing](avfoundation/audio-playback-recording-and-processing.md) — Play, record, and process audio; configure your app’s system audio behavior.
- [Speech synthesis](avfoundation/speech-synthesis.md) — Configure voices to speak strings of text.

### Errors

- [AVFoundationErrorDomain](avfoundation/avfoundationerrordomain.md) — The error domain of AVFoundation errors.
- [AVError](avfoundation/averror-swift.struct.md) — A structure that defines the errors that framework operations can generate.

### Macros

- [Macros](avfoundation/avfoundation-macros.md)
