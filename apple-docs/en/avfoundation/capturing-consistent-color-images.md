---
title: Capturing consistent color images
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capturing-consistent-color-images
source_url: 'https://developer.apple.com/documentation/avfoundation/capturing-consistent-color-images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capturing-consistent-color-images.json'
content_hash: 'sha256:24306926edd5e44e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Photo capture](photo-capture.md)

# Capturing consistent color images

<sub>Sample Code</sub>

Add the power of a photography studio and lighting rig to your app with the new Constant Color API.

## Overview

> [!note] Note
> This sample code project is associated with WWDC24 session 10162: [Capturing consistent color images](https://developer.apple.com/wwdc24/10162/).

### Configure the sample code project

Run this sample code on a device that provides the required flash module, such as the following:

- iPhone 14 or later
- iPhone 14 Pro or later
- iPad Pro 11-inch (M4) or later
- iPad Pro 13-inch (M4) or later

## See Also

### Photo capture

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

## Download

- [CapturingConsistentColorImages.zip](https://docs-assets.developer.apple.com/published/abe78d7af292/CapturingConsistentColorImages.zip)
