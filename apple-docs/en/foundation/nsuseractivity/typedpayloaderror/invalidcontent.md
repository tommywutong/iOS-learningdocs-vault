---
title: NSUserActivity.TypedPayloadError.invalidContent
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/typedpayloaderror/invalidcontent
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayloaderror/invalidcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/typedpayloaderror/invalidcontent.json'
content_hash: 'sha256:f10cbbd8a35670ce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSUserActivity](../../nsuseractivity.md) · [TypedPayloadError](../typedpayloaderror.md)

# NSUserActivity.TypedPayloadError.invalidContent

<sub>Case</sub>

A decoding error that indicates that the user info dictionary is empty or invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case invalidContent
```

## Discussion

The [typedPayload(_:)](<../typedpayload(__).md>) method throws this error.

## See Also

### Typed payload errors

- [NSUserActivity.TypedPayloadError.encodingError](encodingerror.md) — An encoding error that indicates that the content failed to encode into a valid dictionary.
