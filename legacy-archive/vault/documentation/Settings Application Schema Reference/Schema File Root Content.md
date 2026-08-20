---
title: Settings Application Schema Reference
apple_id: TP40007071
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Data Management
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/RootContent.html
archived_at: '2026-07-18T01:51:37.173112Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Settings Application Schema Reference](Introduction.md)


[Next](Group%20Element.md)[Previous](Introduction.md)

# Schema File Root Content

Each distinct settings screen is represented by a property-list file. At a minimum, a settings bundle must have a `Root.plist` file containing the contents of the main settings screen. Additional property-list files may be created and used to display preferences in child screens, which are accessed using a child pane element. Each property list file contains several keys (listed in Table 1) at the top level that provide basic information.

__Table 1__  Root-level keys of a preferences schema

| Key | Type | Value |
| `PreferenceSpecifiers` (required) | Array | An array of dictionaries, each of which contains the data for a single preference element. The order of the elements in the array defines the order that they are displayed on the screen. |
| `StringsTable` | String | The name of the strings file associated with this schema file. A copy of this file (with appropriate localized strings) should be located in each of your bundle’s language-specific project directories. If you do not include this key, the strings in this schema file are not localized. For information on creating strings files, see _[Internationalization and Localization Guide](../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_. |
| `ApplicationGroupContainerIdentifier` | String | The app group identifier to use for storing preference values. Specify this key when you want preferences to be stored in a container other than the one used by your iOS app. For example, specify this key when creating a WatchKit settings bundle so that the WatchKit extension can access the preferences.  Enable the App Groups capability for each executable that needs to access the shared preferences. The group you select should match the value of this key. To access preferences stored in the group, pass the value of this key to the [initWithSuiteName:](https://developer.apple.com/documentation/foundation/userdefaults/1409957-init) method of your `NSUserDefaults` object.  This key is supported in iOS 8.2 and later. |

The title string that appears at the top of each settings screen is derived from an external source. In the case of your app’s root settings screen, the title string is the app name itself. For child settings screens, the title is taken from the Title key of the child pane element used to display that screen. For more information about this key, see [Child Pane Element](Child%20Pane%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjxfvjvomi).

Each dictionary in the `PreferenceSpecifiers` key contains the keys associated with a preferences element. Table 2 lists the element types that are supported.

__Table 2__  Element types contained in the `PreferenceSpecifiers` key

| Element Type | Description |
| `PSTextFieldSpecifier` | A text field preference. This element displays an optional title and an editable text field. You can use this type for preferences that require the user to specify a custom string value. For more information, see [Text Field Element](Text%20Field%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjrfvjvomi). |
| `PSTitleValueSpecifier` | A read-only string preference. You can use this type to display preference values as formatted strings. For more information, see [Title Element](Title%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjvfvjvomi). |
| `PSToggleSwitchSpecifier` | A toggle switch preference. You can use this type to configure a preference that can have only one of two values. Although you typically use this type to represent preferences containing Boolean values, you can also use it with preferences containing non-Boolean values. For more information, see [Toggle Switch Element](Toggle%20Switch%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjsfvjvomi). |
| `PSSliderSpecifier` | A slider preference. You can use this type for a preference that represents a range of values. The value for this type is a real number whose minimum and maximum you specify. For more information, see [Slider Element](Slider%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjtfvjvomi). |
| `PSMultiValueSpecifier` | A multi-value preference. You can use this type for a preference that supports a set of mutually exclusive values. For more information, see [Multi Value Element](Multi%20Value%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjwfvjvomi). |
| `PSRadioGroupSpecifier` | A group item preference used for selecting one item in the group. This type represents a single configurable option with two or more values. For more information, see [Radio Group Element](Radio%20Group%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbzge2tcojwfvjvomq). |
| `PSGroupSpecifier` | A group item preference. The group type is a way for you to organize groups of preferences on a single page. The group type does not represent a configurable preference. For more information, see [Group Element](Group%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tambzfvjvomi). |
| `PSChildPaneSpecifier` | A child pane preference. You can use this type to link to a new page of preferences. For more information, see [Child Pane Element](Child%20Pane%20Element.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tamjxfvjvomi). |

[Next](Group%20Element.md)[Previous](Introduction.md)

