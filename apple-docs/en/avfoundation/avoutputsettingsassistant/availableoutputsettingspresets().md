---
title: availableOutputSettingsPresets()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avoutputsettingsassistant/availableoutputsettingspresets()
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/availableoutputsettingspresets()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant/availableoutputsettingspresets%28%29.json'
content_hash: 'sha256:bbf979b6d96d6ba7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVOutputSettingsAssistant](../avoutputsettingsassistant.md)

# availableOutputSettingsPresets()

<sub>Type Method</sub>

Returns an array of preset values to use to initialize an output settings assistant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func availableOutputSettingsPresets() -> [AVOutputSettingsPreset]
```

## Return Value

An array of available output settings presets.

## See Also

### Creating an assistant

- [+ outputSettingsAssistantWithPreset:](<init(preset_).md>) — Creates an output setting assistant with a preset configuration.
- [AVOutputSettingsPreset](../avoutputsettingspreset.md) — A structure that defines preset configurations for an output settings assistant.
