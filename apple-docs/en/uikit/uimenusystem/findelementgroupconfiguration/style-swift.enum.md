---
title: UIMenuSystem.FindElementGroupConfiguration.Style
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenusystem/findelementgroupconfiguration/style-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uimenusystem/findelementgroupconfiguration/style-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenusystem/findelementgroupconfiguration/style-swift.enum.json'
content_hash: 'sha256:9a3324817ece6d64'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIMenuSystem](../../uimenusystem.md) · [FindElementGroupConfiguration](../findelementgroupconfiguration.md)

# UIMenuSystem.FindElementGroupConfiguration.Style

<sub>Enumeration</sub>

Represents a preference for the structure of Find elements in the main menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Style
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIMenuSystemFindElementGroupConfigurationStyleAutomatic](style-swift.enum/automatic.md) — The default preference. Find elements are automatically included based on the platform and other system behaviors.
- [UIMenuSystemFindElementGroupConfigurationStyleEditableText](style-swift.enum/editabletext.md) — Prefer a full set of elements for finding and replacing text, such as Find, Find and Replace, Find Navigation, and so on.
- [UIMenuSystemFindElementGroupConfigurationStyleNonEditableText](style-swift.enum/noneditabletext.md) — Prefer a set of elements for finding within a non-editable text area
- [UIMenuSystemFindElementGroupConfigurationStyleSearch](style-swift.enum/search.md) — Prefer a minimal set of find elements, only consisting of elements to search content in the app.

### Initializers

- [init(rawValue:)](<style-swift.enum/init(rawvalue_).md>)

## See Also

### Inspecting a configuration of find elements

- [FindElementGroupConfiguration](../findelementgroupconfiguration.md) — Represents a configuration for find elements, should they be present. You don’t create one of these directly. A configuration is provided as part of a `UIMainMenuSystemConfiguration`.
