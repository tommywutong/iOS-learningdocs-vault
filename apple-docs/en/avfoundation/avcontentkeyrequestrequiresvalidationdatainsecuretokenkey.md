---
title: AVContentKeyRequestRequiresValidationDataInSecureTokenKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequestrequiresvalidationdatainsecuretokenkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequestrequiresvalidationdatainsecuretokenkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.json'
content_hash: 'sha256:8f6329c3f438fb78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeyRequestRequiresValidationDataInSecureTokenKey

<sub>Global Variable</sub>

A key that requires the secure token to have extended validation data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVContentKeyRequestRequiresValidationDataInSecureTokenKey: String
```

## Discussion

You create the value for this key by using [- persistableContentKeyFromKeyVendorResponse:options:error:](<avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse_options_).md>).

## See Also

### Getting content key request data

- [- makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:](<avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp_contentidentifier_options_completionhandler_).md>) — Obtains encrypted key request data for a specific combination of app and content.
- [AVContentKeyRequestProtocolVersionsKey](avcontentkeyrequestprotocolversionskey.md) — A key that specifies the versions of the content protection protocol supported by the application.
- [AVContentKeyRequestRandomDeviceIdentifierSeedKey](avcontentkeyrequestrandomdeviceidentifierseedkey.md) — Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [AVContentKeyRequestShouldRandomizeDeviceIdentifierKey](avcontentkeyrequestshouldrandomizedeviceidentifierkey.md) — Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed
