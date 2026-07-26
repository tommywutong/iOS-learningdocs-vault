---
title: numberOfServerAddressChanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/numberofserveraddresschanges
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/numberofserveraddresschanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/numberofserveraddresschanges.json'
content_hash: 'sha256:381159cf9587d7c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# numberOfServerAddressChanges

<sub>Instance Property</sub>

A count of changes to the server address over the last uninterrupted period of playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfServerAddressChanges: Int { get }
```

## Discussion

The property corresponds to “s-ip-changes”.

The value of this property is negative if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting server-related log events

- [URI](uri.md) — The URI of the playback item.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the last delivered media segment.
- [mediaRequestsWWAN](mediarequestswwan.md) — The number of network read requests over a WWAN.
- [transferDuration](transferduration.md) — The accumulated duration, in seconds, of active network transfer of bytes.
- [numberOfBytesTransferred](numberofbytestransferred.md) — The accumulated number of bytes transferred by the item.
- [numberOfMediaRequests](numberofmediarequests.md) — The number of media read requests from the server to this client.
