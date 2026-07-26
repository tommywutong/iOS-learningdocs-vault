---
title: 'init(CMTimeRange:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(cmtimerange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(cmtimerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28cmtimerange%3A%29.json'
content_hash: 'sha256:80fd5a93f93ec819'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(CMTimeRange:)

<sub>Initializer</sub>

Creates a new value object containing the specified CoreMedia time range structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(CMTimeRange timeRange: CMTimeRange)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(timeRange: CMTimeRange)
```

## Parameters

- `timeRange` — The value for the new object.

## Return Value

A new value object that contains the time range information.

## See Also

### Related Documentation

- [CMTimeRange](../../coremedia/cmtimerange.md) — A structure that represents a time range.

### Working with Media Time Values

- [+ valueWithCMTime:](<init(cmtime_).md>) — Creates a new value object containing the specified CoreMedia time structure.
- [+ valueWithCMTimeMapping:](<init(cmtimemapping_).md>) — Creates a new value object containing the specified CoreMedia time mapping structure.
- [CMTimeValue](timevalue.md) — The CoreMedia time structure representation of the value.
- [CMTimeRangeValue](timerangevalue.md) — The CoreMedia time range structure representation of the value.
- [CMTimeMappingValue](timemappingvalue.md) — The CoreMedia time mapping structure representation of the value.
