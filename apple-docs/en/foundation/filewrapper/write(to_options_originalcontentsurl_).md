---
title: 'write(to:options:originalContentsURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filewrapper/write(to:options:originalcontentsurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/write(to:options:originalcontentsurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/write%28to%3Aoptions%3Aoriginalcontentsurl%3A%29.json'
content_hash: 'sha256:4e5120e34227c434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# write(to:options:originalContentsURL:)

<sub>Instance Method</sub>

Recursively writes the entire contents of a file wrapper to a given file-system URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, options: FileWrapper.WritingOptions = [], originalContentsURL: URL?) throws
```

## Parameters

- `url` — URL of the file-system node to which the file wrapper’s contents are written.

- `options` — Option flags for writing to the node located at `url`. See [WritingOptions](writingoptions.md) for possible values.

- `originalContentsURL` — The location of a previous revision of the contents being written. The default implementation of this method attempts to avoid unnecessary I/O by writing hard links to regular files instead of actually writing out their contents when the contents have not changed.  The child file wrappers must return accurate values when its [filename](filename.md) property is accessed for this to work. Use the `NSFileWrapperWritingWithNameUpdating` writing option to increase the likelihood of that. Specify `nil` for this parameter if there is no earlier version of the contents or if you want to ensure that all the contents are written to files.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- readFromURL:options:error:](<read(from_options_).md>) — Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [filename](filename.md) — The filename of the file wrapper object

### Writing Files

- [- writeToFile:atomically:updateFilenames:](<write(tofile_atomically_updatefilenames_).md>) — Writes a file wrapper’s contents to a given file-system node. _(deprecated)_
