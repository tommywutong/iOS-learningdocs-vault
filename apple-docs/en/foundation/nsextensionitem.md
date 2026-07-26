---
title: NSExtensionItem
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionitem
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionitem.json'
content_hash: 'sha256:29dd1ef5f9b52270'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExtensionItem

<sub>Class</sub>

An immutable collection of values representing different aspects of an item for an extension to act upon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSExtensionItem
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Identifying the Item

- [attributedTitle](nsextensionitem/attributedtitle.md) — An optional title for the item.
- [userInfo](nsextensionitem/userinfo.md) — An optional dictionary of keys and values corresponding to the extension item’s properties.

### Item Contents

- [attachments](nsextensionitem/attachments.md) — An optional array of media data associated with the extension item.
- [attributedContentText](nsextensionitem/attributedcontenttext.md) — An optional string describing the extension item content.

### Constants

- [Property Keys](property-keys.md) — These keys correspond to the extension item properties and are specified in the extension’s `Info.plist`.
- [UTI Subtypes for Data Detector Types](uti-subtypes-for-data-detector-types.md) — These constants represent sub-Uniform Type Identifier of `com.apple.structured-text`

### Initializers

- [init(coder:)](<nsextensionitem/init(coder_).md>)

## See Also

### Attachments

- [NSItemProvider](nsitemprovider.md) — An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.
- [Add Functionality to Finder with Action Extensions](../appkit/add-functionality-to-finder-with-action-extensions.md) — Implement Action Extensions to provide quick access to commonly used features of your app.
