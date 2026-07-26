---
title: 'authorizationViewDidHide(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide%28_%3A%29.json'
content_hash: 'sha256:d0219af3579b3ce1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewDidHide(_:)

<sub>Instance Method</sub>

Sent to the delegate to indicate that the view’s visibility has changed.

<sub>macOS</sub>

```swift
func authorizationViewDidHide(_ view: SFAuthorizationView!)
```

## Discussion

This delegate method, if present, is called whenever the [isHidden](../../appkit/nsview/ishidden.md) method is called to show or hide the view.
