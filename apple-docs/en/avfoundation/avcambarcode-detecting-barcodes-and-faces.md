---
title: 'AVCamBarcode: detecting barcodes and faces'
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcambarcode-detecting-barcodes-and-faces
source_url: 'https://developer.apple.com/documentation/avfoundation/avcambarcode-detecting-barcodes-and-faces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcambarcode-detecting-barcodes-and-faces.json'
content_hash: 'sha256:f67254dbb5ab1d85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md)

# AVCamBarcode: detecting barcodes and faces

<sub>Sample Code</sub>

Identify machine readable codes or faces by using the camera.

## Overview

> [!note] Note
> This sample code project is associated with WWDC21 session [10047: What’s New in Camera Capture](https://developer.apple.com/videos/play/wwdc21/10047/).

## See Also

### Capture sessions

- [Setting up a capture session](setting-up-a-capture-session.md) — Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md) — Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Build a responsive camera app that launches quickly](build-a-responsive-camera-app-that-launches-quickly.md) — Build a fast camera launch experience for your iOS and iPadOS apps.
- [Capturing Cinematic video](capturing-cinematic-video.md) — Capture video with an adjustable depth of field and focus points.
- [Supporting Center Stage front camera in your iOS app](supporting-center-stage-front-camera-in-your-ios-app.md) — Enable Center Stage for photos and videos on the iPhone front camera.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md) — Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCaptureSession](avcapturesession.md) — An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [AVCaptureInput](avcaptureinput.md) — An abstract superclass for objects that provide input data to a capture session.
- [AVCaptureOutput](avcaptureoutput.md) — An abstract superclass for objects that provide media output destinations for a capture session.
- [AVCaptureConnection](avcaptureconnection.md) — An object that represents a connection from a capture input to a capture output.

## Download

- [AVCamBarcodeDetectingBarcodesAndFaces.zip](https://docs-assets.developer.apple.com/published/306f40997d58/AVCamBarcodeDetectingBarcodesAndFaces.zip)
