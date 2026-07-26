---
title: denied
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/denied
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/denied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/denied.json'
content_hash: 'sha256:123eaa2832f3e7b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# denied

<sub>Type Property</sub>

A constant that indicates the user denied access to the location service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var denied: CLError.Code { get }
```

## See Also

### Getting general errors

- [locationUnknown](locationunknown.md) — A constant that indicates the location manager was unable to obtain a location value right now.
- [promptDeclined](promptdeclined.md) — A constant that indicates the user didn’t grant the requested temporary authorization.
- [network](network.md) — A constant that indicates the network was unavailable or a network error occurred.
- [headingFailure](headingfailure.md) — A constant that indicates the location manager can’t determine the heading.
- [rangingUnavailable](rangingunavailable.md) — A constant that indicates ranging is disabled.
- [rangingFailure](rangingfailure.md) — A constant that indicates a general ranging error occurred.
- [Code](code.md) — Error codes returned by the location manager object.
