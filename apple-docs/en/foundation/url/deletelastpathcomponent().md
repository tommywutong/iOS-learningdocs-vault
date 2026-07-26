---
title: deleteLastPathComponent()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/deletelastpathcomponent()
source_url: 'https://developer.apple.com/documentation/foundation/url/deletelastpathcomponent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/deletelastpathcomponent%28%29.json'
content_hash: 'sha256:b37e137276d3e006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# deleteLastPathComponent()

<sub>Instance Method</sub>

Returns a URL constructed by removing the last path component of self.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func deleteLastPathComponent()
```

## Discussion

This function may either remove a path component or append `/..`.

If the URL has an empty path (e.g., `http://www.example.com`), then this function will do nothing.

## See Also

### Removing path components

- [deletingLastPathComponent()](<deletinglastpathcomponent().md>) — Returns a URL constructed by removing the last path component of self.
