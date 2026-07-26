---
title: Cinematic
framework: Cinematic
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cinematic
source_url: 'https://developer.apple.com/documentation/cinematic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cinematic.json'
content_hash: 'sha256:bc4d894c13548d31'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Cinematic

<sub>Framework</sub>

Integrate playback and editing of assets captured in Cinematic mode into your app.

## Overview

The Cinematic framework enables you to add professional-level editing and playback features to movies, recorded with the Camera app’s Cinematic mode, to your apps. These are the same features used in applications such as Final Cut Pro, Photos, and iMovie. For example, this enables your apps to change focus distance and aperture in movies, creating a bokeh effect, even after recording.

## Topics

### Essentials

- [Playing and editing Cinematic mode video](cinematic/playing-and-editing-cinematic-mode-video.md) — Play and edit Cinematic mode video with an adjustable depth of field and focus points.
- [CNScript](cinematic/cnscript-1ispe.md) — A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.

### Reading and rendering

- [CNAssetInfo](cinematic/cnassetinfo-2ata2.md) — An object that provides Cinematic-specific information about an asset, including its tracks.
- [CNCompositionInfo](cinematic/cncompositioninfo-7eunn.md) — An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [CNRenderingSession](cinematic/cnrenderingsession-1hzh8.md) — An object representing the context in which rendering occurs.

### Editing

- [Editing Spatial Audio with an audio mix](cinematic/editing-spatial-audio-with-an-audio-mix.md) — Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.
- [CNDetection](cinematic/cndetection-swift.struct.md) — A structure that represents a detected subject, face, torso or pet at a particular time.
- [CNDecision](cinematic/cndecision-swift.struct.md) — An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [CNDetectionTrack](cinematic/cndetectiontrack-2bxtd.md) — An object representing a series of detections of the same subject over time.
- [CNFixedDetectionTrack](cinematic/cnfixeddetectiontrack-93rrw.md) — An object representing the fixed detection track.
- [CNCustomDetectionTrack](cinematic/cncustomdetectiontrack-9a2zo.md) — An object representing a discrete detection track composed of individual detections.
- [CNDetectionType](cinematic/cndetectiontype.md) — The type of object detected, such as face, torso, cat, dog and so on.

### Custom Object Tracking

- [CNBoundsPrediction](cinematic/cnboundsprediction-swift.struct.md) — A structure representing the bounds of the predicted subject.
- [CNObjectTracker](cinematic/cnobjecttracker-1n598.md) — An object that converts a normalized point or rectangle into a detection track that tracks an object over time.

### Structures

- [CNCinematicError](cinematic/cncinematicerror.md)

### Reference

- [Cinematic Enumerations](cinematic/cinematic-enumerations.md)
- [Cinematic Constants](cinematic/cinematic-constants.md)
- [Cinematic Data Types](cinematic/cinematic-data-types.md)

### Classes

- [CNAssetSpatialAudioInfo](cinematic/cnassetspatialaudioinfo-7hdev.md)
- [CNImageRenderingSession](cinematic/cnimagerenderingsession.md) — A session for rendering a shallow depth-of-field (SDoF) effect onto still images using Metal. _(beta)_
- [CNImageRenderingSessionConfiguration](cinematic/cnimagerenderingsessionconfiguration.md) — Configuration for a CNImageRenderingSession, specifying the rendering quality and algorithm version. _(beta)_

### Enumerations

- [CNSpatialAudioContentType](cinematic/cnspatialaudiocontenttype.md)
- [CNSpatialAudioRenderingStyle](cinematic/cnspatialaudiorenderingstyle.md)
