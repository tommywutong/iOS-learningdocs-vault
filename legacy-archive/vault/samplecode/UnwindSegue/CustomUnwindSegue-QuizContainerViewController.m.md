---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/CustomUnwindSegue_QuizContainerViewController_m.html
archived_at: '2026-07-18T03:27:36.416749Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](CustomUnwindSegue-QuizContainerFadeViewControllerSegue.m.md)[Previous](CustomUnwindSegue-AppDelegate.m.md)

# CustomUnwindSegue/QuizContainerViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A custom container view controller that is functionally similar to a 
  UINavigationController.
 */

#import "QuizContainerViewController.h"
#import "QuizContainerFadeViewControllerSegue.h"

@import QuartzCore;

@interface QuizContainerViewController () <UINavigationBarDelegate> {
    UINavigationBar *_navigationBar;
    NSArray *_viewControllers;
}
@end


@implementation QuizContainerViewController

//| ----------------------------------------------------------------------------
//  We provide our own view.
//
- (void)loadView
{
    self.view = [[UIView alloc] init];

    _navigationBar = [[UINavigationBar alloc] init];
    _navigationBar.delegate = self;
    [self.view addSubview:_navigationBar];
}


//| ----------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];
    // The transition animation involves fading out the outgoing view
    // controller's view while fading in the incoming view controller's view.
    // This creates a short 'flash' animation where the color of the flash is 
    // our view's backgroundColor.
    self.view.backgroundColor = [UIColor whiteColor];

    // This segue creates our initial root view controller.  Users of this
    // class are expected to define a segue named 'RootViewController' with
    // segue type QuizContainerRootViewControllerSegue.  The destination
    // of this segue should be the scene of the desired initial root view
    // controller.
    [self performSegueWithIdentifier:@"RootViewController" sender:self];
}


//| ----------------------------------------------------------------------------
//! Returns the appropriate frame for displaying a child view controller.
//
- (CGRect)frameForTopViewController
{
    return CGRectMake(0,
                      _navigationBar.frame.size.height + _navigationBar.frame.origin.y,
                      self.view.bounds.size.width,
                      self.view.bounds.size.height - _navigationBar.frame.size.height - _navigationBar.frame.origin.y);
}


//| ----------------------------------------------------------------------------
- (void)viewDidLayoutSubviews
{
    [_navigationBar sizeToFit];

    // Offset the navigation bar to account for the status bar.
    CGFloat topLayoutGuide = 0.0f;
    if ([self respondsToSelector:@selector(topLayoutGuide)])
        topLayoutGuide = (self.topLayoutGuide).length;
    _navigationBar.frame = CGRectMake(_navigationBar.frame.origin.x, topLayoutGuide,
                                      _navigationBar.frame.size.width, _navigationBar.frame.size.height);

    self.topViewController.view.frame = [self frameForTopViewController];
}

#pragma mark -
#pragma mark Unwind Segue

//| ----------------------------------------------------------------------------
//! Returns the view controller managed by the receiver that wants to handle
//! the specified unwind action.
//
//  This method is called when either unwind segue is triggered in
//  ResultsViewController.  It is the responsibility of the parent of the
//  view controller that triggered the unwind segue to locate a
//  view controller that responds to the unwind action for the triggered segue.
//  
- (UIViewController *)viewControllerForUnwindSegueAction:(SEL)action fromViewController:(UIViewController *)fromViewController withSender:(id)sender
{
    // Like UINavigationController, search the array of view controllers
    // managed by this container in reverse order.
    for (UIViewController *vc in [_viewControllers reverseObjectEnumerator])
        // Always use -canPerformUnwindSegueAction:fromViewController:withSender:
        // to determine if a view controller wants to handle an unwind action.
        if ([vc canPerformUnwindSegueAction:action fromViewController:fromViewController withSender:sender])
            return vc;

    // Always invoke the super's implementation if no view controller managed
    // by this container wanted to handle the unwind action.
    return [super viewControllerForUnwindSegueAction:action fromViewController:fromViewController withSender:sender];
}


//| ----------------------------------------------------------------------------
//! Returns a segue object for transitioning to toViewController.
//
//  This method is called if the destination of an unwind segue is a child
//  view controller of this container.  This method returns an instance
//  of QuizContainerFadeViewControllerSegue that transitions to the destination
//  view controller of the unwind segue (toViewController).
//
- (UIStoryboardSegue*)segueForUnwindingToViewController:(UIViewController *)toViewController fromViewController:(UIViewController *)fromViewController identifier:(NSString *)identifier
{
    // QuizContainerFadeViewControllerSegue is a UIStoryboardSegue subclass
    // for transitioning between view controllers managed by this container.
    QuizContainerFadeViewControllerSegue *unwindStoryboardSegue = [[QuizContainerFadeViewControllerSegue alloc] initWithIdentifier:identifier source:fromViewController destination:toViewController];

    // Set the unwind property to YES so an unwind animation is performed.
    // Note that this property is custom to QuizContainerFadeViewControllerSegue.
    unwindStoryboardSegue.unwind = YES;

    return unwindStoryboardSegue;
}

#pragma mark -
#pragma mark Actions

//| ----------------------------------------------------------------------------
//! Manual implementation of the topViewController property.
//! Returns the view controller at the top of the navigation stack.
//
- (UIViewController*)topViewController
{
    if (self.viewControllers.count == 0)
        return nil;
    return (self.viewControllers).lastObject;
}


//| ----------------------------------------------------------------------------
//! Equivalent to calling -setViewControllers:animated: and passing NO for the
//! animated argument.
//
- (void)setViewControllers:(NSArray *)viewControllers
{
    [self setViewControllers:viewControllers animated:NO];
}


//| ----------------------------------------------------------------------------
//! Replaces the view controllers currently managed by the receiver with the
//! specified items.
//
//! @param  viewControllers
//!         The view controllers to place in the navigation stack.  The
//!         last item added to the array becomes the top item of the
//!         navigation stack.
//! @param  animated
//!         If YES, animate the pushing or popping of the top view controller.
//!         If NO, replace the view controllers without any animations.
//
//  This is where all of the transition magic happens. 
//
- (void)setViewControllers:(NSArray *)viewControllers animated:(BOOL)animated
{
    // Compare the incoming viewControllers array to the existing navigation
    // stack, seperating the differences into two groups.
    NSArray *viewControllersToRemove = [_viewControllers filteredArrayUsingPredicate:[NSPredicate predicateWithFormat:@"NOT (SELF IN %@)", viewControllers]];
    NSArray *viewControllersToAdd = [viewControllers filteredArrayUsingPredicate:[NSPredicate predicateWithFormat:@"NOT (SELF IN %@)", _viewControllers]];

    for (UIViewController *vc in viewControllersToRemove)
        [vc willMoveToParentViewController:nil];

    for (UIViewController *vc in viewControllersToAdd)
        [self addChildViewController:vc];

    void (^finishRemovingViewControllers)(void) = ^() {
        for (UIViewController *vc in viewControllersToRemove)
            [vc removeFromParentViewController];
    };

    void (^finishAddingViewControllers)(void) = ^() {
        for (UIViewController *vc in viewControllersToAdd)
            [vc didMoveToParentViewController:self];
    };

    // The view controller presently at the top of the navigation stack.
    UIViewController *oldTopViewController = (_viewControllers.count) ? _viewControllers.lastObject : nil;
    // The view controller that will be at the stop of the navgation stack.
    UIViewController *newTopViewController = (viewControllers.count) ? viewControllers.lastObject : nil;

    // If the last object in the incoming viewControllers is the
    // already at the top of the current navigation stack then don't 
    // perform any animation as it would be redundant.
    if (oldTopViewController != newTopViewController)
    {
        if (oldTopViewController)
        {
            // Fade animations look wrong unless the root layer of the
            // animation rasterizes itself but be sure to remember the
            // old setting.
            BOOL oldTopViewControllerViewShouldRasterize = oldTopViewController.view.layer.shouldRasterize;
            oldTopViewController.view.layer.shouldRasterize = YES;

            // Fade out the old top view controller of the navigation stack.
            [UIView animateWithDuration:((animated) ? 0.25 : 0) delay:0 options:0 animations:^{
                oldTopViewController.view.alpha = 0.0f;
            } completion:^(BOOL finished) {
                // Restore the old shouldRasterize setting.
                oldTopViewController.view.layer.shouldRasterize = oldTopViewControllerViewShouldRasterize;
                [oldTopViewController.view removeFromSuperview];
                finishRemovingViewControllers();
            }];
        }
        else
            finishRemovingViewControllers();

        if (newTopViewController)
        {
            // Fade animations look wrong unless the root layer of the
            // animation rasterizes itself but be sure to remember the
            // old setting.
            BOOL newTopViewControllerViewShouldRasterize = newTopViewController.view.layer.shouldRasterize;
            newTopViewController.view.layer.shouldRasterize = YES;

            newTopViewController.view.frame = [self frameForTopViewController];
            [self.view addSubview:newTopViewController.view];

            newTopViewController.view.alpha = 0.0f;

            // Fade in the new top view controller of the navigation stack.
            [UIView animateWithDuration:((animated) ? 0.25 : 0) delay:((animated) ? 0.3 : 0) options:0 animations:^{
                newTopViewController.view.alpha = 1.0f;
            } completion:^(BOOL finished) {
                // Restore the old shouldRasterize setting.
                newTopViewController.view.layer.shouldRasterize = newTopViewControllerViewShouldRasterize;
                finishAddingViewControllers();
            }];

        }
        else
            finishAddingViewControllers();
    }
    else
    // No animation required.
    {
        finishRemovingViewControllers();
        finishAddingViewControllers();
    }

    _viewControllers = viewControllers;

    // Update the stack of navigation items for the _navigationBar to
    // reflect the new navigation stack.
    NSMutableArray *newNavigationItemsArray = [NSMutableArray arrayWithCapacity:viewControllers.count];
    for (UIViewController *vc in viewControllers)
        [newNavigationItemsArray addObject:vc.navigationItem];
    [_navigationBar setItems:newNavigationItemsArray animated:animated];
}


//| ----------------------------------------------------------------------------
//! Pushes a view controller onto the receiver’s stack and updates the display.
//
- (void)pushViewController:(UIViewController *)viewController animated:(BOOL)animated
{
    // Replace the navigation stack with a new array that has viewController
    // apeneded to it.
    [self setViewControllers:[self.viewControllers arrayByAddingObject:viewController] animated:animated];
}


//| ----------------------------------------------------------------------------
//! Pops view controllers until the specified view controller is at the top of the navigation stack.
//
- (NSArray *)popToViewController:(UIViewController *)viewController animated:(BOOL)animated
{
    // Check that viewController is in the navigation stack.
    NSUInteger indexOfViewController = [_viewControllers indexOfObject:viewController];
    if (indexOfViewController == NSNotFound)
        return nil;

    NSArray *viewControllersThatWerePopped = [_viewControllers subarrayWithRange:NSMakeRange(indexOfViewController+1, _viewControllers.count - (indexOfViewController+1))];
    NSArray *newViewControllersArray = [_viewControllers subarrayWithRange:NSMakeRange(0, indexOfViewController+1)];

    // Replace the navigation stack with a new array containg only the view
    // controllers up to the specified viewController.
    [self setViewControllers:newViewControllersArray animated:YES];

    return viewControllersThatWerePopped;
}

@end
```

[Next](CustomUnwindSegue-QuizContainerFadeViewControllerSegue.m.md)[Previous](CustomUnwindSegue-AppDelegate.m.md)

