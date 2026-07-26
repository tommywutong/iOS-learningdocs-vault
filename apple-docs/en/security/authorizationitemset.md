---
title: AuthorizationItemSet
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationitemset
source_url: 'https://developer.apple.com/documentation/security/authorizationitemset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationitemset.json'
content_hash: 'sha256:0fa75436c6cfec83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationItemSet

<sub>Structure</sub>

A structure containing a set of authorization items.

<sub>Mac Catalyst, macOS</sub>

```swift
struct AuthorizationItemSet
```

## Overview

Because it is actually a set, the list of items should not contain any duplicates.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<authorizationitemset/init().md>) — Initializes an authorization item set.
- [init(count:items:)](<authorizationitemset/init(count_items_).md>) — Initializes an authorization item set with the given items.

### Instance Properties

- [count](authorizationitemset/count.md) — The number of elements in the `items` array.
- [items](authorizationitemset/items.md) — A pointer to an array of authorization items.
