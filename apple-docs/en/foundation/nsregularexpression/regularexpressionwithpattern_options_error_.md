---
title: 'regularExpressionWithPattern:options:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/regularexpressionwithpattern:options:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/regularexpressionwithpattern:options:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/regularexpressionwithpattern%3Aoptions%3Aerror%3A.json'
content_hash: 'sha256:cb3db3cdb3f5ae68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# regularExpressionWithPattern:options:error:

<sub>Type Method</sub>

Creates an NSRegularExpression instance with the specified regular expression pattern and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSRegularExpression *) regularExpressionWithPattern:(NSString *) pattern options:(NSRegularExpressionOptions) options error:(NSError **) error;
```

## Parameters

- `pattern` — The regular expression pattern to compile.

- `options` — The matching options. See [Options](options-swift.struct.md) for possible values. The values can be combined using the C-bitwise `OR` operator.

- `error` — An out value that returns any error encountered during initialization. Returns an `NSError` object if the regular expression pattern is invalid; otherwise returns `nil`.

## Return Value

An instance of `NSRegularExpression` for the specified regular expression and options.

## See Also

### Creating Regular Expressions

- [- initWithPattern:options:error:](<init(pattern_options_).md>) — Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.
