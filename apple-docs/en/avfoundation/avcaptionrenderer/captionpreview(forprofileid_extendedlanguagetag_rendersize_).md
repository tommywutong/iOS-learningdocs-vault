---
title: 'captionPreview(forProfileID:extendedLanguageTag:renderSize:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionrenderer/captionpreview(forprofileid:extendedlanguagetag:rendersize:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/captionpreview(forprofileid:extendedlanguagetag:rendersize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/captionpreview%28forprofileid%3Aextendedlanguagetag%3Arendersize%3A%29.json'
content_hash: 'sha256:6327f045eb01b2ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRenderer](../avcaptionrenderer.md)

# captionPreview(forProfileID:extendedLanguageTag:renderSize:)

<sub>Type Method</sub>

Generate a caption preview attributed string for the specified profile ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func captionPreview(forProfileID profileID: String, extendedLanguageTag: String?, renderSize: CGSize) -> NSAttributedString
```

## Parameters

- `profileID` — The identifier of the accessibility profile to use for caption appearance. Profile IDs can be obtained from MACaptionAppearanceCopyProfileIDs(). This determines font, color, background, and other visual characteristics.

- `extendedLanguageTag` — The IETF BCP 47 (RFC 4646) language identifier that will be used to generate the localized caption preview text. If nil, the system language will be used.

- `renderSize` — The size of the layer into which the captions will be rendered. This determines the layout and positioning of the caption text.

## Return Value

An NSAttributedString containing the caption preview.

## Discussion

Returns an attributed string containing a preview of captions rendered using the specified profile ID.

> [!important] Important
> It is strongly recommended that the caller take appropriate measures to prevent blocking essential services such as the user interface, for example, by avoiding calling this method in the main thread.
