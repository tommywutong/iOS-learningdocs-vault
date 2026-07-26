---
title: NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy/nsattributedstringmarkdownparsingfailurereturnpartiallyparsedifpossible
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy/nsattributedstringmarkdownparsingfailurereturnpartiallyparsedifpossible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy/nsattributedstringmarkdownparsingfailurereturnpartiallyparsedifpossible.json'
content_hash: 'sha256:6e5824d2d906c3f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedStringMarkdownParsingFailurePolicy](../nsattributedstringmarkdownparsingfailurepolicy.md)

# NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible

<sub>Enumeration Case</sub>

A policy to return a partially parsed string, if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible
```

## Discussion

With this policy, the returned string may include unparsed markup. If returning a partially parsed string isn’t possible, the parser may return an error anyway.

## See Also

### Failure Policies

- [NSAttributedStringMarkdownParsingFailureReturnError](nsattributedstringmarkdownparsingfailurereturnerror.md) — A policy to return an error from the initializer if parsing fails.
