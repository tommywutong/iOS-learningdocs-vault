---
title: webPlugInInitialize()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webplugininitialize()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugininitialize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webplugininitialize%28%29.json'
content_hash: 'sha256:547b8b3a088db8fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInInitialize()

<sub>Instance Method</sub>

Initializes the plug-in.

<sub>macOS</sub>

```swift
func webPlugInInitialize()
```

## Discussion

Tells the plug-in to perform one-time initialization. This method must be called only once per instance of the plug-in object, before any other methods in the protocol are called.

## See Also

### Controlling the Plug-in

- [- webPlugInDestroy](<webplugindestroy().md>) — Prepares the plug-in for deallocation.
- [- webPlugInStart](<webpluginstart().md>) — Tells the plug-in to start normal operation.
- [- webPlugInStop](<webpluginstop().md>) — Tells the plug-in to stop normal operation.
