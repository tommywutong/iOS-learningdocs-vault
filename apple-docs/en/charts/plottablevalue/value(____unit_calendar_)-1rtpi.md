---
title: 'value(_:_:unit:calendar:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/plottablevalue/value(_:_:unit:calendar:)-1rtpi'
source_url: 'https://developer.apple.com/documentation/charts/plottablevalue/value(_:_:unit:calendar:)-1rtpi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plottablevalue/value%28_%3A_%3Aunit%3Acalendar%3A%29-1rtpi.json'
content_hash: 'sha256:aea8d90bb916b710'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [PlottableValue](../plottablevalue.md)

# value(_:_:unit:calendar:)

<sub>Type Method</sub>

Creates a parameter value with label and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func value(_ labelResource: LocalizedStringResource, _ date: Date, unit: Calendar.Component, calendar: Calendar? = nil) -> PlottableValue<Value> where Value == Date
```

## Parameters

- `labelResource` — The localized string resource for label.
