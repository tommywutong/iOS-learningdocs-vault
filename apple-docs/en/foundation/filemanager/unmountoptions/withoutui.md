---
title: withoutUI
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.11+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/unmountoptions/withoutui
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/unmountoptions/withoutui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/unmountoptions/withoutui.json'
content_hash: 'sha256:0ba6dfb2a4444b09'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [UnmountOptions](../unmountoptions.md)

# withoutUI

<sub>Type Property</sub>

Specifies that no UI should accompany the unmount operation.

<sub>macOS</sub>

```swift
static var withoutUI: FileManager.UnmountOptions { get }
```

## Discussion

If this option is not specified when calling [- unmountVolumeAtURL:options:completionHandler:](<../unmountvolume(at_options_completionhandler_).md>), any needed UI will delay completion of the completion handler.

## See Also

### Unmount Behavior

- [init(rawValue:)](<init(rawvalue_).md>) — Creates an unmount option set from the given raw value.
- [NSFileManagerUnmountAllPartitionsAndEjectDisk](allpartitionsandejectdisk.md) — Specifies that all partitions on an unmountable disk should be unmounted.
