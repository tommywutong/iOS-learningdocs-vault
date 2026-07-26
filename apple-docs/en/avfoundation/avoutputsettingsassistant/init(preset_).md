---
title: 'init(preset:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avoutputsettingsassistant/init(preset:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/init(preset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avoutputsettingsassistant/init%28preset%3A%29.json'
content_hash: 'sha256:15997911c064346d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVOutputSettingsAssistant](../avoutputsettingsassistant.md)

# init(preset:)

<sub>Initializer</sub>

Creates an output setting assistant with a preset configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(preset presetIdentifier: AVOutputSettingsPreset)
```

## Discussion

- presetIdentifier: A preset configuration for the object.

## See Also

### Creating an assistant

- [AVOutputSettingsPreset](../avoutputsettingspreset.md) — A structure that defines preset configurations for an output settings assistant.
- [+ availableOutputSettingsPresets](<availableoutputsettingspresets().md>) — Returns an array of preset values to use to initialize an output settings assistant.
