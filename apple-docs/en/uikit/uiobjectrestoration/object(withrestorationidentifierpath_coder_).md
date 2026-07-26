---
title: 'object(withRestorationIdentifierPath:coder:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiobjectrestoration/object(withrestorationidentifierpath:coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiobjectrestoration/object(withrestorationidentifierpath:coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiobjectrestoration/object%28withrestorationidentifierpath%3Acoder%3A%29.json'
content_hash: 'sha256:997893c906d82af7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIObjectRestoration](../uiobjectrestoration.md)

# object(withRestorationIdentifierPath:coder:)

<sub>Type Method</sub>

Requests the object that corresponds to the specified identifier information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func object(withRestorationIdentifierPath identifierComponents: [String], coder: NSCoder) -> (any UIStateRestoring)?
```

## Parameters

- `identifierComponents` — An array of [NSString](../../foundation/nsstring.md) objects corresponding to the restoration identifiers of the desired object and all of its ancestors in the restoration hierarchy. The last value in the array is the restoration identifier of the desired object. Earlier entries represent the restoration identifiers of its ancestors.

- `coder` — The keyed archiver containing the app’s saved state information.

## Return Value

The object to use or `nil` if you do not want to restore this object now.

## Discussion

Your implementation of this method should create (or find) the corresponding object and return it. If your restoration class determines that the object shouldn’t be restored, it may return `nil` from this method.

You use the strings in the `identifierComponents` parameter to identify the object being requested. The object may be at the end of a restoration hierarchy containing your app’s view controllers and other objects. The strings in the `identifierComponents` array identify the path through this hierarchy to the desired object.

It isn’t always necessary to create a new object in your implementation of this method. You can also return an existing object that was created by another means. For example, if the object had already been created by your app delegate at initialization time, you’d return that object rather than create a new one.

Your implementation of this method may use any data in the provided `coder` to assist in the restoration process. However, you don’t need to restore the entire state of the object at this point. During a later pass, objects that define a [- decodeRestorableStateWithCoder:](<../uiviewcontroller/decoderestorablestate(with_).md>) method are given a chance to restore their state from the same coder object.

> [!note] Note
> If you return an object whose class doesn’t match the class of the originally preserved object, or whose class isn’t a direct subclass of the original, the restoration system doesn’t call the [- decodeRestorableStateWithCoder:](<../uiviewcontroller/decoderestorablestate(with_).md>) method of the object.
