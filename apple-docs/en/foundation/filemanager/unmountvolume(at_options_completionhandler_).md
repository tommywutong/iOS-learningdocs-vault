---
title: 'unmountVolume(at:options:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.11+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/unmountvolume(at:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/unmountvolume(at:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/unmountvolume%28at%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:d3e9dd31963fa3cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# unmountVolume(at:options:completionHandler:)

<sub>Instance Method</sub>

Starts the process of unmounting the specified volume.

<sub>macOS</sub>

```swift
func unmountVolume(at url: URL, options mask: FileManager.UnmountOptions = [], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>macOS</sub>

```swift
func unmountVolume(at url: URL, options mask: FileManager.UnmountOptions = []) async throws
```

## Parameters

- `url` — A file URL specifying the volume to be unmounted.

- `mask` — A bitmask of [UnmountOptions](unmountoptions.md) that you can use to customize the unmount operation’s behavior.

- `completionHandler` — A block executed when the unmount operation completes. The block receives an error parameter which is `nil` if unmounting was successful. Otherwise, it indicates why unmounting failed.

## Discussion

If the volume is encrypted, it is relocked after being unmounted.

## See Also

### Unmounting volumes

- [UnmountOptions](unmountoptions.md) — Options that specify the behavior of an unmount operation.
- [NSFileManagerUnmountDissentingProcessIdentifierErrorKey](../nsfilemanagerunmountdissentingprocessidentifiererrorkey.md) — The process identifier of the process that prevented a volume from unmounting.
