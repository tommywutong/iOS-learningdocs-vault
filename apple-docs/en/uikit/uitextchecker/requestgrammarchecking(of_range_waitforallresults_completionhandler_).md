---
title: 'requestGrammarChecking(of:range:waitForAllResults:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uitextchecker/requestgrammarchecking(of:range:waitforallresults:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextchecker/requestgrammarchecking(of:range:waitforallresults:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextchecker/requestgrammarchecking%28of%3Arange%3Awaitforallresults%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:207ef46b32f9a007'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextChecker](../uitextchecker.md)

# requestGrammarChecking(of:range:waitForAllResults:completionHandler:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestGrammarChecking(of stringToCheck: String, range: NSRange, waitForAllResults: Bool, completionHandler: (([NSTextCheckingResult]) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestGrammarChecking(of stringToCheck: String, range: NSRange, waitForAllResults: Bool) async -> [NSTextCheckingResult]
```
