---
title: SSLContext
framework: Security
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslcontext
source_url: 'https://developer.apple.com/documentation/security/sslcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcontext.json'
content_hash: 'sha256:56cd924fcd96f865'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLContext

<sub>Class</sub>

An opaque type that represents an SSL session context object.

<sub>Mac Catalyst, macOS</sub>

```swift
class SSLContext
```

## Overview

The SSL session context object references the state associated with a session. You can’t reuse an SSL session context in multiple sessions.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)
