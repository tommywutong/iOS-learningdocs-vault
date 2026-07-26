---
title: 'queryItemWithName:value:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlqueryitem/queryitemwithname:value:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlqueryitem/queryitemwithname:value:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlqueryitem/queryitemwithname%3Avalue%3A.json'
content_hash: 'sha256:73b23e5712b3cbc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLQueryItem](../nsurlqueryitem.md)

# queryItemWithName:value:

<sub>Type Method</sub>

Creates a new query item with the specified name and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) queryItemWithName:(NSString *) name value:(NSString *) value;
```

## Parameters

- `name` — The name of the query item. For example, in the URL `http://www.apple.com/search/?q=iPad`, the `name` parameter is `q`.

- `value` — The value for the query item. For example, in the URL `http://www.apple.com/search/?q=iPad`, the `value` parameter is `iPad`.

## Return Value

A new query item object.

## Discussion

To use the newly initialized query item in composing a URL, add it to the [queryItems](../nsurlcomponents/queryitems.md) array of an [NSURLComponents](../nsurlcomponents.md) instance. Because assigning an array of query items to an [NSURLComponents](../nsurlcomponents.md) instance automatically encodes the name and value properties, you should not percent-encode these strings.

## See Also

### Creating a Query Item

- [- initWithName:value:](<init(name_value_).md>) — Initializes a newly allocated query item with the specified name and value.
