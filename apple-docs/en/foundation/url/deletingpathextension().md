---
title: deletingPathExtension()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/deletingpathextension()
source_url: 'https://developer.apple.com/documentation/foundation/url/deletingpathextension()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/deletingpathextension%28%29.json'
content_hash: 'sha256:d1348e0201496a9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# deletingPathExtension()

<sub>Instance Method</sub>

Returns a URL constructed by removing any path extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deletingPathExtension() -> URL
```

## Discussion

If the URL has an empty path (e.g., `http://www.example.com`), then this function will return the URL unchanged.

## See Also

### Removing a path extension

- [deletePathExtension()](<deletepathextension().md>) — Returns a URL constructed by removing any path extension.
