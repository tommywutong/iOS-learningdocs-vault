---
title: extendedLogData()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlog/extendedlogdata()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/extendedlogdata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlog/extendedlogdata%28%29.json'
content_hash: 'sha256:c6035ae443ab066d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLog](../avplayeritemerrorlog.md)

# extendedLogData()

<sub>Instance Method</sub>

Returns a serialized representation of the error log in the Extended Log File Format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extendedLogData() -> Data?
```

## Return Value

A serialized representation of the error log in the Extended Log File Format.

## Discussion

This method converts the web server error log into a textual format that conforms to the W3C Extended Log File Format for web server log files. For more information, see [http://www.w3.org/pub/WWW/TR/WD-logfile.html](http://www.w3.org/pub/WWW/TR/WD-logfile.html).

You can generate a string suitable for console output using:

```objc
[[NSString alloc] initWithData:[myLog extendedLogData] encoding:[myLog extendedLogDataStringEncoding]]
```

## See Also

### Accessing error data

- [events](events.md) — A chronologically ordered array of player item error log event objects.
- [extendedLogDataStringEncoding](extendedlogdatastringencoding.md) — The string encoding of the extended log data.
