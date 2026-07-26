---
title: 'presentedSubitem(at:didGain:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presentedsubitem(at:didgain:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didgain:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presentedsubitem%28at%3Adidgain%3A%29.json'
content_hash: 'sha256:00db6ad6f6790719'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedSubitem(at:didGain:)

<sub>Instance Method</sub>

Tells the delegate that the item inside the presented directory gained a new version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedSubitem(at url: URL, didGain version: NSFileVersion)
```

## Parameters

- `url` — The URL of the item inside the presented directory that gained a new version. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

- `version` — The file version object containing information about the new file version.

## Discussion

Your delegate can use this method to determine how to incorporate data from the new version of the item. This might involve incorporating the version silently or asking the user about how to proceed.

## See Also

### Responding to Version Changes

- [- presentedItemDidGainVersion:](<presenteditemdidgain(__).md>) — Tells the delegate that a new version of the file or file package was added.
- [- presentedItemDidLoseVersion:](<presenteditemdidlose(__).md>) — Tells the delegate that a version of the file or file package was removed.
- [- presentedItemDidResolveConflictVersion:](<presenteditemdidresolveconflict(__).md>) — Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [- presentedSubitemAtURL:didLoseVersion:](<presentedsubitem(at_didlose_).md>) — Tells the delegate that the item inside the presented directory lost an existing version.
- [- presentedSubitemAtURL:didResolveConflictVersion:](<presentedsubitem(at_didresolve_).md>) — Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.
