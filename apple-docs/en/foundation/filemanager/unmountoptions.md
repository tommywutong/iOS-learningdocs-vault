---
title: FileManager.UnmountOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.11+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/unmountoptions
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/unmountoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/unmountoptions.json'
content_hash: 'sha256:c27f7bcea6d97308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.UnmountOptions

<sub>Structure</sub>

Options that specify the behavior of an unmount operation.

<sub>macOS</sub>

```swift
struct UnmountOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Unmount Behavior

- [init(rawValue:)](<unmountoptions/init(rawvalue_).md>) — Creates an unmount option set from the given raw value.
- [NSFileManagerUnmountAllPartitionsAndEjectDisk](unmountoptions/allpartitionsandejectdisk.md) — Specifies that all partitions on an unmountable disk should be unmounted.
- [NSFileManagerUnmountWithoutUI](unmountoptions/withoutui.md) — Specifies that no UI should accompany the unmount operation.

## See Also

### Unmounting volumes

- [- unmountVolumeAtURL:options:completionHandler:](<unmountvolume(at_options_completionhandler_).md>) — Starts the process of unmounting the specified volume.
- [NSFileManagerUnmountDissentingProcessIdentifierErrorKey](../nsfilemanagerunmountdissentingprocessidentifiererrorkey.md) — The process identifier of the process that prevented a volume from unmounting.
