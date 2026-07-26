---
title: allPartitionsAndEjectDisk
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.11+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/unmountoptions/allpartitionsandejectdisk
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/unmountoptions/allpartitionsandejectdisk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/unmountoptions/allpartitionsandejectdisk.json'
content_hash: 'sha256:b30550172d9338b1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [UnmountOptions](../unmountoptions.md)

# allPartitionsAndEjectDisk

<sub>Type Property</sub>

Specifies that all partitions on an unmountable disk should be unmounted.

<sub>macOS</sub>

```swift
static var allPartitionsAndEjectDisk: FileManager.UnmountOptions { get }
```

## Discussion

If the volume is on a partitioned disk, this option unmounts all volumes on that disk. Then, then the disk is ejected (if it is ejectable).

## See Also

### Unmount Behavior

- [init(rawValue:)](<init(rawvalue_).md>) — Creates an unmount option set from the given raw value.
- [NSFileManagerUnmountWithoutUI](withoutui.md) — Specifies that no UI should accompany the unmount operation.
