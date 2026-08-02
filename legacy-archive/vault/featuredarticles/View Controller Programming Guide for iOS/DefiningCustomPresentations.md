---
title: View Controller Programming Guide for iOS
apple_id: TP40007457
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/DefiningCustomPresentations.html
archived_at: '2026-07-18T02:28:42.906531Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [View Controller Programming Guide for iOS](index.md)



## Creating Custom Presentations

UIKit separates the content of your view controllers from the way that content is presented and displayed onscreen. Presented view controllers are managed by an underlying presentation controller object, which manages the visual style used to display the view controller’s view. A presentation controller may do the following:

- Set the size of the presented view controller.
- Add custom views to change the visual appearance of the presented content.
- Supply transition animations for any of its custom views.
- Adapt the visual appearance of the presentation when changes occur in the app’s environment.

UIKit provides presentation controllers for the standard presentation styles. When you set the presentation style of a view controller to `UIModalPresentationCustom` and provide an appropriate transitioning delegate, UIKit uses your custom presentation controller instead.

### The Custom Presentation Process

When you present a view controller whose presentation style is [UIModalPresentationCustom](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/custom), UIKit looks for a custom presentation controller to manage the presentation process. As the presentation progresses, UIKit calls methods of the presentation controller, giving it opportunities to set up any custom views and animate them into position.

A presentation controller works alongside any animator objects to implement the overall transition. The animator objects animate the view controller’s contents onto the screen and the presentation controller handles everything else. Normally, your presentation controller animates its own views, but you can also override the presentation controller’s [presentedView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618321-presentedview) method and let the animator objects animate all or some of those views.

During a presentation, UIKit:

1. Calls the [presentationControllerForPresentedViewController:presentingViewController:sourceViewController:](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622057-presentationcontroller) method of the transitioning delegate to retrieve your custom presentation controller
2. Asks the transitioning delegate for the animator and interactive animator objects, if any
3. Calls your presentation controller’s [presentationTransitionWillBegin](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618330-presentationtransitionwillbegin) method

   Your implementation of this method should add any custom views to the view hierarchy and configure the animations for those views.
4. Gets the [presentedView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618321-presentedview) from your presentation controller

   The view returned by this method is animated into position by the animator objects. Normally, this method returns the root view of the presented view controller. Your presentation controller can replace that view with a custom background view, as needed. If you do specify a different view, you must embed the root view of the presented view controller into your view hierarchy.
5. Performs the transition animations

   The transition animations include the main ones created by the animator objects and any animations you configured to run alongside the main animations. For information on the transition animations, see [The Transition Animation Sequence](CustomizingtheTransitionAnimations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmjwfvjvomq).

   During the animation process, UIKit calls the [containerViewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618341-containerviewwilllayoutsubviews) and [containerViewDidLayoutSubviews](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618331-containerviewdidlayoutsubviews) methods of your presentation controller so that you can adjust the layout of your custom views as needed.
6. Calls the [presentationTransitionDidEnd:](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618327-presentationtransitiondidend) method when the transition animations finish

During a dismissal, UIKit:

1. Gets your custom presentation controller from the currently visible view controller
2. Asks the transitioning delegate for the animator and interactive animator objects, if any
3. Calls your presentation controller’s [dismissalTransitionWillBegin](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618342-dismissaltransitionwillbegin) method

   Your implementation of this method should add any custom views to the view hierarchy and configure the animations for those views .
4. Gets the already [presentedView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618321-presentedview) from your presentation controller
5. Performs the transition animations

   The transition animations include the main ones created by the animator objects and any animations you configured to run alongside the main animations. For information on the transition animations, see [The Transition Animation Sequence](CustomizingtheTransitionAnimations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmjwfvjvomq).

   During the animation process, UIKit calls the [containerViewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618341-containerviewwilllayoutsubviews) and [containerViewDidLayoutSubviews](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618331-containerviewdidlayoutsubviews) methods of your presentation controller so that you can remove any custom constraints.
6. Calls the [dismissalTransitionDidEnd:](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618323-dismissaltransitiondidend) method when the transition animations finish

During the presentation process, The [frameOfPresentedViewInContainerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618337-frameofpresentedviewincontainerv) and `presentedView` methods of your presentation controller may be called several times, so your implementations should return quickly. Also, your implementation of your `presentedView` method should not try to set up the view hierarchy. The view hierarchy should already be configured by the time the method is called.

### Creating a Custom Presentation Controller

To implement a custom presentation style, subclass [UIPresentationController](https://developer.apple.com/documentation/uikit/uipresentationcontroller) and add code to create the views and animations for your presentation. When creating a custom presentation controller, consider the following questions:

- What views do you want to add?
- How do you want to animate any additional views onscreen?
- What size should the presented view controller be?
- How should the presentation adapt between a horizontally regular and horizontally compact size class?
- Should the presenting view controller’s view be removed when the presentation finishes?

All of these decisions require overriding different methods of the `UIPresentationController` class.

### Setting the Frame of the Presented View Controller

You can modify the frame rectangle of the presented view controller so that it fills only part of the available space. By default, a presented view controller is sized to completely fill the container view’s frame. To change the frame rectangle, override your presentation controller’s [frameOfPresentedViewInContainerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618337-frameofpresentedviewincontainerv) method. Listing 11-1 shows an example where the frame is changed to cover only the right half of the container view. In this case, the presentation controller uses a background dimming view to cover the other half of the container.

__Listing 11-1__Changing the frame of a presented view controller

1. `- (CGRect)frameOfPresentedViewInContainerView {`
2. `CGRect presentedViewFrame = CGRectZero;`
3. `CGRect containerBounds = [[self containerView] bounds];`
5. `presentedViewFrame.size = CGSizeMake(floorf(containerBounds.size.width / 2.0),`
6. `containerBounds.size.height);`
7. `presentedViewFrame.origin.x = containerBounds.size.width -`
8. `presentedViewFrame.size.width;`
9. `return presentedViewFrame;`
10. `}`

### Managing and Animating Custom Views

Custom presentations often involve adding custom views to the presented content. Use custom views to implement purely visual adornments or use them to add practical behaviors to the presentation. For example, a background view might incorporate gesture recognizers to track specific actions outside the bounds of the presented content.

The presentation controller is responsible for creating and managing all custom views associated with its presentation. Usually, you create custom views during the initialization of your presentation controller. Listing 11-2 shows the initialization method of a custom view controller that creates its own dimming view. This method creates the view and performs some minimal configuration.

__Listing 11-2__Initializing the presentation controller

1. `- (instancetype)initWithPresentedViewController:(UIViewController *)presentedViewController`
2. `presentingViewController:(UIViewController *)presentingViewController {`
3. `self = [super initWithPresentedViewController:presentedViewController`
4. `presentingViewController:presentingViewController];`
5. `if(self) {`
6. `// Create the dimming view and set its initial appearance.`
7. `self.dimmingView = [[UIView alloc] init];`
8. `[self.dimmingView setBackgroundColor:[UIColor colorWithWhite:0.0 alpha:0.4]];`
9. `[self.dimmingView setAlpha:0.0];`
10. `}`
11. `return self;`
12. `}`

You animate your custom views onto the screen using the [presentationTransitionWillBegin](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618330-presentationtransitionwillbegin) method. In this method, configure your custom views and add them to the container view, as shown in Listing 11-3. Use the transition coordinator of either the presented or presenting view controller to create any animations. Do not modify the presented view controller’s view in this method. The animator objects are responsible for animating the presented view controller into the frame rectangle you return from your [frameOfPresentedViewInContainerView](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618337-frameofpresentedviewincontainerv) method.

__Listing 11-3__Animating the dimming view onto the screen

1. `- (void)presentationTransitionWillBegin {`
2. `// Get critical information about the presentation.`
3. `UIView* containerView = [self containerView];`
4. `UIViewController* presentedViewController = [self presentedViewController];`
6. `// Set the dimming view to the size of the container's`
7. `// bounds, and make it transparent initially.`
8. `[[self dimmingView] setFrame:[containerView bounds]];`
9. `[[self dimmingView] setAlpha:0.0];`
11. `// Insert the dimming view below everything else.`
12. `[containerView insertSubview:[self dimmingView] atIndex:0];`
14. `// Set up the animations for fading in the dimming view.`
15. `if([presentedViewController transitionCoordinator]) {`
16. `[[presentedViewController transitionCoordinator]`
17. `animateAlongsideTransition:^(id<UIViewControllerTransitionCoordinatorContext>`
18. `context) {`
19. `// Fade in the dimming view.`
20. `[[self dimmingView] setAlpha:1.0];`
21. `} completion:nil];`
22. `}`
23. `else {`
24. `[[self dimmingView] setAlpha:1.0];`
25. `}`
26. `}`

At the end of a presentation, use the [presentationTransitionDidEnd:](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618327-presentationtransitiondidend) method to handle any cleanup caused by the cancelation of the presentation. An interactive animator object might cancel a transition if its threshold conditions are not met. When that happens, UIKit calls the `presentationTransitionDidEnd:` method with a value of `NO``false`. When a cancelation occurs, remove any custom views you added at the beginning of the presentation and return any other views to their previous configurations, as shown in Listing 11-4.

__Listing 11-4__Handling a cancelled presentation

1. `- (void)presentationTransitionDidEnd:(BOOL)completed {`
2. `// If the presentation was canceled, remove the dimming view.`
3. `if (!completed)`
4. `[self.dimmingView removeFromSuperview];`
5. `}`

When the view controller is dismissed, use the [dismissalTransitionDidEnd:](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618323-dismissaltransitiondidend) methods to remove your custom views from the view hierarchy. If you want to animate the disappearance of your views, set up those animations in the [dismissalTransitionDidEnd:](https://developer.apple.com/documentation/uikit/uipresentationcontroller/1618323-dismissaltransitiondidend) method. Listing 11-5 shows implementations of both methods for removing the dimming view in the previous examples. Always check the parameter of the `dismissalTransitionDidEnd:` method to see if the dismissal was successful or was canceled.

__Listing 11-5__Dismissing the presentation’s views

1. `- (void)dismissalTransitionWillBegin {`
2. `// Fade the dimming view back out.`
3. `if([[self presentedViewController] transitionCoordinator]) {`
4. `[[[self presentedViewController] transitionCoordinator]`
5. `animateAlongsideTransition:^(id<UIViewControllerTransitionCoordinatorContext>`
6. `context) {`
7. `[[self dimmingView] setAlpha:0.0];`
8. `} completion:nil];`
9. `}`
10. `else {`
11. `[[self dimmingView] setAlpha:0.0];`
12. `}`
13. `}`
15. `- (void)dismissalTransitionDidEnd:(BOOL)completed {`
16. `// If the dismissal was successful, remove the dimming view.`
17. `if (completed)`
18. `[self.dimmingView removeFromSuperview];`
19. `}`

### Vending Your Presentation Controller to UIKit

When presenting a view controller, do the following to display it using your custom presentation controller:

- Set the [modalPresentationStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621355-modalpresentationstyle) property of the presented view controller to `UIModalPresentationCustom`.
- Assign a transitioning delegate to the [transitioningDelegate](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621421-transitioningdelegate) property of the presented view controller.
- Implement the [presentationControllerForPresentedViewController:presentingViewController:sourceViewController:](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/1622057-presentationcontroller) method of the transitioning delegate.

UIKit calls the `presentationControllerForPresentedViewController:presentingViewController:sourceViewController:` method of your transitioning delegate when it needs your presentation controller. Your implementation of this method should be as simple as the one in Listing 11-6. Simply create your presentation controller, configure it, and return it. If you return `nil` from this method, UIKit presents the view controller using a full-screen presentation style.

__Listing 11-6__Creating a custom presentation controller

1. `- (UIPresentationController *)presentationControllerForPresentedViewController:`
2. `(UIViewController *)presented`
3. `presentingViewController:(UIViewController *)presenting`
4. `sourceViewController:(UIViewController *)source {`
6. `MyPresentationController* myPresentation = [[MyPresentationController]`
7. `initWithPresentedViewController:presented presentingViewController:presenting];`
9. `return myPresentation;`
10. `}`

### Adapting to Different Size Classes

While a presentation is onscreen, UIKit notifies your presentation controller when changes occur to the underlying traits or to the size of the container view. Such changes typically occur during a device rotation but may occur at other times. You can use trait and size notifications to adjust your presentation’s custom views and update your presentation style as appropriate.

For information about how to adapt to new traits and sizes, see [Building an Adaptive Interface](BuildinganAdaptiveInterface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmzsfvjvomi).

[Customizing the Transition Animations](CustomizingtheTransitionAnimations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmjwfvjvomi)

[The Adaptive Model](TheAdaptiveModel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmjzfvjvomi)
