---
title: numberOfCaptureGroups
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/numberofcapturegroups
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/numberofcapturegroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/numberofcapturegroups.json'
content_hash: 'sha256:eda5e2f4f2a555aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# numberOfCaptureGroups

<sub>Instance Property</sub>

Returns the number of capture groups in the regular expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfCaptureGroups: Int { get }
```

## Discussion

A capture group consists of each possible match within a regular expression. Each capture group can then be used in a replacement template to insert that value into a replacement string.

This value puts a limit on the values of `n` for `$n` in templates, and it determines the number of ranges in the returned [NSTextCheckingResult](../nstextcheckingresult.md) instances returned in the `match...` methods.

An exception will be generated if you attempt to access a result with an index value exceeding `numberOfCaptureGroups``-1`.

## See Also

### Getting the Regular Expression and Options

- [pattern](pattern.md) — Returns the regular expression pattern.
- [options](options-swift.property.md) — Returns the options used when the regular expression option was created.
