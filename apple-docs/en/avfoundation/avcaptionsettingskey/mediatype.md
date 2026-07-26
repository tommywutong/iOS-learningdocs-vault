---
title: mediaType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionsettingskey/mediatype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/mediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionsettingskey/mediatype.json'
content_hash: 'sha256:90246f0ab9f46759'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionSettingsKey](../avcaptionsettingskey.md)

# mediaType

<sub>Type Property</sub>

A key that identifies the output media type of a caption conversion operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let mediaType: AVCaptionSettingsKey
```

## Discussion

This includes the media types [AVMediaTypeClosedCaption](../avmediatype/closedcaption.md) or [AVMediaTypeSubtitle](../avmediatype/subtitle.md), for example.

## See Also

### Keys

- [AVCaptionMediaSubTypeKey](mediasubtype.md) — A key that identifies the output media subtype of a caption conversion operation.
- [AVCaptionTimeCodeFrameDurationKey](timecodeframeduration.md) — A key that identifies the frame duration that the system uses for the time code.
- [AVCaptionUseDropFrameTimeCodeKey](usedropframetimecode.md) — A key that identifies whether the system uses drop frame time code.
