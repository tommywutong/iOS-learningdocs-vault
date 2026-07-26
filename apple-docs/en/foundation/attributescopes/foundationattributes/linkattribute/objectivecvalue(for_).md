---
title: 'objectiveCValue(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributescopes/foundationattributes/linkattribute/objectivecvalue(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute/objectivecvalue(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/linkattribute/objectivecvalue%28for%3A%29.json'
content_hash: 'sha256:cd33c992e99a5c6c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributeScopes](../../../attributescopes.md) · [FoundationAttributes](../../foundationattributes.md) · [LinkAttribute](../linkattribute.md)

# objectiveCValue(for:)

<sub>Type Method</sub>

Returns an object for a specified URL value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func objectiveCValue(for value: URL) throws -> NSObject
```

## Parameters

- `value` — A URL to produce an [NSObject](../../../../objectivec/nsobject-swift.class.md) from.

## Return Value

The object for the specified URL.

## See Also

### Accessing the Attribute Name and Value

- [name](name.md) — The name of the link attribute.
- [value(for:)](<value(for_).md>) — Returns the URL value of the specified object.
- [Value](value.md) — The type of the link attribute’s value.
- [ObjectiveCValue](objectivecvalue.md) — The type of the link attribute’s value when calling it from Objective-C.
