---
title: OSLogInt32ExtendedFormat.truth
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogint32extendedformat/truth
source_url: 'https://developer.apple.com/documentation/os/oslogint32extendedformat/truth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogint32extendedformat/truth.json'
content_hash: 'sha256:5005f749a01e856f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)

# OSLogInt32ExtendedFormat.truth

<sub>Case</sub>

A format that displays a 32-bit integer as true or false.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case truth
```

## Discussion

Use this option to format the interpolated value as either `true` or `false`. The formatter converts all positive and negative nonzero values to `true`, and only zero to `false`. The following example applies the `truth` formatter to the 32-bit integer value `0`:

```swift
// Create a logger with the specified subsystem and category.
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// Assign the value to interpolate.
let value: Int32 = 0
                
// Write the value to the log using the specified format.
logger.info(".truth output is \(value, format: .truth)")
```

And the system writes the following message to the log:

```
[Formatter Output] .truth output is false
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
- [OSLogInt32ExtendedFormat.byteCount](bytecount.md) — A format that displays a 32-bit integer as bytes.
- [OSLogInt32ExtendedFormat.byteCountIEC](bytecountiec.md) — A format that displays a 32-bit integer as IEC bytes.
- [OSLogInt32ExtendedFormat.answer](answer.md) — A format that displays a 32-bit integer as yes or no.
