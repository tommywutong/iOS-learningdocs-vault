---
title: timeCodeFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionsettingskey/timecodeframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/timecodeframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionsettingskey/timecodeframeduration.json'
content_hash: 'sha256:149948ed3734afd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionSettingsKey](../avcaptionsettingskey.md)

# timeCodeFrameDuration

<sub>Type Property</sub>

A key that identifies the frame duration that the system uses for the time code.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let timeCodeFrameDuration: AVCaptionSettingsKey
```

## Discussion

Some formats, such as TTML, use time code notation to indicate the timing of a caption. Use this key to specify the frame rate of the time code.

## See Also

### Keys

- [AVCaptionMediaTypeKey](mediatype.md) — A key that identifies the output media type of a caption conversion operation.
- [AVCaptionMediaSubTypeKey](mediasubtype.md) — A key that identifies the output media subtype of a caption conversion operation.
- [AVCaptionUseDropFrameTimeCodeKey](usedropframetimecode.md) — A key that identifies whether the system uses drop frame time code.
