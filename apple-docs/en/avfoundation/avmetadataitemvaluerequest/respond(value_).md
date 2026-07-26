---
title: 'respond(value:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitemvaluerequest/respond(value:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/respond(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitemvaluerequest/respond%28value%3A%29.json'
content_hash: 'sha256:35ee3e0bc9ad44a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItemValueRequest](../avmetadataitemvaluerequest.md)

# respond(value:)

<sub>Instance Method</sub>

Returns the metadata item’s value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func respond(value: any NSCopying & NSObjectProtocol)
```

## Parameters

- `value` — The value to return for the request.

## Discussion

You call this method to return the metadata item’s value.

## See Also

### Handling the response

- [- respondWithError:](<respond(error_).md>) — Returns an error when the system fails to load the value.
- [metadataItem](metadataitem.md) — The metadata item to request a value for.
