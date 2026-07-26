---
title: CLError.Code.promptDeclined
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/code/promptdeclined
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/promptdeclined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/code/promptdeclined.json'
content_hash: 'sha256:9e427ca50e955af2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLError](../../clerror-swift.struct.md) · [Code](../code.md)

# CLError.Code.promptDeclined

<sub>Case</sub>

A constant that indicates the user didn’t grant the requested temporary authorization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case promptDeclined
```

## Discussion

If the prompt was shown to the user, who declined, or if an error prevented the prompt from being displayed, then `requestTemporaryPreciseLocationAuthorization(withPurposeKey:completion:)` throws this error.

## See Also

### Getting general errors

- [kCLErrorLocationUnknown](locationunknown.md) — A constant that indicates the location manager was unable to obtain a location value right now.
- [kCLErrorDenied](denied.md) — A constant that indicates the user denied access to the location service.
- [kCLErrorNetwork](network.md) — A constant that indicates the network was unavailable or a network error occurred.
- [kCLErrorHeadingFailure](headingfailure.md) — A constant that indicates the location manager can’t determine the heading.
- [kCLErrorRangingUnavailable](rangingunavailable.md) — A constant that indicates ranging is disabled.
- [kCLErrorRangingFailure](rangingfailure.md) — A constant that indicates a general ranging error occurred.
