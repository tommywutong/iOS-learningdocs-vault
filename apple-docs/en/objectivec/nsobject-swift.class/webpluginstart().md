---
title: webPlugInStart()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webpluginstart()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginstart()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginstart%28%29.json'
content_hash: 'sha256:2ddeac3bb7bba7f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInStart()

<sub>Instance Method</sub>

Tells the plug-in to start normal operation.

<sub>macOS</sub>

```swift
func webPlugInStart()
```

## Discussion

The plug-in usually begins its primary task (such as drawing, playing sounds, or animating) in this method. This method may be called more than once, provided that the application has already called [- webPlugInInitialize](<webplugininitialize().md>) and that each call to this method is followed later by a call to [- webPlugInStop](<webpluginstop().md>).

## See Also

### Controlling the Plug-in

- [- webPlugInDestroy](<webplugindestroy().md>) — Prepares the plug-in for deallocation.
- [- webPlugInInitialize](<webplugininitialize().md>) — Initializes the plug-in.
- [- webPlugInStop](<webpluginstop().md>) — Tells the plug-in to stop normal operation.
