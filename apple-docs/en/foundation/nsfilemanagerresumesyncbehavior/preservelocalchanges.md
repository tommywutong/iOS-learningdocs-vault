---
title: NSFileManagerResumeSyncBehavior.preserveLocalChanges
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilemanagerresumesyncbehavior/preservelocalchanges
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/preservelocalchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanagerresumesyncbehavior/preservelocalchanges.json'
content_hash: 'sha256:95ea9af198159c1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileManagerResumeSyncBehavior](../nsfilemanagerresumesyncbehavior.md)

# NSFileManagerResumeSyncBehavior.preserveLocalChanges

<sub>Case</sub>

Resumes synchronizing by uploading the local version of the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case preserveLocalChanges
```

## Discussion

If the server has a newer version, the server may create a conflict copy of the file, or may automatically pick the winner of the conflict. Apps can choose to implement conflict handling themselves by passing `NSFileManagerResumeSyncBehaviorAfterUploadWithFailOnConflict`.

## See Also

### Identifying sync behaviors

- [NSFileManagerResumeSyncBehaviorAfterUploadWithFailOnConflict](afteruploadwithfailonconflict.md) — Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.
- [NSFileManagerResumeSyncBehaviorDropLocalChanges](droplocalchanges.md) — Resumes synchronizing by overwriting any local changes with the remote version of the file.
