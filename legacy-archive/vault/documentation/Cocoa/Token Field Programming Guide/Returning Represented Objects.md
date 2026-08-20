---
title: Token Field Programming Guide
apple_id: TP40006555
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/ReturnRepObjects/ReturnRepObjects.html
archived_at: '2026-07-15T07:20:41.749706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Token Field Programming Guide](Introduction%20to%20Token%20Field%20Programming%20Guide%20for%20Cocoa.md)


[Next](Getting%20and%20Setting%20Token-Field%20Values.md)[Previous](Displaying%20the%20Completion%20List.md)

# Returning Represented Objects

When the user enters a string and presses a tokenizing character, the token field sends the [tokenField:representedObjectForEditingString:](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1527909-tokenfield) message to its delegate. This message asks the delegate to return a represented object for the entered token string (the `editingString` parameter in Listing 1). In this example, the delegate finds and returns the `iTunesTrack` object with the name matching `editingString`.

__Listing 1__  Returning represented objects for tokens

```objc
- (id)tokenField:(NSTokenField *)tokenField representedObjectForEditingString: (NSString *)editingString {
    iTunesTrack *track = [tracks objectWithName:editingString];
    if ([track exists])
        return track;
    return nil;
}
```

If the delegate returns `nil`, no represented objects are associated with the token string. Otherwise, the token field queries its delegate for the display string to use for each token by invoking the [tokenField:displayStringForRepresentedObject:](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1526020-tokenfield) method. Listing 2 shows an implementation of this delegation method.

__Listing 2__  Returning the display string for a represented object

```objc
- (NSString *)tokenField:(NSTokenField *)tokenFieldArg displayStringForRepresentedObject:(id)representedObject {     return [representedObject name]; }
```

[Next](Getting%20and%20Setting%20Token-Field%20Values.md)[Previous](Displaying%20the%20Completion%20List.md)

