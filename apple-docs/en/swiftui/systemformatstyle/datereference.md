---
title: SystemFormatStyle.DateReference
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/systemformatstyle/datereference
source_url: 'https://developer.apple.com/documentation/swiftui/systemformatstyle/datereference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/systemformatstyle/datereference.json'
content_hash: 'sha256:1e7c0b8211c76f07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SystemFormatStyle](../systemformatstyle.md)

# SystemFormatStyle.DateReference

<sub>Structure</sub>

A format style that refers to a date using the most natural phrasing based on how much time separates it from the current time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DateReference
```

## Overview

`DateReference` adapts its output based on how far the referenced date is from the input (which is typically the current time). Close dates use a relative representation, while distant dates switch to an absolute one.

```swift
// Displays "in 5 minutes", "tomorrow", "June 2019", etc.
Text(.currentDate, format: .reference(to: eventDate))
```

### Relative vs. absolute representation

The style uses a relative format (“in 2 hours”, “3 days ago”) when the referenced date is within the threshold distance. Beyond that threshold, it switches to an absolute format (“Monday, June 3”, “June 2019”).

The `thresholdField` parameter controls where this switch happens. With the default value of `.day`, the style uses the relative format as long as the date falls within approximately one month of the reference date:

| Distance | Style | Output |
|---|---|---|
| \< 1 min | Relative | `now` |
| 5 min | Relative | `in 5 minutes` |
| 3 hours | Relative | `in 3 hours` |
| 1 day | Relative | `tomorrow` |
| 3 days | Relative | `3 days ago` |
| 27 days | Relative | `27 days ago` |
| \> 1 month | Absolute | `Monday, June 3` |
| \> 1 year | Absolute | `June 2019` |

### Controlling the absolute representation

The `maxFieldCount` parameter determines how many date components appear in the absolute representation:

```swift
// maxFieldCount: 2 (default)
// Output for a date in a different year: "June 2019"

// maxFieldCount: 3
.reference(to: date, maxFieldCount: 3)
// Output: "June 3, 2019"
```

The style automatically removes higher-order fields that match the reference date. For a date within the same year, the year field is dropped, leaving room for day-level detail:

```swift
// Same year as reference date, maxFieldCount: 2
// Output: "Monday, June 3" (instead of "June 2019")
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [DiscreteFormatStyle](../../foundation/discreteformatstyle.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../../foundation/formatstyle.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(to:allowedFields:maxFieldCount:thresholdField:)](<datereference/init(to_allowedfields_maxfieldcount_thresholdfield_).md>) — Creates a format style that refers to a comparison date using natural language.

### Instance Methods

- [calendar(_:)](<datereference/calendar(__).md>)
