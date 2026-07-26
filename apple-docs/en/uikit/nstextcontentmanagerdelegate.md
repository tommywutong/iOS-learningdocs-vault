---
title: NSTextContentManagerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanagerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanagerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanagerdelegate.json'
content_hash: 'sha256:17c9e63b48d40cad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextContentManagerDelegate

<sub>Protocol</sub>

The optional methods that delegates of content manager objects implement for customizing or validating text elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextContentManagerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [NSTextContentStorageDelegate](nstextcontentstoragedelegate.md)

## Topics

### Finding a text element at a specific location

- [- textContentManager:textElementAtLocation:](<nstextcontentmanagerdelegate/textcontentmanager(__textelementat_).md>) — The method the framework calls to return the text element at a specific location.

### Validating a text element

- [- textContentManager:shouldEnumerateTextElement:options:](<nstextcontentmanagerdelegate/textcontentmanager(__shouldenumerate_options_).md>) — Returns a Boolean value that indicates whether the framework should skip this text element in the enumeration.

## See Also

### Customizing and validating text elements

- [delegate](nstextcontentmanager/delegate.md) — The delegate for the content manager object.
- [EnumerationOptions](nstextcontentmanager/enumerationoptions.md) — Values that control the order in which the framework enumerates text elements.
