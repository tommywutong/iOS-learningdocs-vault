---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/Localization.html
archived_at: '2026-07-15T05:17:29.787475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Specifying%20Access%20Keys.md)[Previous](Dragging%20and%20Dropping.md)

# Localizing Widgets

Localizing your widget provides a more comfortable and pleasant experience for foreign language speakers. If your widget is used in areas where languages other than English are spoken, you should localize it.

There are two sides to localizing your widget:

- What Dashboard does for you
- What you need to provide Dashboard

In addition to localizing your content, this chapter covers how to localize your widget’s name in the Finder and the widget bar.

Before talking about localizing a Dashboard widget, you should be familiar with how OS X handles localization. For most applications on OS X, localized resources such as images, strings, and nib files exist within the application’s bundle in `Contents/Resources/`. Each language gets its own directory, named after the language whose resources it holds. The names and location within the bundle are strict, as OS X is expecting them to be there if a localization is requested. These folders are called _language project directories_ and always end in the extension `.lproj`.

When an application is launched, the executable asks OS X for certain localized resources. When this happens, OS X looks for a language project within the application’s bundle that corresponds with the first entry in the language precedence list, as set in System Preferences. If no language project for the preferred language is found, OS X looks for a language project corresponding to the next language in the precedence list, and so on. Note that this process is mostly automatic, in that the application doesn’t do any of the actual searching for language projects; it simply requests resources and OS X provides them.

More on changing language and local preferences can be found in Language and Local Preferences.

Widgets running within Dashboard use a similar process as Mac apps when trying to load resources. Any time a resource load occurs in your code, Dashboard first looks for it within the language project directories in the Widget bundle. If Dashboard finds the resource within that language project directory, it provides it back to the widget. If not, searches through the rest of the language project directories, based on the precedence set in System Preferences. Finally, if the resource is not found in any language projects, Dashboard looks relative to the root level of the bundle.

Dashboard will look for localized resources in the following contexts:

- Any time the `@import` directive is used
- Any time the `src` attribute is used, including (but not limited to):
- - `<script src='myLogic.js' />`
  - `<img src="myImage.png">`
- Any other resource load targeted within your widget bundle

When localizing your widget, provide Dashboard with localized versions of your resources. These include, but are not limited to, any strings that your widgets displays, images that change based on a language or region, and language-specific layouts. If you import a style sheet into your widget instead of including it in your HTML file, you’ll be able to provide localized style sheets as well.

Each language you localize your widget into needs its own language project directory. In it you place all of the localized resources for that language. Each language project directory needs to be located at the root level of your widget. [Table 16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbxfvjvomi) lists of common languages and their corresponding language project directory names:

__Table 16__  Common languages and corresponding language project names

| Language | Language project directory name |
| Chinese (Simplified) | `zh-Hans.lproj` |
| Chinese (Traditional) | `zh-Hant.lproj` |
| Danish | `da.lproj` |
| Dutch | `nl.lproj` |
| English | `en.lproj` |
| Finnish | `fi.lproj` |
| French | `fr.lproj` |
| German | `de.lproj` |
| Italian | `it.lproj` |
| Japanese | `ja.lproj` |
| Korean | `ko.lproj` |
| Norwegian | `nb.lproj` |
| Portuguese | `pt.lproj` |
| Swedish | `sv.lproj` |
| Spanish | `es.lproj` |

Note that these are just some of the possible localizations available. OS X and Dashboard support many more languages and locals. Language and Locale Designations discusses language project directory naming conventions used for localizing applications on OS X.

An example for widget localization is to have all of your widget’s strings localized. In each localized strings file, you provide an array of strings whose index is a variable common to all of the localized string files. You then include that file in your HTML file, and when you need a string, you simply retrieve it from the array.

The first step to implementing this scheme is to have a uniformly named file containing the strings inside of properly named language project directories. For example, having a file named `LocalizedStrings.js` inside each of your language project directories. The file looks like this for the German localization:

```
var localizedStrings = new Array;

localizedStrings['Hello, World!'] = 'Hallo, Welt!';
localizedStrings['Default'] = 'German';
```

Notice that the index into the `localizedStrings` array is a string. This is useful when combined with an accessor method that tries to retrieve the localized string:

```
function getLocalizedString (key)
{
    try {
        var ret = localizedStrings[key];
        if (ret === undefined)
            ret = key;
        return ret;
    } catch (ex) {}

    return key;
}
```

The advantages to this are twofold: first, the index for a string is memorable, and secondly, if the string retrieval fails, the key string is returned. This way, you are assured that some string will always be returned, no matter the circumstances. This is especially valuable when you are testing your widget in Safari.

Finally, you’ll need to use the localized string in your widget. This code ties together all of these previous concepts and inserts the string into your widget:

```
function setup()
{

    document.getElementById('helloText').innerText = getLocalizedString('Hello, World!');
    document.getElementById('language').innerText = getLocalizedString('Default');
}
```

Since the proper localized strings file is already loaded, this will fetch the localized equivalent of "Hello, World!" in the `localizedStrings` array and placing it in your layout.

In addition to localizing the content of your widget, you should localize your widget’s name. The name is displayed in the Finder and the widget bar and is pulled from your `Info.plist` information property list file and localized `InfoPlist.strings` files.

In your Info.plist, you need to specify the key `CFBundleDisplayName` and provide a corresponding value:

```
<key>CFBundleDisplayName</key>
<string>Hello World</string>
```

This value is a default value that’s used if no localized string can be found. It also needs to be the name of your widget on disk, without the `.wdgt` file extension. Inside of each language project directory in your widget, place a file named `InfoPlist.strings` and in it provide the proper localized name using this format:

```
CFBundleDisplayName = "Hallo Welt";
```

For a more in-depth look at using `CFBundleDisplayName`, read _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_.

[Next](Specifying%20Access%20Keys.md)[Previous](Dragging%20and%20Dropping.md)

