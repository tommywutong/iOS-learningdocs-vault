---
title: Search Fields
apple_id: 10000168i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/Articles/MenuTemplate.html
archived_at: '2026-07-15T07:18:56.616397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Search Fields](Introduction%20to%20Search%20Fields.md)


[Next](Implementing%20the%20Target.md)[Previous](Adding%20a%20Search%20Field%20to%20Your%20Application.md)

# Configuring a Search Menu

A search field has a menu that users can access by clicking the small triangle next to the search button. The items in this pop-up icon menu have two purposes: To list recently entered search strings, and to list search categories for limiting the scope of the search. You can also specify _when_ the search field sends its action message.

A search field has two modes for generating action messages:

- The first mode is similar to a text field; a message is sent when a user clicks the search button or presses Return when the insertion point is in the search field.
- The second mode, which is the default, is for incremental searches; the search field sends an action message at each keystroke.

Typically you set the mode in a xib file (see [Adding a Search Field to Your Application](Adding%20a%20Search%20Field%20to%20Your%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dilkcifbemskcjfaq)). To set the message-generation mode programmatically, send [setSendsWholeSearchString:](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399453-sendswholesearchstring) to the search field cell with an argument of `NO` for incremental searches and `YES` for regular searches.

If you specify a menu, the search button displays a menu indicator and the search menu pops up when the user clicks the search button. Do not modify the menu while it is in use by the search field (because the search field does not make a copy of the menu).

To configure the pop-up menu, create a menu template (which is an `NSMenu` object) and populate the menu template with the items (`NSMenuItem` objects) you want to appear. You can add pre-defined items to the menu by creating a menu item and setting its tag to one of the following values (described in the Constants section of the [NSSearchFieldCell](https://developer.apple.com/documentation/appkit/nssearchfieldcell) reference):

- [NSSearchFieldRecentsTitleMenuItemTag](https://developer.apple.com/documentation/appkit/nssearchfield/1399465-recentstitlemenuitemtag): specifies the menu item that is the title of the menu group for recent search strings (the item is hidden if there are no recent strings);
- [NSSearchFieldRecentsMenuItemTag](https://developer.apple.com/documentation/appkit/nssearchfieldrecentsmenuitemtag): identifies where recent search strings should appear in the “recents” menu group (the item is hidden if there are no recent strings);
- [NSSearchFieldClearRecentsMenuItemTag](https://developer.apple.com/documentation/appkit/nssearchfield/1399438-clearrecentsmenuitemtag): specifies a menu item used to clear existing recent items;
- [NSSearchFieldNoRecentsMenuItemTag](https://developer.apple.com/documentation/appkit/nssearchfield/1399459-norecentsmenuitemtag): the menu item that describes a lack of recent search strings (for example, “No recent searches”).

You can specify the menu template used when generating the pop-up menu in the search field. This is easily done with Xcode, or, if you have programmatically constructed the menu template, invoke `setSearchMenuTemplate:` to install it in the search field.

You can also do all of this programatically. Listing 1 illustrates how you might set up the search menu template.

__Listing 1__  Setting the menu template for recent search strings

```objc
- (void) awakeFromNib
{
    NSMenu *cellMenu = [[NSMenu alloc] initWithTitle:NSLocalizedString(@"Search Menu", @"Search Menu title")];
    NSMenuItem *item;

    item = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Clear", @"Clear menu title")
                               action:NULL keyEquivalent:@""];
    [item setTag:NSSearchFieldClearRecentsMenuItemTag];
    [cellMenu insertItem:item atIndex:0];

    item = [NSMenuItem separatorItem];
    [item setTag:NSSearchFieldRecentsTitleMenuItemTag];
    [cellMenu insertItem:item atIndex:1];

    item = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Recent Searches", @"Recent Searches menu title")
                               action:NULL keyEquivalent:@""];
    [item setTag:NSSearchFieldRecentsTitleMenuItemTag];
    [cellMenu insertItem:item atIndex:2];

    item = [[NSMenuItem alloc] initWithTitle:@"Recents"
                                action:NULL keyEquivalent:@""];
    [item setTag:NSSearchFieldRecentsMenuItemTag];
    [cellMenu insertItem:item atIndex:3];

    id searchCell = [searchField cell];
    [searchCell setSearchMenuTemplate:cellMenu];
}
```

A menu is associated with your search field only if you specify one in a xib file. If you are creating the search field programatically and do not want a menu, set the menu template to `nil`.

To set up a search category, you create a menu item with a title and an action selector and add it to the menu template. The action selector identifies the method that is invoked using [target-action](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/TargetAction.html#//apple_ref/doc/uid/TP40009448-CH3) when the user selects the item; in this method you can set a flag or other value so that your search implementation knows how to limit the scope of its search. Typically you would add the menu item to the menu template in the xib file. You can also do it programmatically, as illustrated in Listing 2. This is useful if you create or update the menu dynamically, for example if the categories depend on what table columns are visible in a table view.

__Listing 2__  Setting the menu template with a search category

```objc
- (void) awakeFromNib
{
    NSMenu *cellMenu = [[NSMenu alloc] initWithTitle:NSLocalizedString(@"Search Menu", @"Search Menu title")];
    NSMenuItem *item;

    item = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"First Name", @"First Name menu title")
                               action:@selector(setSearchCategoryFrom:) keyEquivalent:@""];
    [item setTarget:self];
    [item setTag:1];
    [cellMenu insertItem:item atIndex:0];

    item = [[NSMenuItem alloc] initWithTitle:NSLocalizedString(@"Last Name", @"Last Name menu title")
                               action:@selector(setSearchCategoryFrom:) keyEquivalent:@""];
    [item setTarget:self];
    [item setTag:2];
    [cellMenu insertItem:item atIndex:1];

    id searchCell = [searchField cell];
    [searchCell setSearchMenuTemplate:cellMenu];
}
```

Tags are optional for search categories, but they allow you to easily discriminate between menu items in the action method. If you choose to specify tags, their values must not be the same as any of the values of `NSSearchFieldRecentsTitleMenuItemTag`, `NSSearchFieldRecentsMenuItemTag`, `NSSearchFieldClearRecentsMenuItemTag`, or `NSSearchFieldNoRecentsMenuItemTag`.

You also have to implement the action method invoked by the menu item—see [Search Using a Search Category](Implementing%20the%20Target.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga3tglktk42q).

[Next](Implementing%20the%20Target.md)[Previous](Adding%20a%20Search%20Field%20to%20Your%20Application.md)

