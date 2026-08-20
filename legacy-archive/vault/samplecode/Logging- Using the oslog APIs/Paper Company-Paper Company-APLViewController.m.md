---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/Paper_Company_Paper_Company_APLViewController_m.html
archived_at: '2026-07-18T03:13:47.527970Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](Paper%20Company-ReadMe.md.md)[Previous](Paper%20Company-Paper%20Company-APLPaperCompany.h.md)

# Paper Company/Paper Company/APLViewController.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A simple interface with a few buttons to trigger logging events. Demonstrates the Activity APIs.
 */

@import os.activity;
@import os.log;
#import "APLViewController.h"
#import "APLPaperCompany.h"

static os_log_t ui_log; // See comments in `APLPaperCompany.m`.


@interface APLViewController ()

@property (nonatomic) APLPaperCompany *company;
@property (weak, nonatomic) IBOutlet UIButton *treeButton;
// Put the logs on a truck to take them to the paper mill.
@property (weak, nonatomic) IBOutlet UIButton *truckButton;
@property (weak, nonatomic) IBOutlet UIButton *paperButton;

/// Update the on-screen buttons to match the paper company they represent.
- (void)updateButtonCounts;

@end


@implementation APLViewController

+ (void)initialize {
    // Set up our UI logging component before we use it.
    ui_log = os_log_create("com.example.apple-samplecode.Paper-Company", "UI");
}

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];

    self.company = [[APLPaperCompany alloc] initWithCompanyName:@"Porcupine Pete's Prickly Paper Products"];
    os_log(ui_log, "Created company named %@", self.company.companyName);
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];

    [self updateButtonCounts];
}

- (void)updateButtonCounts {
    os_log(ui_log, "Updating button counts");
    [self.treeButton setTitle:[NSString stringWithFormat:@"🌲 x%lu", (unsigned long)self.company.numTrees]
                     forState: UIControlStateNormal];
    [self.truckButton setTitle:[NSString stringWithFormat:@"🚚 x%lu", (unsigned long)self.company.numLogs]
                      forState: UIControlStateNormal];
    [self.paperButton setTitle:[NSString stringWithFormat:@"📄 x%lu", (unsigned long)self.company.numPapers]
                      forState: UIControlStateNormal];
}

/// Chop down a tree to turn into a log.
- (IBAction)treeButtonTapped:(UIButton *)sender {
    /*
        By initiating an activity, we gain the ability to follow the logs of any actions taken on our behalf.
    For example, when the user taps a Sync button, we can get just the logs from the button press, the
    system's cloud daemon (syncing files at our request), and the system security daemon (allowing us to
    log in to our cloud service). And we only get the logs resulting from action taken to serve our request,
    without anything else the daemon may be doing at the time.
    */
    os_activity_initiate("Chop down tree", OS_ACTIVITY_FLAG_DEFAULT, ^(void) {
        os_log_info(ui_log, "Cutting down trees to turn them into logs");
        os_log_debug(ui_log, "Sender: %@", sender);
        [self.company chopDownTree];
        [self updateButtonCounts];
    });
}

/// Send logs to the paper mill to be turned into paper.
- (IBAction)truckButtonTapped:(UIButton *)sender {
    os_activity_initiate("Pulverize logs", OS_ACTIVITY_FLAG_DEFAULT, ^(void) {
        os_log_info(ui_log, "Taking logs to the paper mill");
        os_log_debug(ui_log, "Sender: %@", sender);
        [self.company makePaper];
        [self updateButtonCounts];
    });
}

/// This does nothing. Paper is useless in our modern world.
- (IBAction)paperButtonTapped:(UIButton *)sender {
    // Well, there is one place paper beats an iPad. Can you guess what it is?
    // See `-[PaperCompany makePaper]` in `PaperCompany.m` for the answer.
    os_activity_initiate("Use paper", OS_ACTIVITY_FLAG_DEFAULT, ^(void) {
        os_log_debug(ui_log, "Sender: %@", sender);
        os_log_info(ui_log, "Paper is useless in our modern world!");

        [self updateButtonCounts];

        // Tell the user why paper does nothing.
        UIAlertController *alertController = [UIAlertController alertControllerWithTitle:@"Paper is useless in our modern world!"
                                                                                 message:nil
                                                                          preferredStyle:UIAlertControllerStyleAlert];
        UIAlertAction *okAction = [UIAlertAction actionWithTitle:@"OK" style:UIAlertActionStyleDefault handler:nil];
        [alertController addAction:okAction];
        [self presentViewController:alertController animated:YES completion:nil];
    });
}

/// Intentionally trigger a crash.
- (IBAction)bombButtonTapped:(id)sender {
    /*
        Use `error` when something goes wrong in your app, and use `fault` when
    something goes wrong involving another process. Both `os_log_error` and
    `os_log_fault` do extra work to make sure the relevant information is
    preserved, so only call them when something actually goes wrong.
    */
    os_log_error(ui_log, "B-b-b-b-b-b-b-bomb!");

    // Don't try this at home, kids!
    NSInteger *x = nil;
    NSInteger __unused y = *x;
}

@end
```

[Next](Paper%20Company-ReadMe.md.md)[Previous](Paper%20Company-Paper%20Company-APLPaperCompany.h.md)

