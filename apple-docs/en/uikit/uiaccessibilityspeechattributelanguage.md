---
title: UIAccessibilitySpeechAttributeLanguage
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityspeechattributelanguage
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributelanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityspeechattributelanguage.json'
content_hash: 'sha256:582d729e8f57b2b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilitySpeechAttributeLanguage

<sub>Global Variable</sub>

A key that indicates the language to use when speaking a string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const UIAccessibilitySpeechAttributeLanguage;
```

## Discussion

The value of this key is an [NSString](../foundation/nsstring.md) object that contains a BCP 47 language code. When applying it to text in a string, the rules for the specified language govern how to pronounce that string.

## See Also

### Constants

- [UIAccessibilitySpeechAttributePunctuation](uiaccessibilityspeechattributepunctuation.md) — A key that indicates whether to speak punctuation.
- [UIAccessibilitySpeechAttributePitch](uiaccessibilityspeechattributepitch.md) — A key that indicates the pitch to apply to spoken content.
- [UIAccessibilitySpeechAttributeQueueAnnouncement](uiaccessibilityspeechattributequeueannouncement.md) — A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [UIAccessibilitySpeechAttributeIPANotation](uiaccessibilityspeechattributeipanotation.md) — A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [UIAccessibilitySpeechAttributeAnnouncementPriority](uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeSpellOut](uiaccessibilityspeechattributespellout.md)
- [UIAccessibilityPriority](uiaccessibilitypriority.md) — Constants that specify priorities for accessibility announcements.
