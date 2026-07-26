---
title: 'read(from:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/read(from:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/read(from:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/read%28from%3Aoptions%3A%29.json'
content_hash: 'sha256:392945599aaceb54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# read(from:options:)

<sub>Instance Method</sub>

Recursively rereads the entire contents of a file wrapper from the specified location on disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func read(from url: URL, options: FileWrapper.ReadingOptions = []) throws
```

## Parameters

- `url` — URL of the file-system node corresponding to the file wrapper.

- `options` — Option flags for reading the node located at `url`. See [ReadingOptions](readingoptions.md) for possible values.

## Discussion

When reading a directory, children are added and removed as necessary to match the file system.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [fileWrappers](filewrappers.md) — The file wrappers contained by a directory file wrapper.
- [- initWithURL:options:error:](<init(url_options_)-70161.md>) — Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [filename](filename.md) — The filename of the file wrapper object
- [fileAttributes](fileattributes.md) — A dictionary of file attributes.
- [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>) — Recursively writes the entire contents of a file wrapper to a given file-system URL.

### Updating File Wrappers

- [- needsToBeUpdatedFromPath:](<needstobeupdated(frompath_).md>) — Indicates whether the file wrapper needs to be updated to match a given file-system node. _(deprecated)_
- [- matchesContentsOfURL:](<matchescontents(of_).md>) — Indicates whether the contents of a file wrapper matches a directory, regular file, or symbolic link on disk.
- [- updateFromPath:](<update(frompath_).md>) — Updates the file wrapper to match a given file-system node. _(deprecated)_
