---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Tasks/filtering.html
archived_at: '2026-07-15T07:12:16.540199Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Controller%20Key-Value%20Observing%20Compliance.md)[Previous](Implementing%20To-One%20Relationships%20Using%20Pop-Up%20Menus.md)

# Filtering Using a Custom Array Controller

This article explains how to use a search field and custom array controller to filter a collection of objects. Although you typically use a search field in conjunction with a table view to implement this style of interface, the tasks discussed in this article are not limited to these components.

The `arrangeObjects:` method sorts the content of the array controller using the current sort descriptors. To restrict the displayed content to a subset of the content you must override `arrangeObjects:`, create a new array containing the subset, and then call the superclass’s implementation of `arrangeObjects:` to provide any appropriate sorting.

The `arrangeObjects:` implementation in Listing 1 performs an anchored search of the title property. In an anchored search, only those objects whose title property matches `searchString` are added to the returned array.

__Listing 1__  Filtering implementation of arrangeObjects:

```objc
- (NSArray *)arrangeObjects:(NSArray *)objects {

    if (searchString == nil) {
        return [super arrangeObjects:objects];
    }

    NSMutableArray *filteredObjects = [NSMutableArray arrayWithCapacity:[objects count]];
    NSEnumerator *objectsEnumerator = [objects objectEnumerator];
    id item;

    while (item = [objectsEnumerator nextObject]) {
        if ([[item valueForKeyPath:@"title"] rangeOfString:searchString options:NSAnchoredSearch].location != NSNotFound) {
            [filteredObjects addObject:item];
        }
    }
    return [super arrangeObjects:filteredObjects];
}
```


You implement the `search:` action method to invoke `rearrangeObjects`, which triggers the invocation of the `arrangeObjects:` method.

Listing 2 shows an implementation of a search: action. The `searchString` is set to the string value of the `sender` object, and `rearrangeObjects` is called.

__Listing 2__  Updating searchString

```objc
- (void)search:(id)sender {
    // set the search string by getting the stringValue
    // from the sender
    [self setSearchString:[sender stringValue]];
    [self rearrangeObjects];
}


- (void)setSearchString:(NSString *)aString
{
    [aString retain];
    [searchString release];
    searchString=aString;
}

@end
```

The `search:` action is invoked by an NSSearchField. The target of the search field is set to the array controller, and the action to the `search:` method. The search field should be configured so that it does not send the whole string as it changes. Turning this option off causes the `search:` method to be invoked each time that a keystroke occurs in the search field.

[Next](Controller%20Key-Value%20Observing%20Compliance.md)[Previous](Implementing%20To-One%20Relationships%20Using%20Pop-Up%20Menus.md)

