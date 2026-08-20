---
title: Token Field Programming Guide
apple_id: TP40006555
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/GetSetTokenFields/GetSetTokenFields.html
archived_at: '2026-07-15T07:20:41.263435Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Token Field Programming Guide](Introduction%20to%20Token%20Field%20Programming%20Guide%20for%20Cocoa.md)


[Next](Implementing%20Menus%20for%20Tokens.md)[Previous](Returning%20Represented%20Objects.md)

# Getting and Setting Token-Field Values

To retrieve the objects represented by the tokens in a token field, send the token field an [objectValue](https://developer.apple.com/documentation/appkit/nscontrol/1428849-objectvalue) message. Although this method is declared by `NSControl`, [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield) implements it to return an array of represented objects. If the token field simply contains a series of strings, `objectValue` returns an array of strings. To set the represented objects of a token field, use the [setObjectValue:](https://developer.apple.com/documentation/appkit/nscontrol/1428849-objectvalue) method, passing in an array of represented objects. If these objects aren’t strings, `NSTokenField` then queries its delegate for the display strings to use for each token.

A common place to call `objectValue` is in an action method. Listing 1 gives an example of such a method.

__Listing 1__  Getting and setting the contents of a token filed

```objc
- (IBAction)addToPlaylist:(id)sender { // sender is token field
    // add songs to playlist, select first one added
    NSIndexSet *curSongIndex = [NSIndexSet indexSetWithIndex:(NSUInteger)[currentList count]];
    [currentList addObjectsFromArray:[sender objectValue]];
    [songTable reloadData];
    [songTable selectRowIndexes:curSongIndex byExtendingSelection:NO];
    [sender setObjectValue:nil];

}
```

Note that this method clears the token field by setting its object value to `nil`.

[Next](Implementing%20Menus%20for%20Tokens.md)[Previous](Returning%20Represented%20Objects.md)

