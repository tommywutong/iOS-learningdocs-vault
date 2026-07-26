---
title: NSTextList.Options
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlist/options
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist/options.json'
content_hash: 'sha256:85d0ab94a2b9657f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextList](../nstextlist.md)

# NSTextList.Options

<sub>Structure</sub>

Values that available options for text list items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Options

- [NSTextListPrependEnclosingMarker](options/prependenclosingmarker.md) — Specifies that a nested list should include the marker for its enclosing superlist before its own marker.

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>) — Returns a new set of text list options using the raw value you specify.

## See Also

### Getting list options

- [ordered](isordered.md) — A Boolean value that indicates whether the list is ordered.
- [listOptions](listoptions.md) — Returns the list options mask value of the receiver.
