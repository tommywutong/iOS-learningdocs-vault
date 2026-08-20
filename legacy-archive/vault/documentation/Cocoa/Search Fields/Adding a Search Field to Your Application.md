---
title: Search Fields
apple_id: 10000168i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/Articles/AddingSearchField.html
archived_at: '2026-07-15T07:18:55.046448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Search Fields](Introduction%20to%20Search%20Fields.md)


[Next](Configuring%20a%20Search%20Menu.md)[Previous](Introduction%20to%20Search%20Fields.md)

# Adding a Search Field to Your Application

You can create a search field programatically, but the easiest way to add a search field to your application is to create it in a xib file in Xcode. Simply drag a search field from the Controls library and add it to a window.

In Xcode, you can use the Attributes Inspector to set search-field-specific attributes:

- _Autosave Name_, which if set, the recent search list is saved to an application preference using the name provided, and restored the next time the recents list is needed for the popup menu. You can also programmatically send the `setRecentsAutosaveName:` message. Setting the autosave name to `nil` does not clear out any saved lists. Setting the autosave name to a valid string discards any current recents and loads the recents from the user defaults.
- _Recents_, which specifies the maximum number of recent searches to show in the recents menu. You can also programmatically send the `setMaximumRecents:` message to the search field’s cell.
- _Behavior_, which specifies whether the search field sends the action message when the user presses the Return key and if it sends the message upon each keystroke (incremental search). You can also programmatically send the `setSendsWholeSearchString:` message to the search field’s cell.

You can also set other attributes inherited from `NSSearchField`’s superclasses, such as:

- _Placeholder_, which specifies text that appears in the search field until the user enters text. You can also programmatically send the `setPlaceholderString:` message to the search field’s cell.

Unless you’re using the Cocoa bindings `Predicate` binding, you need to set the target and action of the search field (for more details see [Implementing the Target](Implementing%20the%20Target.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga3tglkdjjbeuqsfivbq)). You can also connect a search field to a menu template. The details of the menu’s contents are described in [Configuring a Search Menu](Configuring%20a%20Search%20Menu.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dklkcifbemskcjfaq).

[Next](Configuring%20a%20Search%20Menu.md)[Previous](Introduction%20to%20Search%20Fields.md)

