---
title: Immersive Media Support
framework: Immersive Media Support
symbol_kind: module
role: collection
role_heading: Framework
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/immersivemediasupport
source_url: 'https://developer.apple.com/documentation/immersivemediasupport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/immersivemediasupport.json'
content_hash: 'sha256:9fa904f607a0f402'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Immersive Media Support

<sub>Framework</sub>

Read and write essential Apple Immersive Video metadata.

## Overview

Immersive Media Support enables you to create custom workflows for processing Apple Immersive Video (AIV). Use it to read and write AIV-specific metadata and enable previewing content in editorial workflows.

## Topics

### Essentials

- [Authoring Apple Immersive Video](immersivemediasupport/authoring-apple-immersive-video.md) — Prepare and package immersive video content for delivery.
- [Processing Apple Immersive Video with foveation](immersivemediasupport/processing-apple-immersive-video-with-foveation.md) — Reduce a video’s data rate while maintaining high acuity in the center of the imagery by applying foveation to immersive video content.

### Camera metadata

- [VenueDescriptor](immersivemediasupport/venuedescriptor.md) — The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- [ImmersiveCamera](immersivemediasupport/immersivecamera.md) — A structure that holds the required information for an immersive media camera to process and render video frames.
- [ImmersiveCameraLensDefinition](immersivemediasupport/immersivecameralensdefinition.md) — This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.
- [ImmersiveCameraCalibration](immersivemediasupport/immersivecameracalibration.md) — A structure that represents immersive media camera calibration data.
- [ImmersiveCameraMask](immersivemediasupport/immersivecameramask.md) — A structure that holds the camera mask type information and its relevant mask name.
- [ImmersiveDynamicMask](immersivemediasupport/immersivedynamicmask.md) — A type that holds the information required to dynamically generate an immersive media mask at load time.
- [ImmersiveImageMask](immersivemediasupport/immersiveimagemask.md) — An object that holds all the information needed to load immersive media masks from image data or from a file.

### Presentation commands

- [PresentationCommand](immersivemediasupport/presentationcommand.md) — A set of properties that define the interface for a presentation command.
- [FadeCommand](immersivemediasupport/fadecommand.md) — A command type for color fading during immersive media playback.
- [FadeEnvironmentCommand](immersivemediasupport/fadeenvironmentcommand.md) — A command type for opacity fading environment backdrops during immersive media playback.
- [SetCameraCommand](immersivemediasupport/setcameracommand.md) — A command type for immersive camera switching during playback.
- [ShotFlopCommand](immersivemediasupport/shotflopcommand.md) — A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [ShotFlipCommand](immersivemediasupport/shotflipcommand.md) — A command type to flip the video frames vertically during playback for the duration of the command. _(beta)_
- [PresentationDescriptor](immersivemediasupport/presentationdescriptor.md) — A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [PresentationDescriptorReader](immersivemediasupport/presentationdescriptorreader.md) — An object that provides the functionality required to understand and process immersive presentation commands.

### Parametric immersive support

- [ParametricImmersiveAssetInfo](immersivemediasupport/parametricimmersiveassetinfo.md) — An object that helps convert the original wide field of view video asset to parametric immersive asset.

### Immersive video rendering support

- [ImmersiveVideoFrame](immersivemediasupport/immersivevideoframe.md) — A type that represents an immersive video frame, including its layout, presentation time, and pixel buffer data.
- [ImmersiveCameraViewModel](immersivemediasupport/immersivecameraviewmodel.md) — A view model that holds all the resources needed to render an immersive camera view.
- [ImmersiveVideoMask](immersivemediasupport/immersivevideomask.md) — A video mask to use during video rendering to smooth the edges of the mesh.

### Preview

- [ImmersiveMediaPreviewMessagingProtocol](immersivemediasupport/immersivemediapreviewmessagingprotocol.md) — An object that represents the messaging protocol a remote preview sender and receiver use to communicate.
- [ImmersiveMediaRemotePreviewSender](immersivemediasupport/immersivemediaremotepreviewsender.md) — An observable object that helps an app send the required data to all connected receiver applications to help facilitate the complete preview of the immersive media playback.
- [ImmersiveMediaRemotePreviewReceiver](immersivemediasupport/immersivemediaremotepreviewreceiver.md) — An observable object that helps applications handle receiving commands and data sent from an immersive media remote preview sender object.
- [ImmersivePreviewRenderer](immersivemediasupport/immersivepreviewrenderer.md) — An object that renders an immersive video frame into a texture and exposes the command buffer for presentation. _(beta)_

### Validation

- [AIVUValidator](immersivemediasupport/aivuvalidator.md) — A type to validate existing AIVU files to ensure that they meet the minimum requirements for AIV.
