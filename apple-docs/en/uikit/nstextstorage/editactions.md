---
title: NSTextStorage.EditActions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/editactions
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/editactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/editactions.json'
content_hash: 'sha256:92652859e0917c36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# NSTextStorage.EditActions

<sub>Structure</sub>

Constants that indicate the types of changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct EditActions
```

## Overview

These values are also OR’ed together in notifications to inform instances of `NSLayoutManager` was changed—see [textStorage(_:edited:range:changeInLength:invalidatedRange:)](<../../appkit/nslayoutmanager/textstorage(__edited_range_changeinlength_invalidatedrange_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSTextStorageEditedAttributes](editactions/editedattributes.md) — Attributes were added, removed, or changed.
- [NSTextStorageEditedCharacters](editactions/editedcharacters.md) — Characters were added, removed, or replaced.

### Initializers

- [init(rawValue:)](<editactions/init(rawvalue_).md>)
