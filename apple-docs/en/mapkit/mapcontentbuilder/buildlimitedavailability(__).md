---
title: 'buildLimitedAvailability(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 1.2+, watchOS 10.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontentbuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontentbuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:1aabaf3659fc7acf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContentBuilder](../mapcontentbuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildLimitedAvailability(_ content: any MapContent) -> some MapContent

```

## Parameters

- `content` — The map builder content the expression builder operates on.

## Return Value

Returns the conditional map content that meets the conditions the content builder expresses.

## See Also

### Conditionally building map content

- [buildEither(first:)](<buildeither(first_).md>) — Compares content in a multistatement closure, resulting in use of the conditional content if the first argument you provide evaluates to  true.
- [buildEither(second:)](<buildeither(second_).md>) — Compares content in a multistatement closure, resulting in use of the conditional content if the second argument you provide evaluates to true.
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the map content builder.
- [buildIf(_:)](<buildif(__).md>) — Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.
