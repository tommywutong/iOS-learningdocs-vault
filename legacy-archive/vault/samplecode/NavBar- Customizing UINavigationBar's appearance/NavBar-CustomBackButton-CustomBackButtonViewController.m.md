---
title: 'NavBar: Customizing UINavigationBar''s appearance'
apple_id: DTS40007418
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2017-12-07'
source_url: https://developer.apple.com/library/archive/samplecode/NavBar/Listings/NavBar_CustomBackButton_CustomBackButtonViewController_m.html
archived_at: '2026-07-18T03:16:53.058652Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NavBar: Customizing UINavigationBar's appearance](NavBar-%20Customizing%20UINavigationBar%27s%20appearance.md)


[Next](NavBar-CustomBackButton-CustomBackButtonViewController.h.md)[Previous](NavBar-CustomRightView-CustomRightViewController.swift.md)

# NavBar/CustomBackButton/CustomBackButtonViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Demonstrates using a custom back button image with no chevron and no text.
 */

#import "CustomBackButtonViewController.h"
#import "NavBar-Swift.h"

@interface CustomBackButtonViewController ()

/// Our data source is an array of city names, populated from Cities.json.
@property (nonatomic, strong) CitiesDataSource *dataSource;

@end

#pragma mark -

@implementation CustomBackButtonViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    _dataSource = [[CitiesDataSource alloc] init];
    self.tableView.dataSource = self.dataSource;

    // Note that images configured as the back bar button's background do
    // not have the current tintColor applied to them, they are displayed as it.
    UIImage *backButtonBackgroundImage = [UIImage imageNamed:@"Menu"];
    // The background should be pinned to the left and not stretch.
    backButtonBackgroundImage =
        [backButtonBackgroundImage resizableImageWithCapInsets:UIEdgeInsetsMake(0, backButtonBackgroundImage.size.width - 1, 0, 0)];

    id barAppearance =
        [UINavigationBar appearanceWhenContainedInInstancesOfClasses:@[[CustomBackButtonNavController class]]];
    [barAppearance setBackIndicatorImage:backButtonBackgroundImage];
    [barAppearance setBackIndicatorTransitionMaskImage:backButtonBackgroundImage];

    // Provide an empty backBarButton to hide the 'Back' text present by
    // default in the back button.
    //
    // NOTE: You do not need to provide a target or action.  These are set
    //       by the navigation bar.
    // NOTE: Setting the title of this bar button item to ' ' (space) works
    //       around a bug in iOS 7.0.x where the background image would be
    //       horizontally compressed if the back button title is empty.
    UIBarButtonItem *backBarButton = [[UIBarButtonItem alloc] initWithTitle:@" "
                                                                      style:UIBarButtonItemStylePlain
                                                                     target:nil
                                                                     action:nil];
    self.navigationItem.backBarButtonItem = backBarButton;
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    NSString *city = [self.dataSource cityWithIndex:self.tableView.indexPathForSelectedRow.row];
    if ([segue.identifier isEqualToString:@"DetailSegue"])
    {
        [(CustomBackButtonDetailViewController *)segue.destinationViewController setCity:city];
    }
}

@end
```

[Next](NavBar-CustomBackButton-CustomBackButtonViewController.h.md)[Previous](NavBar-CustomRightView-CustomRightViewController.swift.md)

