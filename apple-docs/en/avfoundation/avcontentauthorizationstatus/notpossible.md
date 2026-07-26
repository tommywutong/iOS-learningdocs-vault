---
title: AVContentAuthorizationStatus.notPossible
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentauthorizationstatus/notpossible
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus/notpossible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentauthorizationstatus/notpossible.json'
content_hash: 'sha256:9af97000cac3ecae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)

# AVContentAuthorizationStatus.notPossible

<sub>Case</sub>

The last call to request content authorization couldn’t be completed in a non-recoverable way.

<sub>macOS</sub>

```swift
case notPossible
```

## Discussion

This status is returned when the call can’t be completed, for example, a newer version of iTunes is required.

## See Also

### Content authorization statuses

- [AVContentAuthorizationUnknown](unknown.md) — The content authorization content request hasn’t completed.
- [AVContentAuthorizationCompleted](completed.md) — The last completed call to request content authorization completed.
- [AVContentAuthorizationCancelled](cancelled.md) — The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationTimedOut](timedout.md) — The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationBusy](busy.md) — The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationNotAvailable](notavailable.md) — The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
