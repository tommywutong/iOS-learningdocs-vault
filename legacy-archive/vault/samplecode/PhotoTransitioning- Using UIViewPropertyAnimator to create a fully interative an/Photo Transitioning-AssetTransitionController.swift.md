---
title: 'PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative
  and interruptible custom view controller transition'
apple_id: TP40017554
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoTransitioning/Listings/Photo_Transitioning_AssetTransitionController_swift.html
archived_at: '2026-07-18T03:18:55.469538Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoTransitioning: Using UIViewPropertyAnimator to create a fully interative and interruptible custom view controller transition](PhotoTransitioning-%20Using%20UIViewPropertyAnimator%20to%20create%20a%20fully%20interative%20an.md)


[Next](README.md.md)[Previous](Photo%20Transitioning-AssetTransitionDriver.swift.md)

# Photo Transitioning/AssetTransitionController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The AssetTransitionController class conforms to UINavigationControllerDelegate, UIViewControllerAnimatedTransitioning and UIViewControllerInteractiveTransitioning. 
                This class also manages the gesture recognizer used to initiate the custom interactive pop transition.
*/

import UIKit

let assetTransitionDuration = 0.8

class AssetTransitionController: NSObject {

    weak var navigationController: UINavigationController?
    var operation: UINavigationControllerOperation = .none
    var transitionDriver: AssetTransitionDriver?
    var initiallyInteractive = false
    var panGestureRecognizer: UIPanGestureRecognizer = UIPanGestureRecognizer()

    init(navigationController nc: UINavigationController) {
        navigationController = nc
        super.init()

        nc.delegate = self
        configurePanGestureRecognizer()
    }

    func configurePanGestureRecognizer() {
        panGestureRecognizer.delegate = self
        panGestureRecognizer.maximumNumberOfTouches = 1
        panGestureRecognizer.addTarget(self, action: #selector(initiateTransitionInteractively(_:)))
        navigationController?.view.addGestureRecognizer(panGestureRecognizer)

        guard let interactivePopGestureRecognizer = navigationController?.interactivePopGestureRecognizer else { return }
        panGestureRecognizer.require(toFail: interactivePopGestureRecognizer)
    }

    func initiateTransitionInteractively(_ panGesture: UIPanGestureRecognizer) {
        if panGesture.state == .began && transitionDriver == nil {
            initiallyInteractive = true
            let _ = navigationController?.popViewController(animated: true)
        }
    }
}

extension AssetTransitionController: UIGestureRecognizerDelegate {

    func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool {
        return true
    }

    func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool {
        guard let transitionDriver = self.transitionDriver else {
            let translation = panGestureRecognizer.translation(in: panGestureRecognizer.view)
            let translationIsVertical = (translation.y > 0) && (abs(translation.y) > abs(translation.x))
            return translationIsVertical && (navigationController?.viewControllers.count ?? 0 > 1)
        }

        return transitionDriver.isInteractive
    }
}

extension AssetTransitionController: UINavigationControllerDelegate {

    func navigationController(_ navigationController: UINavigationController, animationControllerFor operation: UINavigationControllerOperation, from fromVC: UIViewController, to toVC: UIViewController) -> UIViewControllerAnimatedTransitioning? {

        // Remember the direction of the transition (.push or .pop)
        self.operation = operation

        // Return ourselves as the animation controller for the pending transition
        return self
    }

    func navigationController(_ navigationController: UINavigationController, interactionControllerFor animationController: UIViewControllerAnimatedTransitioning) -> UIViewControllerInteractiveTransitioning? {

        // Return ourselves as the interaction controller for the pending transition
        return self
    }
}

extension AssetTransitionController: UIViewControllerInteractiveTransitioning {

    func startInteractiveTransition(_ transitionContext: UIViewControllerContextTransitioning) {

        // Create our helper object to manage the transition for the given transitionContext.
        transitionDriver = AssetTransitionDriver(operation: operation, context: transitionContext, panGestureRecognizer: panGestureRecognizer)
    }

    var wantsInteractiveStart: Bool {

        // Determines whether the transition begins in an interactive state
        return initiallyInteractive
    }
}

extension AssetTransitionController: UIViewControllerAnimatedTransitioning {

    func transitionDuration(using transitionContext: UIViewControllerContextTransitioning?) -> TimeInterval {
        return assetTransitionDuration
    }

    func animateTransition(using transitionContext: UIViewControllerContextTransitioning) {}

    func animationEnded(_ transitionCompleted: Bool) {
        // Clean up our helper object and any additional state
        transitionDriver = nil
        initiallyInteractive = false
        operation = .none
    }

    func interruptibleAnimator(using transitionContext: UIViewControllerContextTransitioning) -> UIViewImplicitlyAnimating {
        // The transition driver (helper object), creates the UIViewPropertyAnimator (transitionAnimator) 
        // to be used for this transition. It must live the lifetime of the transitionContext.
        return (transitionDriver?.transitionAnimator)!
    }
}
```

[Next](README.md.md)[Previous](Photo%20Transitioning-AssetTransitionDriver.swift.md)

