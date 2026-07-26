---
title: 'webPlugInMainResourceDidFailWithError(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webpluginmainresourcedidfailwitherror%28_%3A%29.json'
content_hash: 'sha256:7e4ee8c71ebb92b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webPlugInMainResourceDidFailWithError(_:)

<sub>Instance Method</sub>

Invoked when an error occurs loading the main resource.

<sub>macOS</sub>

```swift
func webPlugInMainResourceDidFailWithError(_ error: (any Error)!)
```

## Parameters

- `error` — An error object containing details of why the connection failed to load the request successfully.

## Discussion

This message is invoked when the underlying `NSURLConnection` object for the main resource sends the connection:didFailWithError: message to its delegate.

## See Also

### Main resource messages

- [- webPlugInMainResourceDidFinishLoading](<webpluginmainresourcedidfinishloading().md>) — Invoked when the connection successfully finishes loading data.
- [- webPlugInMainResourceDidReceiveData:](<webpluginmainresourcedidreceive(__)-5b6f6.md>) — Invoked when the connection loads data incrementally.
- [- webPlugInMainResourceDidReceiveResponse:](<webpluginmainresourcedidreceive(__)-6x7b9.md>) — Invoked when the connection receives sufficient data to construct the URL response for its request.
