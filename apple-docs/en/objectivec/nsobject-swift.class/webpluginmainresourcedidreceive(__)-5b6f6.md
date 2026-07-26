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
doc_path: '/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-5b6f6'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive(_:)-5b6f6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidreceive%28_%3A%29-5b6f6.json'
content_hash: 'sha256:0ef0675c76dff623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidReceive(_:)

<sub>Instance Method</sub>

Invoked when the connection loads data incrementally.

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidReceive(_ data: Data!)
```

## Parameters

- `data` — The newly available data.

## Discussion

This message is invoked when the `WebPlugInShouldLoadMainResourceKey` plug-in command-line argument is set to [NO](../no.md) and the underlying `NSURLConnection` object for the main resource sends the connection:didReceiveData: message to its delegate.

## See Also

### Main resource messages

- [- webPlugInMainResourceDidFailWithError:](<webpluginmainresourcedidfailwitherror(__).md>) — Invoked when an error occurs loading the main resource.
- [- webPlugInMainResourceDidFinishLoading](<webpluginmainresourcedidfinishloading().md>) — Invoked when the connection successfully finishes loading data.
- [- webPlugInMainResourceDidReceiveResponse:](<webpluginmainresourcedidreceive(__)-6x7b9.md>) — Invoked when the connection receives sufficient data to construct the URL response for its request.
