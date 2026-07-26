---
title: transferDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/transferduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/transferduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/transferduration.json'
content_hash: 'sha256:597b619ad47fe9b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# transferDuration

<sub>Instance Property</sub>

The accumulated duration, in seconds, of active network transfer of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transferDuration: TimeInterval { get }
```

## Discussion

The value of the property is negative if unknown.

Corresponds to “c-transfer-duration”.

This property is not compatible with key-value observing.

## See Also

### Getting server-related log events

- [URI](uri.md) — The URI of the playback item.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the last delivered media segment.
- [numberOfServerAddressChanges](numberofserveraddresschanges.md) — A count of changes to the server address over the last uninterrupted period of playback.
- [mediaRequestsWWAN](mediarequestswwan.md) — The number of network read requests over a WWAN.
- [numberOfBytesTransferred](numberofbytestransferred.md) — The accumulated number of bytes transferred by the item.
- [numberOfMediaRequests](numberofmediarequests.md) — The number of media read requests from the server to this client.
