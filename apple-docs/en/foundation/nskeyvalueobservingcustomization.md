---
title: NSKeyValueObservingCustomization
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservingcustomization
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservingcustomization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservingcustomization.json'
content_hash: 'sha256:20ec19c8aababb8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueObservingCustomization

<sub>Protocol</sub>

Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSKeyValueObservingCustomization : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Type Methods

- [automaticallyNotifiesObservers(for:)](<nskeyvalueobservingcustomization/automaticallynotifiesobservers(for_).md>)
- [keyPathsAffectingValue(for:)](<nskeyvalueobservingcustomization/keypathsaffectingvalue(for_).md>)

## See Also

### Protocols

- [DiscreteFormatStyle](discreteformatstyle.md) — A format style that transforms a continuous input into a discrete output and provides information about its discretization boundaries.
