---
title: mediaRequestsWWAN
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/mediarequestswwan
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/mediarequestswwan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/mediarequestswwan.json'
content_hash: 'sha256:bd6aeb0227ec87ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# mediaRequestsWWAN

<sub>Instance Property</sub>

The number of network read requests over a WWAN.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mediaRequestsWWAN: Int { get }
```

## Discussion

The value of the property is negative if unknown.

Corresponds to “sc-wwan-count”.

This property is not compatible with key-value observing.

## See Also

### Getting server-related log events

- [URI](uri.md) — The URI of the playback item.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the last delivered media segment.
- [numberOfServerAddressChanges](numberofserveraddresschanges.md) — A count of changes to the server address over the last uninterrupted period of playback.
- [transferDuration](transferduration.md) — The accumulated duration, in seconds, of active network transfer of bytes.
- [numberOfBytesTransferred](numberofbytestransferred.md) — The accumulated number of bytes transferred by the item.
- [numberOfMediaRequests](numberofmediarequests.md) — The number of media read requests from the server to this client.
