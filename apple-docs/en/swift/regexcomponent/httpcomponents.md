---
title: httpComponents
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexcomponent/httpcomponents
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/httpcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/httpcomponents.json'
content_hash: 'sha256:1b7677848a81dbac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# httpComponents

<sub>Type Property</sub>

Creates a regex component to match an HTTP date and time, such as “2015-11-14’T’15:05:03’Z’”, and capture the string as a `DateComponents` using the time zone as specified in the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var httpComponents: DateComponents.HTTPFormatStyle { get }
```
