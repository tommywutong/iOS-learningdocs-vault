---
title: AVContentAuthorizationStatus.busy
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentauthorizationstatus/busy
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus/busy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentauthorizationstatus/busy.json'
content_hash: 'sha256:2670f11a89638d78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)

# AVContentAuthorizationStatus.busy

<sub>Case</sub>

The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.

<sub>macOS</sub>

```swift
case busy
```

## See Also

### Content authorization statuses

- [AVContentAuthorizationUnknown](unknown.md) — The content authorization content request hasn’t completed.
- [AVContentAuthorizationCompleted](completed.md) — The last completed call to request content authorization completed.
- [AVContentAuthorizationCancelled](cancelled.md) — The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationTimedOut](timedout.md) — The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationNotAvailable](notavailable.md) — The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
- [AVContentAuthorizationNotPossible](notpossible.md) — The last call to request content authorization couldn’t be completed in a non-recoverable way.
