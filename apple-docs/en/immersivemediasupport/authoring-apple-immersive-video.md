---
title: Authoring Apple Immersive Video
framework: Immersive Media Support
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 26.0+, Xcode 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/immersivemediasupport/authoring-apple-immersive-video
source_url: 'https://developer.apple.com/documentation/immersivemediasupport/authoring-apple-immersive-video'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/immersivemediasupport/authoring-apple-immersive-video.json'
content_hash: 'sha256:6ba3961f37084816'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Immersive Media Support](../immersivemediasupport.md)

# Authoring Apple Immersive Video

<sub>Sample Code</sub>

Prepare and package immersive video content for delivery.

## Overview

> [!note] Note
> This sample code project is associated with WWDC25 session 403: [Learn about Apple Immersive Video technologies](https://developer.apple.com/videos/play/wwdc2025/403).

### Configure the sample code project

Running this sample requires [downloading](https://devstreaming-cdn.apple.com/videos/streaming/examples/immersive-media/AIV/Apple_Immersive_Video_Beach.zip) a zip file that contains an example QuickTime movie and supporting content. When the download completes, expand the zip file.

To run the app in Xcode, choose Product \> Scheme \> Edit Scheme, and update the command-line argument paths to reference the downloaded files:

- **`--input`** — An Apple Immersive Video MV-HEVC video file without any necessary metadata.
- **`--aime`** — An `AIME` file with the correct camera calibrations for the provided input file.
- **`--usdz`** — An optional `USDZ` file to use for camera calibration instead of an `AIME` file. This argument also requires the `--mask` option.
- **`--mask`** — An optional dynamic mask JSON data file to use for camera calibration instead of an AIME file. This argument also requires the `--usdz` option.
- **`--output`** — The `AIVU` file to write that contains Immersive Media Support metadata.

## See Also

### Essentials

- [Processing Apple Immersive Video with foveation](processing-apple-immersive-video-with-foveation.md) — Reduce a video’s data rate while maintaining high acuity in the center of the imagery by applying foveation to immersive video content.

## Download

- [AuthoringAppleImmersiveVideo.zip](https://docs-assets.developer.apple.com/published/b64c668d9fd1/AuthoringAppleImmersiveVideo.zip)
