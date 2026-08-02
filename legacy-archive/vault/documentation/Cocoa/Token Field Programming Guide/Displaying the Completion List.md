---
title: Token Field Programming Guide
apple_id: TP40006555
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/DisplayComplList/DisplayComplList.html
archived_at: '2026-07-15T07:20:41.257054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Token Field Programming Guide](Introduction%20to%20Token%20Field%20Programming%20Guide%20for%20Cocoa.md)


[Next](Returning%20Represented%20Objects.md)[Previous](Configuring%20Token%20Fields.md)

# Displaying the Completion List

When the user begins typing in a token field, the control sends (after the specified completion delay) a [tokenField:completionsForSubstring:indexOfToken:indexOfSelectedItem:](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1532474-tokenfield) message to its delegate. The delegate evaluates the passed-in substring for the current token and returns an array of strings that are the possible completions of the substring.

The code in Listing 1 is in an application that makes use of the Scripting Bridge technology (introduced in OS X v10.5) to query the iTunes application for the tracks in the user’s music library. The application stores these tracks (`iTunesTrack` objects) in an instance variable named `trackNames`. The delegate in this method gets the names of all tracks and then uses the `NSArray` method [filteredArrayUsingPredicate:](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered) to narrow this array of track names to those whose initial characters match the passed-in substring.

__Listing 1__  Returning a completion list

```objc
- (NSArray *)tokenField:(NSTokenField *)tokenFieldArg completionsForSubstring:(NSString *)substring indexOfToken:(NSInteger)tokenIndex indexOfSelectedItem:(NSInteger *)selectedIndex {

    NSArray *trackNames = [tracks valueForKey:@"name"];
    NSArray *matchingTracks = [trackNames filteredArrayUsingPredicate:
                 [NSPredicate predicateWithFormat:@"SELF beginswith[cd] %@", substring]];
    return matchingTracks;
}
```

The `selectedIndex` parameter, which is not used in this example, allows the delegate to return a default selection in the completion list.

[Next](Returning%20Represented%20Objects.md)[Previous](Configuring%20Token%20Fields.md)

