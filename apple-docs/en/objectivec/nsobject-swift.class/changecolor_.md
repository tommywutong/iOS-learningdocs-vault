---
title: 'changeColor:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/changecolor:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/changecolor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/changecolor%3A.json'
content_hash: 'sha256:bb2d17131ae1e8fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# changeColor:

<sub>Instance Method</sub>

Sent to the first responder when the user selects a color in an `NSColorPanel` object.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) changeColor:(id) sender;
```

## Parameters

- `sender` — The `NSColorPanel` sending the message.

## Discussion

When the user selects a color in an [NSColorPanel](../../appkit/nscolorpanel.md) object, the panel tries to call this method on the first responder. You can override this method in any responder that needs to respond to a color change.
