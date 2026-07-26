---
title: 'presentedItemDidResolveConflict(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presenteditemdidresolveconflict(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidresolveconflict(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presenteditemdidresolveconflict%28_%3A%29.json'
content_hash: 'sha256:d84935647d1c2589'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedItemDidResolveConflict(_:)

<sub>Instance Method</sub>

Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedItemDidResolveConflict(_ version: NSFileVersion)
```

## Parameters

- `version` — The version object containing the conflicting change.

## Discussion

Your delegate can use this method to respond to the resolution of a version conflict by a different file presenter. This might occur if a version of your application running on another device resolves the conflict first. You might then use this method to update your user interface to indicate that there is no longer a conflict.

## See Also

### Responding to Version Changes

- [- presentedItemDidGainVersion:](<presenteditemdidgain(__).md>) — Tells the delegate that a new version of the file or file package was added.
- [- presentedItemDidLoseVersion:](<presenteditemdidlose(__).md>) — Tells the delegate that a version of the file or file package was removed.
- [- presentedSubitemAtURL:didGainVersion:](<presentedsubitem(at_didgain_).md>) — Tells the delegate that the item inside the presented directory gained a new version.
- [- presentedSubitemAtURL:didLoseVersion:](<presentedsubitem(at_didlose_).md>) — Tells the delegate that the item inside the presented directory lost an existing version.
- [- presentedSubitemAtURL:didResolveConflictVersion:](<presentedsubitem(at_didresolve_).md>) — Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.
