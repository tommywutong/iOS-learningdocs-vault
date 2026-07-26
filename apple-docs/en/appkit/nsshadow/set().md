---
title: set()
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsshadow/set()
source_url: 'https://developer.apple.com/documentation/appkit/nsshadow/set()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsshadow/set%28%29.json'
content_hash: 'sha256:fb8016e9c4527636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSShadow](../nsshadow.md)

# set()

<sub>Instance Method</sub>

Sets the shadow of subsequent drawing operations to the current shadow.

<sub>macOS</sub>

```swift
func set()
```

## Discussion

The shadow attributes of the receiver are used until another shadow is set or until the graphics state is restored.
