---
title: txtRecord
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterdestination/txtrecord
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterdestination/txtrecord'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterdestination/txtrecord.json'
content_hash: 'sha256:7abd31dde23da2cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterDestination](../uiprinterdestination.md)

# txtRecord

<sub>Instance Property</sub>

A DNS TXT record to identify the printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var txtRecord: Data? { get set }
```

## Discussion

This property supplies additional information about a printing service as a set of strings that the system can parse into a series of key/value pairs. The TXT record can provide basic access, identity, and capability information about the printing service. The interface can then locate the printer based on categories such as color or duplex printing.

A TXT record isn’t required. When absent, the print system queries the URL and verifies that it can reach the printer before presenting it to the user.

## See Also

### Describing the printer

- [displayName](displayname.md) — A human-readable string that displays the name of a printer.
- [URL](url.md) — The address of the printer.
