---
title: 'presentedItemDidLose(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presenteditemdidlose(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidlose(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemdidlose%28_%3A%29.json'
content_hash: 'sha256:c20c336b5045e6bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemDidLose(_:)

<sub>Instance Method</sub>

Tells the delegate that a version of the file or file package was removed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedItemDidLose(_ version: NSFileVersion)
```

## Parameters

- `version` — The file version object containing information about the version that was removed.

## Discussion

Your delegate can use this method to determine how to handle the loss of the specified file version. You can try to revert the presented document to a previous version or you might want to prompt the user about how to proceed.

## See Also

### Responding to Version Changes

- [- presentedItemDidGainVersion:](<presenteditemdidgain(__).md>) — Tells the delegate that a new version of the file or file package was added.
- [- presentedItemDidResolveConflictVersion:](<presenteditemdidresolveconflict(__).md>) — Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [- presentedSubitemAtURL:didGainVersion:](<presentedsubitem(at_didgain_).md>) — Tells the delegate that the item inside the presented directory gained a new version.
- [- presentedSubitemAtURL:didLoseVersion:](<presentedsubitem(at_didlose_).md>) — Tells the delegate that the item inside the presented directory lost an existing version.
- [- presentedSubitemAtURL:didResolveConflictVersion:](<presentedsubitem(at_didresolve_).md>) — Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.
