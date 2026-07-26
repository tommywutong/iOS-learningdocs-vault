---
title: 'init(rawValue:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeychaineventmask/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaineventmask/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaineventmask/init%28rawvalue%3A%29.json'
content_hash: 'sha256:2a095cc47ff01e12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainEventMask](../seckeychaineventmask.md)

# init(rawValue:)

<sub>Initializer</sub>

Initializes an event mask value.

<sub>Mac Catalyst, macOS</sub>

```swift
init(rawValue: UInt32)
```

## Parameters

- `rawValue` — The bitwise `OR` of one or more of the event mask constants used to initialize an event mask
