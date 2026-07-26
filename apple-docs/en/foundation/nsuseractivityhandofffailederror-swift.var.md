---
title: NSUserActivityHandoffFailedError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivityhandofffailederror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivityhandofffailederror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivityhandofffailederror-swift.var.json'
content_hash: 'sha256:8033f888ac54c86a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserActivityHandoffFailedError

<sub>Global Variable</sub>

The data for the user activity wasn’t available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSUserActivityHandoffFailedError: Int { get }
```

## Discussion

This error can occur if the remote device became unavailable.

## See Also

### Reporting errors

- [NSUserActivityConnectionUnavailableError](nsuseractivityconnectionunavailableerror-swift.var.md) — The user activity couldn’t be continued because a required connection wasn’t available.
- [NSUserActivityErrorMaximum](nsuseractivityerrormaximum-swift.var.md) — The end of the range of error codes reserved for user activity errors.
- [NSUserActivityErrorMinimum](nsuseractivityerrorminimum-swift.var.md) — The start of the range of error codes reserved for user activity errors.
- [NSUserActivityHandoffUserInfoTooLargeError](nsuseractivityhandoffuserinfotoolargeerror-swift.var.md) — The user info dictionary was too large to receive.
- [NSUserActivityRemoteApplicationTimedOutError](nsuseractivityremoteapplicationtimedouterror-swift.var.md) — The remote application failed to send data within the specified time.
