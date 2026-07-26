---
title: UITextDirection
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdirection
source_url: 'https://developer.apple.com/documentation/uikit/uitextdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdirection.json'
content_hash: 'sha256:400bb8ccc598a982'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDirection

<sub>Structure</sub>

The direction of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UITextDirection
```

## Overview

This parameter is used in methods declared by the [UITextInputTokenizer](uitextinputtokenizer.md) protocol. This general direction type subsumes constants of the [UITextStorageDirection](uitextstoragedirection.md) and [UITextLayoutDirection](uitextlayoutdirection.md) types.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Text direction types

- [layout(_:)](<uitextdirection/layout(__).md>) — Specifies the direction of text layout.
- [storage(_:)](<uitextdirection/storage(__).md>) — Specifies the direction of text storage.

### Initializers

- [init(rawValue:)](<uitextdirection/init(rawvalue_).md>) — Creates a text direction with the specified raw value.

## See Also

### Constants

- [UITextStorageDirection](uitextstoragedirection.md) — The direction of text storage.
- [UITextLayoutDirection](uitextlayoutdirection.md) — The direction of text layout.
