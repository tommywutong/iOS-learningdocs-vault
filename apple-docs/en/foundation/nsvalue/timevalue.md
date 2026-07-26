---
title: timeValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/timevalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/timevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/timevalue.json'
content_hash: 'sha256:13393f8bcf111871'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# timeValue

<sub>Instance Property</sub>

The CoreMedia time structure representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeValue: CMTime { get }
```

## See Also

### Related Documentation

- [CMTime](../../coremedia/cmtime.md) — A structure that represents time.

### Working with Media Time Values

- [+ valueWithCMTime:](<init(cmtime_).md>) — Creates a new value object containing the specified CoreMedia time structure.
- [+ valueWithCMTimeRange:](<init(cmtimerange_).md>) — Creates a new value object containing the specified CoreMedia time range structure.
- [+ valueWithCMTimeMapping:](<init(cmtimemapping_).md>) — Creates a new value object containing the specified CoreMedia time mapping structure.
- [CMTimeRangeValue](timerangevalue.md) — The CoreMedia time range structure representation of the value.
- [CMTimeMappingValue](timemappingvalue.md) — The CoreMedia time mapping structure representation of the value.
