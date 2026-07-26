---
title: TimeDataSource
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/timedatasource
source_url: 'https://developer.apple.com/documentation/swiftui/timedatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timedatasource.json'
content_hash: 'sha256:595e8f63b3fff990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TimeDataSource

<sub>Structure</sub>

A source of time related data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TimeDataSource<Value>
```

## Overview

Instances of this type provide [Text](text.md) with live and automatically updating values in Widgets, Live Activities, watchOS Complications, and of course regular apps.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [currentDate](timedatasource/currentdate.md) — A time data source that produces `Date.now`.

### Type Methods

- [dateRange(endingAt:)](<timedatasource/daterange(endingat_).md>) — A time data source that produces `min(date, Date.now)..<date`.
- [dateRange(startingAt:)](<timedatasource/daterange(startingat_).md>) — A time data source that produces `date..<max(date, Date.now)`.
- [durationOffset(to:)](<timedatasource/durationoffset(to_).md>) — A time data source that produces the offset between `Date.now` and the given `date` as a `Duration`.

## See Also

### Formatting date and time

- [SystemFormatStyle](systemformatstyle.md) — A collection of format styles for displaying live-updating time information in text views.
