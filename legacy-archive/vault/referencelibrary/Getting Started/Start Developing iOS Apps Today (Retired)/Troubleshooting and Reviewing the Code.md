---
title: Start Developing iOS Apps Today (Retired)
apple_id: TP40013837
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/RM_YourFirstApp_iOS/Articles/07_Troubleshooting.html
archived_at: '2026-07-18T02:47:15.148151Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps Today (Retired)](Document%20Revision%20History.md)


[Previous](Implementing%20the%20View%20Controller.md)

# Retired Document

__Important:__ This version of _Start Developing iOS Apps Today_ has been retired. The replacement version provides a new, more streamlined walkthrough of the basics. For information covering the same subject area as this page, please see ["Tutorial: Basics"](https://developer.apple.com/library/ios/referencelibrary/GettingStarted/RoadMapiOS/FirstTutorial.html#//apple_ref/doc/uid/TP40011343-CH3-SW1).

# Troubleshooting and Reviewing the Code

If you are having trouble getting your app to work correctly, try the problem-solving approaches described in this chapter. If your app still isn’t working as it should, compare your code with the listings shown at the end of this chapter.

Your code should compile without any warnings. If you do receive warnings, it’s recommended that you treat them as very likely to be errors. Because Objective-C is a very flexible language, sometimes the most you get from the compiler is a warning.

As a developer, if things don’t work correctly, your natural instinct is probably to check your source code for bugs. But when you use Cocoa Touch, another dimension is added. Much of your app’s configuration may be “encoded” in the storyboard. For example, if you haven’t made the correct connections, your app won’t behave as you expect.

- If the text doesn’t update when you click the button, it might be that you didn’t connect the button’s action to the view controller, or that you didn’t connect the view controller’s outlets to the text field or label.
- If the keyboard does not disappear when you click Done, you might not have connected the text field’s delegate or connected the view controller’s `textField` outlet to the text field. Be sure to check the text field’s connections on the storyboard: Control-click the text field to reveal the translucent connections panel. You should see filled-in circles next to the `delegate` outlet and the `textField` referencing outlet.

  If you have connected the delegate, there might be a more subtle problem (see the next section, “Delegate Method Names”).

A common mistake with delegates is to misspell the delegate method name. Even if you’ve set the delegate object correctly, if the delegate doesn’t use the right name in its method implementation, the correct method won’t be invoked. It’s usually best to copy and paste delegate method declarations, such as `textFieldShouldReturn:`, from the documentation.

This section provides listings for the interface and implementation files of the `HelloWorldViewController` class. Note that the listings don’t show comments and other method implementations that are provided by the Xcode template.


```objc
#import <UIKit/UIKit.h>

@interface HelloWorldViewController : UIViewController <UITextFieldDelegate>

@property (copy, nonatomic) NSString *userName;

@end
```



```objc
#import "HelloWorldViewController.h"

@interface HelloWorldViewController ()

@property (weak, nonatomic) IBOutlet UITextField *textField;
@property (weak, nonatomic) IBOutlet UILabel *label;

- (IBAction)changeGreeting:(id)sender;

@end

@implementation HelloWorldViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    return (interfaceOrientation != UIInterfaceOrientationPortraitUpsideDown);
}

- (IBAction)changeGreeting:(id)sender {

    self.userName = self.textField.text;

    NSString *nameString = self.userName;
    if ([nameString length] == 0) {
        nameString = @"World";
    }
    NSString *greeting = [[NSString alloc] initWithFormat:@"Hello, %@!", nameString];
    self.label.text = greeting;
}

- (BOOL)textFieldShouldReturn:(UITextField *)theTextField {

    if (theTextField == self.textField) {
        [theTextField resignFirstResponder];
    }
    return YES;
}

@end
```

[Back to Jump Right In](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/JumpRightIn.html)
!
!
![Previous](../../../_unindexed/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/RM_YourFirstApp_iOS/Articles/06_ImplementingController.md)

---
