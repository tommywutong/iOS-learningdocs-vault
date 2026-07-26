---
title: 'dictionaryHasDefinition(forTerm:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:)'
source_url: 'https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uireferencelibraryviewcontroller/dictionaryhasdefinition%28forterm%3A%29.json'
content_hash: 'sha256:d2824de106126615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIReferenceLibraryViewController](../uireferencelibraryviewcontroller.md)

# dictionaryHasDefinition(forTerm:)

<sub>Type Method</sub>

Returns whether a definition is available for the given term.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func dictionaryHasDefinition(forTerm term: String) -> Bool
```

## Parameters

- `term` — The term to be defined.

## Return Value

[true](../../swift/true.md) if a definition for `term` is available; otherwise, [false](../../swift/false.md).

## See Also

### Creating a reference-library view controller

- [- initWithTerm:](<init(term_).md>) — Initializes a newly created reference-library view controller to display the definition of the given term.
- [- initWithCoder:](<init(coder_).md>) — Creates a reference-library view controller from data in an unarchiver.
