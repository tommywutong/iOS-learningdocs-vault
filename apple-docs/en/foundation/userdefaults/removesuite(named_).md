---
title: 'removeSuite(named:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/removesuite(named:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/removesuite(named:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/removesuite%28named%3A%29.json'
content_hash: 'sha256:01a95293954536a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# removeSuite(named:)

<sub>Instance Method</sub>

Removes the specified domain from the search list of the current object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeSuite(named suiteName: String)
```

## Parameters

- `suiteName` — The bundle identifier for the domain you want to remove. Specify the same string you used when you added the domain.

## See Also

### Adding and removing search domains

- [- addSuiteNamed:](<addsuite(named_).md>) — Inserts settings for the specified domain into the search list of the current object.
