---
title: originatingRecipient
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/originatingrecipient
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/originatingrecipient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/originatingrecipient.json'
content_hash: 'sha256:db2d6c93031c5d11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# originatingRecipient

<sub>Instance Property</sub>

The AVContentKeyRecipient which initiated this request, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var originatingRecipient: (any AVContentKeyRecipient)? { get }
```

## Discussion

The originatingRecipient is an AVFoundation object responsible for initiating an AVContentKeyRequest. For example, an AVURLAsset used for playback can trigger an AVContentKeyRequest.

If an application triggers key loading directly, for example with -[AVContentKeySession processContentKeyRequestWithIdentifier:initializationData:options:], the value of originatingRecipient will be nil.

The originatingRecipient of key requests from HLS interstitials will always be the corresponding interstitial AVURLAsset. To receive key requests for DRM-protected interstitial content, applications must ensure their AVContentKeySession is attached to these interstitial AVURLAssets.

These interstitial AVURLAssets may be retrieved from the primary AVURLAsset via AVPlayerInterstitialEventMonitor.

## See Also

### Getting content key request properties

- [identifier](identifier.md) — The identifier for the content key.
- [canProvidePersistableContentKey](canprovidepersistablecontentkey.md) — The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [error](error.md) — The error description for a failed key request.
- [initializationData](initializationdata.md) — The data used to obtain a key response.
- [renewsExpiringResponseData](renewsexpiringresponsedata.md) — A Boolean value that indicates whether the content key request renews previously provided response data.
- [status](status-swift.property.md) — The current state of the content key request.
- [Status](status-swift.enum.md) — The status for a content key request.
