---
title: 'value(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributescopes/foundationattributes/linkattribute/value(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/linkattribute/value(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/linkattribute/value%28for%3A%29.json'
content_hash: 'sha256:0c78b48bc072009a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributeScopes](../../../attributescopes.md) · [FoundationAttributes](../../foundationattributes.md) · [LinkAttribute](../linkattribute.md)

# value(for:)

<sub>Type Method</sub>

Returns the URL value of the specified object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func value(for object: NSObject) throws -> URL
```

## Parameters

- `object` — An [NSObject](../../../../objectivec/nsobject-swift.class.md) to retrieve a URL value from.

## Return Value

A URL value.

## See Also

### Accessing the Attribute Name and Value

- [name](name.md) — The name of the link attribute.
- [Value](value.md) — The type of the link attribute’s value.
- [objectiveCValue(for:)](<objectivecvalue(for_).md>) — Returns an object for a specified URL value.
- [ObjectiveCValue](objectivecvalue.md) — The type of the link attribute’s value when calling it from Objective-C.
