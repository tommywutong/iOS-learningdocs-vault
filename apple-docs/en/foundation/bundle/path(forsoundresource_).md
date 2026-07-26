---
title: 'path(forSoundResource:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/path(forsoundresource:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/path(forsoundresource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/path%28forsoundresource%3A%29.json'
content_hash: 'sha256:7e58fbee80bb2586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# path(forSoundResource:)

<sub>Instance Method</sub>

Returns the location of the specified sound resource file.

<sub>macOS</sub>

```swift
func path(forSoundResource name: NSSound.Name) -> String?
```

## Parameters

- `name` — The name of the sound resource file, without any pathname information. Including a filename extension is optional

## Return Value

The absolute pathname of the resource file or `nil` if the file was not found.

## Discussion

Sound resources are those files in the bundle that are recognized by the `NSSound` class. The types of sound files can be determined by calling the `soundUnfilteredFileTypes` method of `NSSound`.

## See Also

### Related Documentation

- [- pathForResource:ofType:](<path(forresource_oftype_).md>) — Returns the full pathname for the resource identified by the specified name and file extension.
