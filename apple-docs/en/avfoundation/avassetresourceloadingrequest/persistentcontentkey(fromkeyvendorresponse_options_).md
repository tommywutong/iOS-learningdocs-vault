---
title: 'persistentContentKey(fromKeyVendorResponse:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（18.0 起废弃）, iPadOS 9.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/persistentcontentkey%28fromkeyvendorresponse%3Aoptions%3A%29.json'
content_hash: 'sha256:af9f2b69dbdd5344'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# persistentContentKey(fromKeyVendorResponse:options:)

<sub>Instance Method</sub>

Obtains a persistable content key from a context.

> [!warning] Deprecated
> Use -[AVPersistableContentKeyRequest persistableContentKeyFromKeyVendorResponse:options:error:] instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func persistentContentKey(fromKeyVendorResponse keyVendorResponse: Data, options: [String : Any]? = nil) throws -> Data
```

## Parameters

- `keyVendorResponse` — The response returned from the key vendor as a result of a request generated from [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>).

- `options` — Additional information necessary to obtain the key, or `nil` if no additional information is required.

## Return Value

The persistable content key.

## Discussion

The data returned from this method may be used to immediately satisfy an [AVAssetResourceLoadingDataRequest](../avassetresourceloadingdatarequest.md), as well as any subsequent requests for the same key URL. The value of [contentType](../avassetresourceloadingcontentinformationrequest/contenttype.md) must be set to [AVStreamingKeyDeliveryPersistentContentKeyType](../avstreamingkeydeliverypersistentcontentkeytype.md) when responding with data created with this method.

## See Also

### Accessing the request data

- [request](request.md) — The URL request object for the resource.
- [requestor](requestor.md) — The asset resource requestor that made the request.
- [contentInformationRequest](contentinformationrequest.md) — The information for a requested resource.
- [dataRequest](datarequest.md) — The range of requested resource data.
- [redirect](redirect.md) — An URL request instance if the loading request was redirected.
- [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>) — Obtains key request data for a specific combination of application and content. _(deprecated)_
- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_
