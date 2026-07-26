---
title: UIPrinterDestination
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterdestination
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterdestination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterdestination.json'
content_hash: 'sha256:65512f4f7d30afde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrinterDestination

<sub>Class</sub>

A description of a single printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPrinterDestination
```

## Overview

You can use `UIPrinterDestination` to describe a printer so that it populates in a [UIPrinterPickerController](uiprinterpickercontroller.md) when the printer’s capabilities match the print-job attributes. `UIPrinterDestination` requires a URL to locate the printer. You can include an optional display name that populates in the user interface and a TXT record to detail the printer’s additional features.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a printer destination

- [- initWithURL:](<uiprinterdestination/init(url_)-7ck5j.md>) — Creates a printer destination with the specified address.

### Describing the printer

- [displayName](uiprinterdestination/displayname.md) — A human-readable string that displays the name of a printer.
- [txtRecord](uiprinterdestination/txtrecord.md) — A DNS TXT record to identify the printer.
- [URL](uiprinterdestination/url.md) — The address of the printer.

### Initializers

- [init(URL:)](<uiprinterdestination/init(url_)-c1e8.md>)
- [init(coder:)](<uiprinterdestination/init(coder_).md>)

## See Also

### Printer service discovery

- [UIPrintServiceExtension](uiprintserviceextension.md) — An extension that locates and sets up a printer without a configuration profile.
