---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/subscript(_:)-2yypq'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/subscript(_:)-2yypq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/subscript%28_%3A%29-2yypq.json'
content_hash: 'sha256:e16cfbdda65ea5f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Obtain the discontiguous substring of a selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(selection: AttributedTextSelection) -> DiscontiguousAttributedSubstring { get }
```

## Overview

In the case of an insertion point, this substring is empty. Otherwise, the substring contains all selected characters.
