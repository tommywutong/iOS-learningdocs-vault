---
title: kCFErrorDescriptionKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcferrordescriptionkey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcferrordescriptionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcferrordescriptionkey.json'
content_hash: 'sha256:fa6758f06542f802'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFErrorDescriptionKey

<sub>Global Variable</sub>

Key to identify the description in the `userInfo` dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFErrorDescriptionKey: CFString!
```

## Discussion

When you create a CFError object, you can provide a value for this key if you do not have localizable error strings. The description should be a complete sentence if possible, and should not contain the domain name or error code.

## See Also

### Constants

- [kCFErrorLocalizedDescriptionKey](kcferrorlocalizeddescriptionkey.md) — Key to identify the user-presentable description in the `userInfo` dictionary.
- [kCFErrorLocalizedFailureReasonKey](kcferrorlocalizedfailurereasonkey.md) — Key to identify the user-presentable failure reason in the `userInfo` dictionary.
- [kCFErrorLocalizedRecoverySuggestionKey](kcferrorlocalizedrecoverysuggestionkey.md) — Key to identify the user-presentable recovery suggestion in the `userInfo` dictionary.
- [kCFErrorUnderlyingErrorKey](kcferrorunderlyingerrorkey.md) — Key to identify the underlying error in the `userInfo` dictionary.
- [kCFErrorURLKey](kcferrorurlkey.md) — Key to identify associated URL in the `userInfo` dictionary.
- [kCFErrorFilePathKey](kcferrorfilepathkey.md) — Key to identify associated file path in the `userInfo` dictionary.
