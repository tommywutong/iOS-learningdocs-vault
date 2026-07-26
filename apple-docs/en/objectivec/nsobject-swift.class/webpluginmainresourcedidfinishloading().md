---
title: webPlugInMainResourceDidFinishLoading()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfinishloading%28%29.json'
content_hash: 'sha256:c235510351fbc43a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidFinishLoading()

<sub>Instance Method</sub>

Invoked when the connection successfully finishes loading data.

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidFinishLoading()
```

## Discussion

This message is invoked when the `WebPlugInShouldLoadMainResourceKey` plug-in command-line argument is set to [NO](../no.md) and the underlying `NSURLConnection` object for the main resource sends the connectionDidFinishLoading: message to its delegate.

## See Also

### Main resource messages

- [- webPlugInMainResourceDidFailWithError:](<webpluginmainresourcedidfailwitherror(__).md>) — Invoked when an error occurs loading the main resource.
- [- webPlugInMainResourceDidReceiveData:](<webpluginmainresourcedidreceive(__)-5b6f6.md>) — Invoked when the connection loads data incrementally.
- [- webPlugInMainResourceDidReceiveResponse:](<webpluginmainresourcedidreceive(__)-6x7b9.md>) — Invoked when the connection receives sufficient data to construct the URL response for its request.
