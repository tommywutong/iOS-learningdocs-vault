---
title: DateFormatter.Style
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/style
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/style.json'
content_hash: 'sha256:d328a1d4359b2aa4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# DateFormatter.Style

<sub>Enumeration</sub>

The following constants specify predefined format styles for dates and times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Style
```

## Overview

The format for these date and time styles is not exact because they depend on the locale, user preference settings, and the operating system version. Do not use these constants if you want an exact format.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSDateFormatterNoStyle](style/none.md)
- [NSDateFormatterShortStyle](style/short.md)
- [NSDateFormatterMediumStyle](style/medium.md)
- [NSDateFormatterLongStyle](style/long.md)
- [NSDateFormatterFullStyle](style/full.md)

### Initializers

- [init(rawValue:)](<style/init(rawvalue_).md>)

## See Also

### Constants

- [Behavior](behavior.md) — Constants that specify the behavior `NSDateFormatter` should exhibit.
