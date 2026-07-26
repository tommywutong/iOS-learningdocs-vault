---
title: WebPlugInContainer
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/webplugincontainer
source_url: 'https://developer.apple.com/documentation/objectivec/webplugincontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/webplugincontainer.json'
content_hash: 'sha256:e325b0296eb17c12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# WebPlugInContainer

<sub>API Collection</sub>

`WebPlugInContainer` is an informal protocol that enables a plug-in to send messages to the application.

## Topics

### Performing actions on the enclosing container

- [- webPlugInContainerLoadRequest:inFrame:](<nsobject-swift.class/webplugincontainerload(__inframe_).md>) — Loads a URL into a web frame.
- [- webPlugInContainerShowStatus:](<nsobject-swift.class/webplugincontainershowstatus(__).md>) — Tells the container to show a status message.

### Obtaining information about the container

- [webFrame](nsobject-swift.class/webframe.md) — Returns the `WebFrame` that contains the plug-in.
- [webPlugInContainerSelectionColor](nsobject-swift.class/webplugincontainerselectioncolor.md) — Returns the plug-in selection color.

## See Also

### Related Documentation

- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)

### Interacting with Web Plug-ins

- [WebPlugIn](webplugin.md) — The `WebPlugIn` informal protocol defines methods that enable interaction between an application using the WebKit framework and any WebKit-based plug-ins it may use.
