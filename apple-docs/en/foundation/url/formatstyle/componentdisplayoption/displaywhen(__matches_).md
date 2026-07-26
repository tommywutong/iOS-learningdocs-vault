---
title: 'displayWhen(_:matches:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/formatstyle/componentdisplayoption/displaywhen(_:matches:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption/displaywhen(_:matches:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/componentdisplayoption/displaywhen%28_%3Amatches%3A%29.json'
content_hash: 'sha256:9194e526850469eb'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [FormatStyle](../../formatstyle.md) · [ComponentDisplayOption](../componentdisplayoption.md)

# displayWhen(_:matches:)

<sub>Type Method</sub>

Returns a display option that displays the component when a specified component meets the specified requirements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func displayWhen(_ component: URL.FormatStyle.Component, matches requirements: Set<String>) -> URL.FormatStyle.ComponentDisplayOption
```

## Parameters

- `component` — A component to compare. This may or may not be the component the strategy modifies. For example, a display option for the query might match against known values for the path.

- `requirements` — A set of string values to match against. Matching any member of the set allows the format style to display the component.

## Return Value

A display option that displays the component when a specified component meets the specified requirements.

## See Also

### Display options

- [always](always.md) — A display option that always displays the component.
- [never](never.md) — A display option that never displays the component.
- [omitIfHTTPFamily](omitifhttpfamily.md) — A display option that omits the component if the URL scheme is any flavor of HTTP.
- [omitWhen(_:matches:)](<omitwhen(__matches_).md>) — Returns a display option that omits the component when a specified component meets the specified requirements.
- [Component](../component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.
