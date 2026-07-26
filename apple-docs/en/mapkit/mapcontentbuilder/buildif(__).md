---
title: 'buildIf(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontentbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontentbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:5412391f7aa37a58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContentBuilder](../mapcontentbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildIf<Content>(_ content: Content?) -> Content? where Content : MapContent
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
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.
