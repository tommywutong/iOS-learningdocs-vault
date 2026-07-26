---
title: 'appendPathExtension(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/appendpathextension(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/appendpathextension(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/appendpathextension%28_%3A%29.json'
content_hash: 'sha256:0c05a4290fbb8735'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# appendPathExtension(_:)

<sub>Instance Method</sub>

Appends the specified path extension to self.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendPathExtension(_ pathExtension: String)
```

## Parameters

- `pathExtension` — The extension to append.

## Discussion

If the URL has an empty path, such as `http://www.example.com`, this function does nothing. Certain special characters (for example, Unicode right-to-left marks) can’t be path extensions. If `pathExtension` contains any of those characters, the function returns an unchanged URL.

## See Also

### Adding a path extension

- [appendingPathExtension(_:)](<appendingpathextension(__).md>) — Returns a URL by appending the specified path extension to self.
- [appendPathExtension(for:)](<appendpathextension(for_).md>) — Appends the preferred path extension for the type you specify.
- [appendingPathExtension(for:)](<appendingpathextension(for_).md>) — Returns a URL by appending the preferred path extension for the type you specify to the URL’s last path component.
