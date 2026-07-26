---
title: WebPlugIn
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/webplugin
source_url: 'https://developer.apple.com/documentation/objectivec/webplugin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/webplugin.json'
content_hash: 'sha256:0c24d454f77cac65'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# WebPlugIn

<sub>API Collection</sub>

The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.

## Topics

### Accessing the Scripting Environment

- [objectForWebScript](nsobject-swift.class/objectforwebscript.md) — Returns an object that exposes the plug-in’s scripting interface.

### Using Plug-in State Information

- [- webPlugInSetIsSelected:](<nsobject-swift.class/webpluginsetisselected(__).md>) — Controls plug-in behavior based on its selection.

### Controlling the Plug-in

- [- webPlugInDestroy](<nsobject-swift.class/webplugindestroy().md>) — Prepares the plug-in for deallocation.
- [- webPlugInInitialize](<nsobject-swift.class/webplugininitialize().md>) — Initializes the plug-in.
- [- webPlugInStart](<nsobject-swift.class/webpluginstart().md>) — Tells the plug-in to start normal operation.
- [- webPlugInStop](<nsobject-swift.class/webpluginstop().md>) — Tells the plug-in to stop normal operation.

### Main resource messages

- [- webPlugInMainResourceDidFailWithError:](<nsobject-swift.class/webpluginmainresourcedidfailwitherror(__).md>) — Invoked when an error occurs loading the main resource.
- [- webPlugInMainResourceDidFinishLoading](<nsobject-swift.class/webpluginmainresourcedidfinishloading().md>) — Invoked when the connection successfully finishes loading data.
- [- webPlugInMainResourceDidReceiveData:](<nsobject-swift.class/webpluginmainresourcedidreceive(__)-5b6f6.md>) — Invoked when the connection loads data incrementally.
- [- webPlugInMainResourceDidReceiveResponse:](<nsobject-swift.class/webpluginmainresourcedidreceive(__)-6x7b9.md>) — Invoked when the connection receives sufficient data to construct the URL response for its request.

## See Also

### Interacting with Web Plug-ins

- [WebPlugInContainer](webplugincontainer.md) — `WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.
