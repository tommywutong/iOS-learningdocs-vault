---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSChildPaneSpecifier.html
archived_at: '2026-07-18T01:51:36.493866Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Toggle%20Switch%20Element.md)[Previous](Group%20Element.md)

# Child Pane Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSChildPaneSpecifier` type. This element displays a preferences row, that when tapped loads a new page of preferences. You can use this element type to build hierarchical pages of preferences.

__Table 1__  Keys for the `PSChildPaneSpecifier` dictionary

| Key | Type | Value |
| `Type` (required) | String | The value of this key is always set to `PSChildPaneSpecifier`.  This key is required. |
| `Title` (required, localizable) | String | The title string displayed in the preference row. This is the string the user taps to display the next page. This string is also used as the title of the screen that is subsequently displayed.  This key is required. The value of this key is localizable. |
| `File` (required) | String | The name of the schema file to load. (This file must be a property list file.) The string you specify for this key should not contain path information or the `.plist` filename extension of your schema file. The Settings app looks in the top-level of your settings bundle for a `.plist` file with the specified name. For example, if you had a `MyPrefs.plist` file, you would assign the value `MyPrefs` to this key. This key is required. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |

[Next](Toggle%20Switch%20Element.md)[Previous](Group%20Element.md)

