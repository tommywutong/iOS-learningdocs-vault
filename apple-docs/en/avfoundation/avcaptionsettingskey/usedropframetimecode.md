---
title: useDropFrameTimeCode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionsettingskey/usedropframetimecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/usedropframetimecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionsettingskey/usedropframetimecode.json'
content_hash: 'sha256:0660455b6522300d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionSettingsKey](../avcaptionsettingskey.md)

# useDropFrameTimeCode

<sub>Type Property</sub>

A key that identifies whether the system uses drop frame time code.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let useDropFrameTimeCode: AVCaptionSettingsKey
```

## Discussion

Some formats, such as SCC, use time code notation to indicate the timing of a caption. Use the property to specify whether the system uses the drop frame time code or non-drop frame time code.

The default is [false](../../swift/false.md).

## See Also

### Keys

- [AVCaptionMediaTypeKey](mediatype.md) — A key that identifies the output media type of a caption conversion operation.
- [AVCaptionMediaSubTypeKey](mediasubtype.md) — A key that identifies the output media subtype of a caption conversion operation.
- [AVCaptionTimeCodeFrameDurationKey](timecodeframeduration.md) — A key that identifies the frame duration that the system uses for the time code.
