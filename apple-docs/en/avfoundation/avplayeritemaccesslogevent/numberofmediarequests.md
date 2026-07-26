---
title: numberOfMediaRequests
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/numberofmediarequests
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/numberofmediarequests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/numberofmediarequests.json'
content_hash: 'sha256:c5559b721de761da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# numberOfMediaRequests

<sub>Instance Property</sub>

The number of media read requests from the server to this client.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfMediaRequests: Int { get }
```

## Discussion

For HTTP live streaming, this property contains the count of media requests downloaded from the server. For progressive-style HTTP media downloads, it contains a count of HTTP `GET` (byte-range) requests for the resource.

The property corresponds to “sc-count”.

The value of this property is negative if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting server-related log events

- [URI](uri.md) — The URI of the playback item.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the last delivered media segment.
- [numberOfServerAddressChanges](numberofserveraddresschanges.md) — A count of changes to the server address over the last uninterrupted period of playback.
- [mediaRequestsWWAN](mediarequestswwan.md) — The number of network read requests over a WWAN.
- [transferDuration](transferduration.md) — The accumulated duration, in seconds, of active network transfer of bytes.
- [numberOfBytesTransferred](numberofbytestransferred.md) — The accumulated number of bytes transferred by the item.
