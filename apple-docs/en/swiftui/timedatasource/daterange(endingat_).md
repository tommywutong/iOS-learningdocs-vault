---
title: 'dateRange(endingAt:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timedatasource/daterange(endingat:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timedatasource/daterange(endingat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timedatasource/daterange%28endingat%3A%29.json'
content_hash: 'sha256:7ed6f0db50eee1c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimeDataSource](../timedatasource.md)

# dateRange(endingAt:)

<sub>Type Method</sub>

A time data source that produces `min(date, Date.now)..<date`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func dateRange(endingAt date: Date) -> TimeDataSource<Range<Date>>
```
