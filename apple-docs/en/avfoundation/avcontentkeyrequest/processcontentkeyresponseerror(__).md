---
title: 'processContentKeyResponseError(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponseerror(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponseerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponseerror%28_%3A%29.json'
content_hash: 'sha256:b9027a8157cd107a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# processContentKeyResponseError(_:)

<sub>Instance Method</sub>

Tells the receiver that the app was unable to obtain a content key response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func processContentKeyResponseError(_ error: any Error)
```

## Parameters

- `error` — An [NSError](../../foundation/nserror.md) that describes why the content key response failed.

## See Also

### Responding to the content key request

- [- processContentKeyResponse:](<processcontentkeyresponse(__).md>) — Sends the specified content key response to the receiver for processing.
- [- respondByRequestingPersistableContentKeyRequest](<respondbyrequestingpersistablecontentkeyrequest().md>) — Tells the receiver that the app requires a persistable content key request object for processing. _(deprecated)_
