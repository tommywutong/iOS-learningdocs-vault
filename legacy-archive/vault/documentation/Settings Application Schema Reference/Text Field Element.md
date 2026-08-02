---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSTextFieldSpecifier.html
archived_at: '2026-07-18T01:51:36.954113Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Multi%20Value%20Element.md)[Previous](Title%20Element.md)

# Text Field Element

Table 1 lists the keys that may be placed in a dictionary that is associated with the `PSTextFieldSpecifier` type.

__Table 1__  Keys for the `PSTextFieldSpecifier` dictionary

| Key | Value type | Value |
| `Type` (required) | String | The value of this key is always set to `PSTextFieldSpecifier`.  This key is required. |
| `Title` (localizable) | String | The string displayed to the left of the text field’s value. This string is drawn left aligned and in bold face. If you omit this key, the editable text field spans the width of the row.  The value of this key is localizable. |
| `Key` (required) | String | The preference key with which to associate the value. This is the string you use this to retrieve the preference value in your code.  This key is required. |
| `DefaultValue` | String | The default value for the preference key. This value is returned when the specified preferences key (represented by the `Key` entry) is not present in the preferences database. If this key is not present, an empty string is associated with the key. |
| `IsSecure` | Boolean | If Yes, the text field is a password-entry text field, which replaces the typed text with bullet characters. If No, the text field is a standard text field that displays the typed text. If this key is not present, the default is No. |
| `KeyboardType` | String | The type of keyboard to display to the user. This value must contain one of the following strings: `Alphabet` , `NumbersAndPunctuation` , `NumberPad` , `URL` , `EmailAddress`.  If this key is not present, the default value is `Alphabet`. |
| `AutocapitalizationType` | String | The auto-capitalization style to apply to typed text. This value must contain one of the following strings: `None` , `Sentences` , `Words` , `AllCharacters`.  If this key is not present, the default value is `None`. |
| `AutocorrectionType` | String | The auto-correction style to apply when typing. This value must contain one of the following strings: `Default` , `No` , `Yes`.  If this key is not present, the default value is `Default`. |
| `SupportedUserInterfaceIdioms` | Array | Indicates that the element is displayed only on specific types of devices. The value of this key is an array of strings with the supported idioms. Include the string “Phone” to display the element on iPhone and iPod touch. Include the string to “Pad” to display it on iPad.  This key is available in iOS 4.2 and later. |

For more information about the keyboards, auto-capitalization, and auto-correction options used by text fields, see the constants defined in _UITextInputTraits Protocol Reference_.

[Next](Multi%20Value%20Element.md)[Previous](Title%20Element.md)

