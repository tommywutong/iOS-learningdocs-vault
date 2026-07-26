---
title: ObjectiveCConvertibleAttributedStringKey
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/objectivecconvertibleattributedstringkey
source_url: 'https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/objectivecconvertibleattributedstringkey.json'
content_hash: 'sha256:7a8e8568ae796340'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ObjectiveCConvertibleAttributedStringKey

<sub>Protocol</sub>

A protocol that defines Objective-C interoperability with an attribute key’s value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ObjectiveCConvertibleAttributedStringKey : AttributedStringKey
```

## Overview

Conform to this protocol to allow your attributed string key to customize its Objective-C conversion behavior. This allows you to define an Objective-C value type and provide methods to convert to and from this type.

Attributed string keys that don’t conform to this protocol cast the value to [AnyObject](../swift/anyobject.md) before converting to Objective-C. When converting from Objective-C, the value casts to the key’s [Value](attributedstringkey/value.md) type. In cases where Swift types bridge automatically to Objective-C types, like [String](../swift/string.md) to [NSString](nsstring.md), this default behavior is adequate. But for unbridged value types, you need to conform to this protocol and provide the conversion methods.

## Relationships

- **Inherits From**: [AttributedStringKey](attributedstringkey.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AdjustedPitchAttribute](attributescopes/accessibilityattributes/adjustedpitchattribute.md), [AnnouncementPriorityAttribute](attributescopes/accessibilityattributes/announcementpriorityattribute.md), [HeadingLevelAttribute](attributescopes/accessibilityattributes/headinglevelattribute.md), [TextualContextAttribute](attributescopes/accessibilityattributes/textualcontextattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/appkitattributes/adaptiveimageglyphattribute.md), [StrikethroughStyleAttribute](attributescopes/appkitattributes/strikethroughstyleattribute.md), [UnderlineStyleAttribute](attributescopes/appkitattributes/underlinestyleattribute.md), [InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md), [InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md), [LinkAttribute](attributescopes/foundationattributes/linkattribute.md), [ListItemDelimiterAttribute](attributescopes/foundationattributes/listitemdelimiterattribute.md), [PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponentattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/uikitattributes/adaptiveimageglyphattribute.md), [StrikethroughStyleAttribute](attributescopes/uikitattributes/strikethroughstyleattribute.md), [UnderlineStyleAttribute](attributescopes/uikitattributes/underlinestyleattribute.md)

## Topics

### Accessing the Objective-C Type

- [ObjectiveCValue](objectivecconvertibleattributedstringkey/objectivecvalue.md) — The Objective-C type that corresponds to this key’s value type.

### Converting between Swift and Objective-C Types

- [objectiveCValue(for:)](<objectivecconvertibleattributedstringkey/objectivecvalue(for_).md>) — Returns an Objective-C typed value for a given value of this key’s type.
- [value(for:)](<objectivecconvertibleattributedstringkey/value(for_).md>) — Returns a value of this key’s type for a given Objective-C value.
