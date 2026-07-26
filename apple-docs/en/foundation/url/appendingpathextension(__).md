---
title: 'appendingPathExtension(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/appendingpathextension(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/appendingpathextension(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/appendingpathextension%28_%3A%29.json'
content_hash: 'sha256:69b44691886e880c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# appendingPathExtension(_:)

<sub>Instance Method</sub>

Returns a URL by appending the specified path extension to self.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingPathExtension(_ pathExtension: String) -> URL
```

## Parameters

- `pathExtension` — The extension to append.

## Discussion

If the URL has an empty path, such as `http://www.example.com`, this function returns an unchanged URL.

Certain special characters (for example, Unicode right-to-left marks) can’t be path extensions. If `pathExtension` contains any of those characters, the function returns an unchanged URL.

## See Also

### Adding a path extension

- [appendPathExtension(_:)](<appendpathextension(__).md>) — Appends the specified path extension to self.
- [appendPathExtension(for:)](<appendpathextension(for_).md>) — Appends the preferred path extension for the type you specify.
- [appendingPathExtension(for:)](<appendingpathextension(for_).md>) — Returns a URL by appending the preferred path extension for the type you specify to the URL’s last path component.
