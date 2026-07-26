---
title: 'processContentKeyResponse(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponse(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponse%28_%3A%29.json'
content_hash: 'sha256:ed7c6d9cbb02da92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# processContentKeyResponse(_:)

<sub>Instance Method</sub>

Sends the specified content key response to the receiver for processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func processContentKeyResponse(_ keyResponse: AVContentKeyResponse)
```

## Parameters

- `keyResponse` — An [AVContentKeyResponse](../avcontentkeyresponse.md) object carrying a response to a content key request.

## Discussion

After receiving a content key request and calling [- makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:](<makestreamingcontentkeyrequestdata(forapp_contentidentifier_options_completionhandler_).md>) on that request, you must obtain a response to the request in accordance with the protocol used by the entity that controls the use of the media data. Use this method to provide the content key response, to make protected content available for processing.

## See Also

### Responding to the content key request

- [- processContentKeyResponseError:](<processcontentkeyresponseerror(__).md>) — Tells the receiver that the app was unable to obtain a content key response.
- [- respondByRequestingPersistableContentKeyRequest](<respondbyrequestingpersistablecontentkeyrequest().md>) — Tells the receiver that the app requires a persistable content key request object for processing. _(deprecated)_
