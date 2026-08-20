---
title: XCPlayground Module Reference
apple_id: TP40016564
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/XCPlaygroundModuleRef/XCPlayground.html
archived_at: '2026-07-27T06:57:10.260929Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Document%20Revision%20History.md)

# XCPlayground Module Reference

The XCPlayground module lets you interact with Xcode from a playground.

To use this module in a playground, import the `XCPlayground` module as follows:

```
import XCPlayground
```

## XCPlaygroundPage Class

An `XCPlaygroundPage` object provides methods and properties that represent the state of a playground page that enable you to interact with Xcode. Functionality includes capturing and displaying values, ending the execution of a playground, and managing a live view.

### Tasks

#### Getting the Current Playground Page

##### currentPage

Gets the current playground page.

__Declaration__

```swift
public class let currentPage: XCPlayground.XCPlaygroundPage
```

__Discussion__

Use `currentPage` to find the playground page instance.

__Availability__

Available in Xcode 7.1 and later.

#### Managing Playground Execution

##### needsIndefiniteExecution

Sets a Boolean value to indicate whether indefinite execution is enabled.

__Declaration__

```
public var needsIndefiniteExecution: Bool
```

__Discussion__

By default, all top-level code is executed, and then execution is terminated. When working with asynchronous code, enable indefinite execution to allow execution to continue after the end of the playground’s top-level code is reached. This, in turn, gives threads and callbacks time to execute.

Editing the playground automatically stops execution, even when indefinite execution is enabled.

Set `needsIndefiniteExecution` to `true` to continue execution after the end of top-level code. set it to `false` to stop execution at that point.

The default value is `false`. It is set to `true` when [liveView](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknltcma) is set to a non-`nil` value.

__Availability__

Available in Xcode 7.1 and later.

##### finishExecution

Terminates execution of the current playground page.

__Declaration__

```
@noreturn public func finishExecution()
```

__Discussion__

Any function running in the playground is terminated by `finishExecution` and does not return a value.

__Availability__

Available in Xcode 7.1 and later.

#### Displaying Information

##### captureValue:withIdentifier:

Captures a value to be displayed with the specified identifier in the timeline.

__Declaration__

```swift
public func captureValue<T>(value: T, withIdentifier identifier: String)
```

__Parameters__

|  |  |
| --- | --- |
| value | The value to be captured and displayed. |
| identifier | The identifier to display in the timeline above the captured value. |

__Discussion__

Capturing multiple values with the same value history identifier displays the values on the same timeline item, such as a graph. Capturing values with different identifiers displays them on different timeline items.

The identifier is displayed in the timeline as the item’s title.

__Availability__

Available in Xcode 7.1 and later.

#### Managing Live Views

##### liveView

The active live view in the assistant timeline or `nil` if there is no live view.

__Declaration__

```
public var liveView: XCPlaygroundLiveViewable?
```

__Discussion__

Display a live view by setting `liveView` to an object that conforms to the `XCPlaygroundLiveViewable` protocol.

Dismiss any open live view by setting `liveView` to `nil`.

The live view is displayed in the assistant editor for the current playground page. There can be only one live view open at any time.

Displaying the live view requires that `needsIndefiniteExecution` is set to `true`. When `liveView` is set to a non-`nil` value the system sets `needsIndefiniteExecution` to `true`.

__Availability__

Available in Xcode 7.1 and later.

## XCPlaygroundLiveViewable Protocol

`XCPlaygroundLiveViewable Protocol` is a protocol for types that can be displayed as the live view for a playground. By default `UIView` and `UIViewController` conform to this protocol on iOS and tvOS, and `NSView` and `NSViewController` conform to this protocol on OS X.

Developers need to implement this protocol only for custom objects that do not inherit from `UIView`, `UIViewController`, `NSView`, or `NSViewController`.

```
public protocol XCPlaygroundLiveViewable
```

### Tasks

#### Returning the Playground Data Directory

##### playgroundLiveViewRepresentation

Returns the view or view controller used to render and manage the live view.

__Declaration__

```swift
public func playgroundLiveViewRepresentation() -> XCPlayground.XCPlaygroundLiveViewRepresentation
```

__Return Value__

A view controller or view able to render and manage the live view. View controllers are preferred.

__Important:__ The view or view controller returned by this method must be the root of the hierarchy. Views cannot have superviews or associated view controllers. View controllers cannot have parent view controllers.

__Discussion__

This protocol enables you to display any type of object in a live view. For example, a playground that presents a simplified user interface programming environment can make its view-like type conform to `XCPlaygroundLiveViewable` and appear in the live view.

The value returned by `playgroundLiveViewRepresentation` can be different each time the method is called.

A custom playgroundLiveViewRepresentation method will have the form:

```swift
func playgroundLiveViewRepresentation() -> XCPlaygroundLiveViewRepresentation {
        let viewController: {NS,UI}ViewController = … // code producing a {NS,UI}ViewController
            // configure the view controller
            …
        return .ViewController(viewController)
}
```

__Availability__

Available in Xcode 7.1 and later.

### Data Types

#### XCPlaygroundLiveViewRepresentation

The system-provided base classes supporting live view representation in a playground.

__Declaration for iOS and tvOS__

```swift
public enum XCPlaygroundLiveViewRepresentation {
        case View(UIView)
        case ViewController(UIViewController)
}
```

__Declaration for OS X__

```swift
public enum XCPlaygroundLiveViewRepresentation {
        case View(NSView)
        case ViewController(NSViewController)
}
```

__Availability__

Available in Xcode 7.1 and later.

## Constants

### XCPlaygroundSharedDataDirectoryURL

The directory used for persistent data shared between playgrounds and playground executions.

__Declaration__

```
public let XCPlaygroundSharedDataDirectoryURL: NSURL
```

__Discussion__

Shared data files are stored in `~/Documents/Shared Playground Data/`. `XCPlaygroundSharedDataDirectoryURL` returns a sandbox-aware directory URL useable in any playground. Constructing your own directory URL is not guaranteed to work.

__Important:__ You must create the `~/Documents/Shared Playground Data/` directory before using this constant. Xcode doesn’t create the directory for you.

__Availability__

Available in Xcode 7.1 and later.

## Deprecated Functions and Properties

The following functions and properties are deprecated in Xcode 7.1 and later.

### XCPCaptureValue

__Deprecated in Xcode 7.1:__ Use [captureValue:withIdentifier:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknltq) instead.

Captures a value to be displayed in the specified value history in the timeline.

__Parameters__

```swift
func XCPCaptureValue<T>(identifier: String, value: T)
```

**identifier**
: The identifier of the value history.

**value**
: The value to be captured.

Capturing multiple values with the same value history identifier displays the values on the same timeline item such as a graph. Capturing values with different identifiers displays them on different timeline items.

The identifier is displayed in the timeline as the item’s title.

### XCPExecutionShouldContinueIndefinitely

__Deprecated in Xcode 7.1:__ Use [needsIndefiniteExecution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknlts) instead.

Returns a Boolean value indicating whether indefinite execution is enabled.

```swift
func XCPExecutionShouldContinueIndefinitely() -> Bool
```

__Return Value__

Returns `true` if execution continues after the end of the playground’s top-level code is reached; otherwise, `false`.

See also [XCPSetExecutionShouldContinueIndefinitely](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknltg).

### XCPSetExecutionShouldContinueIndefinitely

__Deprecated in Xcode 7.1:__ Set [needsIndefiniteExecution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknlts) instead.

Sets a Boolean value to indicate whether indefinite execution is enabled.

```swift
func XCPSetExecutionShouldContinueIndefinitely(continueIndefinitely: Bool = default)
```

**continueIndefinitely**
: Pass `true` to continue execution after the end of top-level code. Pass `false` to stop execution at that point.

The default value is `true`.

By default, all top-level code is executed, and then execution is terminated. When working with asynchronous code, enable indefinite execution to allow execution to continue after the end of the playground’s top-level code is reached. This, in turn, gives threads and callbacks time to execute.

The amount of time that execution continues is controlled by a setting in the timeline. Editing the playground automatically stops execution, even when indefinite execution is enabled.

See also [XCPExecutionShouldContinueIndefinitely](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknlte).

### XCPShowView

__Deprecated in Xcode 7.1:__ Use [liveView](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknltcma) instead.

Displays a view during playground execution and records frames for playback after execution.

```swift
func XCPShowView(identifier: String, view: NSView)
func XCPShowView(identifier: String, view: UIView)
```

**identifier**
: The identifier for the live view.

**view**
: The view to be displayed.

This view must not have a superview. It is automatically added to a window when it is displayed in the timeline.

This function ensures that indefinite execution is enabled, like calling the `XCPExecutionShouldContinueIndefinitely` function.

The identifier is displayed in the timeline with a caption that is the same as the item’s title.

### XCPSharedDataDirectoryPath

__Deprecated in Xcode 7.1:__ Use [XCPlaygroundSharedDataDirectoryURL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknrufvbuqmjnknltcmi) instead.

Returns the path to the directory containing data shared between all playgrounds.

```
let XCPSharedDataDirectoryPath: String
```

Use this directory to store data that needs to be persisted between playground runs or shared between multiple playgrounds.

[Next](Document%20Revision%20History.md)
