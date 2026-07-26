---
title: 'validModesForFontPanel:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel%3A.json'
content_hash: 'sha256:bf0a1743814f4abf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validModesForFontPanel:

<sub>Instance Method</sub>

Returns the mode mask corresponding to the expected font panel mode.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSFontPanelModeMask) validModesForFontPanel:(NSFontPanel *) fontPanel;
```

## Discussion

The mode masks are defined in [Mode Masks](../../appkit/mode-masks.md).

The Font Panel has the ability to hide elements that are not applicable for a given context by having the target respond to [validModesForFontPanel:](validmodesforfontpanel_.md). If the target desires a font panel mode other than the standard mode mask, it must respond to this method.

This message is sent up the responder chain to the first responder implementing the method. Ideally that object should be the first responder found that also implements [changeFont:](changefont_.md).
