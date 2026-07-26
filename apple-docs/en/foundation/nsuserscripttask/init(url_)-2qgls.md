---
title: 'init(url:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuserscripttask/init(url:)-2qgls'
source_url: 'https://developer.apple.com/documentation/foundation/nsuserscripttask/init(url:)-2qgls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuserscripttask/init%28url%3A%29-2qgls.json'
content_hash: 'sha256:bbab25dd6dd786d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserScriptTask](../nsuserscripttask.md)

# init(url:)

<sub>Initializer</sub>

Return a user script task instance given a URL for a script file.

<sub>macOS</sub>

```swift
init(url: URL) throws
```

## Parameters

- `url` — The script URL.

## Return Value

An instance of an `NSUserScriptTask` subclass or `nil` if the file does not appear to match any of the known types.

## Discussion

The returned object will be of one of the specific sub-classes ([NSUserUnixTask](../nsuserunixtask.md), [NSUserAppleScriptTask](../nsuserapplescripttask.md), and [NSUserAutomatorTask](../nsuserautomatortask.md)), or `nil` if the file does not appear to match any of the known types.

If invoked from a subclass, the result will be that class or `nil`.

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Specifying the Script

- [scriptURL](scripturl.md) — The URL of the script file.
