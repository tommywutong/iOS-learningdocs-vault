---
title: AVContentKeyRequestRandomDeviceIdentifierSeedKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequestrandomdeviceidentifierseedkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequestrandomdeviceidentifierseedkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequestrandomdeviceidentifierseedkey.json'
content_hash: 'sha256:d166420b01d95c69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeyRequestRandomDeviceIdentifierSeedKey

<sub>Global Variable</sub>

Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVContentKeyRequestRandomDeviceIdentifierSeedKey: String
```

## Discussion

This property must be used in conjunction with AVContentKeyRequestShouldRandomizeDeviceIdentifierKey. Use a RND function to generate a 16 byte seed. This seed will be used to randomize the user’s anonymized device ID if AVContentKeyRequestShouldRandomizeDeviceIdentifierKey is true. Content providers use the SPC to distinguish the playback device from other devices, typically to enforce per-screen business rule limits. If the app developer, in cooperation with the content vendor, does not require to distinguish the playback device, they can further enhance user privacy by making this identifier non-constant, using this option. In either case, apps are not allowed to store or use the FairPlay anonymized device ID for anything other than to enforce business rule limits. App developers must use the AppTrackingTransparency framework to disclose to users if the application or the related FairPlay Key Server collect data about end users and share it with other companies for purposes of tracking across apps and web sites.

## See Also

### Getting content key request data

- [- makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:](<avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp_contentidentifier_options_completionhandler_).md>) — Obtains encrypted key request data for a specific combination of app and content.
- [AVContentKeyRequestProtocolVersionsKey](avcontentkeyrequestprotocolversionskey.md) — A key that specifies the versions of the content protection protocol supported by the application.
- [AVContentKeyRequestRequiresValidationDataInSecureTokenKey](avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md) — A key that requires the secure token to have extended validation data.
- [AVContentKeyRequestShouldRandomizeDeviceIdentifierKey](avcontentkeyrequestshouldrandomizedeviceidentifierkey.md) — Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed
