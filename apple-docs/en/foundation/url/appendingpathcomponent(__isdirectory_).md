---
title: 'appendingPathComponent(_:isDirectory:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 8.0+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/url/appendingpathcomponent(_:isdirectory:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/appendingpathcomponent(_:isdirectory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/appendingpathcomponent%28_%3Aisdirectory%3A%29.json'
content_hash: 'sha256:e905eceb026358dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# appendingPathComponent(_:isDirectory:)

<sub>Instance Method</sub>

Returns a URL by appending the specified path component to self, specifying whether the resulting path is a directory.

> [!warning] Deprecated
> Use appending(path:directoryHint:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingPathComponent(_ pathComponent: String, isDirectory: Bool) -> URL
```

## Parameters

- `pathComponent` — The path component to add.

- `isDirectory` — If `true`, the method treats the path component as a directory.

## Return Value

A new URL with the path component appended.

## Discussion

The URL syntax for a directory and for a file at otherwise the same location are slightly different — directory URLs must end in `/`. If you append the path component `second` to the URL `http://www.example.com/first/`, if `isDirectory` is `true`, the resulting URL is `http://www.example.com/first/second/.` If `isDirectory` is `false`, the resulting URL is `http://www.example.com/first/second`.

This difference is particularly important if you resolve another URL against this new URL. For example, the path component `file.html` relative to `http://www.example.com/first/second` is `http://www.apple.com/first/file.html`, whereas relative to `http://www.example.com/first/second/`, it’s `http://www.example.com/first/second/file.html`.

New code should use [appending(path:directoryHint:)](<appending(path_directoryhint_).md>) instead of this method.

## See Also

### Adding path components

- [append(path:directoryHint:)](<append(path_directoryhint_).md>) — Appends a path to the URL, with a hint for handling directory awareness.
- [append(component:directoryHint:)](<append(component_directoryhint_).md>) — Appends a path component to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:)](<appendpathcomponent(__).md>) — Appends a path component to the URL. _(deprecated)_
- [appendPathComponent(_:isDirectory:)](<appendpathcomponent(__isdirectory_).md>) — Appends a path component to the URL, specifying whether the resulting path is a directory. _(deprecated)_
- [appending(path:directoryHint:)](<appending(path_directoryhint_).md>) — Returns a URL by appending the specified path to the URL, with a hint for handling directory awareness.
- [appending(component:directoryHint:)](<appending(component_directoryhint_).md>) — Returns a URL by appending the specified path component to the URL, with a hint for handling directory awareness.
- [appendingPathComponent(_:)](<appendingpathcomponent(__).md>) — Returns a URL by appending the specified path component to self. _(deprecated)_
- [append(components:directoryHint:)](<append(components_directoryhint_).md>) — Appends multiple path components to the URL, with a hint for handling directory awareness.
- [appending(components:directoryHint:)](<appending(components_directoryhint_).md>) — Returns a new URL by appending multiple path components to the URL, with a hint for handling directory awareness.
- [appendPathComponent(_:conformingTo:)](<appendpathcomponent(__conformingto_).md>) — Appends a path component to the URL that conforms to a uniform type identifier.
- [appendingPathComponent(_:conformingTo:)](<appendingpathcomponent(__conformingto_).md>) — Returns a URL by appending the specified path component that conforms to a uniform type identifier.
