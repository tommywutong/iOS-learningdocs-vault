---
title: NSUserActivity.TypedPayloadError.encodingError
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/typedpayloaderror/encodingerror
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayloaderror/encodingerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/typedpayloaderror/encodingerror.json'
content_hash: 'sha256:564eb9184b208597'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSUserActivity](../../nsuseractivity.md) · [TypedPayloadError](../typedpayloaderror.md)

# NSUserActivity.TypedPayloadError.encodingError

<sub>Case</sub>

An encoding error that indicates that the content failed to encode into a valid dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case encodingError
```

## Discussion

The [setTypedPayload(_:)](<../settypedpayload(__).md>) method throws this error.

## See Also

### Typed payload errors

- [NSUserActivity.TypedPayloadError.invalidContent](invalidcontent.md) — A decoding error that indicates that the user info dictionary is empty or invalid.
