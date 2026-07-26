---
title: 'Back to the Mac? 12 features from iOS I''d like to see in Lion | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/11/back-to-mac-12-features-from-ios-i-like.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:e1c506b190469004'
translated: false
---

> 原文：[Back to the Mac? 12 features from iOS I'd like to see in Lion | Cocoa with Love](https://www.cocoawithlove.com/2010/11/back-to-mac-12-features-from-ios-i-like.html)　·　Cocoa with Love (Matt Gallagher)

A few user-features of Mac OS X Lion have been announced but no Cocoa API changes have been publicly announced. However, I think there are dozens of non-user areas where the Cocoa Mac APIs could be improved by integrating approaches from Cocoa Touch APIs. What follows are a dozen areas where I'd like to see a more iOS approach in Mac OS X Lion.

## Introduction

The changes I'm going to discuss fall four basic categories:

- simplifying common tasks
- making important classes simpler to customize
- updating APIs on the Mac that seem to have been ignored since iOS appeared
- making CoreAnimation good enough to be used for all views on the Mac

## 1. Converting NSColor to CGColor

This first point is a minor simplification of a common task but I think it illustrates the fact that iOS integrates CoreGraphics and other forms of drawing well, where this integration seems to be lacking on the Mac.

On iOS, converting a UIColor to a Core Graphics CGColor is a basic property accessor:

```objc
CGColor myCGColor = myUIColor.cgColor;
```

It's as simple as can be. On the Mac, it's as convoluted as I could have imagined:

```objc
// Ensure that the color is in the "generic" RGB space so we can safely get the components
NSColor *rgbColor = [self colorUsingColorSpaceName:NSCalibratedRGBColorSpace];

// Get the r, g, b, a components
CGFloat colorComponents[4];
[rgbColor getComponents:colorComponents];

// Create the CGColor
CGColorRef myCGColor =
    (CGColorRef)[(id)CGColorCreateGenericRGB(
        colorComponents[0],
        colorComponents[1],
        colorComponents[2],
        colorComponents[3])
    autorelease];
```

While I'm on the topic of colors, I don't think the documentation for NSColor is clear enough about the choice between "Device" colors or "Calibrated" colors in an application user-interface. On iOS, there are only device colors — so there's no question — but on the Mac, you can create a white NSColor as either:

```objc
NSColor *calibratedColor = [NSColor colorWithCalibratedWhite:1.0 alpha:1.0];
```

or

```objc
NSColor *deviceColor = [NSColor colorWithDeviceWhite:1.0 alpha:1.0];
```

The User Interface Guidelines, NSColorSpace and the NSColor documentation offer no information about which should be the default choice in an arbitrary application. It'd be nice to have a clearer statement about when each is appropriate.

**Edit**: as pointed out in the comments, Apple do have a line in the Color Programming Topics documentation that suggests that you use _calibrated_ color spaces where possible.

## 2. A constructor for NSTextField that constructs it as a static label

Another simplification of a common task that I'd like to see is the ability to create a static text label in a single statement. On iOS, we have the UILabel subclass of NSView for non-editable text display.

```objc
UILabel *label = [[UILabel alloc] initWithFrame:labelFrame];
```

On the Mac, the editable NSTextField can be configured to handle non-editable display. Unfortunately, while there is an efficient way to construct NSTextField as a static text label in Interface Builder, there is no similarly efficient way in code:

```objc
NSTextView *label = [[NSTextField alloc] initWithFrame:labelFrame];
[label setEditable:NO];
[label setBezeled:NO];
```

Not a huge gripe but if you're constructing a view in code, the two extra lines for every label can become tiresome. An -initStaticLabelWithFrame: or +staticLabelWithFrame: method would be nice.

## 3. Simplified methods for common actions, e.g. -[UIImage drawInRect:]

A final type of common task I'd like to see simplified is offering simpler methods for common cases.

One of the most prominent examples of simpler methods that I'd like to see is for drawing an image. To draw a UIImage in iOS we use a simple method:

```objc
[myImage drawInRect:someRect];
```

On the Mac:

```objc
[myImage
    drawInRect:someRect
    fromRect:NSZeroRect
    operation:NSCompositeSourceOver
    fraction:1.0
    respectFlipped:YES
    hints:nil];
```

I realize that in both cases it's only one method. I also realize that the Mac example is significantly more capable. However, the functionality of the iOS method is overwhelming the common case and I think that this option should be added to the Mac as well, to recognize that this is the common path.

## 4. Resizable NSImage

Another NSImage/UIImage point — but now in the topic area of making important classes easier to customize — it would be really good to see the method:

```objc
- (UIImage *)stretchableImageWithLeftCapWidth:(NSInteger)leftCapWidth
    topCapHeight:(NSInteger)topCapHeight
```

brought from iOS to the Mac. If you've never used this method before, it allows you to take a square image — like a button image — and label and specify the boundary of the image (the left and top "caps") so that when the image is stretched to fit a new size, the cap areas are preserved and only the middle of the image is stretched.

On the Mac, you can use the function NSDrawNinePartImage() but while this function is significantly more configurable, it lacks the ability to be used anywhere you use an NSImage — so you can't use it as the background to an NSButton, you must subclass NSButtonCell and handle the drawing manually.

## 5. Setting the text color on an NSButton

The second "making important classes easier to customize" point is setting text color on a button. For UIButton it looks like this:

```objc
button.titleLabel.textColor = [UIColor whiteColor];
```

On the Mac there are no standard methods and you have to change the attributed string for the NSButton's title:

```objc
NSMutableAttributedString *title =
    [[[NSMutableAttributedString alloc] 
        initWithAttributedString:[button attributedTitle]]
    autorelease];
[title
    addAttribute:NSForegroundColorAttributeName 
    value:[NSColor whiteColor]
    range:NSMakeRange(0, [title length])];
[title fixAttributesInRange:range];
[button setAttributedTitle:title];
```

Not only is this ugly, but you may have to redo it if the title changes.

## 6. Support for white on black in other controls

It should be much easier is changing the color of other standard controls too. Specifically, I think it should be possible to place any control on a black background and make it visible.

Do you want a white "spinner" (indeterminate progress indicator) to go on a black background? On iOS, all you need is:

```objc
UIActivityIndicatorView *indicator =
    [[[UIActivityIndicatorView alloc]
        initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleWhite]
    autorelease];
```

If you want to make the `NSProgressIndicator` on the make white... you can't. You need to draw the entire control yourself.

## 7. An NSTableView equivalent that uses NSView for rows

The final "making important classes easier to customize" point is about NSTableView: we need an NSTableView like class on the Mac that handles the same column and row operations but contains proper NSViews instead of NSCell.

I've [spoken about this desire before](https://www.cocoawithlove.com/2010/03/custom-ui-bindings-in-interface-builder.html). The idea is pretty straightforward: UITableView creates a proper UITableViewCell (a subclass of UIView) for every row — this means that rows in a UITableView can behave like any UIView — they can be loaded from a NIB by a UIViewController, they can receive touches, contain buttons and be animated.

The iOS UITableView lacks bindings and doesn't have columns at all but in nearly every other respect, it is superior to the options on the Mac.

The NSCell that draws an NSTableView on the Mac is just limited. It can't animate, it can't contain regular views or buttons or receive clicks independent of the NSTableView. While using just one lightweight cell object per column may have made sense in the 1990's, it seems unnecessarily limiting in 2010.

There is certainly NSCollectionView which handles grids of actual NSViews but this class would need some work in terms of efficiency if it is to replace an NSTableView.

What's wrong with NSCollectionView? Simple: it constructs every view, including those that aren't visible. If your NSCollectionView contains 1 million views, this isn't going to work well. Further: NSCollectionView doesn't handle table-like interaction (you can't use column or row operations by default).

The reality is that NSCollectionView is designed to fill a slightly different niche; what we really need is a better NSTableView.

## 8. Get rid of NSNib

Now to the first of the APIs that I think were updated when they were implemented in iOS but these updates never seemed to make it into Mac OS itself.

The first is a fairly mild point: what is the purpose of the NSNib class on the Mac? Technically, the answer is "it loads and instantiates NIB files". It also provides the ability to cache the loaded NIB for faster instantiation. In reality though, iOS does all of this work without needing a new class.

Specifically in this case, I'm looking at loading a NIB file and getting the array of top level objects.

Both iOS and Mac OS X can load a NIB through NSBundle without getting the top level array but on Mac OS X (connecting only to the "owner" object) but getting full access to the created objects requires using NSNib. In iOS though, you can do this directly from NSBundle, making the existence of the NSNib class seem a little pointless.

On iOS:

```objc
contentArray =
    [[[NSBundle mainBundle]
        loadNibNamed:nibName
        owner:self
        options:nil]
    retain];
```

On the Mac:

```objc
NSNib *nib =
    [[[NSNib alloc]
        initWithNibNamed:nibName
        bundle:[NSBundle mainBundle]]
    autorelease];
[nib instantiateNibWithOwner:self
    topLevelObjects:&contentArray];
[contentArray retain];
```

You could probably argue that the Mac implementation lets you cache the NSNib and reinstantiate again later. The reality is: the iOS version [seems to handle this cacheing behind the scenes, automatically](https://www.cocoawithlove.com/2010/03/load-from-nib-or-construct-views-in.html). Less code, more powerful; it's better. We can get rid of NSNib on the Mac.

**Edit**: it appears I overlooked the fact that iOS introduced UINib in 4.0 — so Apple are bringing the Mac approach to iOS instead of the other way around. So I guess this is a point where I simply disagree; I think that the cacheing should be done automatically in NSBundle (so that the simplest approach is also the best). This could be combined with optional cache/don't cache flags passed into the "options" parameter if you need finer control.

## 9. Language Rotor for Text-To-Speech

This is probably the most "user" feature of the points in this post but iOS has had dramatic improvements in text-to-speech relative to the Mac.

On iOS devices that support VoiceOver, the voice in Australia (where I live and work) has an Australian accent. This is due to the "Language Rotor" settings on iOS.

Now, I realize that I'm not blind and the only time I ever need to turn on VoiceOver is when I'm testing the UIAccessibility/NSAccessibility protocol implementations in my applications but whenever I do this on the Mac the voice doesn't sound right.

## 10. Update OpenGL!

Do I need to explain this one?

In iOS, you have access to OpenGL ES 2.0 — the current version of the OpenGL ES standard.

I realize that OpenGL on the Mac is not the OpenGL ES version. I also realize that it's version number is OpenGL 2.1 which is 0.1 higher than the iOS version. Obviously, I'm not suggesting that the Mac adopt exactly the same version of OpenGL that iOS uses.

What I mean is that iOS is using the up-to-date, relevant version of OpenGL whereas the OpenGL 2.1 standard on the Mac was superceeded 2 and a half years ago but Apple have not updated to support it. It is a complete embarrassment to the Mac as a platform. The current version of OpenGL for computers, OpenGL 4.1, was released in July this year. There are already cards available for the Mac that support OpenGL 4.1 on other operating systems but can't due so on the Mac because the OS does not support it.

## 11. Integration between CoreAnimation and standard views

The last two features from iOS I'd like to see both relate to making CALayer-backed views useable by default on the Mac.

Major views should offer animated changes for common actions. If you want to animate a new row into a UITableView on iOS, you only need one line:

```objc
[myTableView
    insertRowsAtIndexPaths:someIndexPath
    withRowAnimation:UITableViewRowAnimationLeft];
```

On the Mac — there certainly isn't a single line option. In fact, there's no easy solution at all, since rows are drawn by NSCell and don't generally have CALayers of their own (even when CoreAnimation is enabled for the NSTableView).

## 12. Fix the horrible text rendering when CoreAnimation is enabled

The following image shows Helvetica Bold 18pt, rendered on the Mac in two different ways.

Both are an NSTextField over a custom drawn gradient but where the top row uses a regular, non-CALayer-backed view, the bottom row uses CALayer-backed views for the entire window.

![](https://www.cocoawithlove.com/assets/objc-era/CoreAnimationText.png)

At first glance, the second row may simply look less fat but if you look closely, you'll see that it is more irregular, less proportionate, badly kerned and far less smooth.

This horrible text rendering affects all text in CALayer-backed views.

On iOS, which always uses CoreAnimation, the text rendering looks very similar to the top example (except that iOS doesn't use sub-pixel antialiasing). Clearly, there is a way to improve the situation with CALayers.

This text quality problem with CoreAnimation has been a burden since CoreAnimation first appeared in Mac OS X 10.5 and it remains the biggest disincentive towards using it on the Mac. It really needs to be addressed.

## Conclusion

These points illustrate my feeling that the Mac Cocoa APIs, AppKit in particular, need some general tidying up (and in some cases, a major refresh) if they are to feel anything other than dated with respect to their iOS equivalents.

While some of these features would be major changes, many simply reflect the fact that AppKit could do with a well-applied coat of paint in many areas. These minor changes can already be addressed by each programmer (a category or a little extra code) but if these sorts of additions are considered commonplace, I think it's an indication that they should be rolled into the default API.

Some of these features might require deprecating major classes in favor of more modern implementations — possibly NSTableView and all NSCells. I wouldn't be sad to see them replaced by something that feels more up-to-date.
