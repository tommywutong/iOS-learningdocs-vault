---
title: 'webPlugInMainResourceDidReceive(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-6x7b9'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-6x7b9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive%28_%3A%29-6x7b9.json'
content_hash: 'sha256:e7f5503274926f71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidReceive(_:)

<sub>Instance Method</sub>

Invoked when the connection receives sufficient data to construct the URL response for its request.

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidReceive(_ response: URLResponse!)
```

## Parameters

- `response` — The URL response for the connection’s request.

## Discussion

This message is invoked when the `WebPlugInShouldLoadMainResourceKey` plug-in command-line argument is set to [NO](../no.md) and the underlying `NSURLConnection` object for the main resource sends the connection:didReceiveResponse: message to its delegate.

## See Also

### Main resource messages

- [- webPlugInMainResourceDidFailWithError:](<webpluginmainresourcedidfailwitherror(__).md>) — Invoked when an error occurs loading the main resource.
- [- webPlugInMainResourceDidFinishLoading](<webpluginmainresourcedidfinishloading().md>) — Invoked when the connection successfully finishes loading data.
- [- webPlugInMainResourceDidReceiveData:](<webpluginmainresourcedidreceive(__)-5b6f6.md>) — Invoked when the connection loads data incrementally.
