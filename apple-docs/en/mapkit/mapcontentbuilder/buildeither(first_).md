---
title: 'buildEither(first:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontentbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontentbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:1a3297028e9fa06c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContentBuilder](../mapcontentbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Compares content in a multistatement closure, resulting in use of the conditional content if the first argument you provide evaluates to  true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalMapContent<TrueContent, FalseContent> where TrueContent : MapContent, FalseContent : MapContent
```

## Parameters

- `first` — The content that represents the `true` content element to compare against.

## Return Value

Returns the conditional map content that meets the conditions the content builder expresses.

## See Also

### Conditionally building map content

- [buildEither(second:)](<buildeither(second_).md>) — Compares content in a multistatement closure, resulting in use of the conditional content if the second argument you provide evaluates to true.
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the map content builder.
- [buildIf(_:)](<buildif(__).md>) — Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.
