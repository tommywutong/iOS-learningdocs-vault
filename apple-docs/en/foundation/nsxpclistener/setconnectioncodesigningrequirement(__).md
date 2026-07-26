---
title: 'setConnectionCodeSigningRequirement(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpclistener/setconnectioncodesigningrequirement(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/setconnectioncodesigningrequirement(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/setconnectioncodesigningrequirement%28_%3A%29.json'
content_hash: 'sha256:6ec7bd4a5048691f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# setConnectionCodeSigningRequirement(_:)

<sub>Instance Method</sub>

Sets the code signing requirement for connections to this listener.

<sub>macOS</sub>

```swift
func setConnectionCodeSigningRequirement(_ requirement: String)
```

## Parameters

- `requirement` — A string that describes requirements expected of the connection peer. See [Code Signing Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/) for more information on the code signing format.

## Discussion

Use this method to enforce a code-signing requirement on incoming XPC connections.

The following example shows how a listener can ensure that the XPC client service on the other end of a connection has a specific entitlement.

**Swift**

```swift
func listener(_ listener: NSXPCListener,
                      shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool {
    newConnection.exportedObject = MyExportedObject()
    newConnection.exportedInterface = NSXPCInterface(with: MyExportedObjectProtocol.self)
    newConnection.setCodeSigningRequirement("entitlement [com.example.testentitlement] exists")
    newConnection.resume()
    return true
}
```

**Objective-C**

```objc
- (BOOL)listener:(NSXPCListener *)listener shouldAcceptNewConnection:(NSXPCConnection *)newConnection {
    MyExportedObject *e = [[MyExportedObject new] autorelease];
    newConnection.exportedObject = e;
    newConnection.exportedInterface = [NSXPCInterface interfaceWithProtocol:@protocol(MyExportedObjectProtocol)];
    
    // This is an entitlement that must exist on the incoming connection's app signature
    [newConnection setCodeSigningRequirement:@"entitlement [com.example.testentitlement] exists"];
    [newConnection resume];

    return YES;
}
```
