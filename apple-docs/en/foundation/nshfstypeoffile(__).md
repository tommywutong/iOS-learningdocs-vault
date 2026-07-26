---
title: 'NSHFSTypeOfFile(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshfstypeoffile(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshfstypeoffile(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshfstypeoffile%28_%3A%29.json'
content_hash: 'sha256:cecdc15b9d7fb03e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHFSTypeOfFile(_:)

<sub>Function</sub>

Returns a string encoding a file type.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSHFSTypeOfFile(_ fullFilePath: String!) -> String!
```

## Parameters

- `fullFilePath` — The full absolute path of a file.

## Return Value

A string that encodes `fullFilePath`’s HFS file type, or `nil` if the operation was not successful

## See Also

### Working with HFS file types

- [NSFileTypeForHFSTypeCode](<nsfiletypeforhfstypecode(__).md>) — Returns a string encoding a file type code.
- [NSHFSTypeCodeFromFileType](<nshfstypecodefromfiletype(__).md>) — Returns a file type code.
