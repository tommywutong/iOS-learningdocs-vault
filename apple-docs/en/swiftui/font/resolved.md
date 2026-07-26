---
title: Font.Resolved
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/font/resolved
source_url: 'https://developer.apple.com/documentation/swiftui/font/resolved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/resolved.json'
content_hash: 'sha256:c39b461e7960235b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# Font.Resolved

<sub>Structure</sub>

A concrete font value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Resolved
```

## Overview

`Font.Resolved` is a concrete representation of a Font that can be shown, with a specific set of `EnvironmentValues`. A `Resolved` font will always map to the same CTFont on a given platform.

> [!info] See Also
> [Font](../font.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [ctFont](resolved/ctfont.md) — Returns the CTFont opaque type that represents a CoreText font object.
- [isBold](resolved/isbold.md) — Returns `true` if the resolved font has a bold trait according to CoreText or the font’s weight is semi-bold or greater.
- [isItalic](resolved/isitalic.md) — Returns `true` if the resolved font is italic.
- [isLowercaseSmallCaps](resolved/islowercasesmallcaps.md) — Returns `true` if the resolved font’s lowercased characters use small caps.
- [isMonospaced](resolved/ismonospaced.md) — Returns `true` if a resolved font is monospaced, false otherwise.
- [isSmallCaps](resolved/issmallcaps.md) — Returns `true` if all of the resolved font’s characters use small caps.
- [isUppercaseSmallCaps](resolved/isuppercasesmallcaps.md) — Returns `true` if the resolved font’s uppercased characters use small caps.
- [leading](resolved/leading.md) — The leading of a resolved font.
- [pointSize](resolved/pointsize.md) — The point size of a resolved font.
- [weight](resolved/weight.md) — The weight of a resolved font.
- [width](resolved/width.md) — The width of a resolved font.
