---
title: Text.TruncationMode
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/truncationmode
source_url: 'https://developer.apple.com/documentation/swiftui/text/truncationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/truncationmode.json'
content_hash: 'sha256:5edb0226f3966d2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# Text.TruncationMode

<sub>Enumeration</sub>

The type of truncation to apply to a line of text when it’s too long to fit in the available space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TruncationMode
```

## Overview

When a text view contains more text than it’s able to display, the view might truncate the text and place an ellipsis (…) at the truncation point. Use the [truncationMode(_:)](<../view/truncationmode(__).md>) modifier with one of the `TruncationMode` values to indicate which part of the text to truncate, either at the beginning, in the middle, or at the end.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting text truncation modes

- [Text.TruncationMode.head](truncationmode/head.md) — Truncate at the beginning of the line.
- [Text.TruncationMode.middle](truncationmode/middle.md) — Truncate in the middle of the line.
- [Text.TruncationMode.tail](truncationmode/tail.md) — Truncate at the end of the line.

## See Also

### Fitting text into available space

- [textScale(_:isEnabled:)](<textscale(__isenabled_).md>) — Applies a text scale to the text.
- [Scale](scale.md) — Defines text scales
