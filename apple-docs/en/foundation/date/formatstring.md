---
title: Date.FormatString
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstring
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstring.json'
content_hash: 'sha256:be405941f78de61d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.FormatString

<sub>Structure</sub>

A type that represents a fixed date format string using string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatString
```

## Overview

Use `Date.FormatString` with [VerbatimFormatStyle](verbatimformatstyle.md) or [ParseStrategy](parsestrategy.md) to create fixed-pattern format strings for dates. You build format strings using string interpolation with date field symbols:

```swift
let format: Date.FormatString = "\(year: .defaultDigits)-\(month: .twoDigits)-\(day: .twoDigits)"
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](../../swift/expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Default Implementations

- [ExpressibleByStringInterpolation Implementations](formatstring/expressiblebystringinterpolation-implementations.md)
