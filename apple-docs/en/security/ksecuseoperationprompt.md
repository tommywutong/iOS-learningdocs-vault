---
title: kSecUseOperationPrompt
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.10+（11.0 起废弃）, tvOS 9.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecuseoperationprompt
source_url: 'https://developer.apple.com/documentation/security/ksecuseoperationprompt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecuseoperationprompt.json'
content_hash: 'sha256:fe469dbddc549933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecUseOperationPrompt

<sub>Global Variable</sub>

A key whose value is an operation prompt.

> [!warning] Deprecated
> Use kSecUseAuthenticationContext and set LAContext.localizedReason property

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecUseOperationPrompt: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and represents a string describing the operation for which the app is attempting to authenticate. When performing user authentication, the system includes the string in the user prompt. The app is responsible for text localization.
