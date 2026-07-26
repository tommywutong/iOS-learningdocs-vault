---
title: kSecCSDedicatedHost
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccsdedicatedhost
source_url: 'https://developer.apple.com/documentation/security/kseccsdedicatedhost'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccsdedicatedhost.json'
content_hash: 'sha256:443a610a8f0ae175'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSDedicatedHost

<sub>Global Variable</sub>

Declares dedicated hosting for the given host.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSDedicatedHost: UInt32 { get }
```

## Discussion

In dedicated hosting, the host has exactly one guest (the one this call specifies) and the host spends all of its time running that guest (or running on its behalf). This declaration is irreversible for the lifetime of the host. If the guest terminates, the host terminates as well. Any code object that refers to a dedicated host is assumed by the system to be referring to the guest. Note that this is a declaration about the given host, and is not binding on other hosts on either side of the hosting chain (though they may declare dedicated hosting as well).

It is invalid to declare dedicated hosting if the host already has other guests, and it is invalid to introduce additional guests for this host after this call.
