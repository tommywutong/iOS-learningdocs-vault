---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSGroupSpecifier.html
archived_at: '2026-07-18T01:51:36.604530Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Child%20Pane%20Element.md)[Previous](Schema%20File%20Root%20Content.md)

# Group Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSGroupSpecifier` type. This type defines a group element, which is a way to visually group preferences on a page. This element should be placed in front of the preferences associated with the group. You can assign a title to the group or omit the key to display a gap between preferences.

__Table 1__  Keys for the `PSGroupSpecifier` dictionary

| Key | Value type | Value |
| `Type` (required) | String | The value of this key is always set to `PSGroupSpecifier`. This key is required. |
| `Title` (localizable) | String | The title of the group. If you do not specify this key, a gap is inserted between preferences. The value of this key is localizable. |
| `FooterText` (localizable) | String | Additional text to display below the group box. Providing a footer is optional. The value of this key is localizable. On tvOS, the additional text is limited to 5 lines.  This key is available in iOS 4.0 and later. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |

[Next](Child%20Pane%20Element.md)[Previous](Schema%20File%20Root%20Content.md)

