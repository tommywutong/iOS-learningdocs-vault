---
title: 'authorizationViewCreatedAuthorization(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization%28_%3A%29.json'
content_hash: 'sha256:803e5283d9e3f9cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewCreatedAuthorization(_:)

<sub>Instance Method</sub>

Sent to the delegate to indicate the authorization object has been created or changed.

<sub>macOS</sub>

```swift
func authorizationViewCreatedAuthorization(_ view: SFAuthorizationView!)
```

## Discussion

If you have saved a copy of the authorization object for your own purposes, you should discard it and call [authorization()](<../../securityinterface/sfauthorizationview/authorization().md>) for a new authorization object.
