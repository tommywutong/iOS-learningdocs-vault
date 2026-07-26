---
title: 'presentedItemDidGain(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presenteditemdidgain(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidgain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemdidgain%28_%3A%29.json'
content_hash: 'sha256:8b3873665305965e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemDidGain(_:)

<sub>Instance Method</sub>

Tells the delegate that a new version of the file or file package was added.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedItemDidGain(_ version: NSFileVersion)
```

## Parameters

- `version` — The file version object containing information about the new file version.

## Discussion

Your delegate can use this method to determine how to incorporate data from the new version of the file or file package. If the file has not been modified by your code, you might simply update to the new version quietly. However, if your application has its own changes, you might need to ask the user how to proceed.

## See Also

### Responding to Version Changes

- [- presentedItemDidLoseVersion:](<presenteditemdidlose(__).md>) — Tells the delegate that a version of the file or file package was removed.
- [- presentedItemDidResolveConflictVersion:](<presenteditemdidresolveconflict(__).md>) — Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [- presentedSubitemAtURL:didGainVersion:](<presentedsubitem(at_didgain_).md>) — Tells the delegate that the item inside the presented directory gained a new version.
- [- presentedSubitemAtURL:didLoseVersion:](<presentedsubitem(at_didlose_).md>) — Tells the delegate that the item inside the presented directory lost an existing version.
- [- presentedSubitemAtURL:didResolveConflictVersion:](<presentedsubitem(at_didresolve_).md>) — Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.
