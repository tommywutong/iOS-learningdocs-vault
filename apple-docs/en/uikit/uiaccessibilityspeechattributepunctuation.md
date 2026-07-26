---
title: UIAccessibilitySpeechAttributePunctuation
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityspeechattributepunctuation
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributepunctuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityspeechattributepunctuation.json'
content_hash: 'sha256:13de8b5e1919267f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilitySpeechAttributePunctuation

<sub>Global Variable</sub>

A key that indicates whether to speak punctuation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const UIAccessibilitySpeechAttributePunctuation;
```

## Overview

The value of this key is an [NSNumber](../foundation/nsnumber.md) object that the system interprets as a Boolean value. When the value is `YES`, the assistive app speaks all punctuation in the text. You might use this for code or other text where the punctuation is relevant.

## See Also

### Constants

- [UIAccessibilitySpeechAttributeLanguage](uiaccessibilityspeechattributelanguage.md) — A key that indicates the language to use when speaking a string.
- [UIAccessibilitySpeechAttributePitch](uiaccessibilityspeechattributepitch.md) — A key that indicates the pitch to apply to spoken content.
- [UIAccessibilitySpeechAttributeQueueAnnouncement](uiaccessibilityspeechattributequeueannouncement.md) — A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [UIAccessibilitySpeechAttributeIPANotation](uiaccessibilityspeechattributeipanotation.md) — A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [UIAccessibilitySpeechAttributeAnnouncementPriority](uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeSpellOut](uiaccessibilityspeechattributespellout.md)
- [UIAccessibilityPriority](uiaccessibilitypriority.md) — Constants that specify priorities for accessibility announcements.
