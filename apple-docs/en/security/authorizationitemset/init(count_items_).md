---
title: 'init(count:items:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationitemset/init(count:items:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationitemset/init(count:items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationitemset/init%28count%3Aitems%3A%29.json'
content_hash: 'sha256:904ff228783ffa8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationItemSet](../authorizationitemset.md)

# init(count:items:)

<sub>Initializer</sub>

Initializes an authorization item set with the given items.

<sub>Mac Catalyst, macOS</sub>

```swift
init(count: UInt32, items: UnsafeMutablePointer<AuthorizationItem>?)
```

## Parameters

- `count` — The number of items in the `items` array.

- `items` — A pointer to the first authorization item in an array of items.
