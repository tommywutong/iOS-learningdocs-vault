---
title: 'speechAnnouncementsQueued(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/speechannouncementsqueued(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/speechannouncementsqueued(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/speechannouncementsqueued%28_%3A%29.json'
content_hash: 'sha256:c52bb3faa1fcd6e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# speechAnnouncementsQueued(_:)

<sub>Instance Method</sub>

Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func speechAnnouncementsQueued(_ value: Bool = true) -> Text
```

## Parameters

- `value` — A Boolean value that determines if VoiceOver speaks changes to text immediately or enqueues them behind existing speech. Defaults to `true`.

## Discussion

Use this modifier when you want affect the order in which the accessibility system delivers spoken text. Announcements can occur automatically when the label or value of an accessibility element changes.

## See Also

### Configuring voiceover

- [speechAdjustedPitch(_:)](<speechadjustedpitch(__).md>) — Raises or lowers the pitch of spoken text.
- [speechAlwaysIncludesPunctuation(_:)](<speechalwaysincludespunctuation(__).md>) — Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechSpellsOutCharacters(_:)](<speechspellsoutcharacters(__).md>) — Sets whether VoiceOver should speak the contents of the text view character by character.
