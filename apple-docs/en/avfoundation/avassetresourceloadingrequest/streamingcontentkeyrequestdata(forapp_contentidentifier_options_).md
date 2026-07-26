---
title: 'streamingContentKeyRequestData(forApp:contentIdentifier:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/streamingcontentkeyrequestdata%28forapp%3Acontentidentifier%3Aoptions%3A%29.json'
content_hash: 'sha256:c6ee9d780255483f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# streamingContentKeyRequestData(forApp:contentIdentifier:options:)

<sub>Instance Method</sub>

Obtains key request data for a specific combination of application and content.

> [!warning] Deprecated
> Use -[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:] instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func streamingContentKeyRequestData(forApp appIdentifier: Data, contentIdentifier: Data, options: [String : Any]? = nil) throws -> Data
```

## Parameters

- `appIdentifier` — An opaque content identifier for the application. The value of this identifier depends on the particular system used to provide the decryption key.

- `contentIdentifier` — An opaque identifier for the content. The value of this identifier depends on the particular system used to provide the decryption key.

- `options` — Additional information necessary to obtain the key, or `nil` if no additional information is required.

## Return Value

The key request data that must be transmitted to the key vendor to obtain the content key.

## Topics

### Configuration options

- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_

## See Also

### Accessing the request data

- [request](request.md) — The URL request object for the resource.
- [requestor](requestor.md) — The asset resource requestor that made the request.
- [contentInformationRequest](contentinformationrequest.md) — The information for a requested resource.
- [dataRequest](datarequest.md) — The range of requested resource data.
- [redirect](redirect.md) — An URL request instance if the loading request was redirected.
- [- persistentContentKeyFromKeyVendorResponse:options:error:](<persistentcontentkey(fromkeyvendorresponse_options_).md>) — Obtains a persistable content key from a context. _(deprecated)_
- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_
