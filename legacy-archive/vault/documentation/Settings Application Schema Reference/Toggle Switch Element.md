---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSToggleSwitchSpecifier.html
archived_at: '2026-07-18T01:51:37.002009Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Slider%20Element.md)[Previous](Child%20Pane%20Element.md)

# Toggle Switch Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSToggleSwitchSpecifier` type. This element displays an ON/OFF button that can be toggled by the user.

__Table 1__  Keys for the `PSToggleSwitchSpecifier` dictionary

| Key | Value type | Value |
| `Type` (required) | String | The value of this key is always set to `PSToggleSwitchSpecifier`.  This key is required. |
| `Title` (required, localizable) | String | The string displayed to the left of the switch.  This key is required. The value of this key is localizable. |
| `Key` (required) | String | The preference key identifying the value. This is the string you use this to retrieve the preference value from the defaults database.  This key is required. |
| `DefaultValue` (required) | Any | The default value for the preference key. This value is returned when the specified preferences key (represented by the `Key` entry) is not present in the defaults database.  This key is required. |
| `TrueValue` | Any | The value associated with the preference when the toggle switch is in the ON position. The value type for this key can be any scalar type, including Boolean, String, Number, Date, or Data. If this key is not present, the default value type is a Boolean with the value Yes. |
| `FalseValue` | Any | The value associated with the preference when the toggle switch is in the OFF position. The value type for this key can be any scalar type, including Boolean, String, Number, Date, or Data. If this key is not present, the default value type is a Boolean with the value No. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |

[Next](Slider%20Element.md)[Previous](Child%20Pane%20Element.md)

