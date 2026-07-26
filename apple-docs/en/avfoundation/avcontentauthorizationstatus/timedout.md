---
title: AVContentAuthorizationStatus.timedOut
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentauthorizationstatus/timedout
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus/timedout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentauthorizationstatus/timedout.json'
content_hash: 'sha256:f89bd76007f2e40d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)

# AVContentAuthorizationStatus.timedOut

<sub>Case</sub>

The last call to request content authorization was cancelled because the timeout interval was reached.

<sub>macOS</sub>

```swift
case timedOut
```

## See Also

### Content authorization statuses

- [AVContentAuthorizationUnknown](unknown.md) — The content authorization content request hasn’t completed.
- [AVContentAuthorizationCompleted](completed.md) — The last completed call to request content authorization completed.
- [AVContentAuthorizationCancelled](cancelled.md) — The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationBusy](busy.md) — The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationNotAvailable](notavailable.md) — The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
- [AVContentAuthorizationNotPossible](notpossible.md) — The last call to request content authorization couldn’t be completed in a non-recoverable way.
