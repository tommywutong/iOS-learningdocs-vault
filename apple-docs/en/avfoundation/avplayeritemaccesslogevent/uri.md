---
title: uri
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/uri
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/uri'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/uri.json'
content_hash: 'sha256:9df7d7f7f010e9e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# uri

<sub>Instance Property</sub>

The URI of the playback item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uri: String? { get }
```

## Discussion

The property corresponds to “uri”.

The value of this property is `nil` if the URI is unknown.

This property is not compatible with key-value observing.

## See Also

### Getting server-related log events

- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the last delivered media segment.
- [numberOfServerAddressChanges](numberofserveraddresschanges.md) — A count of changes to the server address over the last uninterrupted period of playback.
- [mediaRequestsWWAN](mediarequestswwan.md) — The number of network read requests over a WWAN.
- [transferDuration](transferduration.md) — The accumulated duration, in seconds, of active network transfer of bytes.
- [numberOfBytesTransferred](numberofbytestransferred.md) — The accumulated number of bytes transferred by the item.
- [numberOfMediaRequests](numberofmediarequests.md) — The number of media read requests from the server to this client.
