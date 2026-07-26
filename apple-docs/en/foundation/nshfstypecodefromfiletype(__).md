---
title: 'NSHFSTypeCodeFromFileType(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshfstypecodefromfiletype(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshfstypecodefromfiletype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshfstypecodefromfiletype%28_%3A%29.json'
content_hash: 'sha256:18b3f7102359f00b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHFSTypeCodeFromFileType(_:)

<sub>Function</sub>

Returns a file type code.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSHFSTypeCodeFromFileType(_ fileTypeString: String!) -> OSType
```

## Parameters

- `fileTypeString` — A string of the sort encoded by `NSFileTypeForHFSTypeCode()`.

## Return Value

The HFS file type code corresponding to `fileTypeString`, or `0` if it cannot be found.

## See Also

### Working with HFS file types

- [NSFileTypeForHFSTypeCode](<nsfiletypeforhfstypecode(__).md>) — Returns a string encoding a file type code.
- [NSHFSTypeOfFile](<nshfstypeoffile(__).md>) — Returns a string encoding a file type.
