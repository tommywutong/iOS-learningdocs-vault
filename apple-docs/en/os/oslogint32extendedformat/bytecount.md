---
title: OSLogInt32ExtendedFormat.byteCount
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogint32extendedformat/bytecount
source_url: 'https://developer.apple.com/documentation/os/oslogint32extendedformat/bytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogint32extendedformat/bytecount.json'
content_hash: 'sha256:b2b2f036e9a9c2dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)

# OSLogInt32ExtendedFormat.byteCount

<sub>Case</sub>

A format that displays a 32-bit integer as bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case byteCount
```

## Discussion

Use this option to format the interpolated value as bytes, such as `100 kB`. The following example applies the `byteCount` formatter to the 32-bit integer value `100_000`:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate.
let value: Int32 = 100_000
                
// Write the value to the log using the specified format.
logger.info(".byteCount output is \(value, format: .byteCount)")
```

And the system writes the folllowing message to the log:

```
[Formatter Output] .byteCount output is 100 kB
```

## See Also

### Getting the Formats

- [OSLogInt32ExtendedFormat.ipv4Address](ipv4address.md) — A format that displays a 32-bit integer as an IPv4 address.
- [OSLogInt32ExtendedFormat.secondsSince1970](secondssince1970.md) — A format that displays a 32-bit integer as a date.
- [OSLogInt32ExtendedFormat.darwinErrno](darwinerrno.md) — A format that displays a 32-bit integer as a Darwin error number.
- [OSLogInt32ExtendedFormat.darwinMode](darwinmode.md) — A format that displays a 32-bit integer as a Darwin file mode.
- [OSLogInt32ExtendedFormat.darwinSignal](darwinsignal.md) — A format that displays a 32-bit integer as a Darwin signal.
- [OSLogInt32ExtendedFormat.bitrate](bitrate.md) — A format that displays a 32-bit integer as a bit rate.
- [OSLogInt32ExtendedFormat.bitrateIEC](bitrateiec.md) — A format that displays a 32-bit integer as an IEC bit rate.
- [OSLogInt32ExtendedFormat.byteCountIEC](bytecountiec.md) — A format that displays a 32-bit integer as IEC bytes.
- [OSLogInt32ExtendedFormat.truth](truth.md) — A format that displays a 32-bit integer as true or false.
- [OSLogInt32ExtendedFormat.answer](answer.md) — A format that displays a 32-bit integer as yes or no.
