---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_TheElementsAppDelegate_m.html
archived_at: '2026-07-18T03:26:46.503785Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElementFlippedView.m.md)[Previous](main.m.md)

# Classes/TheElementsAppDelegate.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate that sets up the application.
*/


#import "TheElementsAppDelegate.h"
#import "ElementsTableViewController.h"

// each data source responsible for backing our 4 varying table view controllers
#import "ElementsSortedByNameDataSource.h"
#import "ElementsSortedByAtomicNumberDataSource.h"
#import "ElementsSortedBySymbolDataSource.h"
#import "ElementsSortedByStateDataSource.h"

@implementation TheElementsAppDelegate

@synthesize window;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    // for each tableview 'screen' we need to create a datasource instance
    // (the class that is passed in) we then need to create an instance of
    // ElementsTableViewController with that datasource instance finally we need to return
    // a UINaviationController for each screen, with the ElementsTableViewController as the
    // root view controller.
    //
    UITabBarController *tabBarController = (UITabBarController *)self.window.rootViewController;

    // the class type for the datasource is not crucial, but that it implements the
    // ElementsDataSource protocol and the UITableViewDataSource Protocol
    //
    id<ElementsDataSource, UITableViewDataSource> dataSource;

    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"MainStoryboard" bundle:nil];
    NSMutableArray *viewControllers = [NSMutableArray arrayWithCapacity:4];

    // create our tabbar view controllers, since we already have one defined in our storyboard
    // we will create 3 more instances of it, and assign each it's own kind data source

    // by name
    UINavigationController *navController = [storyboard instantiateViewControllerWithIdentifier:@"navForTableView"];
    ElementsTableViewController *viewController =
        (ElementsTableViewController *)[navController topViewController];
    dataSource = [[ElementsSortedByNameDataSource alloc] init];
    viewController.dataSource = dataSource;
    [viewControllers addObject:navController];

    // by atomic number
    navController = [storyboard instantiateViewControllerWithIdentifier:@"navForTableView"];
    viewController = (ElementsTableViewController *)[navController topViewController];
    dataSource = [[ElementsSortedByAtomicNumberDataSource alloc] init];
    viewController.dataSource = dataSource;
    [viewControllers addObject:navController];

    // by symbol
    navController = [storyboard instantiateViewControllerWithIdentifier:@"navForTableView"];
    viewController = (ElementsTableViewController *)[navController topViewController];
    dataSource = [[ElementsSortedBySymbolDataSource alloc] init];
    viewController.dataSource = dataSource;
    [viewControllers addObject:navController];

    // by state
    navController = [storyboard instantiateViewControllerWithIdentifier:@"navForTableView"];
    viewController = (ElementsTableViewController *)[navController topViewController];
    dataSource = [[ElementsSortedByStateDataSource alloc] init];
    viewController.dataSource = dataSource;
    [viewControllers addObject:navController];

    tabBarController.viewControllers = viewControllers;

    return YES;
}

@end
```

[Next](Classes-AtomicElementFlippedView.m.md)[Previous](main.m.md)

