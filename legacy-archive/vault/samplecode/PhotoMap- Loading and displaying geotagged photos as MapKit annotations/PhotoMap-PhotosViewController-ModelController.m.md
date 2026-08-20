---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_PhotosViewController_ModelController_m.html
archived_at: '2026-07-18T03:18:52.588388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-PhotosViewController-DataViewController.m.md)[Previous](PhotoMap-PhotosViewController-ModelController.h.md)

# PhotoMap/PhotosViewController/ModelController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The model or data source for PhotosViewController.
 */

#import "ModelController.h"
#import "DataViewController.h"
#import "PhotosViewController.h"

/*
 A controller object that manages a simple model -- a collection of map annotations

 The controller serves as the data source for the page view controller; it therefore implements pageViewController:viewControllerBeforeViewController: and pageViewController:viewControllerAfterViewController:.
 It also implements a custom method, viewControllerAtIndex: which is useful in the implementation of the data source methods, and in the initial configuration of the application.

 There is no need to actually create view controllers for each page in advance -- indeed doing so incurs unnecessary overhead. Given the data model, these methods create, configure, and return a new view controller on demand.
 */

@implementation ModelController

- (id)init {
    self = [super init];
    if (self != nil) {
        _currentPageIndex = 0;
    }
    return self;
}

- (DataViewController *)viewControllerAtIndex:(NSUInteger)index storyboard:(UIStoryboard *)storyboard {
    // return the data view controller for the given index
    if (([self.pageData count] == 0) || (index >= [self.pageData count])) {
        return nil;
    }

    // vreate a new view controller and pass suitable data
    DataViewController *dataViewController = [storyboard instantiateViewControllerWithIdentifier:@"DataViewController"];
    dataViewController.dataObject = self.pageData[index];
    return dataViewController;
}

- (NSUInteger)indexOfViewController:(DataViewController *)viewController {
    // Return the index of the given data view controller.
    // For simplicity, this implementation uses a static array of model objects and the
    // view controller stores the model object; you can therefore use the model object to identify the index.
    //
    return [self.pageData indexOfObject:viewController.dataObject];
}


#pragma mark - UIPageViewControllerDataSource

- (UIViewController *)pageViewController:(UIPageViewController *)pageViewController viewControllerBeforeViewController:(UIViewController *)viewController {
    PhotosViewController *photosViewController = (PhotosViewController *)pageViewController.delegate;

    if (photosViewController.pageAnimationFinished == NO) {
        // we are still animating don't return a previous view controller too soon
        return nil;
    }

    NSUInteger index = [self indexOfViewController:(DataViewController *)viewController];
    if (index == 0 || index == NSNotFound) {
        // we are at the first page, don't go back any further
        return nil;
    }

    index--;
    _currentPageIndex = index;

    return [self viewControllerAtIndex:index storyboard:viewController.storyboard];
}

- (UIViewController *)pageViewController:(UIPageViewController *)pageViewController viewControllerAfterViewController:(UIViewController *)viewController {
    PhotosViewController *photosViewController = (PhotosViewController *)pageViewController.delegate;

    if (photosViewController.pageAnimationFinished == NO) {
        // we are still animating don't return a next view controller too soon
        return nil;
    }

    NSUInteger index = [self indexOfViewController:(DataViewController *)viewController];
    if (index == NSNotFound) {
        // we are at the last page, don't go back any further
        return nil;
    }

    index++;
    _currentPageIndex = index;

    if (index == [self.pageData count]) {
        return nil;
    }
    return [self viewControllerAtIndex:index storyboard:viewController.storyboard];
}

@end
```

[Next](PhotoMap-PhotosViewController-DataViewController.m.md)[Previous](PhotoMap-PhotosViewController-ModelController.h.md)

