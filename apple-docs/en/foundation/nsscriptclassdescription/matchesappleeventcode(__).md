---
title: 'matchesAppleEventCode(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptclassdescription/matchesappleeventcode(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptclassdescription/matchesappleeventcode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptclassdescription/matchesappleeventcode%28_%3A%29.json'
content_hash: 'sha256:8749333e81349051'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptClassDescription](../nsscriptclassdescription.md)

# matchesAppleEventCode(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.

<sub>Mac Catalyst, macOS</sub>

```swift
func matchesAppleEventCode(_ appleEventCode: FourCharCode) -> Bool
```

## Parameters

- `appleEventCode` — An Apple event code to compare against the receiver’s primary or secondary codes.

## Return Value

[true](../../swift/true.md) if the receiver’s primary four-character Apple event code or any of its secondary codes (its synonyms) matches `code`; otherwise, [false](../../swift/false.md).

## See Also

### Getting and comparing Apple event codes

- [appleEventCode](appleeventcode.md) — Returns the Apple event code associated with the receiver’s class.
- [- appleEventCodeForKey:](<appleeventcode(forkey_).md>) — Returns the Apple event code for the specified attribute or relationship in the receiver.
