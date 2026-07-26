---
title: targetView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowsertransitioncontroller/targetview
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowsertransitioncontroller/targetview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowsertransitioncontroller/targetview.json'
content_hash: 'sha256:4095286dd97aaf6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserTransitionController](../uidocumentbrowsertransitioncontroller.md)

# targetView

<sub>Instance Property</sub>

The target view for transition animations when presenting or dismissing the transition controller’s document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var targetView: UIView? { get set }
```

## Discussion

When this property is set, the transition controller acts as a [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) object for the transition from the browser to the document view controller. It provides transition animation that zooms and cross fades from the document’s thumbnail to the target view.

To use the transition animation:

1. Instantiate the view controller to display the document.
2. Call the document view controller’s [- loadViewIfNeeded](<../uiviewcontroller/loadviewifneeded().md>) method to ensure that the view hierarchy is loaded.
3. Request a transition controller for the document you are going to present.
4. Assign a view from the document view controller to the transition controller’s [targetView](targetview.md) property.
5. Create a [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md) object that returns the transition controller. You must keep a strong reference to both the transition controller and the transitioning delegate throughout the entire animation.
6. Set the document view controller’s [modalPresentationStyle](../uiviewcontroller/modalpresentationstyle.md) property to custom.
7. Assign the transitioning delegate to the document view controller’s [transitioningDelegate](../uiviewcontroller/transitioningdelegate.md) property.
8. Present the document view controller.

In the following code, the transition controller provides a zoom and fade transition animation both when presenting the document view controller, and when dismissing it.

```swift
let doc = // Create a UIDocument subclass for the selected URL.
let editor = // Create a view controller to edit the document.

// Load the editor's view hierarchy.
editor.loadViewIfNeeded()

// Get the transition controller
let transitionController = controller.transitionController(forDocumentURL: url)

// Set the target view
transitionController.targetView = editor.textView

// Instantiate the transitioning delegate
let transitionDelegate = UIDocumentBrowserTransitioningDelegate(withTransitionController: transitionController)

// Configure the transition animation
editor.modalPresentationStyle = .custom
editor.transitioningDelegate = transitionDelegate

// Keep a strong reference to the transition delegate.
doc.transitioningDelegate = transitionDelegate

// Open the document
doc.open { (success) in
    guard success else {
        // Handle the error here...
    }
        
    // When the load is done, present the document
    controller.present(editor, animated: true, completion: nil)
}
```

```swift
class UIDocumentBrowserTransitioningDelegate : NSObject, UIViewControllerTransitioningDelegate {
    
    let transitionController : UIDocumentBrowserTransitionController
    
    init(withTransitionController transitionController: UIDocumentBrowserTransitionController) {
        self.transitionController = transitionController
    }
    
    func animationController(forPresented presented: UIViewController, presenting: UIViewController, source: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return transitionController
    }
    
    func animationController(forDismissed dismissed: UIViewController) -> UIViewControllerAnimatedTransitioning? {
        return transitionController
    }
}
```

## See Also

### Animating transitions

- [loadingProgress](loadingprogress.md) — A progress object that tracks a document as it loads.
