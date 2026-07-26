---
title: 'respond(error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitemvaluerequest/respond(error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/respond(error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitemvaluerequest/respond%28error%3A%29.json'
content_hash: 'sha256:3a726aa90c0166d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItemValueRequest](../avmetadataitemvaluerequest.md)

# respond(error:)

<sub>Instance Method</sub>

Returns an error when the system fails to load the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func respond(error: any Error)
```

## Parameters

- `error` — The error to return for the request.

## See Also

### Handling the response

- [- respondWithValue:](<respond(value_).md>) — Returns the metadata item’s value.
- [metadataItem](metadataitem.md) — The metadata item to request a value for.
