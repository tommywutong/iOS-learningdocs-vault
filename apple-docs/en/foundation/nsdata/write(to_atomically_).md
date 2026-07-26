---
title: 'write(to:atomically:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/write(to:atomically:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/write(to:atomically:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/write%28to%3Aatomically%3A%29.json'
content_hash: 'sha256:15196f3160b6a3b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# write(to:atomically:)

<sub>Instance Method</sub>

Writes the data object’s bytes to the location specified by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, atomically: Bool) -> Bool
```

## Parameters

- `url` — The location to which to write the receiver’s bytes. Only `file://` URLs are supported.

- `atomically` — If [true](../../swift/true.md), the data is written to a backup location, and then—assuming no errors occur—the backup location is renamed to the name specified by `aURL`; otherwise, the data is written directly to `aURL`. `atomically` is ignored if `aURL` is not of a type the supports atomic writes.

## Return Value

[true](../../swift/true.md) if the operation succeeds, otherwise [false](../../swift/false.md).

## Discussion

Since at present only `file://` URLs are supported, there is no difference between this method and [- writeToFile:atomically:](<write(tofile_atomically_).md>), except for the type of the first argument.

This method may not be appropriate when writing to publicly accessible files. To securely write data to a public location, use [FileHandle](../filehandle.md) instead. For more information, see [Securing File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585-SW9) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## See Also

### Writing Data to a File

- [- writeToFile:atomically:](<write(tofile_atomically_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToFile:options:error:](<write(tofile_options_).md>) — Writes the data object’s bytes to the file specified by a given path.
- [- writeToURL:options:error:](<write(to_options_).md>) — Writes the data object’s bytes to the location specified by a given URL.
- [WritingOptions](writingoptions.md) — Options for methods used to write data objects.
