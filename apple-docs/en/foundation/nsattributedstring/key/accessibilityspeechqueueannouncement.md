---
title: accessibilitySpeechQueueAnnouncement
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+（1.0 起废弃）, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/accessibilityspeechqueueannouncement
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityspeechqueueannouncement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/accessibilityspeechqueueannouncement.json'
content_hash: 'sha256:c49a01c970e02b97'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# accessibilitySpeechQueueAnnouncement

<sub>Type Property</sub>

A key that indicates whether to queue an announcement behind existing speech or to interrupt it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let accessibilitySpeechQueueAnnouncement: NSAttributedString.Key
```

## Discussion

The value of this key is an [NSNumber](../../nsnumber.md) object that the system interprets as a Boolean value. When the value is [true](../../../swift/true.md), the system queues the announcement behind existing speech. When the value is [false](../../../swift/false.md), the announcement interrupts the existing speech. The default behavior is to interrupt existing speech.

## See Also

### Getting accessibility attribute keys

- [accessibilityAlignment](accessibilityalignment.md)
- [accessibilityAnnotationTextAttribute](accessibilityannotationtextattribute.md)
- [accessibilityAttachment](accessibilityattachment.md) — Text attachment (`id`). _(deprecated)_
- [accessibilityAutocorrected](accessibilityautocorrected.md) — Autocorrected text (`NSNumber` as a Boolean value).
- [accessibilityBackgroundColor](accessibilitybackgroundcolor.md) — Text background color (`CGColorRef`).
- [accessibilityCustomText](accessibilitycustomtext.md)
- [accessibilityFont](accessibilityfont.md) — Font keys (`NSDictionary`).
- [accessibilityFontBoldAttribute](accessibilityfontboldattribute.md)
- [accessibilityFontItalicAttribute](accessibilityfontitalicattribute.md)
- [accessibilityForegroundColor](accessibilityforegroundcolor.md) — Text foreground color (`CGColorRef`).
- [accessibilityLanguage](accessibilitylanguage.md)
- [accessibilityLink](accessibilitylink.md) — Text link (`id`).
- [accessibilityListItemIndex](accessibilitylistitemindex.md)
- [accessibilityListItemLevel](accessibilitylistitemlevel.md)
- [accessibilityListItemPrefix](accessibilitylistitemprefix.md)
