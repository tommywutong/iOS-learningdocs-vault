---
title: UIAccessibilityPriority
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitypriority
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitypriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitypriority.json'
content_hash: 'sha256:4f2568431eef26da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityPriority

<sub>Structure</sub>

Constants that specify priorities for accessibility announcements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIAccessibilityPriority
```

## Overview

Use these constants either with the [accessibilitySpeechAnnouncementPriority](../foundation/attributescopes/accessibilityattributes/accessibilityspeechannouncementpriority.md) property of [AttributedString](../foundation/attributedstring.md), or with the [UIAccessibilitySpeechAttributeAnnouncementPriority](uiaccessibilityspeechattributeannouncementpriority.md) attributed key. For example, the following code shows how to create an announcement with a [UIAccessibilityPriorityHigh](uiaccessibilitypriority/high.md) announcement priority:

```swift
let highPriorityAnnouncement = NSAttributedString(string: "Camera active", attributes:
[NSAttributedString.Key.accessibilitySpeechAnnouncementPriority: UIAccessibilityPriority.high])
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Choosing a priority

- [UIAccessibilityPriorityHigh](uiaccessibilitypriority/high.md) — A high-priority announcement that interrupts other speech and isn’t interruptible after it starts.
- [UIAccessibilityPriorityDefault](uiaccessibilitypriority/default.md) — A default-priority announcement that interrupts existing speech, but is interruptible if a new speech utterance starts.
- [UIAccessibilityPriorityLow](uiaccessibilitypriority/low.md) — A low-priority announcement that the system queues and speaks after other speech utterances are complete.

### Creating a priority

- [init(rawValue:)](<uiaccessibilitypriority/init(rawvalue_).md>) — Creates a priority structure with the specified raw value.

## See Also

### Constants

- [accessibilitySpeechPunctuation](../foundation/nsattributedstring/key/accessibilityspeechpunctuation.md) — A key that indicates whether to speak punctuation.
- [accessibilitySpeechLanguage](../foundation/nsattributedstring/key/accessibilityspeechlanguage.md) — A key that indicates the language to use when speaking a string.
- [accessibilitySpeechPitch](../foundation/nsattributedstring/key/accessibilityspeechpitch.md) — A key that indicates the pitch to apply to spoken content.
- [accessibilitySpeechQueueAnnouncement](../foundation/nsattributedstring/key/accessibilityspeechqueueannouncement.md) — A key that indicates whether to queue an announcement behind existing speech or to interrupt it. _(deprecated)_
- [accessibilitySpeechIPANotation](../foundation/nsattributedstring/key/accessibilityspeechipanotation.md) — A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [accessibilitySpeechAnnouncementPriority](../foundation/nsattributedstring/key/accessibilityspeechannouncementpriority.md)
- [accessibilitySpeechSpellOut](../foundation/nsattributedstring/key/accessibilityspeechspellout.md)
