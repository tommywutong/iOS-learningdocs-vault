---
title: kAuthorizationRightExecute
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kauthorizationrightexecute
source_url: 'https://developer.apple.com/documentation/security/kauthorizationrightexecute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kauthorizationrightexecute.json'
content_hash: 'sha256:d72e2e696a8726a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kAuthorizationRightExecute

<sub>Global Variable</sub>

The type for an authorization item requesting the right to execute with privileges.

<sub>Mac Catalyst, macOS</sub>

```swift
var kAuthorizationRightExecute: String { get }
```

## Discussion

In addition to this right, you should obtain whatever rights the tool needs to perform its operation on your behalf. The [AuthorizationItem](authorizationitem.md) should contain the full path of the tool you wish to execute in the `value` and `valueLength` fields.  In the future we will limit the right to only execute the requested path, and we will display this information to the user.
