---
title: 'speechAlwaysIncludesPunctuation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/speechalwaysincludespunctuation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/speechalwaysincludespunctuation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/speechalwaysincludespunctuation%28_%3A%29.json'
content_hash: 'sha256:570b5d1fb5973891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# speechAlwaysIncludesPunctuation(_:)

<sub>Instance Method</sub>

Sets whether VoiceOver should always speak all punctuation in the text view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func speechAlwaysIncludesPunctuation(_ value: Bool = true) -> Text
```

## Parameters

- `value` — A Boolean value that you set to `true` if VoiceOver should speak all punctuation in the text. Defaults to `true`.

## Discussion

Use this modifier to control whether the system speaks punctuation characters in the text. You might use this for code or other text where the punctuation is relevant, or where you want VoiceOver to speak a verbatim transcription of the text you provide. For example, given the text:

```swift
Text("All the world's a stage, " +
     "And all the men and women merely players;")
     .speechAlwaysIncludesPunctuation()
```

VoiceOver would speak “All the world apostrophe s a stage comma and all the men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## See Also

### Configuring voiceover

- [speechAdjustedPitch(_:)](<speechadjustedpitch(__).md>) — Raises or lowers the pitch of spoken text.
- [speechAnnouncementsQueued(_:)](<speechannouncementsqueued(__).md>) — Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](<speechspellsoutcharacters(__).md>) — Sets whether VoiceOver should speak the contents of the text view character by character.
