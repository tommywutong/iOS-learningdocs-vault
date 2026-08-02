---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_TwoViewController_m.html
archived_at: '2026-07-18T03:26:20.567072Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-AppDelegate.h.md)[Previous](Tabster-Classes-ModalViewController.h.md)

# Tabster/Classes/TwoViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The view controller for page two. 
 */

#import "TwoViewController.h"
#import "LandscapeViewController.h"

NSString *kRainbowImageName = @"Rainbow";
NSString *kSunsetImageName = @"Sunset";

@interface TwoViewController ()

@property (nonatomic, strong) NSArray *dataArray;

@end

#pragma mark -

@implementation TwoViewController

// This is called when its tab is first tapped by the user.

- (void)viewDidLoad
{
    [super viewDidLoad];

    self.dataArray = @[kRainbowImageName, kSunsetImageName];
}


#pragma mark - UITableViewDelegate

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return self.dataArray.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *kCellID = @"cellIDTwo";

    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:kCellID];
    cell.textLabel.text = self.dataArray[indexPath.row];

    return cell;
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"LandscapeViewSegue"])
    {
        LandscapeViewController *landscapeViewController = segue.destinationViewController;
        UITableViewCell *cell = sender;
        UIImage *image = nil;
        if ([cell.textLabel.text isEqualToString:kRainbowImageName])
        {
            image = [UIImage imageNamed:kRainbowImageName];
        }
        else if ([cell.textLabel.text isEqualToString:kSunsetImageName])
        {
            image = [UIImage imageNamed:kSunsetImageName];
        }
        landscapeViewController.image = image;
    }
}

@end
```

[Next](Tabster-Classes-AppDelegate.h.md)[Previous](Tabster-Classes-ModalViewController.h.md)

