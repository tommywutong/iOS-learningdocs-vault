---
title: callerSecuritySession
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/callersecuritysession
source_url: 'https://developer.apple.com/documentation/security/callersecuritysession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/callersecuritysession.json'
content_hash: 'sha256:6e56b5ce68fbe2d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# callerSecuritySession

<sub>Global Variable</sub>

A value that is a placeholder for the caller’s session.

<sub>Mac Catalyst, macOS</sub>

```swift
var callerSecuritySession: SecuritySessionId { get }
```

## Discussion

When you provide this value as the `session` input to the [SessionGetInfo](<sessiongetinfo(______).md>) function, the function will return the actual session ID via the `sessionId` output.
