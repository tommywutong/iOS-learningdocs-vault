---
title: PersonNameComponents.FormatStyle.Style
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponents/formatstyle/style-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/style-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatstyle/style-swift.enum.json'
content_hash: 'sha256:236c4a5cb494869e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [PersonNameComponents](../../personnamecomponents.md) · [FormatStyle](../formatstyle.md)

# PersonNameComponents.FormatStyle.Style

<sub>Enumeration</sub>

The type that represents the style of the formatted result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Style
```

## Overview

The style type describes a length of the string representation of the name. The available values are [PersonNameComponents.FormatStyle.Style.long](style-swift.enum/long.md), [PersonNameComponents.FormatStyle.Style.medium](style-swift.enum/medium.md), [PersonNameComponents.FormatStyle.Style.short](style-swift.enum/short.md), and [PersonNameComponents.FormatStyle.Style.abbreviated](style-swift.enum/abbreviated.md).

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [PersonNameComponents.FormatStyle.Style.abbreviated](style-swift.enum/abbreviated.md) — Specifies an abbreviated person name components style.
- [PersonNameComponents.FormatStyle.Style.long](style-swift.enum/long.md) — Specifies a long person name components style.
- [PersonNameComponents.FormatStyle.Style.medium](style-swift.enum/medium.md) — Specifies a medium person name components style.
- [PersonNameComponents.FormatStyle.Style.short](style-swift.enum/short.md) — Specifies a short person name components style.

## See Also

### Modifying a Format Style

- [style](style-swift.property.md) — Specifies the style of the formatted result.
- [locale](locale.md) — The locale to use when formatting the person name components.
- [attributed](attributed.md) — The style used to create a locale-aware attributed string representation of an instance of person name components.
- [locale(_:)](<locale(__).md>) — Modifies the person name components format style to use the specified locale.
