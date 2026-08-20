---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/RadioGroupElement.html
archived_at: '2026-07-18T01:51:37.030410Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Multi%20Value%20Element.md)

# Radio Group Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSRadioGroupSpecifier` type. This type defines a radio group element, which provides two or more choices of which only one at a time can be selected.

__Table 1__  Keys for the `PSRadioGroupSpecifier` dictionary

| Key | Value type | Value |
| `Type` (required) | String | The value of this key is always set to `PSRadioGroupSpecifier`. This key is required. |
| `Title` (localizable) | String | The title of the group. If you do not specify this key, a gap is inserted between preferences. The value of this key is localizable. |
| `FooterText` (localizable) | String | Additional text to display below the group box. Providing a footer is optional. The value of this key is localizable. |
| `Key` (required) | String | The preference key with which to associate the value. This is the string you use to retrieve the preference value in your code.  This key is required. |
| `DefaultValue` (required) | Any | The default value for the preference key. This value is returned when the specified preferences key (represented by the `Key` entry) is not present in the preferences database.  This key is required. |
| `Values` (required) | Array | An array of the values that could be associated with the preference key (`Key` entry) in the defaults database. These values can be of any type. Each value should have a corresponding value in the `Titles` array. |
| `Titles` (required, localizable) | Array | An array of strings that represent user-readable versions of the values in the `Values` array. These are the strings that are actually displayed on the selection page. When a string is selected, the value at the matching index is stored in the defaults database.  The values in this array are localizable. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |
| `DisplaySortedByTitle` | Boolean | If Yes, the values are displayed in the localized sort order of the Titles array.  This key is available in iOS 7.0 and later. |

[Next](Document%20Revision%20History.md)[Previous](Multi%20Value%20Element.md)

