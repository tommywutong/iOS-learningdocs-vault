---
title: C Callbacks in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/06/c-callbacks-in-swift/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:8752e53c6ff47d3f'
translated: false
---

> 原文：[C Callbacks in Swift](https://oleb.net/blog/2015/06/c-callbacks-in-swift/)　·　Ole Begemann

# C Callbacks in Swift

**Update November 12, 2017:** In the iOS 11 and macOS 10.13 SDKs, Apple added new [`CGPath.applyWithBlock(_:)`](https://developer.apple.com/documentation/coregraphics/cgpath/2873218-applywithblock) (Swift) and [`CGPathApplyWithBlock`](https://developer.apple.com/documentation/coregraphics/2873218-cgpathapplywithblock?language=objc) (C/Objective-C) APIs. This means this article is no longer relevant for this particular example (unless you need to support older OS versions). However, the principles I discuss here apply to calling any C API that takes a function pointer argument from Swift.

---

A few years ago I wrote about [how to access the elements](https://oleb.net/blog/2012/12/accessing-pretty-printing-cgpath-elements/) of a `CGPath` or `UIBezierPath`. To do that in Objective-C, you call the [`CGPathApply`](https://developer.apple.com/reference/coregraphics/1411203-cgpathapply?language=objc) function and pass in a pointer to a callback function. `CGPathApply` then calls this callback for each path element.

If you wanted to do this in Swift 1.x, you were out of luck because there was no way to bridge a Swift function to a C function pointer. You had to write a small wrapper in C or Objective-C that encapsulated the callback function.

As of Swift 2, it’s now possible to do this fully natively in Swift. C function pointers are [imported into Swift as closures](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/BuildingCocoaApps/InteractingWithCAPIs.html#//apple_ref/doc/uid/TP40014216-CH8-ID148). You can pass any Swift closure expression or function with matching parameters to code that expects a C function pointer — with one massive caveat: unlike closures, C function pointers don’t have the concept of capturing state. As a result, the compiler will only allow Swift functions that don’t capture any outside state to be bridged to a C function pointer. Swift uses the `@convention(c)` notation to indicate this calling convention.

# Accessing the elements of a UIBezierPath

Let’s take the familiar task of iterating over the elements of a path as an example.

## A Swift data structure for path elements

First, consider the data structures we have to deal with. [`CGPath.apply`](https://developer.apple.com/reference/coregraphics/cgpath/1411203-apply) will [pass a pointer](https://developer.apple.com/reference/coregraphics/cgpathapplierfunction) to a [`CGPathElement`](https://developer.apple.com/reference/coregraphics/cgpathelement) to the callback function. This is a struct that contains a constant indicating the [type of the path element](https://developer.apple.com/reference/coregraphics/cgpathelementtype) and a C array of [`CGPoint`s](https://developer.apple.com/reference/coregraphics/cgpoint). The number of points in the array varies between 0 and 3 depending on the element type.

Working with `CGPathElement` in Swift is not very pleasant. The C array gets imported as a [`UnsafeMutablePointer<CGPoint>`](https://developer.apple.com/reference/swift/unsafemutablepointer) whose lifetime is limited to the callback function, so we’d have to copy its contents to somewhere else if we wanted to keep the data around. A safer and more convenient way to access the correct number of points for each element type would be nice too.

A Swift `enum` with associated values for the points is ideal for this purpose. A custom initializer does the conversion from `CGPathElement`:

```
/// A Swiftified representation of a `CGPathElement`
/// Simpler and safer than `CGPathElement`.
public enum PathElement {
    case moveToPoint(CGPoint)
    case addLineToPoint(CGPoint)
    case addQuadCurveToPoint(CGPoint, CGPoint)
    case addCurveToPoint(CGPoint, CGPoint, CGPoint)
    case closeSubpath

    init(element: CGPathElement) {
        switch element.type {
        case .moveToPoint:
            self = .moveToPoint(element.points[0])
        case .addLineToPoint:
            self = .addLineToPoint(element.points[0])
        case .addQuadCurveToPoint:
            self = .addQuadCurveToPoint(
                element.points[0], element.points[1])
        case .addCurveToPoint:
            self = .addCurveToPoint(element.points[0],
                element.points[1], element.points[2])
        case .closeSubpath:
            self = .closeSubpath
        }
    }
}
```

Next, let’s add a nice string representation to our new data type for easier debugging.

```
extension PathElement: CustomDebugStringConvertible {
    public var debugDescription: String {
        switch self {
        case let .moveToPoint(point):
            return "moveto \(point)"
        case let .addLineToPoint(point):
            return "lineto \(point)"
        case let .addQuadCurveToPoint(point1, point2):
            return "quadcurveto \(point1), \(point2)"
        case let .addCurveToPoint(point1, point2, point3):
            return "curveto \(point1), \(point2), \(point3)"
        case .closeSubpath:
            return "closepath"
        }
    }
}
```

While we’re at it, we should also make `PathElement` `Equatable` because that’s what [you should always do](https://developer.apple.com/videos/play/wwdc2015/414/) for value types.

```
extension PathElement : Equatable {
    public static func ==(lhs: PathElement, rhs: PathElement) -> Bool {
        switch(lhs, rhs) {
        case let (.moveToPoint(l), .moveToPoint(r)):
            return l == r
        case let (.addLineToPoint(l), .addLineToPoint(r)):
            return l == r
        case let (.addQuadCurveToPoint(l1, l2), .addQuadCurveToPoint(r1, r2)):
            return l1 == r1 && l2 == r2
        case let (.addCurveToPoint(l1, l2, l3), .addCurveToPoint(r1, r2, r3)):
            return l1 == r1 && l2 == r2 && l3 == r3
        case (.closeSubpath, .closeSubpath):
            return true
        case (_, _):
            return false
        }
    }
}
```

## Enumerating path elements

Now comes the interesting part. We’d like to extend [`UIBezierPath`](https://developer.apple.com/reference/uikit/uibezierpath) with a new computed property named `elements` that iterates over the path and returns an array of `PathElement`s. We know that we have to call `CGPath.apply` and pass it a function that gets called for each element. Inside the callback function, we need to convert the `CGPathElement` to a `PathElement` and store it somehow in an array. This last part is not as easy as it sounds because the C calling convention prevents the function from accessing any variables from the surrounding context.

Since pure C implementations of this API face the same problem, `CGPath.apply` takes one more argument in the form of an untyped pointer (`void *` in C) and passes this pointer on to the callback function. This enables the caller to pass an arbitrary piece of data (such as a pointer to an array) to the callback — exactly what we need.

`void *` gets imported into Swift as an optional [`UnsafeMutableRawPointer`](https://developer.apple.com/reference/swift/unsafemutablerawpointer). This is a new type that was [introduced in Swift 3](https://github.com/apple/swift-evolution/blob/master/proposals/0107-unsaferawpointer.md) to differentiate untyped pointers (`void *`) from typed ones (`Unsafe[Mutable]Pointer<T>`).

We can use the [`Unmanaged`](https://developer.apple.com/documentation/swift/unmanaged) type to bridge between the type-safe world and raw pointers. `Unmanged` only works with class instances, however, so it won’t accept a `[PathElement]` value. To work around this, we can create a very simple `Box` class that can wrap any value in an object:

```
class Box<T> {
    private(set) var unbox: T
    
    init(_ value: T) {
        self.unbox = value
    }

    /// Use this method to mutate the boxed value.
    func mutate(_ mutation: (inout T) -> ()) {
        mutation(&unbox)
    }
}
```

In the implementation for the `elements` property, we create an empty array to hold the `PathElement` values and box it up twice, first inside a `Box` and then in an `Unmanaged` instance. The `Unmanaged.toOpaque()` method then provides us with an `UnsafeMutableRawPointer` to the box. It’s this pointer that we pass to `CGPath.apply` as our `userInfo` parameter. The final step in `CGPath.apply`’s callback function is to convert the raw pointer back to an `Unmanaged<Box<[PathElement]>>` value, unbox the array and append the new path element.

The full implementation looks like this:

```
extension UIBezierPath {
    var elements: [PathElement] {
        var pathElements: [PathElement] = []
        // Wrap the array in a Box
        // Wrap the box in an Unmanaged
        let unmanaged = Unmanaged.passRetained(Box(pathElements))
        self.cgPath.apply(info: unmanaged.toOpaque()) {
            userInfo, nextElementPointer in
            // Create the new path element
            let nextElement = PathElement(
                element: nextElementPointer.pointee)
            // Unbox the array and append
            let box: Box<[PathElement]> =
                Unmanaged.fromOpaque(userInfo!).takeUnretainedValue()
            box.mutate { array in array.append(nextElement) }
        }
        // Unwrap the array
        pathElements = unmanaged.takeRetainedValue().unbox
        return pathElements
    }
}
```

## Conforming `UIBezierPath` to `Sequence`

Now that we have an array of path elements, it is trivial to turn `UIBezierPath` into a [`Sequence`](https://developer.apple.com/reference/swift/sequence). This allows users to iterate over the path with a `for element in path` loop or to call methods like [`map`](https://developer.apple.com/reference/swift/sequence/1641748-map) or [`filter`](https://developer.apple.com/reference/swift/sequence/1641239-filter) directly on the path:

```
extension UIBezierPath: Sequence {
    public func makeIterator() -> AnyIterator<PathElement> {
        return AnyIterator(elements.makeIterator())
    }
}
```

# Example

Let’s try this with an example path:

```
let path = UIBezierPath()
path.move(to: CGPoint(x: 0, y: 0))
path.addLine(to: CGPoint(x: 100, y: 0))
path.addLine(to: CGPoint(x: 50, y: 100))
path.close()
path.move(to: CGPoint(x: 0, y: 100))
path.addQuadCurve(to: CGPoint(x: 100, y: 100),
    controlPoint: CGPoint(x: 50, y: 200))
path.close()
path.move(to: CGPoint(x: 100, y: 0))
path.addCurve(to: CGPoint(x: 200, y: 0),
    controlPoint1: CGPoint(x: 125, y: 100),
    controlPoint2: CGPoint(x: 175, y: -100))
path.close()
```

![The example path](https://oleb.net/media/uibezierpath-example.png)

<sub>The example path.</sub>

Now we can iterate over the path and print a description of each element:

```
for element in path {
    debugPrint(element)
}
/* Output:
moveto (0.0, 0.0)
lineto (100.0, 0.0)
lineto (50.0, 100.0)
closepath
moveto (0.0, 100.0)
quadcurveto (50.0, 200.0), (100.0, 100.0)
closepath
moveto (100.0, 0.0)
curveto (125.0, 100.0), (175.0, -100.0), (200.0, 0.0)
closepath
*/
```

Or we can count how many `closepath` commands there are in the path:

```
let closePathCount = path.filter {
    $0 == .closeSubpath
}.count
// -> 3
```

# Conclusion

Swift automatically bridges C function pointers to Swift function types. This makes it possible (and very convenient) to work with a large number of C APIs that take function pointers as callbacks. Because the C calling convention does not allow these functions to capture external state, you often have to pass external variables your callback function needs through an untyped pointer that many C APIs offer for this purpose. Doing this from Swift is a bit convoluted but entirely possible.
