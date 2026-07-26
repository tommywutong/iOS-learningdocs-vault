---
title: 'dateRange(startingAt:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timedatasource/daterange(startingat:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timedatasource/daterange(startingat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timedatasource/daterange%28startingat%3A%29.json'
content_hash: 'sha256:d658081a482ec897'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimeDataSource](../timedatasource.md)

# dateRange(startingAt:)

<sub>Type Method</sub>

A time data source that produces `date..<max(date, Date.now)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func dateRange(startingAt date: Date) -> TimeDataSource<Range<Date>>
```
