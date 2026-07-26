---
title: webPlugInDestroy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webplugindestroy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webplugindestroy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webplugindestroy%28%29.json'
content_hash: 'sha256:32be07958249eade'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInDestroy()

<sub>Instance Method</sub>

Prepares the plug-in for deallocation.

<sub>macOS</sub>

```swift
func webPlugInDestroy()
```

## Discussion

Typically, this method frees the memory and other resources used by the plug-in. For example, if the plug-in had a copy of a WebPlugInContainer object, this method should relinquish ownership of that object. Do not send any other messages to the plug-in after invoking this method, because calling this method destroys the plug-in. No other methods in this interface may be called after the application has called this method.

## See Also

### Controlling the Plug-in

- [- webPlugInInitialize](<webplugininitialize().md>) — Initializes the plug-in.
- [- webPlugInStart](<webpluginstart().md>) — Tells the plug-in to start normal operation.
- [- webPlugInStop](<webpluginstop().md>) — Tells the plug-in to stop normal operation.
