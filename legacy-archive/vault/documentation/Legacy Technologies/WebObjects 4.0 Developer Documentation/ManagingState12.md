---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState12.html
archived_at: '2026-07-18T01:20:13.789658Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState11.md)

## Archiving Custom Objects in Other Applications

Custom classes that can't take advantage of an EOEditingContext for archiving must take a different approach. These classes still must conform to the NSCoding protocol and implement its __encodeWithCoder__: and __initWithCoder__: methods; however, you must implement them differently. In __encodeWithCoder:__, you use the coder argument provided to encode the object's instance variables. In __initWithCoder:__, the object uses the decoder provided to initialize itself.
For example:

```
- encodeWithCoder:(NSCoder *)coder {
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


The Java version of the same example looks like this:

```
public void encodeWithCoder(NSCoder coder) {
    coder.encodeObject(leaseTerm);
    coder.encodeObject(downPayment);
// The custom Car object that contains all other info about the car.
    coder.encodeObject(car);
}

public ShoppingCart(NSCoder coder) {
    super();
    leaseTerm = coder.decodeObject();
    downPayment = coder.decodeObject();
    Car aCar = (Car)coder.decodeObject();
    setCar(aCar);
}
```


For more information on archiving, see the class specifications for NSCoding, NSCoder, NSArchiver, and NSUnarchiver in the _Foundation Framework Reference_.

[!Table of Contents](Managing%20State.md) [!Next Section](Controlling%20Session%20State.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
