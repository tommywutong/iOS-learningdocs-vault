---
title: Font.Leading
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/font/leading
source_url: 'https://developer.apple.com/documentation/swiftui/font/leading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/leading.json'
content_hash: 'sha256:0a4c066832622b6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# Font.Leading

<sub>Enumeration</sub>

A line spacing adjustment that you can apply to a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Leading
```

## Overview

Apply one of the `Leading` values to a font using the [leading(_:)](<leading(__).md>) method to increase or decrease the line spacing.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting leading line spacing options

- [Font.Leading.standard](leading/standard.md) — The font’s default line spacing.
- [Font.Leading.loose](leading/loose.md) — Increased line spacing.
- [Font.Leading.tight](leading/tight.md) — Reduced line spacing.

## See Also

### Styling a font

- [bold()](<bold().md>) — Adds bold or emphasized styling to the font.
- [italic()](<italic().md>) — Adds italics to the font.
- [monospaced()](<monospaced().md>) — Returns a fixed-width font from the same family as the base font.
- [monospacedDigit()](<monospaceddigit().md>) — Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [smallCaps()](<smallcaps().md>) — Adjusts the font to enable all small capitals.
- [lowercaseSmallCaps()](<lowercasesmallcaps().md>) — Adjusts the font to enable lowercase small capitals.
- [uppercaseSmallCaps()](<uppercasesmallcaps().md>) — Adjusts the font to enable uppercase small capitals.
- [weight(_:)](<weight(__).md>) — Sets the weight of the font.
- [width(_:)](<width(__).md>) — Sets the width of the font.
- [Width](width.md) — A width to use for fonts that have multiple widths.
- [leading(_:)](<leading(__).md>) — Adjusts the line spacing of a font.
