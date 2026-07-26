---
title: webPlugInStop()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webpluginstop()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginstop()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginstop%28%29.json'
content_hash: 'sha256:1fc73ac644d9bd3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInStop()

<sub>Instance Method</sub>

Tells the plug-in to stop normal operation.

<sub>macOS</sub>

```swift
func webPlugInStop()
```

## Discussion

This method may be called more than once, provided that the application has already called [- webPlugInInitialize](<webplugininitialize().md>) and that each call to this method is preceded by a call to [- webPlugInStart](<webpluginstart().md>).

## See Also

### Controlling the Plug-in

- [- webPlugInDestroy](<webplugindestroy().md>) — Prepares the plug-in for deallocation.
- [- webPlugInInitialize](<webplugininitialize().md>) — Initializes the plug-in.
- [- webPlugInStart](<webpluginstart().md>) — Tells the plug-in to start normal operation.
