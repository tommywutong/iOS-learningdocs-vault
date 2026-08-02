---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSMultiValueSpecifier.html
archived_at: '2026-07-18T01:51:36.641165Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Radio%20Group%20Element.md)[Previous](Text%20Field%20Element.md)

# Multi Value Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSMultiValueSpecifier` type. When the user taps a preference containing a multi-value element, the Settings app displays a new page with the possible values to choose from. Upon selecting a value, the user is returned to the previous page, and the selected value is displayed in the preference row.

__Table 1__  Keys for the `PSMultiValueSpecifier` dictionary

| Key | Value type | Description |
| `Type` (required) | String | The value of this key is always set to `PSMultiValueSpecifier`.  This key is required. |
| `Title` (required, localizable) | String | The user-readable string identifying the preference.  This key is required. The value of this key is localizable. |
| `Key` (required) | String | The preference key with which to associate the value. This is the string you use this to retrieve the preference value in your code.  This key is required. |
| `DefaultValue` (required) | Any | The default value for the preference key. This value is returned when the specified preferences key (represented by the `Key` entry) is not present in the preferences database.  This key is required. |
| `Values` (required) | Array | An array of the values that could be associated with the preference key (`Key` entry) in the defaults database. These values can be of any type. Each value should have a corresponding value in the `Titles` array. |
| `Titles` (required, localizable) | Array | An array of strings that represent user-readable versions of the values in the `Values` array. These are the strings that are actually displayed on the selection page. When a string is selected, the value at the matching index is stored in the defaults database.  The values in this array are localizable. |
| `ShortTitles` (localizable) | Array | An array of strings that are abbreviated versions of the strings in the `Titles` array. When this key is included, the preference row uses the strings in the corresponding array instead of the strings in the `Titles` array. (The preference row shows the title of the preference and the currently selected value.) The longer strings in the `Titles` array are still displayed in the new page presented to the user.  The values in this array are localizable. This key is available in iOS 5.0 and later. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |
| `DisplaySortedByTitle` | Boolean | If Yes, the values are displayed in the localized sort order of the Titles array.  This key is available in iOS 7.0 and later. |

The `Values` and `Titles` keys let you associate human-readable strings with values in the defaults database that might otherwise be considered cryptic. The number of entries in both arrays must be equal. When a value at a given index is associated with the preference key, the string at the same index in the `Titles` array is displayed for the preference by the Settings app.

[Next](Radio%20Group%20Element.md)[Previous](Text%20Field%20Element.md)

