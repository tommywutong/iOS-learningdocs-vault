---
title: 'SessionGetInfo(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sessiongetinfo(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sessiongetinfo(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessiongetinfo%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:86a0575e765d5a6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SessionGetInfo(_:_:_:)

<sub>Function</sub>

Obtains information about a security session.

<sub>Mac Catalyst, macOS</sub>

```swift
func SessionGetInfo(_ session: SecuritySessionId, _ sessionId: UnsafeMutablePointer<SecuritySessionId>?, _ attributes: UnsafeMutablePointer<SessionAttributeBits>?) -> OSStatus
```

## Parameters

- `session` — The session you are asking about. You can use one of the special sessions given in [Session ID Values](session-id-values.md), for example to ask about your own session.

- `sessionId` — A pointer to a [SecuritySessionId](securitysessionid.md) value that the function populates with the actual session ID for the session you asked about. This value will not be one of the special values from [Session ID Values](session-id-values.md), but will instead be an actual session ID.

- `attributes` — A pointer to a [SessionAttributeBits](sessionattributebits.md) structure that the function fills with the attribute bits for the session.

## Return Value

A result code. See [Sessions API Result Codes](sessions-api-result-codes.md).

## Discussion

You can ask about any session whose identifier you know. Use the [callerSecuritySession](callersecuritysession.md) constant to ask about your own session (the one your process is in).
