---
title: 'presentedSubitem(at:didLose:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/presentedsubitem(at:didlose:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/presentedsubitem(at:didlose:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/presentedsubitem%28at%3Adidlose%3A%29.json'
content_hash: 'sha256:fd7a8ea0b07ea04e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# presentedSubitem(at:didLose:)

<sub>Instance Method</sub>

Tells the delegate that the item inside the presented directory lost an existing version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func presentedSubitem(at url: URL, didLose version: NSFileVersion)
```

## Parameters

- `url` — The URL of the item inside the presented directory that lost a version. The item need not be at the top level of the presented directory but may itself be inside a nested subdirectory.

- `version` — The file version object containing information about the version that was removed.

## Discussion

Your delegate can use this method to determine how to handle the loss of the specified file version. For an old version, you might not have to do anything. However, if your application is currently using the lost version, you would need to update your application’s user interface or prompt the user about how to proceed.

## See Also

### Responding to Version Changes

- [- presentedItemDidGainVersion:](<presenteditemdidgain(__).md>) — Tells the delegate that a new version of the file or file package was added.
- [- presentedItemDidLoseVersion:](<presenteditemdidlose(__).md>) — Tells the delegate that a version of the file or file package was removed.
- [- presentedItemDidResolveConflictVersion:](<presenteditemdidresolveconflict(__).md>) — Tells the delegate that some other entity resolved a version conflict for the presenter’s file or file package.
- [- presentedSubitemAtURL:didGainVersion:](<presentedsubitem(at_didgain_).md>) — Tells the delegate that the item inside the presented directory gained a new version.
- [- presentedSubitemAtURL:didResolveConflictVersion:](<presentedsubitem(at_didresolve_).md>) — Tells the delegate that the item inside the presented directory had a version conflict resolved by an outside entity.
