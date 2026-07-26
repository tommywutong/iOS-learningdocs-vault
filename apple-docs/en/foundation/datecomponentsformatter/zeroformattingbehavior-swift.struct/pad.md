---
title: pad
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.struct/pad
source_url: 'https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.struct/pad'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.struct/pad.json'
content_hash: 'sha256:40a549171a18e2eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [DateComponentsFormatter](../../datecomponentsformatter.md) · [ZeroFormattingBehavior](../zeroformattingbehavior-swift.struct.md)

# pad

<sub>Type Property</sub>

The add padding zeroes behavior. This behavior pads values with zeroes as appropriate. For example, consider the value of one hour formatted using the positional and abbreviated unit styles. When days, hours, minutes, and seconds are allowed, the value is displayed as “0d 1:00:00” using the positional style, and as “0d 1h 0m 0s” using the abbreviated style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var pad: DateComponentsFormatter.ZeroFormattingBehavior { get }
```

## See Also

### Constants

- [NSDateComponentsFormatterZeroFormattingBehaviorDefault](default.md) — The default formatting behavior. When using positional units, this behavior drops leading zeroes but pads middle and trailing values with zeros as needed. For example, with hours, minutes, and seconds displayed, the value for one hour and 10 seconds is “1:00:10”. For all other unit styles, this behavior drops all units whose values are 0. For example, when days, hours, minutes, and seconds are allowed, the abbreviated version of one hour and 10 seconds is displayed as “1h 10s”.
- [NSDateComponentsFormatterZeroFormattingBehaviorDropLeading](dropleading.md) — The drop leading zeroes formatting behavior. Units whose values are 0 are dropped starting at the beginning of the sequence. Units continue to be dropped until a non-zero value is encountered. For example, when days, hours, minutes, and seconds are allowed, the abbreviated version of ten minutes is displayed as “10m 0s”.
- [NSDateComponentsFormatterZeroFormattingBehaviorDropMiddle](dropmiddle.md) — The drop middle zero units behavior. Units whose values are 0 are dropped from anywhere in the middle of a sequence. For example, when days, hours, minutes, and seconds are allowed, the abbreviated version of one hour, zero minutes, and five seconds is displayed as “0d 1h 5s”.
- [NSDateComponentsFormatterZeroFormattingBehaviorDropTrailing](droptrailing.md) — The drop trailing zero units behavior. Units whose value is 0 are dropped starting at the end of the sequence. For example, when days, hours, minutes, and seconds are allowed, the abbreviated version of one hour is displayed as “0d 1h”.
- [NSDateComponentsFormatterZeroFormattingBehaviorDropAll](dropall.md) — The drop all zero units behavior. This behavior drops all units whose values are 0. For example, when days, hours, minutes, and seconds are allowed, the abbreviated version of one hour is displayed as “1h”.
