---
title: UIGestureRecognizerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate.json'
content_hash: 'sha256:465210ad070d70bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGestureRecognizerDelegate

<sub>Protocol</sub>

A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIGestureRecognizerDelegate : NSObjectProtocol
```

## Overview

The delegates receive messages from a gesture recognizer, and their responses to these messages enable them to affect the operation of the gesture recognizer or to specify a relationship between it and another gesture recognizer, such as allowing simultaneous recognition or setting up a dynamic failure requirement.

An example of a situation where dynamic failure requirements are useful is in an app that attaches a screen-edge pan gesture recognizer to a view. In this case, you might want all other relevant gesture recognizers associated with that view’s subtree to require the screen-edge gesture recognizer to fail so you can prevent any graphical glitches that might occur when the other recognizers get canceled after starting the recognition process. To do this, you could use code similar to the following:

**Swift**

```swift
let myScreenEdgePanGestureRecognizer = UIScreenEdgePanGestureRecognizer(target: self, action:#selector(handleScreenEdgePan))
myScreenEdgePanGestureRecognizer.delegate = self
    // Configure the gesture recognizer and attach it to the view.
 
...
 
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldBeRequiredToFailBy otherGestureRecognizer: UIGestureRecognizer) -> Bool {
    guard let myView = myScreenEdgePanGestureRecognizer.view,
          let otherView = otherGestureRecognizer.view else { return false }
    
    return gestureRecognizer == myScreenEdgePanGestureRecognizer &&
           otherView.isDescendant(of: myView)}
```

**Objective-C**

```objc
UIScreenEdgePanGestureRecognizer *myScreenEdgePanGestureRecognizer;
...
myScreenEdgePanGestureRecognizer = [[UIScreenEdgePanGestureRecognizer alloc] initWithTarget:self action:@selector(handleScreenEdgePan:)];
myScreenEdgePanGestureRecognizer.delegate = self;
// Configure the gesture recognizer and attach it to the view.
...
 - (BOOL)gestureRecognizer:(UIGestureRecognizer *)gestureRecognizer shouldBeRequiredToFailByGestureRecognizer:(UIGestureRecognizer *)otherGestureRecognizer {
    BOOL result = NO;
    if ((gestureRecognizer == myScreenEdgePanGestureRecognizer) && [[otherGestureRecognizer view] isDescendantOfView:[gestureRecognizer view]]) {
        result = YES;
    }
    return result;
 }
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITableViewCell](uitableviewcell.md)

## Topics

### Regulating gesture recognition

- [- gestureRecognizerShouldBegin:](<uigesturerecognizerdelegate/gesturerecognizershouldbegin(__).md>) — Asks the delegate if a gesture recognizer should begin interpreting touches.
- [- gestureRecognizer:shouldReceiveTouch:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldreceive_)-16fuh.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [- gestureRecognizer:shouldReceivePress:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldreceive_)-73vzu.md>) — Asks the delegate if a gesture recognizer should receive an object representing a press.
- [- gestureRecognizer:shouldReceiveEvent:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldreceive_)-evxd.md>) — Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.

### Controlling simultaneous gesture recognition

- [- gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldrecognizesimultaneouslywith_).md>) — Asks the delegate if two gesture recognizers should be allowed to recognize gestures simultaneously.

### Setting up failure requirements

- [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldrequirefailureof_).md>) — Asks the delegate if a gesture recognizer should require another gesture recognizer to fail.
- [- gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldberequiredtofailby_).md>) — Asks the delegate if a gesture recognizer should be required to fail by another gesture recognizer.

## See Also

### Custom gestures

- [Implementing a custom gesture recognizer](implementing-a-custom-gesture-recognizer.md) — Discover when and how to build your own gesture recognizers.
- [UIGestureRecognizer](uigesturerecognizer.md) — The base class for concrete gesture recognizers.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — Enrich your app’s user experience by supporting standard and custom gesture interaction.
