---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSSliderSpecifier.html
archived_at: '2026-07-18T01:51:36.852308Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Title%20Element.md)[Previous](Toggle%20Switch%20Element.md)

# Slider Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSSliderSpecifier` type. This element displays a slider that you can use to specify a continuous range of values for the user.

__Table 1__  Keys for the `PSSliderSpecifier` dictionary

| Key | Value type | Value |
| `Type` | String | The value of this key is always set to `PSSliderSpecifier`.  This key is required. |
| `Key` (required) | String | The preference key identifying the value. This is the string you use this to retrieve the preference value from the defaults database.  This key is required. |
| `DefaultValue` (required) | Real | The default value for the preference key. This value is returned when the specified preferences key (represented by the `Key` entry) is not present in the preferences database.  This key is required. |
| `MinimumValue` (required) | Real | The minimum value for the slider.  This key is required. |
| `MaximumValue` (required) | Real | The maximum value for the slider.  This key is required. |
| `MinimumValueImage` | String | The image to display on the side of the slider representing the minimum value. This image should be 21 by 21 pixels. |
| `MaximumValueImage` | String | The image to display on the side of the slider representing the maximum value. This image should be 21 by 21 pixels. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |

[Next](Title%20Element.md)[Previous](Toggle%20Switch%20Element.md)

