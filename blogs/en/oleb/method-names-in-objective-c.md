---
title: Method Names in Objective-C
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/method-names-in-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0ee2d52ef99fc283'
translated: false
---

> 原文：[Method Names in Objective-C](https://oleb.net/blog/2010/12/method-names-in-objective-c/)　·　Ole Begemann

# Method Names in Objective-C

Apple’s Cocoa framework is well-known for its very long and descriptive method names. As an extreme example, take this method to initialize an `NSBitmapImageRep` instance with a specific bitmap format (only available on the Mac, not on iOS):

```
- (id)initWithBitmapDataPlanes:(unsigned char **)planes
                    pixelsWide:(NSInteger)width
                    pixelsHigh:(NSInteger)height
                 bitsPerSample:(NSInteger)bps
               samplesPerPixel:(NSInteger)spp
                      hasAlpha:(BOOL)alpha
                      isPlanar:(BOOL)isPlanar
                colorSpaceName:(NSString *)colorSpaceName
                  bitmapFormat:(NSBitmapFormat)bitmapFormat
                   bytesPerRow:(NSInteger)rowBytes
                  bitsPerPixel:(NSInteger)pixelBits
```

Objective-C (the language) aids Cocoa (the framework) in the quest for the longest method names of any framework with its syntax. The descriptive text for each argument before the colon is not a named parameter but a substantial part of the method signature itself. So the signature of the method above is:

```
initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:
```

Descriptive, isn’t it? While virtually all methods in Cocoa and elsewhere adhere to this scheme, all the text describing the method arguments is actually optional in Objective-C. So the following method in the `CAMediaTimingFunction` class has a perfectly valid name:

```
+ (id)functionWithControlPoints:(float)c1x
                               :(float)c1y
                               :(float)c2x
                               :(float)c2y
```

Consequently, the selector for this method is:

```
functionWithControlPoints::::
```

Not pretty in my opinion, but doable. Now it gets really weird. If we can omit the text before the colon for the second and all additional arguments, why not leave out the text before the first argument, as well? It turns out we can do exactly that!

Believe it or not, these are valid method declarations:

```
- (void):(id)param;
- (void):(id)param1 :(id)param2;
```

And this is how you would send these messages to an object:

```
[myObject :obj1];
[myObject :obj1 :obj2];
```

Please don’t ever use this knowledge in your own code.

**Update December 19, 2010:** Incidentally, Stack Overflow user [outis](http://stackoverflow.com/users/90527/outis) asked a very interesting question about message names in Obj-C the other day: [Why must the last part of an Objective-C method name take an argument?](http://stackoverflow.com/questions/4479967/why-must-the-last-part-of-an-objective-c-method-name-take-an-argument-when-there) The answers make an interesting read, and even the designer of Objective-C himself, Brad Cox, replied: [I simply didn’t think of departing from Smalltalk’s keyword structure.](http://stackoverflow.com/questions/4479967/why-must-the-last-part-of-an-objective-c-method-name-take-an-argument-when-there/4485347#4485347)
