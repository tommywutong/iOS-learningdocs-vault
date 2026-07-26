---
title: AttributeScopes.AccessibilityAttributes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes.json'
content_hash: 'sha256:74388bebdcb8b5e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeScopes](../attributescopes.md)

# AttributeScopes.AccessibilityAttributes

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityAttributes
```

## Relationships

- **Conforms To**: [AttributeScope](../attributescope.md), [DecodingConfigurationProviding](../decodingconfigurationproviding.md), [EncodingConfigurationProviding](../encodingconfigurationproviding.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [accessibilityHeadingLevel](accessibilityattributes/accessibilityheadinglevel.md)
- [accessibilitySpeechAdjustedPitch](accessibilityattributes/accessibilityspeechadjustedpitch.md)
- [accessibilitySpeechAnnouncementPriority](accessibilityattributes/accessibilityspeechannouncementpriority.md)
- [accessibilitySpeechAnnouncementsQueued](accessibilityattributes/accessibilityspeechannouncementsqueued.md) _(deprecated)_
- [accessibilitySpeechIncludesPunctuation](accessibilityattributes/accessibilityspeechincludespunctuation.md)
- [accessibilitySpeechPhoneticNotation](accessibilityattributes/accessibilityspeechphoneticnotation.md)
- [accessibilitySpeechSpellsOutCharacters](accessibilityattributes/accessibilityspeechspellsoutcharacters.md)
- [accessibilityTextCustom](accessibilityattributes/accessibilitytextcustom.md)
- [accessibilityTextualContext](accessibilityattributes/accessibilitytextualcontext.md)

### Enumerations

- [AdjustedPitchAttribute](accessibilityattributes/adjustedpitchattribute.md) — An attribute to adjust the pitch the spoken speech.
- [AnnouncementPriorityAttribute](accessibilityattributes/announcementpriorityattribute.md) — An attribute to define the urgency of the announcement.
- [HeadingLevelAttribute](accessibilityattributes/headinglevelattribute.md) — An attribute for the level of this heading.
- [IPANotationAttribute](accessibilityattributes/ipanotationattribute.md) — An attribute to define the International Phonetic Alphabet representation for speech.
- [IncludesPunctuationAttribute](accessibilityattributes/includespunctuationattribute.md) — An attribute to define how punctuation should be spoken.
- [QueueAnnouncementAttribute](accessibilityattributes/queueannouncementattribute.md) — An attribute to define if speech announcements spoken by VoiceOver should be queued behind existing speech rather than interrupting speech in progress. _(deprecated)_
- [SpellOutAttribute](accessibilityattributes/spelloutattribute.md) — An attribute to define if each character should be spoken separately.
- [TextCustomAttribute](accessibilityattributes/textcustomattribute.md) — An attribute for custom, localized text attributes.
- [TextualContextAttribute](accessibilityattributes/textualcontextattribute.md) — An attribute for the textual context.
