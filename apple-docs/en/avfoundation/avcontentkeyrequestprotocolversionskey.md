---
title: AVContentKeyRequestProtocolVersionsKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequestprotocolversionskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequestprotocolversionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequestprotocolversionskey.json'
content_hash: 'sha256:593707a1a1d7a2ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeyRequestProtocolVersionsKey

<sub>Global Variable</sub>

A key that specifies the versions of the content protection protocol supported by the application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVContentKeyRequestProtocolVersionsKey: String
```

## Discussion

The contents of this key are an [NSArray](../foundation/nsarray.md) or one or more [NSNumber](../foundation/nsnumber.md) objects.

## See Also

### Getting content key request data

- [- makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:](<avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp_contentidentifier_options_completionhandler_).md>) — Obtains encrypted key request data for a specific combination of app and content.
- [AVContentKeyRequestRequiresValidationDataInSecureTokenKey](avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md) — A key that requires the secure token to have extended validation data.
- [AVContentKeyRequestRandomDeviceIdentifierSeedKey](avcontentkeyrequestrandomdeviceidentifierseedkey.md) — Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [AVContentKeyRequestShouldRandomizeDeviceIdentifierKey](avcontentkeyrequestshouldrandomizedeviceidentifierkey.md) — Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed
