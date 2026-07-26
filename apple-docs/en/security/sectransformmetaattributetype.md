---
title: SecTransformMetaAttributeType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformmetaattributetype
source_url: 'https://developer.apple.com/documentation/security/sectransformmetaattributetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformmetaattributetype.json'
content_hash: 'sha256:86c911f5f0af1cc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformMetaAttributeType

<sub>Enumeration</sub>

The keys that describe the metadata attributes of transform attributes.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
enum SecTransformMetaAttributeType
```

## Overview

Use one of these values as the `type` parameter in a call to the [SecTransformCustomSetAttribute](<sectransformcustomsetattribute(________).md>) or [SecTransformCustomGetAttribute](<sectransformcustomgetattribute(______).md>) function. These values allow you to access not only the value of an attribute, as you would do directly with calls the [SecTransformSetAttribute](<sectransformsetattribute(________).md>) or [SecTransformGetAttribute](<sectransformgetattribute(____).md>) function, but also the metadata associated with that attribute, such as the name of an attribute, or whether it is required to have a value.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecTransformMetaAttributeCanCycle](sectransformmetaattributetype/cancycle.md) — The transform allows cyclic behavior. _(deprecated)_
- [kSecTransformMetaAttributeDeferred](sectransformmetaattributetype/deferred.md) — The attribute defers notifications. _(deprecated)_
- [kSecTransformMetaAttributeExternalize](sectransformmetaattributetype/externalize.md) — The attribute is exportable. _(deprecated)_
- [kSecTransformMetaAttributeHasInboundConnection](sectransformmetaattributetype/hasinboundconnection.md) — The attribute has an inbound connection. _(deprecated)_
- [kSecTransformMetaAttributeHasOutboundConnections](sectransformmetaattributetype/hasoutboundconnections.md) — The attribute has an outbound connection. _(deprecated)_
- [kSecTransformMetaAttributeName](sectransformmetaattributetype/name.md) — The name of the attribute. _(deprecated)_
- [kSecTransformMetaAttributeRef](sectransformmetaattributetype/ref.md) — A direct reference to an attribute’s value. _(deprecated)_
- [kSecTransformMetaAttributeRequired](sectransformmetaattributetype/required.md) — Indicates whether the attribute value is optional. _(deprecated)_
- [kSecTransformMetaAttributeRequiresOutboundConnection](sectransformmetaattributetype/requiresoutboundconnection.md) — The attribute requires an outbound connection. _(deprecated)_
- [kSecTransformMetaAttributeStream](sectransformmetaattributetype/stream.md) — The attribute expects stream operation. _(deprecated)_
- [kSecTransformMetaAttributeValue](sectransformmetaattributetype/value.md) — The actual value of the attribute. _(deprecated)_

### Initializers

- [init(rawValue:)](<sectransformmetaattributetype/init(rawvalue_).md>) _(deprecated)_
