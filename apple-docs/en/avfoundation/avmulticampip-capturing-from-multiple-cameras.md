---
title: 'AVMultiCamPiP: Capturing from Multiple Cameras'
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmulticampip-capturing-from-multiple-cameras
source_url: 'https://developer.apple.com/documentation/avfoundation/avmulticampip-capturing-from-multiple-cameras'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmulticampip-capturing-from-multiple-cameras.json'
content_hash: 'sha256:638b7bb45c2da892'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md)

# AVMultiCamPiP: Capturing from Multiple Cameras

<sub>Sample Code</sub>

Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.

## Overview

> [!note] Note
> This sample code project is associated with WWDC 2019 session [225: Advances in Camera Capture & Portrait Segmentation](https://developer.apple.com/videos/play/wwdc19/225/).

### Configure the sample code project

You must run this sample code on one of these devices:

- An iPhone with an A12 or later processor
- An iPad Pro with an A12X or later processor

## See Also

### Capture sessions

- [Setting up a capture session](setting-up-a-capture-session.md) — Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md) — Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Build a responsive camera app that launches quickly](build-a-responsive-camera-app-that-launches-quickly.md) — Build a fast camera launch experience for your iOS and iPadOS apps.
- [Capturing Cinematic video](capturing-cinematic-video.md) — Capture video with an adjustable depth of field and focus points.
- [Supporting Center Stage front camera in your iOS app](supporting-center-stage-front-camera-in-your-ios-app.md) — Enable Center Stage for photos and videos on the iPhone front camera.
- [AVCamBarcode: detecting barcodes and faces](avcambarcode-detecting-barcodes-and-faces.md) — Identify machine readable codes or faces by using the camera.
- [AVCaptureSession](avcapturesession.md) — An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [AVCaptureInput](avcaptureinput.md) — An abstract superclass for objects that provide input data to a capture session.
- [AVCaptureOutput](avcaptureoutput.md) — An abstract superclass for objects that provide media output destinations for a capture session.
- [AVCaptureConnection](avcaptureconnection.md) — An object that represents a connection from a capture input to a capture output.

## Download

- [AVMultiCamPiPCapturingFromMultipleCameras.zip](https://docs-assets.developer.apple.com/published/cc1a2216fde0/AVMultiCamPiPCapturingFromMultipleCameras.zip)
