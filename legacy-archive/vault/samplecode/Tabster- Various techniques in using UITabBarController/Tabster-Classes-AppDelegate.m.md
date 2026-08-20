---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_AppDelegate_m.html
archived_at: '2026-07-18T03:26:19.539569Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-OneViewController.h.md)[Previous](Tabster-Classes-LandscapeViewController.m.md)

# Tabster/Classes/AppDelegate.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate class used for installing our UITabBarController
 */

#import "AppDelegate.h"
#import "FeaturedViewController.h"
#import "CrossfadeAnimationController.h"

// Compile time option to turn on or off custom tab bar appearance.
#define kCustomizeTabBar 0

// NSUserDefaults key value.
NSString *kTabBarOrderPrefKey = @"kTabBarOrder";  // The ordering of the tabs.

#pragma mark -

@interface AppDelegate () <UIApplicationDelegate, UITabBarControllerDelegate, UINavigationControllerDelegate>

@property (strong, nonatomic) UITabBarController *myTabBarController;
@property (nonatomic, strong) CrossfadeAnimationController *animationController;

@end

#pragma mark -

@implementation AppDelegate

// The app delegate must implement the window @property
// from UIApplicationDelegate @protocol to use a main storyboard file.
//
@synthesize window;

- (BOOL)application:(UIApplication *)application willFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // Add the tab bar controller's current view as a subview of the window.
    _myTabBarController = (UITabBarController *)self.window.rootViewController;

    // Customize the More page's navigation bar color
    self.myTabBarController.moreNavigationController.navigationBar.tintColor = [UIColor grayColor];

    // As a delegate to our tab bar controller, we can custom animate between view controllers.
    self.myTabBarController.delegate = self;

    // Adding controller from the Four.storyboard.
    NSArray *classController = self.myTabBarController.viewControllers;
    NSMutableArray *controllerArray = [NSMutableArray arrayWithArray:classController];

    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"Four" bundle:nil];
    UIViewController *four = [storyboard instantiateInitialViewController];

    [controllerArray insertObject:four atIndex:3];

    self.myTabBarController.viewControllers = controllerArray;

#if kCustomizeTabBar
    self.myTabBarController.tabBar.barTintColor = [UIColor darkGrayColor];
    self.myTabBarController.tabBar.tintColor = [UIColor yellowColor];

    // Note:
    // 1) You can also apply additional custom appearance to UITabBar using:
    // "backgroundImage" and "selectionIndicatorImage".
    // 2) You can also customize the appearance of individual UITabBarItems as well.
#endif

    // Restore the tab-order from prefs.
    NSArray *classNames = [[NSUserDefaults standardUserDefaults] arrayForKey:kTabBarOrderPrefKey];
    if (classNames.count > 0)
    {
        NSMutableArray *controllers = [[NSMutableArray alloc] init];
        for (NSString *className in classNames)
        {
            for (UIViewController* controller in self.myTabBarController.viewControllers)
            {
                NSString* controllerClassName = nil;

                if ([controller isKindOfClass:[UINavigationController class]])
                {
                    controllerClassName = NSStringFromClass([((UINavigationController *)controller).topViewController class]);
                }
                else
                {
                    controllerClassName = NSStringFromClass([controller class]);
                }

                if ([className isEqualToString:controllerClassName])
                {
                    [controllers addObject:controller];
                    break;
                }
            }
        }

        if (controllers.count == self.myTabBarController.viewControllers.count)
        {
            self.myTabBarController.viewControllers = controllers;
        }

    }

    // Listen for changes in view controller from the More screen.
    self.myTabBarController.moreNavigationController.delegate = self;

    // Choose to make one of our view controllers ("FeaturedViewController"),
    // not movable/reorderable in More's edit screen.
    //
    NSMutableArray *customizeableViewControllers = (NSMutableArray *)self.myTabBarController.viewControllers;
    for (UIViewController *viewController in customizeableViewControllers)
    {
        if ([viewController isKindOfClass:[FeaturedViewController class]])
        {
            [customizeableViewControllers removeObject:viewController];
            break;
        }
    }
    self.myTabBarController.customizableViewControllers = customizeableViewControllers;

    // Setup our transition animator for cross fading.
    _animationController = [[CrossfadeAnimationController alloc] init];
    self.animationController.duration = 0.5;

    return YES;
}

- (void)saveTabOrder
{
    // Store the tab-order to preferences.
    NSMutableArray *classNames = [[NSMutableArray alloc] init];
    for (UIViewController *controller in self.myTabBarController.viewControllers)
    {
        if ([controller isKindOfClass:[UINavigationController class]])
        {
            UINavigationController *navController = (UINavigationController *)controller;

            [classNames addObject:NSStringFromClass([navController.topViewController class])];
        }
        else
        {
            [classNames addObject:NSStringFromClass([controller class])];
        }
    }

    [[NSUserDefaults standardUserDefaults] setObject:classNames forKey:kTabBarOrderPrefKey];

}

- (void)applicationDidEnterBackground:(UIApplication *)application
{
    // This will store tab ordering.
    [self saveTabOrder];
}


#pragma mark - UINavigationControllerDelegate (More screen)

- (void)navigationController:(UINavigationController *)navigationController willShowViewController:(UIViewController *)viewController animated:(BOOL)animated
{
    if (viewController == self.myTabBarController.moreNavigationController.viewControllers[0])
    {
        // Returned to the More page.
    }
}

#pragma mark - State Restoration

- (BOOL)application:(UIApplication *)application shouldRestoreApplicationState:(NSCoder *)coder
{
    return YES;
}

- (BOOL)application:(UIApplication *)application shouldSaveApplicationState:(NSCoder *)coder
{
    return YES;
}

#pragma mark - UITabBarControllerDelegate

- (id <UIViewControllerAnimatedTransitioning>)tabBarController:(UITabBarController *)tabBarController
            animationControllerForTransitionFromViewController:(UIViewController *)fromVC
                                              toViewController:(UIViewController *)toVC
{
    CrossfadeAnimationController *animator = nil;

    NSUInteger fromVCIdx = [tabBarController.viewControllers indexOfObject:fromVC];
    NSUInteger toVCIdx = [tabBarController.viewControllers indexOfObject:toVC];

    // For this particular example only cross-fade animate between tab 1 to tab 2.
    if ((fromVCIdx == 0 && toVCIdx == 1) || (fromVCIdx == 1 && toVCIdx == 0))
    {
        animator = self.animationController;
        self.animationController.reverse = fromVCIdx < toVCIdx;
    }

    return animator;
}


@end
```

[Next](Tabster-Classes-OneViewController.h.md)[Previous](Tabster-Classes-LandscapeViewController.m.md)

