---
title: NSFileManagerUnmountDissentingProcessIdentifierErrorKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.11+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanagerunmountdissentingprocessidentifiererrorkey
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanagerunmountdissentingprocessidentifiererrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanagerunmountdissentingprocessidentifiererrorkey.json'
content_hash: 'sha256:3ed1c1ae032d1a5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileManagerUnmountDissentingProcessIdentifierErrorKey

<sub>Global Variable</sub>

The process identifier of the process that prevented a volume from unmounting.

<sub>macOS</sub>

```swift
let NSFileManagerUnmountDissentingProcessIdentifierErrorKey: String
```

## Discussion

If [- unmountVolumeAtURL:options:completionHandler:](<filemanager/unmountvolume(at_options_completionhandler_).md>) fails, the error sent to its completion handler will contain a `userInfo` dictionary with this string as one of its keys. The value is the process identifier of the process that prevented the unmounting, as an [NSNumber](nsnumber.md).

## See Also

### Unmounting volumes

- [- unmountVolumeAtURL:options:completionHandler:](<filemanager/unmountvolume(at_options_completionhandler_).md>) — Starts the process of unmounting the specified volume.
- [UnmountOptions](filemanager/unmountoptions.md) — Options that specify the behavior of an unmount operation.
