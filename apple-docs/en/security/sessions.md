---
title: Sessions
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sessions
source_url: 'https://developer.apple.com/documentation/security/sessions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sessions.json'
content_hash: 'sha256:9a6fe6e600c41403'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Sessions

<sub>API Collection</sub>

Manage login, authorization, and security sessions in macOS.

## Overview

Use the `Security.AuthSession` API to work with session management and inquiry functions.

## Topics

### Creating a Session

- [SessionCreate](<sessioncreate(____).md>) — Creates a security session.
- [SessionCreationFlags](sessioncreationflags.md) — The flags that affect the creation of a security session.
- [SessionAttributeBits](sessionattributebits.md) — The attributes of a security session.

### Session Information

- [SessionGetInfo](<sessiongetinfo(______).md>) — Obtains information about a security session.
- [Session ID Values](session-id-values.md) — Use these values as placeholders for specific sessions.
- [SecuritySessionId](securitysessionid.md) — A type that contains an authorization session identifier.

### Result Codes

- [Sessions API Result Codes](sessions-api-result-codes.md) — Recognize result codes specific to the sessions API.
