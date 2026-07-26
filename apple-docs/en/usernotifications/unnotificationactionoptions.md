---
title: UNNotificationActionOptions
framework: User Notifications
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationactionoptions
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationactionoptions.json'
content_hash: 'sha256:c242d8ecae3fc367'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationActionOptions

<sub>Structure</sub>

The behaviors you can apply to an action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct UNNotificationActionOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<unnotificationactionoptions/init(rawvalue_).md>) — Initializes an action options object using the specified raw value.

### Constants

- [UNNotificationActionOptionAuthenticationRequired](unnotificationactionoptions/authenticationrequired.md) — The action can be performed only on an unlocked device.
- [UNNotificationActionOptionDestructive](unnotificationactionoptions/destructive.md) — The action performs a destructive task.
- [UNNotificationActionOptionForeground](unnotificationactionoptions/foreground.md) — The action causes the app to launch in the foreground.

## See Also

### Getting Options

- [options](unnotificationaction/options.md) — The behaviors associated with the action.
