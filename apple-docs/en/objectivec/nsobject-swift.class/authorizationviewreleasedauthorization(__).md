---
title: 'authorizationViewReleasedAuthorization(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization%28_%3A%29.json'
content_hash: 'sha256:529aad0aa2e09729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewReleasedAuthorization(_:)

<sub>Instance Method</sub>

Sent to the delegate to indicate that deauthorization is about to occur.

<sub>macOS</sub>

```swift
func authorizationViewReleasedAuthorization(_ view: SFAuthorizationView!)
```

## Discussion

This method is called after deauthorization has been approved (either you called the [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) method, or the user clicked an open lock icon and the [- authorizationViewShouldDeauthorize:](<authorizationviewshoulddeauthorize(__).md>) delegate method did not cancel the operation), and before the user is deauthorized (that is, before the [- authorizationViewDidDeauthorize:](<authorizationviewdiddeauthorize(__).md>) delegate method is called).

## See Also

### Related Documentation

- [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) — Sets the authorization state to unauthorized and locks the lock icon in the view.
