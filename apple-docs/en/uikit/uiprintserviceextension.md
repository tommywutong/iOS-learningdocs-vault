---
title: UIPrintServiceExtension
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintserviceextension
source_url: 'https://developer.apple.com/documentation/uikit/uiprintserviceextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintserviceextension.json'
content_hash: 'sha256:334be584b17a7d07'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPrintServiceExtension

<sub>Class</sub>

An extension that locates and sets up a printer without a configuration profile.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPrintServiceExtension
```

## Overview

Support cloud printing by creating an extension instead of requiring users to install a managed configuration profile to set up an AirPrint printer. Create an extension by subclassing `UIPrintServiceExtension`. By creating your own extension, you can expose a cloud printer destination to a [UIPrinterPickerController](uiprinterpickercontroller.md). The extension matches printer destinations that fulfill the specified print-job attributes.

Create an instance of `UIPrinterDestination` to describe a printer to the system. The extension can then search for the printer, or set of printers, using [- printerDestinationsForPrintInfo:](<uiprintserviceextension/printerdestinations(for_).md>). This method matches the requirements of a [UIPrintInfo](uiprintinfo.md) object and returns an array of [UIPrinterDestination](uiprinterdestination.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Locating a printer

- [- printerDestinationsForPrintInfo:](<uiprintserviceextension/printerdestinations(for_).md>) — Searches for a printer destination that matches the print-job attributes.

## See Also

### Related Documentation

- [App extensions](app-extensions.md) — Extend your app’s basic functionality to other parts of the system.

### Printer service discovery

- [UIPrinterDestination](uiprinterdestination.md) — A description of a single printer.
