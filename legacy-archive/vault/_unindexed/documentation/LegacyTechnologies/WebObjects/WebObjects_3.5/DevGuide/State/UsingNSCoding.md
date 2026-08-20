---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/UsingNSCoding.html
archived_at: '2026-07-15T07:52:24.313014Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](UsingEOEditingContext.md)

## Archiving Custom Objects in Other Applications

Custom classes that can't take advantage of an EOEditingContext for archiving must take a different approach. These classes still must conform to the NSCoding protocol and implement its encodeWithCoder: and initWithCoder: methods; however, you must implement them differently. In __encodeWithCoder:__, you use the coder argument provided to encode the object's instance variables. In __initWithCoder:__, the object uses the decoder provided to initialize itself.
You can see implementations of __encodeWithCoder:__ and __initWithCoder:__ in the DodgeDemo application, in the class ShoppingCart.

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


The Java version of DodgeDemo's ShoppingCart implements these methods instead:

```
    public void encodeWithCoder(Coder coder) {
        coder.encodeObject(leaseTerm);
        coder.encodeObject(downPayment);
        // DodgeDemoJava defines a custom Car object that contains all
        // info about the car.
        coder.encodeObject(car);
    }

    public ShoppingCart(Coder coder) {
        super();
        leaseTerm = coder.decodeObject();
        downPayment = coder.decodeObject();
        Car aCar = (Car)coder.decodeObject();
        setCar(aCar);
    }
```


For more information on archiving, see the class specifications for NSCoding, NSCoder, NSArchiver, and NSUnarchiver in the _Foundation Framework Reference_.

[!Table of Contents](StateTOC.md) [!Next Section](ControllingSessionState.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
