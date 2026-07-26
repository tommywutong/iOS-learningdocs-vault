---
title: UIAlertControllerSeverity
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontrollerseverity
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontrollerseverity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontrollerseverity.json'
content_hash: 'sha256:ae9b800f812636d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAlertControllerSeverity

<sub>Enumeration</sub>

Constants for specifying the severity of an alert in apps built with Mac Catalyst.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIAlertControllerSeverity
```

## Overview

This enumeration defines the severity options used by the [severity](uialertcontroller/severity.md) property of [UIAlertController](uialertcontroller.md). In apps built with Mac Catalyst, the severity determines the style of the presented alert. A [UIAlertControllerSeverityCritical](uialertcontrollerseverity/critical.md) alert appears with a caution icon, and an alert with a [UIAlertControllerSeverityDefault](uialertcontrollerseverity/default.md) severity doesn’t. UIKit ignores the alert severity on iOS.

You should only use the [UIAlertControllerSeverityCritical](uialertcontrollerseverity/critical.md) severity if an alert truly requires special attention from the user. For more information, see the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos/windows-and-views/alerts/) on alerts.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIAlertControllerSeverityCritical](uialertcontrollerseverity/critical.md) — Indicates that the system should present the alert using the critical, or caution, style.
- [UIAlertControllerSeverityDefault](uialertcontrollerseverity/default.md) — Indicates that the system should present the alert using the standard alert style.

### Initializers

- [init(rawValue:)](<uialertcontrollerseverity/init(rawvalue_).md>)

## See Also

### Configuring alert severity

- [severity](uialertcontroller/severity.md) — Indicates the severity of the alert.
