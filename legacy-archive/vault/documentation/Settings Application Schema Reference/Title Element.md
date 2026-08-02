---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSTitleValueSpecifier.html
archived_at: '2026-07-18T01:51:36.976852Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Text%20Field%20Element.md)[Previous](Slider%20Element.md)

# Title Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSTitleValueSpecifier` type. This element represents a read-only preference. You can use it to provide the user with information about your app’s configuration.

__Table 1__  Keys for the `PSTitleValueSpecifier` type

| Key | Value type | Description |
| `Type` (required) | String | The value of this key is always set to `PSTitleValueSpecifier`.  This key is required. |
| `Title` (localizable) | String | The string displayed to the left of the value.  The value of this key is localizable. |
| `Key` (required) | String | The preference key identifying the value. This is the string you use this to retrieve the preference value from the defaults database.  This key is required. |
| `DefaultValue` (required) | String | The default value for the preference key. This value is returned when the specified preferences key (represented by the `Key` entry) is not present in the preferences database.  This key is required. |
| `Values` | Array | An array of the values that could be associated with the preference key (`Key` entry) in the defaults database. These values can be of any type. Each value should have a corresponding value in the `Titles` array. |
| `Titles` (localizable) | Array | An array of strings that represent user-readable versions of the values in the `Values` array.  The values in this array are localizable. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |

The `Values` and `Titles` keys let you associate human-readable strings with values in the defaults database that might otherwise be considered cryptic. The number of entries in both arrays must be equal. When a value at a given index is associated with the preference key, the string at the same index in the `Titles` array is displayed for the preference by the Settings app.

[Next](Text%20Field%20Element.md)[Previous](Slider%20Element.md)

