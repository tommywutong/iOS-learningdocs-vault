---
title: NSFileManagerResumeSyncBehavior.dropLocalChanges
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanagerresumesyncbehavior/droplocalchanges
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/droplocalchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanagerresumesyncbehavior/droplocalchanges.json'
content_hash: 'sha256:87cd1eac7f1b4651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileManagerResumeSyncBehavior](../nsfilemanagerresumesyncbehavior.md)

# NSFileManagerResumeSyncBehavior.dropLocalChanges

<sub>Case</sub>

Resumes synchronizing by overwriting any local changes with the remote version of the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case dropLocalChanges
```

## Discussion

If a conflict occurs, the file manager stores the local changes as an alternate version. Only use this behavior if you provide a separate means of resolving and merging conflicts.

## See Also

### Identifying sync behaviors

- [NSFileManagerResumeSyncBehaviorPreserveLocalChanges](preservelocalchanges.md) — Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehaviorAfterUploadWithFailOnConflict](afteruploadwithfailonconflict.md) — Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.
