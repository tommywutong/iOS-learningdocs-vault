---
title: Date.RelativeFormatStyle.UnitsStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/unitsstyle-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/unitsstyle-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/unitsstyle-swift.struct.json'
content_hash: 'sha256:182241255faaae0a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# Date.RelativeFormatStyle.UnitsStyle

<sub>Structure</sub>

A type that represents the style to use when formatting the units of relative dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnitsStyle
```

## Overview

Cases include [wide](unitsstyle-swift.struct/wide.md), [narrow](unitsstyle-swift.struct/narrow.md), [abbreviated](unitsstyle-swift.struct/abbreviated.md) and [spellOut](unitsstyle-swift.struct/spellout.md).

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Modifying a Relative Date Format Units Style

- [abbreviated](unitsstyle-swift.struct/abbreviated.md) — A style that uses abbreviated units, such as “2 mo. ago”.
- [narrow](unitsstyle-swift.struct/narrow.md) — A style that uses the shortest units, such as “2 mo. ago”.
- [spellOut](unitsstyle-swift.struct/spellout.md) — A style that spells out units, such as “two months ago”.
- [wide](unitsstyle-swift.struct/wide.md) — A style that uses full representation of units, such as “2 months ago”.

### Comparing Relative Date Format Units Styles

- [==(_:_:)](<../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

## See Also

### Supporting Types

- [Presentation](presentation-swift.struct.md) — A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
