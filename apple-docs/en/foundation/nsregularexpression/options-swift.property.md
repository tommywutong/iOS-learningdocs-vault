---
title: options
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/options-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/options-swift.property.json'
content_hash: 'sha256:5eea7d7c205b41b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# options

<sub>Instance Property</sub>

Returns the options used when the regular expression option was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: NSRegularExpression.Options { get }
```

## Discussion

The options property specifies aspects of the regular expression matching that are always used when matching the regular expression. For example, if the expression is case sensitive, allows comments, ignores metacharacters, etc. See [Options](options-swift.struct.md) for a complete discussion of the possible constants and their meanings.

## See Also

### Related Documentation

- [- initWithPattern:options:error:](<init(pattern_options_).md>) — Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.

### Getting the Regular Expression and Options

- [pattern](pattern.md) — Returns the regular expression pattern.
- [numberOfCaptureGroups](numberofcapturegroups.md) — Returns the number of capture groups in the regular expression.
