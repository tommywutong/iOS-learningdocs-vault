---
title: NSAttributeType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributetype
source_url: 'https://developer.apple.com/documentation/coredata/nsattributetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributetype.json'
content_hash: 'sha256:6748f9aced7f0e37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSAttributeType

<sub>Enumeration</sub>

The types of attribute that Core Data supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSAttributeType
```

## Overview

Core Data supports the following attribute types, which differentiate between bit sizes to enable data-store independence. For some types, a scalar option is available.

| **Attribute Type** | **Type** | **Scalar type** | **Scalar by default?** |
|---|---|---|---|
| Integer 16 | [NSNumber](../foundation/nsnumber.md) | [int16_t](../kernel/int16_t.md) | yes |
| Integer 32 | [NSNumber](../foundation/nsnumber.md) | [int32_t](../kernel/int32_t.md) | yes |
| Integer 64 | [NSNumber](../foundation/nsnumber.md) | [int64_t](../kernel/int64_t.md) | yes |
| Double | [NSNumber](../foundation/nsnumber.md) | `double` | yes |
| Float | [NSNumber](../foundation/nsnumber.md) | `float` | yes |
| Boolean | [NSNumber](../foundation/nsnumber.md) | [BOOL](../objectivec/bool.md) | yes |
| Date | [NSDate](../foundation/nsdate.md) | [TimeInterval](../foundation/timeinterval.md) | no |
| Decimal | [NSDecimalNumber](../foundation/nsdecimalnumber.md) | [NSDecimalNumber](../foundation/nsdecimalnumber.md) | no |
| UUID | [NSUUID](../foundation/nsuuid.md) | [NSUUID](../foundation/nsuuid.md) | no |
| URI | [NSURL](../foundation/nsurl.md) | — | — |
| String | [NSString](../foundation/nsstring.md) | — | — |
| Binary data | [NSData](../foundation/nsdata.md) | — | — |
| Transformable | [NSObject](../objectivec/nsobject-swift.class.md) | — | — |
| Composite | — | — | — |
| Undefined | — | — | — |

> [!note] Note
> If your application uses Binary Large Objects (BLOBs) like image and sound data, prefer to store its binary data outside of the Core Data store.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Attribute types

- [NSBinaryDataAttributeType](nsattributetype/binarydataattributetype.md) — An attribute that stores binary data.
- [NSBooleanAttributeType](nsattributetype/booleanattributetype.md) — An attribute that stores a Boolean value.
- [NSCompositeAttributeType](nsattributetype/compositeattributetype.md) — An attribute that derives its value by composing other attributes.
- [NSDateAttributeType](nsattributetype/dateattributetype.md) — An attribute that stores a date.
- [NSDecimalAttributeType](nsattributetype/decimalattributetype.md) — An attribute that stores a decimal value.
- [NSDoubleAttributeType](nsattributetype/doubleattributetype.md) — An attribute that stores a double value.
- [NSFloatAttributeType](nsattributetype/floatattributetype.md) — An attribute that stores a float value.
- [NSInteger16AttributeType](nsattributetype/integer16attributetype.md) — An attribute that stores a 16-bit signed integer value.
- [NSInteger32AttributeType](nsattributetype/integer32attributetype.md) — An attribute that stores a 32-bit signed integer value.
- [NSInteger64AttributeType](nsattributetype/integer64attributetype.md) — An attribute that stores a 64-bit signed integer value.
- [NSObjectIDAttributeType](nsattributetype/objectidattributetype.md) — An attribute that stores a managed object’s ID.
- [NSStringAttributeType](nsattributetype/stringattributetype.md) — An attribute that stores a string.
- [NSTransformableAttributeType](nsattributetype/transformableattributetype.md) — An attribute that uses a value transformer to derive its value.
- [NSUndefinedAttributeType](nsattributetype/undefinedattributetype.md) — An attribute that doesn’t have an explicit type.
- [NSURIAttributeType](nsattributetype/uriattributetype.md) — An attribute that stores a uniform resource identifier.
- [NSUUIDAttributeType](nsattributetype/uuidattributetype.md) — An attribute that stores a universally unique identifier.

### Initializers

- [init(rawValue:)](<nsattributetype/init(rawvalue_).md>)

## See Also

### Standard attributes

- [NSPropertyDescription](nspropertydescription.md) — A description of a single property belonging to an entity.
- [NSAttributeDescription](nsattributedescription.md) — A description of a single attribute belonging to an entity.
- [NSRelationshipDescription](nsrelationshipdescription.md) — A description of a relationship between two entities.
