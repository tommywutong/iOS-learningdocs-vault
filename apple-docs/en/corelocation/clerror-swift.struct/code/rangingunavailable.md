---
title: CLError.Code.rangingUnavailable
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/code/rangingunavailable
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/rangingunavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/code/rangingunavailable.json'
content_hash: 'sha256:6ab1dec83803bcd2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLError](../../clerror-swift.struct.md) · [Code](../code.md)

# CLError.Code.rangingUnavailable

<sub>Case</sub>

A constant that indicates ranging is disabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case rangingUnavailable
```

## Discussion

This might happen if the device is in Airplane mode or if Bluetooth or location services are disabled.

## See Also

### Getting general errors

- [kCLErrorLocationUnknown](locationunknown.md) — A constant that indicates the location manager was unable to obtain a location value right now.
- [kCLErrorDenied](denied.md) — A constant that indicates the user denied access to the location service.
- [kCLErrorPromptDeclined](promptdeclined.md) — A constant that indicates the user didn’t grant the requested temporary authorization.
- [kCLErrorNetwork](network.md) — A constant that indicates the network was unavailable or a network error occurred.
- [kCLErrorHeadingFailure](headingfailure.md) — A constant that indicates the location manager can’t determine the heading.
- [kCLErrorRangingFailure](rangingfailure.md) — A constant that indicates a general ranging error occurred.
