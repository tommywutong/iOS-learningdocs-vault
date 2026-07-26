---
title: 'write(toFile:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/write(tofile:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/write(tofile:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/write%28tofile%3Aatomically%3A%29.json'
content_hash: 'sha256:83a3c8958447056f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# write(toFile:atomically:)

<sub>Instance Method</sub>

Writes the data object’s bytes to the file specified by a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

## Parameters

- `path` — The location to which to write the receiver’s bytes. If `path` contains a tilde (~) character, you must expand it with [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md) before invoking this method.

- `useAuxiliaryFile` — If [true](../../swift/true.md), the data is written to a backup file, and then—assuming no errors occur—the backup file is renamed to the name specified by `path`; otherwise, the data is written directly to `path`.

## Return Value

[true](../../swift/true.md) if the operation succeeds, otherwise [false](../../swift/false.md).

## Discussion

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [FileHandle](../filehandle.md) instead. For more information, see [Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## See Also

### Writing Data to a File

- [- writeToFile:options:error:](<write(tofile_options_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToURL:atomically:](<write(to_atomically_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [- writeToURL:options:error:](<write(to_options_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [WritingOptions](writingoptions.md) — Options for methods used to write data objects.
