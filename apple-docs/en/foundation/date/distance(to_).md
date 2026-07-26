---
title: 'distance(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/distance(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/distance%28to%3A%29.json'
content_hash: 'sha256:039e3da880cc983f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance from this date to another date, specified as a time interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: Date) -> TimeInterval
```

## Parameters

- `other` — Another date.

## Return Value

The distance from this date to the other date, as a [TimeInterval](../timeinterval.md).

## See Also

### Comparing Dates

- [==(_:_:)](<==(____).md>) — Returns true if the two `Date` values represent the same point in time.
- [\>(_:_:)](<_(____)-880ns.md>) — Returns true if the left hand `Date` is later in time than the right hand `Date`.
- [\<(_:_:)](<_(____)-42kro.md>) — Returns true if the left hand `Date` is earlier in time than the right hand `Date`.
- [compare(_:)](<compare(__).md>) — Compares another date to this one.
