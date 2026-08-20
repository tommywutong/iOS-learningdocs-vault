---
title: Search Fields
apple_id: 10000168i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/Articles/ConfiguringTargetAction.html
archived_at: '2026-07-15T07:18:55.644863Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Search Fields](Introduction%20to%20Search%20Fields.md)


[Next](Customizing%20Your%20Search%20Field%E2%80%99s%20Appearance.md)[Previous](Configuring%20a%20Search%20Menu.md)

# Implementing the Target

A search field is a control object and so uses the [target-action](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/TargetAction.html#//apple_ref/doc/uid/TP40009448-CH3) pattern: when a user does something to activate the search field, it sends an action message to a target object telling it to perform the search. Other than invoking the action method, `NSSearchFieldCell` and `NSSearchField` provide no support for textual searches. You must implement the search behavior yourself.

Typically you implement the action method in a controller object in your application. You need to find out what the search string is and then perform the search using the search term, as illustrated in Listing 1.

__Listing 1__  Simple action method for a search field’s target

```objc
- (IBAction)updateFilter:(id)sender {

    NSString *searchString = [searchField stringValue];
    /*
     Method continues to perform the search and display the results.
     */
}
```


If you want to support search categories (see [Specifying a Search Category](Configuring%20a%20Search%20Menu.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dkljxgy4dcoa)), you have to implement the action method invoked by the category menu items as well as that invoke by the search field itself. Your category action method should record in some way the menu item that was selected (typically by remembering the item’s tag). You might also set the placeholder string for the search menu (typically to the menu item’s title, to remind the user which item they chose), as illustrated in Listing 2.

__Listing 2__  Example search category menu item action method

```objc
- (IBAction)setSearchCategoryFrom:(NSMenuItem *)menuItem {

    self.searchCategory = [menuItem tag];
    [[self.searchField cell] setPlaceholderString:[menuItem title]];
}
```

In the search field’s action method, you need to find out what the search string is and then perform the search using the search term, taking into account any category that might have been set. A common way to represent the search is as an instance of [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate). In Listing 3, `searchCategory` is set in the `setSearchCategoryFrom:` method illustrated in Listing 2.

__Listing 3__  Example action method for a search field’s target

```objc
- (IBAction)updateFilter:(id)sender {
    /*
     Create a predicate based on what is the current string in the
     search field and the value of searchCategory.
     */
    NSString *searchString = [self.searchField stringValue];
    NSPredicate *predicate;

    if ((searchString != nil) && (![searchString isEqualToString:@""])) {
        if (searchCategory == 1) {
            predicate = [NSPredicate predicateWithFormat:
                                     @"firstName contains[cd] %@", searchString];
        }
        if (searchCategory == 2) {
            predicate = [NSPredicate predicateWithFormat:
                                     @"lastName contains[cd] %@", searchString];
        }
    }

    /*
     Method continues to perform the search and display the results.
     */
}
```


Clicking the cancel button behaves exactly as if the user selected all the text in the field and deleted it. The action message is sent to the target as usual. The target would typically see that the string in the field is the empty string, and so wouldn't filter anything.

[Next](Customizing%20Your%20Search%20Field%E2%80%99s%20Appearance.md)[Previous](Configuring%20a%20Search%20Menu.md)

