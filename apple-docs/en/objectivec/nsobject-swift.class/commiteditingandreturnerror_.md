---
title: 'commitEditingAndReturnError:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/commiteditingandreturnerror:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commiteditingandreturnerror:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commiteditingandreturnerror%3A.json'
content_hash: 'sha256:38b8c204037faf77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitEditingAndReturnError:

<sub>Instance Method</sub>

Attempt to commit pending edits, returning an error in the case of failure.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) commitEditingAndReturnError:(NSError **) error;
```

## Parameters

- `error` — If an error occurs during the commit operation, upon returns contains an `NSError` object that describes the problem.

## Return Value

[YES](../yes.md) if the commit is successful, otherwise [NO](../no.md).

## Discussion

During autosaving, commit editing may fail, due to a pending edit. Rather than interrupt the user with an unexpected alert, this method provides the caller with the option to either present the error or fail silently, leaving the pending edit in place and the user’s editing uninterrupted. In your implementation of this method, you should attempt to commit editing, but if there is a failure return [NO](../no.md) and in `error` an error object to be presented or ignored as appropriate.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.
