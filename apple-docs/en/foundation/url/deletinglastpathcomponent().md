---
title: deletingLastPathComponent()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/deletinglastpathcomponent()
source_url: 'https://developer.apple.com/documentation/foundation/url/deletinglastpathcomponent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/deletinglastpathcomponent%28%29.json'
content_hash: 'sha256:11cc11a849086a5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# deletingLastPathComponent()

<sub>Instance Method</sub>

Returns a URL constructed by removing the last path component of self.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deletingLastPathComponent() -> URL
```

## Discussion

This function may either remove a path component or append `/..`.

If the URL has an empty path (e.g., `http://www.example.com`), then this function will return the URL unchanged.

## See Also

### Removing path components

- [deleteLastPathComponent()](<deletelastpathcomponent().md>) — Returns a URL constructed by removing the last path component of self.
