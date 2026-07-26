---
title: 'authorizationViewShouldDeauthorize(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize%28_%3A%29.json'
content_hash: 'sha256:b47e54e543a5442a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewShouldDeauthorize(_:)

<sub>Instance Method</sub>

Sent to the delegate when a user clicks the open lock icon.

<sub>macOS</sub>

```swift
func authorizationViewShouldDeauthorize(_ view: SFAuthorizationView!) -> Bool
```

## Discussion

The delegate can react to this before deauthorization happens and avoid it by returning [NO](../no.md). This delegate method is not called when you call the [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) method.

## See Also

### Related Documentation

- [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) — Sets the authorization state to unauthorized and locks the lock icon in the view.
