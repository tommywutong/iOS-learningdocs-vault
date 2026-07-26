---
title: UIAccessibilitySpeechAttributeQueueAnnouncement
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+（1.0 起废弃）, watchOS 4.0+]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiaccessibilityspeechattributequeueannouncement
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityspeechattributequeueannouncement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityspeechattributequeueannouncement.json'
content_hash: 'sha256:e8fde1a640cf8baf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilitySpeechAttributeQueueAnnouncement

<sub>Global Variable</sub>

A key that indicates whether to queue an announcement behind existing speech or to interrupt it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const UIAccessibilitySpeechAttributeQueueAnnouncement;
```

## Overview

The value of this key is an [NSNumber](../foundation/nsnumber.md) object that the system interprets as a Boolean value. When the value is `YES`, the system queues the announcement behind existing speech. When the value is `NO`, the announcement interrupts the existing speech. The default behavior is to interrupt existing speech.

## See Also

### Constants

- [UIAccessibilitySpeechAttributePunctuation](uiaccessibilityspeechattributepunctuation.md) — A key that indicates whether to speak punctuation.
- [UIAccessibilitySpeechAttributeLanguage](uiaccessibilityspeechattributelanguage.md) — A key that indicates the language to use when speaking a string.
- [UIAccessibilitySpeechAttributePitch](uiaccessibilityspeechattributepitch.md) — A key that indicates the pitch to apply to spoken content.
- [UIAccessibilitySpeechAttributeIPANotation](uiaccessibilityspeechattributeipanotation.md) — A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [UIAccessibilitySpeechAttributeAnnouncementPriority](uiaccessibilityspeechattributeannouncementpriority.md)
- [UIAccessibilitySpeechAttributeSpellOut](uiaccessibilityspeechattributespellout.md)
- [UIAccessibilityPriority](uiaccessibilitypriority.md) — Constants that specify priorities for accessibility announcements.
