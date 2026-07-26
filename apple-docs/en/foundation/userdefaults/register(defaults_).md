---
title: 'register(defaults:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/register(defaults:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/register(defaults:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/register%28defaults%3A%29.json'
content_hash: 'sha256:096529be7ca56109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# register(defaults:)

<sub>Instance Method</sub>

Specifies the set of default settings and values to use as a fallback in cases where the app domain doesn’t have them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func register(defaults registrationDictionary: [String : Any])
```

## Parameters

- `registrationDictionary` — The dictionary of key-value pairs that contain the default values for your app’s settings. Build this dictionary programmatically or load it from a property list resource file in your app’s bundle.

## Discussion

Call this method shortly after launch to specify the default values for your app’s settings. This method assigns the key-value pairs you provide to the registration domain, which is typically the last domain in the search list. The registration domain is volatile, so you must register the set of default values each time your app launches.
