---
title: Reflection
apple_id: DTS40008063
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2015-09-24'
source_url: https://developer.apple.com/library/archive/samplecode/Reflection/Listings/SliderCell_m.html
archived_at: '2026-07-18T03:22:04.975937Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Reflection](Reflection.md)


[Next](SliderCell.h.md)[Previous](main.m.md)

# SliderCell.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 UITableViewCell to host a slider, its label and value.
 */

#import "SliderCell.h"

@implementation SliderCell

- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:UITableViewCellStyleValue1 reuseIdentifier:reuseIdentifier];
    if (self != nil)
    {
        // Label for type of slider
        self.textLabel.backgroundColor = [UIColor clearColor];
        self.textLabel.font = [UIFont boldSystemFontOfSize:14.0];
        self.textLabel.textColor = [UIColor blackColor];
        self.selectionStyle = UITableViewCellSelectionStyleNone;

        // Slider
        UISlider *slider =
            [[UISlider alloc] initWithFrame:CGRectMake(self.contentView.bounds.origin.x + 55.0, 0.0,
                                                       self.contentView.bounds.size.width - 110.0, 40.0)];
        slider.continuous = YES;
        slider.tag = kSliderTag;
        [self.contentView addSubview:slider];

        // Label for slider values
        self.detailTextLabel.backgroundColor = [UIColor clearColor];
        self.detailTextLabel.font = [UIFont boldSystemFontOfSize:12.0];
        self.detailTextLabel.textColor = [UIColor blackColor];
    }
    return self;
}

@end
```

[Next](SliderCell.h.md)[Previous](main.m.md)

