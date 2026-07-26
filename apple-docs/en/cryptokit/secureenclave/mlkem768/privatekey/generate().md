---
title: generate()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/mlkem768/privatekey/generate()
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey/generate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mlkem768/privatekey/generate%28%29.json'
content_hash: 'sha256:abba55df61dca4a7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# generate()

<sub>Type Method</sub>

Generates a new random private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func generate() throws -> SecureEnclave.MLKEM768.PrivateKey
```

## Return Value

The generated private key

## Discussion

This method implements the required interface for the KEMPrivateKey extension, in this case invoking the initializer with a default SecAccessControl and no LAContext.

## See Also

### Creating a private key

- [init(accessControl:authenticationContext:)](<init(accesscontrol_authenticationcontext_).md>)
- [init(dataRepresentation:authenticationContext:)](<init(datarepresentation_authenticationcontext_).md>)
