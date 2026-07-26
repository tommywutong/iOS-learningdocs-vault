---
title: Session ID Values
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/session-id-values
source_url: 'https://developer.apple.com/documentation/security/session-id-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/session-id-values.json'
content_hash: 'sha256:5e67a8fbbb561301'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Sessions](sessions.md)

# Session ID Values

<sub>API Collection</sub>

Use these values as placeholders for specific sessions.

## Discussion

You can use these values as the `session` input to the [SessionGetInfo](<sessiongetinfo(______).md>) function as a stand-in for specific sessions when you don’t already know the ID for that session. They are _not_ returned in the `sessionId` output of that function. Instead, you receive the actual session ID.

## Topics

### Constants

- [callerSecuritySession](callersecuritysession.md) — A value that is a placeholder for the caller’s session.
- [noSecuritySession](nosecuritysession.md) — Not a valid session.
