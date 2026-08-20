---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_ThreeViewController_m.html
archived_at: '2026-07-18T03:26:20.444588Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-FeaturedViewController.m.md)[Previous](Tabster-Classes-SubLevelViewController.m.md)

# Tabster/Classes/ThreeViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The view controller for page three. 
 */

#import "ThreeViewController.h"

NSString *kBadgeValuePrefKey = @"kBadgeValue";  // badge value key for storing to NSUserDefaults

@interface ThreeViewController () <UITextFieldDelegate>

@property (nonatomic, strong) UIBarButtonItem *doneButton;
@property (nonatomic, weak) IBOutlet UITextField *badgeField;

- (void)doneAction:(id)sender;

@end

#pragma mark -

@implementation ThreeViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    // Set the badge value in our test field and tabbar item.
    NSString *badgeValue = [[NSUserDefaults standardUserDefaults] stringForKey:kBadgeValuePrefKey];
    _doneButton = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemDone target:self action:@selector(doneAction:)];
    if (badgeValue.length != 0)
    {
        self.badgeField.text = badgeValue;
        self.navigationController.tabBarItem.badgeValue = self.badgeField.text;
    }
}

- (void)doneAction:(id)sender
{
    // Dismiss the keyboard by resigning our badge edit field as first responder.
    [self.badgeField resignFirstResponder];

    // Set the badge value to our tab item (but only if a valid string).
    if (self.badgeField.text.length > 0)
    {
        // A value was entered, because we are inside a navigation controller,
        // we must access its tabBarItem to set the badgeValue.
        self.navigationController.tabBarItem.badgeValue = self.badgeField.text;
    }
    else
    {
        // No value was entered.
        self.navigationController.tabBarItem.badgeValue = nil;
    }

    [[NSUserDefaults standardUserDefaults] setValue:self.badgeField.text forKey:kBadgeValuePrefKey];
}


#pragma mark - UITextFieldDelegate

- (void)textFieldDidBeginEditing:(UITextField *)textField
{
    // user is starting to edit, add the done button to the navigation bar
    self.navigationItem.rightBarButtonItem = self.doneButton;
}

- (void)textFieldDidEndEditing:(UITextField *)textField
{
    /// user is done editing, remove the done button from the navigation bar
    self.navigationItem.rightBarButtonItem = nil;
}

- (BOOL)textField:(UITextField *)textField shouldChangeCharactersInRange:(NSRange)range replacementString:(NSString *)string
{
    BOOL result = YES;

    // restrict the maximum number of characters to 5
    if (textField.text.length == 5 && string.length > 0)
        result = NO;

    return result;
}

@end
```

[Next](Tabster-Classes-FeaturedViewController.m.md)[Previous](Tabster-Classes-SubLevelViewController.m.md)

