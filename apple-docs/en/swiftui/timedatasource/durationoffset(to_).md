---
title: 'durationOffset(to:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/timedatasource/durationoffset(to:)'
source_url: 'https://developer.apple.com/documentation/swiftui/timedatasource/durationoffset(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/timedatasource/durationoffset%28to%3A%29.json'
content_hash: 'sha256:12aa2553b6e0e02d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TimeDataSource](../timedatasource.md)

# durationOffset(to:)

<sub>Type Method</sub>

A time data source that produces the offset between `Date.now` and the given `date` as a `Duration`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func durationOffset(to date: Date) -> TimeDataSource<Duration>
```
