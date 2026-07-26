---
title: 'speechAdjustedPitch(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/speechadjustedpitch(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/speechadjustedpitch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/speechadjustedpitch%28_%3A%29.json'
content_hash: 'sha256:a2208f1c7b31e50a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# speechAdjustedPitch(_:)

<sub>Instance Method</sub>

Raises or lowers the pitch of spoken text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func speechAdjustedPitch(_ value: Double) -> some View

```

## Parameters

- `value` — The amount to raise or lower the pitch. Values between `-1` and `0` result in a lower pitch while values between `0` and `1` result in a higher pitch. The method clamps values to the range `-1` to `1`.

## Discussion

Use this modifier when you want to change the pitch of spoken text. The value indicates how much higher or lower to change the pitch.

## See Also

### Configuring VoiceOver

- [speechAlwaysIncludesPunctuation(_:)](<speechalwaysincludespunctuation(__).md>) — Sets whether VoiceOver should always speak all punctuation in the text view.
- [speechAnnouncementsQueued(_:)](<speechannouncementsqueued(__).md>) — Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [speechSpellsOutCharacters(_:)](<speechspellsoutcharacters(__).md>) — Sets whether VoiceOver should speak the contents of the text view character by character.
