---
title: 'presentedSubitem(at:didResolve:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presentedsubitem(at:didresolve:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didresolve:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presentedsubitem%28at%3Adidresolve%3A%29.json'
content_hash: 'sha256:53e6b76755095e94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedSubitem(at:didResolve:)

<sub>Instance Method</sub>

Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedSubitem(at url: URL, didResolve version: NSFileVersion)
```

## Parameters

- `url` — The URL of the item inside the presented directory that was in conflict. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

- `version` — The version object containing the conflicting change.

## Discussion

Your delegate can use this method to respond to the resolution of a version conflict by a different file presenter. This might occur if a version of your application running on another device resolves the conflict first. You might then use this method to update your user interface to indicate that there is no longer a conflict.

## See Also

### Responding to Version Changes

- [- presentedItemDidGainVersion:](<presenteditemdidgain(__).md>) — Tells the delegate that a new version of the file or file package was added.
- [- presentedItemDidLoseVersion:](<presenteditemdidlose(__).md>) — Tells the delegate that a version of the file or file package was removed.
- [- presentedItemDidResolveConflictVersion:](<presenteditemdidresolveconflict(__).md>) — Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [- presentedSubitemAtURL:didGainVersion:](<presentedsubitem(at_didgain_).md>) — Tells the delegate that the item inside the presented directory gained a new version.
- [- presentedSubitemAtURL:didLoseVersion:](<presentedsubitem(at_didlose_).md>) — Tells the delegate that the item inside the presented directory lost an existing version.
