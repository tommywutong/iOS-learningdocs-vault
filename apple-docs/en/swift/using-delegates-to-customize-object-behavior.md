---
title: Using Delegates to Customize Object Behavior
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-delegates-to-customize-object-behavior
source_url: 'https://developer.apple.com/documentation/swift/using-delegates-to-customize-object-behavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-delegates-to-customize-object-behavior.json'
content_hash: 'sha256:2709725258c86411'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Cocoa Design Patterns](cocoa-design-patterns.md)

# Using Delegates to Customize Object Behavior

<sub>Article</sub>

Respond to events on behalf of a delegator.

## Overview

You use delegates to interact with Cocoa objects that inform you of events in an app.

### Adopt a Delegate Protocol

Cocoa APIs often provide protocols that include delegate methods. When an event occurs—such as a user resizing a window—a class that’s a delegator will detect the event and call delegate methods on the class you specify as the delegate. Delegate methods can customize how an app responds to an event.

The example below adopts the [NSWindowDelegate](../appkit/nswindowdelegate.md) protocol and implements its [window(_:willUseFullScreenContentSize:)](<../appkit/nswindowdelegate/window(__willusefullscreencontentsize_).md>) method:

```swift
class MyDelegate: NSObject, NSWindowDelegate {
    func window(_ window: NSWindow, willUseFullScreenContentSize proposedSize: NSSize) -> NSSize {
        return proposedSize
    }
}
```

### Check That Delegates Exist

The Cocoa delegation pattern doesn’t require that delegates are instantiated. If you don’t need to respond to events, you don’t need to create a delegate. Before you call a method on an object’s delegate, make sure that the delegate isn’t `nil`.

The example below creates an [NSWindow](../appkit/nswindow.md) and uses optional chaining to check that the window’s delegate exists before sending a message to the delegate.

```swift
let myWindow = NSWindow(
    contentRect: NSRect(x: 0, y: 0, width: 5120, height: 2880),
    styleMask: .fullScreen,
    backing: .buffered,
    defer: false
)

myWindow.delegate = MyDelegate()
if let fullScreenSize = myWindow.delegate?.window(myWindow, willUseFullScreenContentSize: mySize) {
    print(NSStringFromSize(fullScreenSize))
}
```

## See Also

### Common Patterns

- [Using Key-Value Observing in Swift](using-key-value-observing-in-swift.md) — Notify objects about changes to the properties of other objects.
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md) — Provide access to a shared resource using a single, shared class instance.
- [About Imported Cocoa Error Parameters](about-imported-cocoa-error-parameters.md) — Learn how Cocoa error parameters are converted to Swift throwing methods.
- [Handling Cocoa Errors in Swift](handling-cocoa-errors-in-swift.md) — Throw and catch errors that use Cocoa’s error types.
