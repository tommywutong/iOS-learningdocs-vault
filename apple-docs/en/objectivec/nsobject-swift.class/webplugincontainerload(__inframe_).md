---
title: 'webPlugInContainerLoad(_:inFrame:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webplugincontainerload(_:inframe:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugincontainerload(_:inframe:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webplugincontainerload%28_%3Ainframe%3A%29.json'
content_hash: 'sha256:08f034e46eb7157c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInContainerLoad(_:inFrame:)

<sub>Instance Method</sub>

Loads a URL into a web frame.

<sub>macOS</sub>

```swift
func webPlugInContainerLoad(_ request: URLRequest!, inFrame target: String!)
```

## Parameters

- `request` — The request that specifies the URL.

- `target` — The frame into which the URL is loaded.

## Discussion

If the frame specified by `target` is not found, a new window is opened, loaded with the URL request, and given the specified frame name. If `target` is `nil`, the frame enclosing the plug-in is loaded with the URL request.

## See Also

### Performing actions on the enclosing container

- [- webPlugInContainerShowStatus:](<webplugincontainershowstatus(__).md>) — Tells the container to show a status message.
