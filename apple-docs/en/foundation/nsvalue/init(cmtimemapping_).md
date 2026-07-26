---
title: 'init(CMTimeMapping:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(cmtimemapping:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(cmtimemapping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28cmtimemapping%3A%29.json'
content_hash: 'sha256:ff153fba0bb8cbf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(CMTimeMapping:)

<sub>Initializer</sub>

Creates a new value object containing the specified CoreMedia time mapping structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(CMTimeMapping timeMapping: CMTimeMapping)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(timeMapping: CMTimeMapping)
```

## Parameters

- `timeMapping` — The value for the new object.

## Return Value

A new value object that contains the time mapping information.

## See Also

### Related Documentation

- [CMTimeMapping](../../coremedia/cmtimemapping.md) — A structure that maps a segment of a source time range to a target time range.

### Working with Media Time Values

- [+ valueWithCMTime:](<init(cmtime_).md>) — Creates a new value object containing the specified CoreMedia time structure.
- [+ valueWithCMTimeRange:](<init(cmtimerange_).md>) — Creates a new value object containing the specified CoreMedia time range structure.
- [CMTimeValue](timevalue.md) — The CoreMedia time structure representation of the value.
- [CMTimeRangeValue](timerangevalue.md) — The CoreMedia time range structure representation of the value.
- [CMTimeMappingValue](timemappingvalue.md) — The CoreMedia time mapping structure representation of the value.
