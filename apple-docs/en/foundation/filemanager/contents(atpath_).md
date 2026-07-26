---
title: 'contents(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/contents(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/contents(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/contents%28atpath%3A%29.json'
content_hash: 'sha256:78715ca33ebc8697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# contents(atPath:)

<sub>Instance Method</sub>

Returns the contents of the file at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contents(atPath path: String) -> Data?
```

## Parameters

- `path` — The path of the file whose contents you want.

## Return Value

An [NSData](../nsdata.md) object with the contents of the file. If `path` specifies a directory, or if some other error occurs, this method returns `nil`.

## See Also

### Related Documentation

- [- createFileAtPath:contents:attributes:](<createfile(atpath_contents_attributes_).md>) — Creates a file with the specified content and attributes at the given location.

### Getting and comparing file contents

- [- contentsEqualAtPath:andPath:](<contentsequal(atpath_andpath_).md>) — Returns a Boolean value that indicates whether the files or directories in specified paths have the same contents.
