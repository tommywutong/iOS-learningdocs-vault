---
title: 'makeStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/makestreamingcontentkeyrequestdata%28forapp%3Acontentidentifier%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:2891bb9d07d35d9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# makeStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)

<sub>Instance Method</sub>

Obtains encrypted key request data for a specific combination of app and content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeStreamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data?, options: [String : Any]? = nil, completionHandler handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeStreamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data?, options: [String : Any]? = nil) async throws -> Data
```

## Parameters

- `appIdentifier` — An opaque identifier for the app.

- `contentIdentifier` — An opaque identifier for the content.

- `options` — A dictionary containing any additional information required to obtain the key. The value of this parameter is `nil` when no additional information is required.

- `handler` — A block called after the streaming content key request has been prepared. - **contentKeyRequestData** — The streaming content key request data. - **error** — An object that describes the error, if one occurred; otherwise, the value is `nil`.

## Discussion

If [AVContentKeyRequestProtocolVersionsKey](../avcontentkeyrequestprotocolversionskey.md) is not specified in the `options` parameter, the default protocol of `1` is used.

## See Also

### Getting content key request data

- [AVContentKeyRequestProtocolVersionsKey](../avcontentkeyrequestprotocolversionskey.md) — A key that specifies the versions of the content protection protocol supported by the application.
- [AVContentKeyRequestRequiresValidationDataInSecureTokenKey](../avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md) — A key that requires the secure token to have extended validation data.
- [AVContentKeyRequestRandomDeviceIdentifierSeedKey](../avcontentkeyrequestrandomdeviceidentifierseedkey.md) — Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [AVContentKeyRequestShouldRandomizeDeviceIdentifierKey](../avcontentkeyrequestshouldrandomizedeviceidentifierkey.md) — Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed
