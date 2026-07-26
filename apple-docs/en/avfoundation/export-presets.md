---
title: Export presets
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/export-presets
source_url: 'https://developer.apple.com/documentation/avfoundation/export-presets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/export-presets.json'
content_hash: 'sha256:c862816395769928'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media reading and writing](media-reading-and-writing.md) · [AVAssetExportSession](avassetexportsession.md)

# Export presets

<sub>API Collection</sub>

Configure an export session to output media in standard sizes and formats.

## Overview

Use the preset name constants to initialize an instance of [AVAssetExportSession](avassetexportsession.md).

## Topics

### Quality presets

- [AVAssetExportPresetLowQuality](avassetexportpresetlowquality.md) — A preset to export a low-quality movie file.
- [AVAssetExportPresetMediumQuality](avassetexportpresetmediumquality.md) — A preset to export a medium-quality movie file.
- [AVAssetExportPresetHighestQuality](avassetexportpresethighestquality.md) — A preset to export a high-quality movie file.
- [AVAssetExportPresetHEVCHighestQuality](avassetexportpresethevchighestquality.md) — A preset to export the highest available video quality and HEVC video compression.
- [AVAssetExportPresetHEVCHighestQualityWithAlpha](avassetexportpresethevchighestqualitywithalpha.md) — A preset to export the highest available video quality and HEVC video compression with alpha.

### Size presets

- [AVAssetExportPreset640x480](avassetexportpreset640x480.md) — A preset to export a 640 by 480 movie that contains H.264 video and AAC audio.
- [AVAssetExportPreset960x540](avassetexportpreset960x540.md) — A preset to export a 960 by 540 movie that contains H.264 video and AAC audio.
- [AVAssetExportPreset1280x720](avassetexportpreset1280x720.md) — A preset to export a 1280 by 720 movie that contains H.264 video and AAC audio.
- [AVAssetExportPreset1920x1080](avassetexportpreset1920x1080.md) — A preset to export a 1920 by 1080 movie that contains H.264 video and AAC audio.
- [AVAssetExportPreset3840x2160](avassetexportpreset3840x2160.md) — A preset to export a 3840 by 2160 movie that contains H.264 video and AAC audio.

### HEVC size presets

- [AVAssetExportPresetHEVC1920x1080](avassetexportpresethevc1920x1080.md) — A preset to export a 1920 by 1080 movie that contains HEVC video and AAC audio.
- [AVAssetExportPresetHEVC3840x2160](avassetexportpresethevc3840x2160.md) — A preset to export a 3840 by 2160 movie that contains HEVC video and AAC audio.
- [AVAssetExportPresetHEVC1920x1080WithAlpha](avassetexportpresethevc1920x1080withalpha.md) — A preset to export a 1920 by 1080 movie that contains HEVC video with alpha and AAC audio.
- [AVAssetExportPresetHEVC3840x2160WithAlpha](avassetexportpresethevc3840x2160withalpha.md) — A preset to export a 3840 by 2160 movie that contains HEVC video with alpha and AAC audio.
- [AVAssetExportPresetHEVC4320x2160](avassetexportpresethevc4320x2160.md)
- [AVAssetExportPresetHEVC7680x4320](avassetexportpresethevc7680x4320.md) — A preset to export a 7680 by 4320 movie that contains HEVC video and AAC audio.

### MV-HEVC presets

- [AVAssetExportPresetMVHEVC960x960](avassetexportpresetmvhevc960x960.md) — A preset to export a 960 by 960 movie that contains MV-HEVC video and AAC audio.
- [AVAssetExportPresetMVHEVC1440x1440](avassetexportpresetmvhevc1440x1440.md) — A preset to export a 1440 by 1440 movie that contains MV-HEVC video and AAC audio.
- [AVAssetExportPresetMVHEVC4320x4320](avassetexportpresetmvhevc4320x4320.md)
- [AVAssetExportPresetMVHEVC7680x7680](avassetexportpresetmvhevc7680x7680.md)

### M4V presets

- [AVAssetExportPresetAppleM4V480pSD](avassetexportpresetapplem4v480psd.md) — A preset to export a 480p Standard Definition format suitable for playing on Apple devices.
- [AVAssetExportPresetAppleM4V720pHD](avassetexportpresetapplem4v720phd.md) — A preset to export a 720p High Definition format suitable for playing on Apple devices.
- [AVAssetExportPresetAppleM4V1080pHD](avassetexportpresetapplem4v1080phd.md) — A preset to export a 1080p High Definition format suitable for playing on Apple devices.
- [AVAssetExportPresetAppleM4ViPod](avassetexportpresetapplem4vipod.md) — A preset to export a format suitable for playing on an iPod.
- [AVAssetExportPresetAppleM4VAppleTV](avassetexportpresetapplem4vappletv.md) — A preset to export a format suitable for playing on Apple TV.
- [AVAssetExportPresetAppleM4VCellular](avassetexportpresetapplem4vcellular.md) — A preset to export a format suitable for playing on Apple devices when it streams over a cellular network.
- [AVAssetExportPresetAppleM4VWiFi](avassetexportpresetapplem4vwifi.md) — A preset to export a format suitable for playing on Apple devices it streams over a WiFi network.

### Apple ProRes presets

- [AVAssetExportPresetAppleProRes422LPCM](avassetexportpresetappleprores422lpcm.md) — A preset to export a QuickTime movie with Apple ProRes 422 video and LPCM audio.
- [AVAssetExportPresetAppleProRes4444LPCM](avassetexportpresetappleprores4444lpcm.md) — A preset to export a QuickTime movie with Apple ProRes 4444 video and LPCM audio.

### Passthrough presets

- [AVAssetExportPresetPassthrough](avassetexportpresetpassthrough.md) — A preset to export the asset in its current format, unless otherwise prohibited.

### Audio-only presets

- [AVAssetExportPresetAppleM4A](avassetexportpresetapplem4a.md) — A preset to export an audio-only MPEG 4 Audio file with appropriate iTunes gapless playback data.

## See Also

### Creating an export session

- [- initWithAsset:presetName:](<avassetexportsession/init(asset_presetname_).md>) — Creates an export session with a preset configuration.
