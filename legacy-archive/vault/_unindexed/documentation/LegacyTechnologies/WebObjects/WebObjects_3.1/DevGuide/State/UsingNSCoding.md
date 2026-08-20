---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/UsingNSCoding.html
archived_at: '2026-07-15T07:47:55.895612Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](UsingEOEditingContext.md)

# __Using the NSCoding Protocol to Archive Custom Objects__

Custom classes that can't take advantage of an EOEditingContext for archiving must take a different approach. These classes must conform to the NSCoding protocol and implement its __encodeWithCoder:__ and __initWithCoder:__ methods. __encodeWithCoder:__ instructs an object to encode its instance variables to the coder provided; an object can receive this message any number of times. __initWithCoder:__ instructs an object to initialize itself from data in the coder provided; as such, it replaces any other initialization method and is only sent once per object.

__Note:__  Most of the Foundation classes already conform to the NSCoding protocol. This section only applies to the custom classes you write yourself.

For example, the DodgeDemo ShoppingCart class in the WebObjects examples includes the following implementations for __encodeWithCoder:__ and __initWithCoder:__.

```objc
- (void)encodeWithCoder:(NSCoder *)coder {
    [coder encodeObject:carID];
    [coder encodeObject:colorID];
    [coder encodeObject:colorPicture];
    [coder encodeObject:packagesIDs];
    [coder encodeObject:downPayment];
    [coder encodeObject:leaseTerm];
}

- initWithCoder:(NSCoder *)coder {
    self = [super init];
    carID = [[coder decodeObject] retain];
    colorID = [[coder decodeObject] retain];
    colorPicture = [[coder decodeObject] retain];
    packagesIDs = [[coder decodeObject] retain];
    downPayment = [[coder decodeObject] retain];
    leaseTerm = [[coder decodeObject] retain];
    car = nil;
    return self;
}
```

For more information on archiving, see the NSCoding, NSCoder, NSArchiver, and NSUnarchiver class specifications in the _Foundation Framework Reference_.

[!Table of Contents](ManagingState.book.md)
[!Next Section](ControllingSessionState.md)
