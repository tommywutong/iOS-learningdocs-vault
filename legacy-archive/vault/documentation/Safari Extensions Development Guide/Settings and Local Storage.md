---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/ExtensionSettings/ExtensionSettings.html
archived_at: '2026-07-27T06:57:07.775774Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Debugging%20Extensions.md)[Previous](Access%20and%20Permissions.md)

# Settings and Local Storage

You can define settings for your extension using Extension Builder. You can choose a type of user interface—such as a checkbox, radio button, text field, or slider—and a default value for each setting. You can choose to make any setting secure (encrypted).

The settings you define appear in your extension’s preference pane, in Safari preferences. Safari handles the user interface, stores the values, and notifies you when a value changes.

There is also an API for accessing your settings programmatically. The API provides for both normal and secure (encrypted) settings. The API is similar to the HTML5 local storage API, but the settings API has an additional feature: support for default values.

You can also make use of HTML5 client-side data storage, commonly referred to as local storage. You can use both Safari settings and HTML5 local storage if you like.

## How to Create User Settings

You create your extension’s user settings and define the user interfaces for them in Extension Builder. Click New Setting Item under Extension Settings to begin.

The extension settings pane expands, as shown in Figure 18-1.

__Figure 18-1__  Settings pane

（原归档配图获取待重试：`extensionSettings.jpg`）

The pane changes depending on the type of setting you choose, but you are usually prompted for a key, a default value, and a title, along with the option of saving the item in secure settings.

The key is the identifier for the item, used in the settings API.

The default value is the initial value for the item when your extension is installed. A default value is optional.

The title is the label the user sees for the setting.

Use the Type pop-up menu to choose the user interface control type. The menu is shown in Figure 18-2.

__Figure 18-2__  Setting types

（原归档配图获取待重试：`settingsTypes.jpg`）

### Hidden Settings

Hidden settings have no title and are not displayed in the extension’s settings pane. They are for your internal settings that you intend to handle programmatically. The reason you might want to define a hidden setting in Extension Builder is to give it a default value.

### Text Field Settings

Text field settings take a string as a value and have the option of being displayed as a password (characters are not visible after entry).

（原归档配图获取待重试：`textField.jpg`）

### Checkbox Settings

A checkbox is true when checked, false when unchecked. But you can assign any pair of values to a checkbox’s two states.

（原归档配图获取待重试：`checkbox.jpg`）

### Slider Settings

Sliders have a minimum value at the far left, a maximum value at the far right, and step value (the smallest change possible for the control).

（原归档配图获取待重试：`slider.jpg`）

### Pop-Up Button Settings

A pop-up button displays the title of the currently selected item. When the user clicks the button, a pop-up menu presents a list of all the items, allowing the user to choose one. The button itself has a title, a key, and a value. The list items have titles and values.

（原归档配图获取待重试：`Pop-upButton.jpg`）

### List Box Settings

List box settings contain a list of items, such a file list. Each item has a title the user sees and a value that the list box returns when that item is chosen. The box itself has a title, a key, and a value. The list items have titles and values.

（原归档配图获取待重试：`listBox.jpg`）

### Radio Buttons Settings

You should have at least two radio buttons for this user interface item to make sense. The user must choose one, but only one, of the radio buttons. Each radio button has a title that the user sees and a value that the button selects for.

（原归档配图获取待重试：`radioButtons.jpg`）

### Groups and Separators

If your user settings should be grouped, enter a group label before each block of settings. This puts a large, bold heading before the group.

If you want to put separators between settings, insert a separator.

## How to Use the Settings API

The display and user interface for settings are managed by Safari. You can use the `SafariExtensionSettings` class to get the current value of a setting before using it. Use in the setting’s key as a property name to get its current value:

`var myVolume = safari.extension.settings.volume`

Whenever a setting is changed, Safari generates a `"change"` event. The event is generated whether the change is made programmatically or by a user. The target of the event is the `settings` or `secureSettings` object.

To find out which value has changed, read the `key` property of the event:

`var mySettingKey = event.key`

The new value and old value of the setting are in the `newValue` and `oldValue` properties of the event.

To be sure you are using the current value of your settings, you must either install an event listener for the `"change"` event in your global page or extension bar, or get the value of your variables directly from the `safari.extension.settings` property immediately before using them.

[Listing 18-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjrfvjvomju) installs a listener function for an extension with only one user setting, whose key is `"volume"`. The function updates a global variable whenever the setting changes.

__Listing 18-1__  Responding to settings changes

```
var myVolume
function volumeChanged {
    if (event.key == "volume") {
        myVolume = event.newValue;
    }
}

safari.extension.settings.addEventListener("change", volumeChanged, false);
```

You can set values programmatically by setting the `safari.extension.settings.`_key_ property to the desired value. For example:

`safari.extension.settings.volume = myVolume`

or:

`safari.extension.secureSettings.volume = myVolume`

## Using HTML5 Local Storage

Safari provides full support for HTML5 client-side storage, both simple local storage of key-value pairs, and the client-side database API that allows you to create persistent relational databases on the client machine.

When used from an injected script, the domain of the local storage is the domain of the webpage the script is injected into. In other words, local data is stored with the webpage’s data.

For injected scripts, the amount of database storage available is set in the user’s security preferences.

You can use client-side databases in your global page or in extension bars as well. When used from a global HTML page or extension bar, the domain of the local storage is the extension. This data belongs to your extension.

__Note:__ Attempting to use local storage to convey data between the global page or an extension bar and full page content does not work. Message passing is the best mechanism for this purpose.

To use client-side databases from your global page or an extension bar, you need to allocate database storage for your extension in the Extension Storage section of Extension Builder, as shown in Figure 18-3.

__Figure 18-3__  Extension storage

（原归档配图获取待重试：`DatabaseQuota.jpg`）

The default storage amount is none. You can choose a value from 1 to 100 megabytes.

__Important:__ If you do not allocate storage in Extension Builder, any call to `openDatabase` from the global page or an extension bar returns `null`.

The local storage API is documented in _[Safari Client-Side Storage and Offline Applications Programming Guide](../iPhone/Safari%20Client-Side%20Storage%20and%20Offline%20Applications%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjw)_.

[Next](Debugging%20Extensions.md)[Previous](Access%20and%20Permissions.md)
