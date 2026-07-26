---
title: AuthorizationExternalForm
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationexternalform
source_url: 'https://developer.apple.com/documentation/security/authorizationexternalform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationexternalform.json'
content_hash: 'sha256:312f85f789836ce0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationExternalForm

<sub>Structure</sub>

The external representation of an authorization reference.

<sub>Mac Catalyst, macOS</sub>

```swift
struct AuthorizationExternalForm
```

## Overview

Authorization references are bound by session, process, and time limits, so you can’t store the authorization references for another process to use. Use the functions [AuthorizationMakeExternalForm](<authorizationmakeexternalform(____).md>) and [AuthorizationCreateFromExternalForm](<authorizationcreatefromexternalform(____).md>) to externalize and internalize the authorization reference. Apps should take care not to disclose the external authorization reference to potential attackers since any process can use this external authorization reference to access the authorization reference.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<authorizationexternalform/init().md>)
- [init(bytes:)](<authorizationexternalform/init(bytes_).md>)

### Instance Properties

- [bytes](authorizationexternalform/bytes.md) — An array of characters representing the external form of an authorization reference.
