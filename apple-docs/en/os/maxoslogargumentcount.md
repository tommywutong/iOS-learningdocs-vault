---
title: maxOSLogArgumentCount
framework: os
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/maxoslogargumentcount
source_url: 'https://developer.apple.com/documentation/os/maxoslogargumentcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/maxoslogargumentcount.json'
content_hash: 'sha256:0372fcbbcb7c0120'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# maxOSLogArgumentCount

<sub>Global Variable</sub>

The maximum number of interpolated expressions that a log message may contain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maxOSLogArgumentCount: UInt8 { get }
```

## Discussion

For log messages that include interpolated values, the system imposes a limit on the total number of expressions that a single message may include. The following example shows a string that contains an interpolated value:

```swift
let fileID = 941
let message = "Created a file with ID \(fileID)"
```

## See Also

### Getting the Message Details

- [bufferSize](oslogmessage/buffersize.md) — The byte size of the buffer that the logging system receives.
- [interpolation](oslogmessage/interpolation.md) — The log message’s string interpolation.
