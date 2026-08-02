---
title: XMLPerformance
apple_id: DTS40008094
resource_type: Sample Code
platform: iOS
topic: Performance
technology: Foundation
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/XMLPerformance/Listings/Classes_DetailController_m.html
archived_at: '2026-07-18T03:28:29.537994Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [XMLPerformance](XMLPerformance.md)


[Next](Classes-iTunesRSSParser.h.md)[Previous](Classes-ParserChoiceViewController.m.md)

# Classes/DetailController.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Displays details of a single parsed song.
 */

#import "DetailController.h"
#import "Song.h"

@interface DetailController ()

@property (nonatomic, readonly, strong) NSDateFormatter *dateFormatter;

@end

#pragma mark -

@implementation DetailController

- (void)viewDidLoad
{
    [super viewDidLoad];

    _dateFormatter = [[NSDateFormatter alloc] init];
    (self.dateFormatter).dateStyle = NSDateFormatterMediumStyle;
    (self.dateFormatter).timeStyle = NSDateFormatterNoStyle;
}

// When the view appears, update the title and table contents.
- (void)viewWillAppear:(BOOL)animated {

    [super viewWillAppear:animated];

    self.title = self.song.title;
    [self.tableView reloadData];
}


#pragma mark - UITableViewDataSource

- (NSInteger)tableView:(UITableView *)tv numberOfRowsInSection:(NSInteger)section {
    return 4;
}

- (UITableViewCell *)tableView:(UITableView *)table cellForRowAtIndexPath:(NSIndexPath *)indexPath {

    static NSString *kCellIdentifier = @"SongDetailCell";
    UITableViewCell *cell = (UITableViewCell *)[self.tableView dequeueReusableCellWithIdentifier:kCellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleValue2 reuseIdentifier:kCellIdentifier];
        cell.selectionStyle = UITableViewCellSelectionStyleNone;
    }
    switch (indexPath.row) {
        case 0: {
            cell.textLabel.text = NSLocalizedString(@"album", @"album label");
            cell.detailTextLabel.text = self.song.album;
        } break;
        case 1: {
            cell.textLabel.text = NSLocalizedString(@"artist", @"artist label");
            cell.detailTextLabel.text = self.song.artist;
        } break;
        case 2: {
            cell.textLabel.text = NSLocalizedString(@"category", @"category label");
            cell.detailTextLabel.text = self.song.category;
        } break;
        case 3: {
            cell.textLabel.text = NSLocalizedString(@"released", @"released label");
            cell.detailTextLabel.text = [self.dateFormatter stringFromDate:self.song.releaseDate];
        } break;
    }
    return cell;
}

- (NSString *)tableView:(UITableView *)tv titleForHeaderInSection:(NSInteger)section {
    return NSLocalizedString(@"Song details:", @"Song details label");
}

@end
```

[Next](Classes-iTunesRSSParser.h.md)[Previous](Classes-ParserChoiceViewController.m.md)

