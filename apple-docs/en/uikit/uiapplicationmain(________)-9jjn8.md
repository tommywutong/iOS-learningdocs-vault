---
title: 'UIApplicationMain(_:_:_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, Swift（4.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationmain(_:_:_:_:)-9jjn8'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationmain(_:_:_:_:)-9jjn8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationmain%28_%3A_%3A_%3A_%3A%29-9jjn8.json'
content_hash: 'sha256:dea872f48b496611'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIApplicationMain(_:_:_:_:)

<sub>Function</sub>

Creates the application object and the application delegate and sets up the event cycle.

> [!warning] Deprecated
> Use [@main](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#main) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func UIApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, _ principalClassName: String?, _ delegateClassName: String?) -> Int32
```

## Parameters

- `argc` — The count of arguments in `argv`; this usually is the corresponding parameter to `main`.

- `argv` — A variable list of arguments; this usually is the corresponding parameter to `main`.

- `principalClassName` — The name of the [UIApplication](uiapplication.md) class or subclass. If you specify `nil`, [UIApplication](uiapplication.md) is assumed.

- `delegateClassName` — The name of the class from which the application delegate is instantiated. If `principalClassName` designates a subclass of [UIApplication](uiapplication.md), you may designate the subclass as the delegate; the subclass instance receives the application-delegate messages. Specify `nil` if you load the delegate object from your application’s main nib file.

## Return Value

Even though an integer return type is specified, this function never returns. When users exits an iOS app by pressing the Home button, the application moves to the background.

## Discussion

This function instantiates the application object from the principal class and instantiates the delegate (if any) from the given class and sets the delegate for the application. It also sets up the main event loop, including the application’s run loop, and begins processing events. If the application’s `Info.plist` file specifies a main nib file to be loaded, by including the [NSMainNibFile](../bundleresources/information-property-list/nsmainnibfile.md) key and a valid nib file name for the value, this function loads that nib file.

Despite the declared return type, this function never returns.

## See Also

### Deprecated functions

- [UIGraphicsBeginImageContext](<uigraphicsbeginimagecontext(__).md>) — Creates a bitmap-based graphics context and makes it the current context. _(deprecated)_
- [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) — Returns an image from the contents of the current bitmap-based graphics context. _(deprecated)_
- [UIGraphicsEndImageContext](<uigraphicsendimagecontext().md>) — Removes the current bitmap-based graphics context from the top of the stack. _(deprecated)_
