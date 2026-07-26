---
title: 'append(component:directoryHint:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/append(component:directoryhint:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/append(component:directoryhint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/append%28component%3Adirectoryhint%3A%29.json'
content_hash: 'sha256:713ccb1161f2dc7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# append(component:directoryHint:)

<sub>Instance Method</sub>

Appends a path component to the URL, with a hint for handling directory awareness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<S>(component: S, directoryHint: URL.DirectoryHint = .inferFromPath) where S : StringProtocol
```

## Parameters

- `component` — The path component to add.

- `directoryHint` — A hint to the initializer to indicate whether the path is a directory, or to instruct the method to make this determination. Defaults to [URL.DirectoryHint.inferFromPath](directoryhint/inferfrompath.md).

## Discussion

This method percent-encodes any path separators (`/`) in the path component before appending the component to the path. If you don’t want this encoding, use [append(path:directoryHint:)](<append(path_directoryhint_).md>) instead.

## See Also

### Adding path components

- [append(path:directoryHint:)](<append(path_directoryhint_).md>) — Appends a path to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:)](<appendpathcomponent(__).md>) — Appends a path component to the URL. _(deprecated)_
- [appendPathComponent(_:isDirectory:)](<appendpathcomponent(__isdirectory_).md>) — Appends a path component to the URL, specifying whether the resulting path is a directory. _(deprecated)_
- [appending(path:directoryHint:)](<appending(path_directoryhint_).md>) — Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [appending(component:directoryHint:)](<appending(component_directoryhint_).md>) — Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [appendingPathComponent(_:)](<appendingpathcomponent(__).md>) — Returns a URL by appending the specified path component to self. _(deprecated)_
- [appendingPathComponent(_:isDirectory:)](<appendingpathcomponent(__isdirectory_).md>) — Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory. _(deprecated)_
- [append(components:directoryHint:)](<append(components_directoryhint_).md>) — Appends multiple path components to the URL, with a hint for handling directory awareness.
- [appending(components:directoryHint:)](<appending(components_directoryhint_).md>) — Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:conformingTo:)](<appendpathcomponent(__conformingto_).md>) — Appends a path component to the URL that conforms to a uniform type identifier.
- [appendingPathComponent(_:conformingTo:)](<appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component that conforms to a uniform type identifier.
