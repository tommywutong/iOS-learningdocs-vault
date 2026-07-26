---
title: 'appendPathComponent(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 8.0+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/url/appendpathcomponent(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/appendpathcomponent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/appendpathcomponent%28_%3A%29.json'
content_hash: 'sha256:708d5d3029d16480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# appendPathComponent(_:)

<sub>Instance Method</sub>

Appends a path component to the URL.

> [!warning] Deprecated
> Use append(path:directoryHint:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendPathComponent(_ pathComponent: String)
```

## Parameters

- `pathComponent` — The path component to add.

## Discussion

> [!note] Note
> This function performs a file system operation to determine if the path component is a directory. If so, it will append a trailing `/`. If you know in advance that the path component is a directory or not, then use `func appendingPathComponent(_:isDirectory:)`.

New code should use [append(path:directoryHint:)](<append(path_directoryhint_).md>) instead of this method.

## See Also

### Adding path components

- [append(path:directoryHint:)](<append(path_directoryhint_).md>) — Appends a path to the URL, with a hint for handling directory awareness.
- [append(component:directoryHint:)](<append(component_directoryhint_).md>) — Appends a path component to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:isDirectory:)](<appendpathcomponent(__isdirectory_).md>) — Appends a path component to the URL, specifying whether the resulting path is a directory. _(deprecated)_
- [appending(path:directoryHint:)](<appending(path_directoryhint_).md>) — Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [appending(component:directoryHint:)](<appending(component_directoryhint_).md>) — Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [appendingPathComponent(_:)](<appendingpathcomponent(__).md>) — Returns a URL by appending the specified path component to self. _(deprecated)_
- [appendingPathComponent(_:isDirectory:)](<appendingpathcomponent(__isdirectory_).md>) — Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory. _(deprecated)_
- [append(components:directoryHint:)](<append(components_directoryhint_).md>) — Appends multiple path components to the URL, with a hint for handling directory awareness.
- [appending(components:directoryHint:)](<appending(components_directoryhint_).md>) — Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:conformingTo:)](<appendpathcomponent(__conformingto_).md>) — Appends a path component to the URL that conforms to a uniform type identifier.
- [appendingPathComponent(_:conformingTo:)](<appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component that conforms to a uniform type identifier.
