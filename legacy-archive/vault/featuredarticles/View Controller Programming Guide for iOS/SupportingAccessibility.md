---
title: View Controller Programming Guide for iOS
apple_id: TP40007457
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/SupportingAccessibility.html
archived_at: '2026-07-18T02:29:02.080337Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [View Controller Programming Guide for iOS](index.md)



## Supporting Accessibility

An accessible app is one that can be used by everyone—including those with a disability or physical impairment—while retaining its functionality and usability as a helpful tool. To be accessible, an iOS app must supply information about its user interface elements to VoiceOver, so that vision-impaired users can interact with those elements. UIKit objects are accessible by default, but there are still things you can do from the view controller’s perspective to address accessibility, including the following:

- Ensure that every user element in your interface is accessible, including controls and static elements such as labels.
- Ensure that accessible elements supply accurate and helpful information.

You can enhance the VoiceOver user’s experience in your app by setting the position of the VoiceOver focus ring programmatically, by responding to special VoiceOver gestures, and by observing accessibility notifications.

### Moving the VoiceOver Cursor to a Specific Element

When your app presents new views onscreen, consider setting the position of the VoiceOver cursor. When the layout of a screen changes, the VoiceOver focus ring, also known as the _VoiceOver cursor_, resets its position to the first element displayed on the screen from left to right and top to bottom. Placing the cursor over a more appropriate element can speed the user’s navigation of your interface. For example, when pushing a new view controller onto a navigation controller’s stack, the VoiceOver cursor falls on the Back button of the navigation bar. You might want to move that cursor to the heading of the navigation bar or to an element on the newly pushed page.

To change the position of the cursor, post a [UIAccessibilityScreenChangedNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620198-screenchanged) notification using the [UIAccessibilityPostNotification](https://developer.apple.com/documentation/uikit/1615194-uiaccessibilitypostnotification) function. The notification tells VoiceOver that the contents of the screen changed. When posting the notification, specify the element to which you want to assign the focus, as shown in Listing 6-1.

__Listing 6-1__Posting an accessibility notification can change the first element read aloud

1. `@implementation MyViewController`
2. `- (void)viewDidAppear:(BOOL)animated {`
3. `[super viewDidAppear:animated];`
5. `// The second parameter is the new focus element.`
6. `UIAccessibilityPostNotification(UIAccessibilityScreenChangedNotification,`
7. `self.myFirstElement);`
8. `}`
9. `@end`

Layout changes, including those caused by rotations, reset the position of the VoiceOver cursor. When the layout of your view controller changes, post the notification [UIAccessibilityLayoutChangedNotification](https://developer.apple.com/documentation/uikit/uiaccessibilitylayoutchangednotification). Like the `UIAccessibilityScreenChangedNotification` notification, you can specify the object that you want to become the new first element for VoiceOver.

### Responding to Special VoiceOver Gestures

VoiceOver defines five special gestures for triggering app-specific actions.

- __Escape.__ A two-finger Z-shaped gesture that dismisses a modal dialog, or goes back one level in a navigation hierarchy.
- __Magic Tap.__ A two-finger double-tap that performs the most-intended action.
- __Three-Finger Scroll.__ A three-finger swipe that scrolls content vertically or horizontally.
- __Increment.__ A one-finger swipe up that increments a value in an element.
- __Decrement.__ A one-finger swipe down that decrements a value in an element.

Use these gestures to perform tasks that are specific to your views and view controllers. UIKit looks for a method that implements the method corresponding to the gesture. It searches for the method using the [responder](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1) chain, starting with the element that has the VoiceOver focus. If no object implements the appropriate method, UIKit performs the default system action for that gesture. For example, the Magic Tap gesture plays and pauses music playback from the Music app if no Magic Tap implementation is found from the current view to the app delegate.

Although you can take any actions you want in your handlers, VoiceOver users expect your app’s actions to follow certain guidelines. Like any gesture, your implementation of a VoiceOver gesture should follow a pattern so that interaction with an accessible app remains intuitive.

> [!NOTE]
> 

### Escape

Use the [accessibilityPerformEscape](https://developer.apple.com/documentation/objectivec/nsobject/1615091-accessibilityperformescape) method to handle the Escape gesture. For a view that overlays content—such as a modal dialog or an alert—use the method to dismiss the overlay. The function of the Escape gesture is like the function of the `Esc` key on a computer keyboard; it cancels a temporary dialog or sheet to reveal the main content. You might also use the Escape gesture to navigate back one level in a custom navigation hierarchy. You do not need to implement this gesture if you are already using a `UINavigationController` object, which already handles this gesture.

### Magic Tap

Use the [accessibilityPerformMagicTap](https://developer.apple.com/documentation/objectivec/nsobject/1615137-accessibilityperformmagictap) method to handle the Magic Tap gesture. The Magic Tap gesture performs an often-used or most-intended action quickly. For example, in the Phone app, a Magic Tap picks up or hangs up a phone call, and in the Clock app, a Magic Tap starts and stops the stopwatch. You might use this gesture to trigger actions that are not necessarily relevant to the element that the VoiceOver cursor is highlighting. To handle Magic Tap gestures from anywhere in your app, implement the `accessibilityPerformMagicTap` method in your app delegate.

### Three-Finger Scroll

Use the [accessibilityScroll:](https://developer.apple.com/documentation/objectivec/nsobject/1615161-accessibilityscroll) method to scroll the content of a custom view when a VoiceOver user performs a three-finger scroll gesture. A custom view that displays the pages of a book might use this gesture to turn the page. The parameter passed to the method indicates the direction in which to scroll.

### Increment and Decrement

Use the [accessibilityIncrement](https://developer.apple.com/documentation/objectivec/nsobject/1615076-accessibilityincrement) and [accessibilityDecrement](https://developer.apple.com/documentation/objectivec/nsobject/1615169-accessibilitydecrement) methods to increment or decrement a value in the element. Elements with the `UIAccessibilityTraitAdjustable` trait must implement this method.

### Observing Accessibility Notifications

UIKit sends accessibility notifications to inform your app about relevant events. The objects of your app can observe any relevant notifications and use them to perform appropriate tasks. For example, the iBooks app uses the [UIAccessibilityAnnouncementDidFinishNotification](https://developer.apple.com/documentation/uikit/uiaccessibility/1620202-announcementdidfinishnotificatio) notification to turn the page and continue reading when VoiceOver finishes speaking the last line on a page. This behavior provides a seamless, uninterrupted reading experience.

Use the default notification center to register as an observer for accessibility notifications. Listing 6-2 shows an example of a view that records whether the reading of an announcement was successful or was interrupted by the user.

__Listing 6-2__Registering as an observer for accessibility notifications

1. `@implementation MyViewController`
2. `- (void)viewDidLoad`
3. `{`
4. `[super viewDidLoad];`
6. `[[NSNotificationCenter defaultCenter]`
7. `addObserver:self`
8. `selector:@selector(didFinishAnnouncement:)`
9. `name:UIAccessibilityAnnouncementDidFinishNotification`
10. `object:nil];`
11. `}`
13. `- (void)didFinishAnnouncement:(NSNotification *)dict`
14. `{`
15. `NSString *valueSpoken = [[dict userInfo] objectForKey:UIAccessibilityAnnouncementKeyStringValue];`
16. `NSString *wasSuccessful = [[dict userInfo] objectForKey:UIAccessibilityAnnouncementKeyWasSuccessful];`
17. `// ...`
18. `}`
19. `@end`

Another helpful notification to subscribe to is the [UIAccessibilityVoiceOverStatusChanged](https://developer.apple.com/documentation/uikit/uiaccessibilityvoiceoverstatuschanged) notification. You can use that notification to detect when VoiceOver is toggled on or off. If this notification occurs while your app is suspended, you receive the notification when your app returns to the foreground.

For a list of accessibility notifications you can observe, see _[UIAccessibility Protocol Reference](https://developer.apple.com/documentation/uikit/accessibility/uiaccessibility)_.

[Implementing a Container View Controller](ImplementingaContainerViewController.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmjrfvjvomi)

[Preserving and Restoring State](PreservingandRestoringState.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tinjxfvbuqmryfvjvomi)
