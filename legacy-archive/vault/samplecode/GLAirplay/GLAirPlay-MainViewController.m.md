---
title: GLAirplay
apple_id: DTS40013259
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/GLAirplay/Listings/GLAirPlay_MainViewController_m.html
archived_at: '2026-07-18T03:09:50.346118Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLAirplay](GLAirplay.md)


[Next](ReadMe.md.md)[Previous](GLAirPlay-AppDelegate.h.md)

# GLAirPlay/MainViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The root view controller. Demonstrates detailed steps on how to show content on an external display.
 */

#import "MainViewController.h"
#import "GLViewController.h"

@interface MainViewController ()

@property (nonatomic, strong) UIWindow *extWindow;
@property (nonatomic, strong) UIScreen *extScreen;

@end

@implementation MainViewController

- (void)screenDidChange:(NSNotification *)notification
{
    // To display content on an external display, do the following:
    // 1. Use the screens class method of the UIScreen class to determine if an external display is available.
    NSArray *screens = [UIScreen screens];

    NSUInteger screenCount = [screens count];

    if (screenCount > 1)
    {
        // 2. If an external screen is available, get the screen object and look at the values in its availableModes
        // property. This property contains the configurations supported by the screen.

        // Select first external screen
        self.extScreen = [screens objectAtIndex:1]; //index 0 is your iPhone/iPad
        NSArray *availableModes = [self.extScreen availableModes];

        // 3. Select the UIScreenMode object corresponding to the desired resolution and assign it to the currentMode
        // property of the screen object.

        // Select the highest resolution in this sample
        NSInteger selectedRow = [availableModes count] - 1;
        self.extScreen.currentMode = [availableModes objectAtIndex:selectedRow];

        // Set a proper overscanCompensation mode
        self.extScreen.overscanCompensation = UIScreenOverscanCompensationInsetApplicationFrame;

        if (self.extWindow == nil) {
            // 4. Create a new window object (UIWindow) to display your content.
            UIWindow *extWindow = [[UIWindow alloc] initWithFrame:[self.extScreen bounds]];
            self.extWindow = extWindow;
            self.extWindow.rootViewController = self.glController;
        }

        // 5. Assign the screen object to the screen property of your new window.
        self.extWindow.screen = self.extScreen;

        // 6. Configure the window (by adding views or setting up your OpenGL ES rendering context).

        // Resize the GL view to fit the external screen
        self.glController.view.frame = self.extWindow.frame;

        // Set the target screen to the external screen
        // This will let the GL view create a CADisplayLink that fires at the native fps of the target display.
        [(GLViewController *)self.glController setTargetScreen:self.extScreen];

        // Configure user interface
        // In this sample, we use the same UI layout when an external display is connected or not.
        // In your real application, you probably want to provide distinct UI layouts for best user experience.
        [(GLViewController *)self.glController screenDidConnect:self.userInterfaceController];

        // Add the GL view
        [self.extWindow addSubview:self.glController.view];

        // 7. Show the window.
        [self.extWindow makeKeyAndVisible];

        // On the iPhone/iPad screen
        // Remove the GL view (it is displayed on the external screen)
        for (UIView* v in [self.view subviews])
            [v removeFromSuperview];

        // Display the fullscreen UI on the iPhone/iPad screen
        [self.view addSubview:self.userInterfaceController.view];
    }
    else //handles disconnection of the external display
    {
        // Release external screen and window
        self.extScreen = nil;
        self.extWindow = nil;

        // On the iPhone/iPad screen
        // Remove the fullscreen UI (a window version will be displayed atop the GL view)
        for (UIView* v in [self.view subviews])
            [v removeFromSuperview];

        // Resize the GL view to fit the iPhone/iPad screen
        self.glController.view.frame = self.view.frame;

        // Set the target screen to the main screen
        // This will let the GL view create a CADisplayLink that fires at the native fps of the target display.
        [(GLViewController *)self.glController setTargetScreen:[UIScreen mainScreen]];

        // Configure user interface
        // In this sample, we use the same UI layout when an external display is connected or not.
        // In your real application, you probably want to provide distinct UI layouts for best user experience.
        [(GLViewController *)self.glController screenDidDisconnect:self.userInterfaceController];

        // Display the GL view on the iPhone/iPad screen
        [self.view addSubview:self.glController.view];
    }
}

- (void)dealloc
{
    [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:UIScreenDidConnectNotification
                                                  object:nil];

    [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:UIScreenDidDisconnectNotification
                                                  object:nil];
}

- (void)viewDidLoad
{
    [super viewDidLoad];

    UIViewController *userInterfaceController = [[UIStoryboard storyboardWithName:@"MainStoryboard" bundle:NULL] instantiateViewControllerWithIdentifier:@"UserInterfaceViewController"];
    self.userInterfaceController = userInterfaceController;

    UIViewController *glController = [[UIStoryboard storyboardWithName:@"MainStoryboard" bundle:NULL] instantiateViewControllerWithIdentifier:@"GLViewController"];
    self.glController = glController;

    // No notifications are sent for screens that are present when the app is launched.
    [self screenDidChange:nil];

    // Register for screen connect and disconnect notifications.
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(screenDidChange:)
                                                 name:UIScreenDidConnectNotification
                                               object:nil];

    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(screenDidChange:)
                                                 name:UIScreenDidDisconnectNotification
                                               object:nil];
}

- (BOOL)shouldAutorotate {
    return YES;
}

@end
```

[Next](ReadMe.md.md)[Previous](GLAirPlay-AppDelegate.h.md)

