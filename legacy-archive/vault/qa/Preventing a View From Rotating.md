---
title: Preventing a View From Rotating
apple_id: DTS40015222
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2015-03-27'
source_url: https://developer.apple.com/library/archive/qa/qa1890/_index.html
archived_at: '2026-07-18T02:35:23.316400Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1890

# Preventing a View From Rotating

## Q:  My view controller supports auto-rotation but I need to lock the orientation of a specific subview. How can I prevent a view from rotating?

A: Autorotation is implemented by applying a rotation transform to the application's window when the system determines that the interface must rotate. The window then adjusts its bounds for the new orientation and propagates this change down through the view controller hierarchy via calls to each view controller's and presentation controller's `-viewWillTransitionToSize:withTransitionCoordinator:` method. Invocations of this method are provided a transition coordinator object containing the delta of the window's current transform and new transform, which can be retrieved by sending a `-targetTransform` message to the transition coordinator. Your view controller or presentation controller can derive the appropriate inverse transform and apply it to the target view. This nullifies the effect of the window transform on that particular view and gives the appearance that the view has remained fixed in its current orientation as the rest of the interface rotates normally.

__Listing 1__  Excerpt of a view controller which uses the technique described above to lock the orientation of a view referenced by an instance variable named notRotatingView.

```objc
- (void)viewWillLayoutSubviews
{
    [super viewWillLayoutSubviews];

    self.notRotatingView.center = CGPointMake(CGRectGetMidX(self.view.bounds), CGRectGetMidY(self.view.bounds));
}

- (void)viewWillTransitionToSize:(CGSize)size withTransitionCoordinator:(id<UIViewControllerTransitionCoordinator>)coordinator
{
    [super viewWillTransitionToSize:size withTransitionCoordinator:coordinator];

    [coordinator animateAlongsideTransition:^(id<UIViewControllerTransitionCoordinatorContext> context) {
        CGAffineTransform deltaTransform = coordinator.targetTransform;
        CGFloat deltaAngle = atan2f(deltaTransform.b, deltaTransform.a);

        CGFloat currentRotation = [[self.notRotatingView.layer valueForKeyPath:@"transform.rotation.z"] floatValue];
        // Adding a small value to the rotation angle forces the animation to occur in a the desired direction, preventing an issue where the view would appear to rotate 2PI radians during a rotation from LandscapeRight -> LandscapeLeft.
        currentRotation += -1 * deltaAngle + 0.0001;
        [self.notRotatingView.layer setValue:@(currentRotation) forKeyPath:@"transform.rotation.z"];

    } completion:^(id<UIViewControllerTransitionCoordinatorContext> context) {
        // Integralize the transform to undo the extra 0.0001 added to the rotation angle.
        CGAffineTransform currentTransform = self.notRotatingView.transform;
        currentTransform.a = round(currentTransform.a);
        currentTransform.b = round(currentTransform.b);
        currentTransform.c = round(currentTransform.c);
        currentTransform.d = round(currentTransform.d);
        self.notRotatingView.transform = currentTransform;
    }];
}
```


The above technique should only be applied to views which your view controller is directly responsible for the layout of (i.e. descendants of your view controller's view). A view controller should never modify the transform or other geometric properties of its own view, these are managed by the parent view controller or presentation controller. If you need to prevent a view controller from rotating, see [Controlling What Interface Orientations Are Supported](https://developer.apple.com/library/ios/featuredarticles/ViewControllerPGforiPhoneOS/RespondingtoDeviceOrientationChanges/RespondingtoDeviceOrientationChanges.html) in the View Controller Programming Guide for iOS.

Modifying the transform of a view which has opted into Autolayout is not recommended. If you are using Autolayout, factor the view to which the transform will be applied into a separate xib file with Autolayout disabled. Then at runtime, load the xib file and programmatically add the view to the view hierarchy.

__Listing 2__  Loading notRotatingView from a xib file.

```objc
// Connected to the root view in the xib.
@property (nonatomic, strong) IBOutlet UIView *notRotatingView;

- (void)viewDidLoad
{
    [super viewDidLoad];

    // Load the notRotatingView from a xib, which has Autolayout disabled.
    [[UINib nibWithNibName:@"NotRotatingView" bundle:[NSBundle bundleForClass:self.class]] instantiateWithOwner:self options:nil];
    [self.view addSubview:self.notRotatingView];
}
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-27 | New document that describes how to 'lock' the orientation of a view while allowing the rest of the interface to rotate. |

