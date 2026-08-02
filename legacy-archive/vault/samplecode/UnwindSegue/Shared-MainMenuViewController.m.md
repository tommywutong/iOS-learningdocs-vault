---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_MainMenuViewController_m.html
archived_at: '2026-07-18T03:27:36.671713Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Document%20Revision%20History.md)[Previous](Shared-Quiz.m.md)

# Shared/MainMenuViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for the initial screen.  Manages creating the Quiz  
  and displaying the user's highest score.
 */

#import "MainMenuViewController.h"
#import "Quiz.h"
#import "QuestionViewController.h"
#import "ResultsViewController.h"

@interface MainMenuViewController () <UITableViewDataSource, UITabBarControllerDelegate>
@property (nonatomic, weak) IBOutlet UITableView *tableView;
@property (readwrite) float highScore;
@end


@implementation MainMenuViewController

//| ----------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // match the background color to the status bar
    [[UINavigationBar appearance] setTranslucent:NO];

    // No highscrore when the view first loads.
    self.highScore = -1.0f;
}


//| ----------------------------------------------------------------------------
- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];

    [self.tableView reloadData];
}


//| ----------------------------------------------------------------------------
//  This method will be called when the 'Begin' button is tapped.
//
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    // Set the quiz of the destination view controller.
    // In a navigation stack the segue.destinationViewController is instantiated.
    // However for a custom segue it is not, so we will set the quiz in the segue's -perform method.
    if ([segue.destinationViewController isKindOfClass:[UINavigationController class]])
    {
        [Quiz setQuizOnQuestionViewController:segue.destinationViewController.childViewControllers.firstObject];
    }
}

//| ----------------------------------------------------------------------------
//! Unwinds from the ResultsViewController back to the MainMenuViewController
//! when the user taps the 'Return to the Home Screen' button.
//
//  This is an unwind action.  Note that the sender parameter is a
//  'UIStoryboardSegue*' instead of the usual 'id'.  Like all unwind actions,
//  this method is invoked early in the unwind process, before the visual
//  transition.  Note that the receiver of this method is the
//  destinationViewController of the segue.  Your view controller should use
//  this callback to retrieve information from the sourceViewController.  Used
//  properly, this method can replace existing delegation techniques for
//  passing information from a detail view controller to a previous view
//  controller in the navigation hierarchy.
//
- (IBAction)exitToHomeScreen:(UIStoryboardSegue *)unwindSegue
{
    // Retrieve the score from the ResultsViewController and update the high
    // score.
    ResultsViewController *resultVC = (ResultsViewController*)unwindSegue.sourceViewController;
    self.highScore = MAX(resultVC.currentQuiz.percentageScore, self.highScore);
}

#pragma mark -
#pragma mark UITableViewDatasource

//| ----------------------------------------------------------------------------
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    // If there is a highscore to display, there are three sections.  Else,
    // there are two sections.
    return (self.highScore > -1.0f) ? 3 : 2;
}


//| ----------------------------------------------------------------------------
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    // There is only one row per section.
    return 1;
}


//| ----------------------------------------------------------------------------
- (UITableViewCell*)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell;

    if (indexPath.section == 0)
        cell = [tableView dequeueReusableCellWithIdentifier:@"Instructions"];
    else if (indexPath.section == 1 && tableView.numberOfSections == 3)
    // If there are three setions being displayed, the second row shows the
    // highscore.
    {
        cell = [tableView dequeueReusableCellWithIdentifier:@"Score"];
        cell.textLabel.text = [NSString stringWithFormat:@"Your best recorded score is %.0f%%", self.highScore * 100];
    }
    else
        // Last section is always the Begin button.
        cell = [tableView dequeueReusableCellWithIdentifier:@"Begin"];

    return cell;
}

#pragma mark -
#pragma mark UITableViewDelegate

//| ----------------------------------------------------------------------------
//  This delegate method is implemented because the height of the
//  instructions cell will need to change depending on the height required to
//  display the instruction text.  As the device rotates this will change.
//
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    if (indexPath.section == 0)
    // Instructions cell
    {
        UITableViewCell *instructionsCell = [tableView dequeueReusableCellWithIdentifier:@"Instructions"];
        UILabel *instructionsLabel = instructionsCell.textLabel;

        // Use the -boundingRectWithSize:options:attributes:context: method of NSString to
        // determine the required height of the instructions cell in order
        // to display the instructions without cutting off any of the text.

        // The width must be constrained to the width of the table view minus the
        // left and right margin of a grouped style cell.
        // Unfortunately, there is no way to lookup exactly what that margin is,
        // so it must be hardcoded.
        // The height is left unconstrained.
        CGSize constrainingSize = CGSizeMake(tableView.bounds.size.width - 40*2, MAXFLOAT);

        return ceill([instructionsLabel.text boundingRectWithSize:constrainingSize options:NSStringDrawingUsesLineFragmentOrigin attributes:nil context:nil].size.height + 40);
    }

    return tableView.rowHeight;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](Shared-Quiz.m.md)

