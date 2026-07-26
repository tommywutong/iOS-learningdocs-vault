---
title: 'init(term:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uireferencelibraryviewcontroller/init(term:)'
source_url: 'https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller/init(term:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uireferencelibraryviewcontroller/init%28term%3A%29.json'
content_hash: 'sha256:c53f195a0698f368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIReferenceLibraryViewController](../uireferencelibraryviewcontroller.md)

# init(term:)

<sub>Initializer</sub>

Initializes a newly created reference-library view controller to display the definition of the given term.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(term: String)
```

## Parameters

- `term` — The term to define.

## Return Value

The newly initialized reference library view controller.

## Discussion

If a definition for the term is not available, a localized message is displayed instead. Use the [+ dictionaryHasDefinitionForTerm:](<dictionaryhasdefinition(forterm_).md>) class method to determine whether a definition is available before creating instances of this class.

## See Also

### Creating a reference-library view controller

- [+ dictionaryHasDefinitionForTerm:](<dictionaryhasdefinition(forterm_).md>) — Returns whether a definition is available for the given term.
- [- initWithCoder:](<init(coder_).md>) — Creates a reference-library view controller from data in an unarchiver.
