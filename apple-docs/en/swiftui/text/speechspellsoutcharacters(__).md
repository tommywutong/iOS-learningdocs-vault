---
title: 'speechSpellsOutCharacters(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/speechspellsoutcharacters(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/speechspellsoutcharacters(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/speechspellsoutcharacters%28_%3A%29.json'
content_hash: 'sha256:ce4af07284ab5e83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# speechSpellsOutCharacters(_:)

<sub>Instance Method</sub>

Sets whether VoiceOver should speak the contents of the text view character by character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func speechSpellsOutCharacters(_ value: Bool = true) -> Text
```

## Parameters

- `value` — A Boolean value that when `true` indicates VoiceOver should speak text as individual characters. Defaults to `true`.

## Discussion

Use this modifier when you want VoiceOver to speak text as individual letters, character by character. This is important for text that is not meant to be spoken together, like:

- An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.
- A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## See Also

### Configuring voiceover

- [speechAdjustedPitch(_:)](<speechadjustedpitch(__).md>) — Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](<speechalwaysincludespunctuation(__).md>) — Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](<speechannouncementsqueued(__).md>) — Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
