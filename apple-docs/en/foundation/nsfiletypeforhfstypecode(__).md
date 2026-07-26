---
title: 'NSFileTypeForHFSTypeCode(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfiletypeforhfstypecode(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfiletypeforhfstypecode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfiletypeforhfstypecode%28_%3A%29.json'
content_hash: 'sha256:38b2118f26144de0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileTypeForHFSTypeCode(_:)

<sub>Function</sub>

Returns a string encoding a file type code.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSFileTypeForHFSTypeCode(_ hfsFileTypeCode: OSType) -> String!
```

## Parameters

- `hfsFileTypeCode` — An HFS file type code.

## Return Value

A string that encodes `hfsFileTypeCode`.

## See Also

### Working with HFS file types

- [NSHFSTypeCodeFromFileType](<nshfstypecodefromfiletype(__).md>) — Returns a file type code.
- [NSHFSTypeOfFile](<nshfstypeoffile(__).md>) — Returns a string encoding a file type.
