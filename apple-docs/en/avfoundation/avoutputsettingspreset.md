---
title: AVOutputSettingsPreset
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingspreset
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingspreset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingspreset.json'
content_hash: 'sha256:e44cccefc5ab6868'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVOutputSettingsPreset

<sub>Structure</sub>

A structure that defines preset configurations for an output settings assistant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVOutputSettingsPreset
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Presets

- [AVOutputSettingsPreset640x480](avoutputsettingspreset/preset640x480.md) — A preset for H.264 video at 640 by 480 pixels.
- [AVOutputSettingsPreset960x540](avoutputsettingspreset/preset960x540.md) — A preset for H.264 video at 960 by 540 pixels.
- [AVOutputSettingsPreset1280x720](avoutputsettingspreset/preset1280x720.md) — A preset for H.264 video at 1280 by 720 pixels.
- [AVOutputSettingsPreset1920x1080](avoutputsettingspreset/preset1920x1080.md) — A preset for H.264 video at 1920 by 1080 pixels.
- [AVOutputSettingsPreset3840x2160](avoutputsettingspreset/preset3840x2160.md) — A preset for H.264 video at 3840 by 2160 pixels.
- [AVOutputSettingsPresetHEVC1920x1080WithAlpha](avoutputsettingspreset/hevc1920x1080withalpha.md) — A preset for HEVC with Alpha video at 1920 by 1080 pixels.
- [AVOutputSettingsPresetHEVC1920x1080](avoutputsettingspreset/hevc1920x1080.md) — A preset for HEVC video at 1920 by 1080 pixels.
- [AVOutputSettingsPresetHEVC3840x2160WithAlpha](avoutputsettingspreset/hevc3840x2160withalpha.md) — A preset for HEVC with Alpha video at 3840 by 2160 pixels.
- [AVOutputSettingsPresetHEVC3840x2160](avoutputsettingspreset/hevc3840x2160.md) — A preset for HEVC video at 3840 by 2160 pixels.
- [AVOutputSettingsPresetHEVC4320x2160](avoutputsettingspreset/hevc4320x2160.md)
- [AVOutputSettingsPresetHEVC7680x4320](avoutputsettingspreset/hevc7680x4320.md) — A preset for HEVC video at 7680 by 4320 pixels.
- [AVOutputSettingsPresetMVHEVC1440x1440](avoutputsettingspreset/mvhevc1440x1440.md) — A preset for MV-HEVC video at 1440 by 1440 pixels.
- [AVOutputSettingsPresetMVHEVC4320x4320](avoutputsettingspreset/mvhevc4320x4320.md)
- [AVOutputSettingsPresetMVHEVC7680x7680](avoutputsettingspreset/mvhevc7680x7680.md)
- [AVOutputSettingsPresetMVHEVC960x960](avoutputsettingspreset/mvhevc960x960.md) — A preset for MV-HEVC video at 960 by 960 pixels.

### Initializers

- [init(rawValue:)](<avoutputsettingspreset/init(rawvalue_).md>) — Creates a preset with a string value.

## See Also

### Creating an assistant

- [+ outputSettingsAssistantWithPreset:](<avoutputsettingsassistant/init(preset_).md>) — Creates an output setting assistant with a preset configuration.
- [+ availableOutputSettingsPresets](<avoutputsettingsassistant/availableoutputsettingspresets().md>) — Returns an array of preset values to use to initialize an output settings assistant.
