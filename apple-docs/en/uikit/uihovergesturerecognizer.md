---
title: UIHoverGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uihovergesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uihovergesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uihovergesturerecognizer.json'
content_hash: 'sha256:548fdf034c2a05e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIHoverGestureRecognizer

<sub>Class</sub>

A continuous gesture recognizer that interprets pointer movement over a view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIHoverGestureRecognizer
```

## Overview

On macOS and iPadOS devices, a person can move the pointer over user interface elements. For some UI designs, it’s important to know when the pointer moves over an element, with no other user interactions, such as clicking the mouse button. The text for a hyperlink, for instance, may change colors or appear with an underline as the pointer moves over the link. This creates a rollover effect.

> [!note] Note
> On iOS, this class doesn’t recognize gestures.

To provide this experience in your app, add a hover gesture recognizer that reacts as the pointer moves over the view. Provide the gesture recognizer with a `target` and `action` that the system calls when the pointer enters, exits, and moves across the view. [UIHoverGestureRecognizer](uihovergesturerecognizer.md) has no effect when your app runs in iOS. The following code changes the button’s default color to red as the pointer moves over the button.

```swift
class ViewController: UIViewController {

    @IBOutlet var button: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()

        let hover = UIHoverGestureRecognizer(target: self, action: #selector(hovering(_:)))
        button.addGestureRecognizer(hover)
    }

    @objc
    func hovering(_ recognizer: UIHoverGestureRecognizer) {
        switch recognizer.state {
        case .began, .changed:
            button.titleLabel?.textColor = #colorLiteral(red: 1, green: 0, blue: 0, alpha: 1)
        case .ended:
            button.titleLabel?.textColor = UIColor.link
        default:
            break
        }
    }
}
```

## Relationships

- **Inherits From**: [UIGestureRecognizer](uigesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Supporting Apple Pencil hover

- [altitudeAngle](uihovergesturerecognizer/altitudeangle.md) — A value that represents the altitude angle of the hovering pointing device.
- [- azimuthAngleInView:](<uihovergesturerecognizer/azimuthangle(in_).md>) — A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [- azimuthUnitVectorInView:](<uihovergesturerecognizer/azimuthunitvector(in_).md>) — A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [rollAngle](uihovergesturerecognizer/rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
- [zOffset](uihovergesturerecognizer/zoffset.md) — A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

## See Also

### User interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md) — Detect when someone presses and releases keys on a physical keyboard.
