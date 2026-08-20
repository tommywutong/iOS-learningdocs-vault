---
title: 'SeismicXML: Using NSXMLParser to parse XML documents'
apple_id: DTS40007323
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2016-01-08'
source_url: https://developer.apple.com/library/archive/samplecode/SeismicXML/Listings/SeismicXML_APLEarthquakeTableViewCell_m.html
archived_at: '2026-07-18T03:23:39.761910Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SeismicXML: Using NSXMLParser to parse XML documents](SeismicXML-%20Using%20NSXMLParser%20to%20parse%20XML%20documents.md)


[Next](SeismicXML-APLParseOperation.m.md)[Previous](SeismicXML-APLAppDelegate.h.md)

# SeismicXML/APLEarthquakeTableViewCell.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view cell to display an earthquake.
 */

#import "APLEarthquakeTableViewCell.h"
#import "APLEarthquake.h"

@interface APLEarthquakeTableViewCell ()

// References to the subviews which display the earthquake data.
@property (nonatomic, weak) IBOutlet UILabel *locationLabel;
@property (nonatomic, weak) IBOutlet UILabel *dateLabel;
@property (nonatomic, weak) IBOutlet UILabel *magnitudeLabel;
@property (nonatomic, weak) IBOutlet UIImageView *magnitudeImage;

@property (nonatomic, readonly) NSDateFormatter *dateFormatter;

@end


#pragma mark -

@implementation APLEarthquakeTableViewCell

- (void)configureWithEarthquake:(APLEarthquake *)earthquake {

    self.locationLabel.text = earthquake.location;
    self.dateLabel.text = [NSString stringWithFormat:@"%@", [self.dateFormatter stringFromDate:earthquake.date]];
    self.magnitudeLabel.text = [NSString stringWithFormat:@"%.1f", earthquake.magnitude];
    self.magnitudeImage.image = [self imageForMagnitude:earthquake.magnitude];
}

// Based on the magnitude of the earthquake, return an image indicating its seismic strength.
- (UIImage *)imageForMagnitude:(CGFloat)magnitude {

    if (magnitude >= 5.0) {
        return [UIImage imageNamed:@"5.0.png"];
    }
    if (magnitude >= 4.0) {
        return [UIImage imageNamed:@"4.0.png"];
    }
    if (magnitude >= 3.0) {
        return [UIImage imageNamed:@"3.0.png"];
    }
    if (magnitude >= 0.0) {
        return [UIImage imageNamed:@"2.0.png"];
    }
    return nil;
}

// On-demand initializer for read-only property.
- (NSDateFormatter *)dateFormatter {

    static NSDateFormatter *dateFormatter = nil;
    if (dateFormatter == nil) {
        dateFormatter = [[NSDateFormatter alloc] init];
        dateFormatter.timeZone = [NSTimeZone localTimeZone];
        dateFormatter.dateStyle = NSDateFormatterMediumStyle;
        dateFormatter.timeStyle = NSDateFormatterMediumStyle;
    }
    return dateFormatter;
}

@end
```

[Next](SeismicXML-APLParseOperation.m.md)[Previous](SeismicXML-APLAppDelegate.h.md)

