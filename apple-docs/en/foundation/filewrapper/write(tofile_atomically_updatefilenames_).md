---
title: 'write(toFile:atomically:updateFilenames:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filewrapper/write(tofile:atomically:updatefilenames:)'
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/write(tofile:atomically:updatefilenames:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/write%28tofile%3Aatomically%3Aupdatefilenames%3A%29.json'
content_hash: 'sha256:54590b428c251737'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# write(toFile:atomically:updateFilenames:)

<sub>Instance Method</sub>

Writes a file wrapper’s contents to a given file-system node.

> [!warning] Deprecated
> Use [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>) instead.

<sub>macOS</sub>

```swift
func write(toFile path: String, atomically atomicFlag: Bool, updateFilenames updateFilenamesFlag: Bool) -> Bool
```

## Parameters

- `path` — Pathname of the file-system node to which the receiver’s contents are written.

- `atomicFlag` — [true](../../swift/true.md) to write the file safely so that: - An existing file is not overwritten - The method fails if the file cannot be written in its entirety [false](../../swift/false.md) to overwrite an existing file and ignore incomplete writes.

- `updateFilenamesFlag` — [true](../../swift/true.md) to update the receiver’s filenames (its filename and—for directory file wrappers—the filenames of its sub–file wrappers) be changed to the filenames of the corresponding nodes in the file system, after a successful write operation. Use this in Save or Save As operations. [false](../../swift/false.md) to specify that the receiver’s filenames not be updated. Use this in Save To operations.

## Return Value

[true](../../swift/true.md) when the write operation is successful, [false](../../swift/false.md) otherwise.

## Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>).

## See Also

### Related Documentation

- [filename](filename.md) — The filename of the file wrapper object

### Writing Files

- [- writeToURL:options:originalContentsURL:error:](<write(to_options_originalcontentsurl_).md>) — Recursively writes the entire contents of a file wrapper to a given file-system URL.
