---
title: webFrame
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webframe
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webframe.json'
content_hash: 'sha256:b846e475a1d132c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webFrame

<sub>Instance Property</sub>

Returns the `WebFrame` that contains the plug-in.

<sub>macOS</sub>

```swift
var webFrame: WebFrame! { get }
```

## Return Value

The WebFrame that contains the plug-in.

## Discussion

Only implemented by containers that are based on the WebKit’s plug-in architecture.

## See Also

### Obtaining information about the container

- [webPlugInContainerSelectionColor](webplugincontainerselectioncolor.md) — Returns the plug-in selection color.
