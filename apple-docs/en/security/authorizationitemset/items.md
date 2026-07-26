---
title: items
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationitemset/items
source_url: 'https://developer.apple.com/documentation/security/authorizationitemset/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationitemset/items.json'
content_hash: 'sha256:a99e25e94e65cea6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationItemSet](../authorizationitemset.md)

# items

<sub>Instance Property</sub>

A pointer to an array of authorization items.

<sub>Mac Catalyst, macOS</sub>

```swift
var items: UnsafeMutablePointer<AuthorizationItem>?
```

## Discussion

If `count` is greater than `1`, `items` points to the first item in an array of such items. You should set this parameter to `NULL` if there are no items.

Ensure that the array of items does not contain duplicates because it actually represents a set.
