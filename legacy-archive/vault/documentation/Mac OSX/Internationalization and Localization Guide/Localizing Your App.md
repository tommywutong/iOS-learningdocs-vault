---
title: Internationalization and Localization Guide
apple_id: 10000171i
resource_type: Guide
platform: iOS|Xcode Developer Tools|macOS
topic: User Experience
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LocalizingYourApp/LocalizingYourApp.html
archived_at: '2026-07-15T08:15:59.083448Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Internationalization and Localization Guide](About%20Internationalization%20and%20Localization.md)


[Next](Testing%20Your%20Internationalized%20App.md)[Previous](Supporting%20Right-to-Left%20Languages.md)

# Localizing Your App

When you are done internationalizing the app’s user interface and code, begin the localization process. Export all the development language strings files that contain user-facing text to a standard XML Localization Interchange File Format (XLIFF). Submit the XLIFF file to a localization team for translation into multiple languages. Continue developing your app while waiting for the translations. Import the XLIFF translations into the project and test the app in each language you added. Repeat the process as needed, translating just the changes between each app revision. As necessary, perform additional localization steps yourself.

![../Art/export_import_process_2x.png](attachments/Art/export_import_process_2x.png)

You can choose from more than 100 different languages and dialects designated by regions to localize your app. However, the more general you make your localized resources, the more regions you can support with a single set of resources. This can save a lot of space in your app bundle and help reduce localization costs. For example, if you don’t need to distinguish between different regions that use the English language, you can add English to support users in the United States, United Kingdom, and Australia. Even if you provide region-specific resources always provide a complete set of language-specific resources for all the languages you support.

When searching for resources, the bundle APIs try to find the best match between the languages the app supports and the user’s language and region settings. The region-specific resource folders are searched before the language-specific resource folders. For example, if you add English (United States), English (United Kingdom), and English (Australia) to your project, the bundle APIs search the appropriate region-specific folders first, followed by the English language folder. For more information about how the bundle APIs find localized resources, read [The Bundle Search Pattern](../../Core%20Foundation/Bundle%20Programming%20Guide/Accessing%20a%20Bundle%E2%80%99s%20Contents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbufvjvony) in _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

If you are unsure about what languages to add, consider the primary languages used in the App Store territories you choose in App Store Connect to market your app. The App Store territories are listed in [App Store territories](https://help.apple.com/itunes-connect/developer/#/dev997f9cf7c).

In Interface Builder, lock views you don’t want to accidentally change while waiting for translations. When a view is locked, you can’t change some or all of its properties in the inspector or the project editor. You specify the set of properties to lock by choosing a locking level (see Table 6-1).

__Table 6-1__  Locking levels

| Locking level | Description |
| Nothing | You can edit all properties of the view. |
| All properties | You can’t edit any properties of the view. |
| Localizable properties | You can’t change any user-visible strings and can’t change a limited set of other attributes, such as the view’s size. You can make other changes; for example, you can change the enabled state of a control or cell. |
| Non-localizable properties | You can change user-visible strings and attributes—such as the size of the view—but can’t change any other attributes of the view. |

You can set the lock attribute for a single view or the entire nib file. By default, views inherit their lock attribute from their parent view and top-level views inherit their lock attribute from the `.storyboard` or `.xib` file. If you set a view’s lock attribute, it sets the lock attribute for all its descendant views.

__To change the locking level of a view__

1. In Interface Builder, select the view you want to lock.
2. In the Identity inspector (under the Document section), choose a locking level from the Lock pop-up menu.

   Refer to [Table 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk42q) for a description of the locking choices in this menu.

   To obtain the lock value from its parent view, choose Inherited.

For example, choose Localizable Properties to continue developing your app while waiting for a nib or strings file to be localized. Choose Non-localizable Properties if you are incorporating translations into a nib file and don’t want to make other changes inadvertently.

__To change the locking level of the nib file__

1. In project navigator, select a `.storyboard` or `.xib` file.
2. Choose a locking level from the Editor > Localization Locking menu.

   Refer to [Table 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk42q) for a description of the locking choices in this menu.

   To unlock all the views in the file, choose Reset Locking Controls.

For example, to prevent any edits to the nib file that would impact localized strings files, choose Reset Locking Controls followed by Localizable Properties.

Export the development language resources to an XLIFF file and submit it to a localization team for translation into multiple languages.

The first time you export localizations, only the base internationalization—the `.storyboard` and `.xib` resource files—exist in the project folder. Xcode generates the strings files from your project files and includes them in the exported `.xliff` file. Xcode doesn’t add the strings files to the project until you import localizations later. The exported `[Language ID].xliff` file encodes the strings files in the standard XML Localization Interchange File Format (XLIFF). (Most third-party localization tools support this XLIFF file format.) For example, if the development language is English, the `en.xliff` file contains base internationalization strings files (one for each `.storyboard` and `.xib` file), a `Localizable.strings` file, and an `InfoPlist.strings` file. The source text in the strings files is in English.

Translators should return a separate `.xliff` file for each language. The files should use the language ID as the prefix. For example, if you request `en.xliff` for English be translated into German and Russian, the returned files should be named `de.xliff` for German and `ru.xliff` for Russian. The individual .`xliff` files contain the actual translations.

![../Art/export_details_2x.png](attachments/Art/export_details_2x.png)![../Art/export_details_2x.png](attachments/Art/export_details_2x.png)

The first step to localize your app is to export the development language or base localization for translation. Before doing this, verify that the development language copyright notice in the `Info.plist` file is correct. Xcode includes the human-readable copyright notice in the XLIFF file. For a complete list of the localizable `Info.plist` keys, read [Locking Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk43a).

__To export the development language translation__

1. In the Xcode project editor, select the project or target.
2. Choose Editor > Export For Localization.
3. In the sheet that appears, enter a location in the Save As field and click Save.

   Xcode saves the file to the location you specified with a `.xliff` extension. Xcode creates the folder (if it doesn’t exist) and places a file named `[Language ID].xliff` in the folder where `Language ID` is the identifier for the development language. For example, if the development language is English, the filename is `en.xliff`.

   If you never added a language to your project, the export dialog appears similar to this screenshot:

   ![../Art/export_base_localization_2x.png](attachments/Art/export_base_localization_2x.png)

The next time you export localizations, optionally export the development language resources, specific language resources, or all language resources.

__To export multiple localizations for translation__

1. In the Xcode project editor, select the project or target.
2. Choose Editor > Export For Localization.
3. In the sheet that appears, enter a location in the Save As field.

   If you added a language to your project, the export dialog appears similar to this screenshot:

   ![../Art/export_multiple_localizations_2x.png](attachments/Art/export_multiple_localizations_2x.png)
4. From the Include pop-up menu, choose Existing Translations or Development Language Only.

   To export all or specific language resources, choose Existing Translations and then deselect the languages that you don’t want to include in the export in the Languages section below. To export the development language resources, choose Development Language Only.
5. Click Save.

   For each language you select, Xcode saves an XLIFF file (a file with a language ID prefix and `.xliff` extension) to the location you specified in the Save As field. For example, if you select German and French from the language list, Xcode adds a `de.xliff` and `fr.xliff` file to the folder.

When you import localizations, Xcode adds the language and a set of localized strings files for the language to the project. For example, if you import `ru.xliff` in the standard XML Localization Interchange File Format (XLIFF) that includes the target language attribute, the Russian language is added to the project. The first time you import localizations, the base internationalization files change to a group containing the strings files in the project navigator. Xcode stores the language-specific strings files in language folders. For example, Xcode creates a `ru.lproj` folder in the project folder and adds a localized copy of the `Localizable.strings` and `InfoPlist.strings` files to the `ru.lproj` folder. The localized strings files are extracted from the corresponding `[Language ID].xliff` file. The next time you import localizations, the strings files are merged with your existing project files.

![../Art/import_details_2x.png](attachments/Art/import_details_2x.png)

__To import localizations from translators__

1. In the Xcode project editor, select the project or target.
2. Choose Editor > Import Localizations.
3. In the sheet that appears, select a file with a `.xliff` extension and click Open.

   A sheet appears showing the differences between the imported XLIFF file and the existing resources in the project folder.

   ![../Art/import_localizations_2x.png](attachments/Art/import_localizations_2x.png)
4. Click Import.

   Xcode decodes the localized strings files from the XLIFF file and adds them to the project folder. Xcode replaces existing strings files.

After you import localizations, Xcode updates the project navigator to show the new language-specific resources. Localized `.storyboard` and `.xib` files now appear as groups in the project navigator. Click the disclosure triangle next to a `.storyboard` or `.xib` file to reveal the base resource and language-specific strings files.

![../Art/localized_nib_2x.png](attachments/Art/localized_nib_2x.png)

Select a strings file to view and optionally, edit the contents. The strings file contains key-value pairs that Xcode automatically generates from the text it finds in the corresponding `.storyboard` or `.xib` file. If you use `NSLocalizedString` macros in your code, as described in [Separating User-Facing Text from Your Code](Internationalizing%20Your%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedilktk4zq), a `Localizable.strings` group also appears in the project navigator.

![../Art/localized_strings_2x.png](attachments/Art/localized_strings_2x.png)

Another kind of strings file is `InfoPlist.strings`, which you use for localizing app properties that are visible to users (such as the app’s name). For the keys you can localize in an `InfoPlist.strings` file, read [Locking Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk43a).

Alternatively, you can use the `xcodebuild` command-line utility to export and import localizations.

To export localizations, enter this command in Terminal, replacing the `<dirpath>` and `<projectname>` arguments:

```
xcodebuild -exportLocalizations -localizationPath <dirpath> -project <projectname> [[-exportLanguage <targetlanguage>]]
```

The exported XLIFF files are placed in `<dirpath>`. Optionally, use the `exportLanguage` argument to export other localizations.

To import localizations, enter this command in Terminal, replacing the `<filepath>` and `<projectname>` arguments:

```
xcodebuild -importLocalizations -localizationPath <filepath> -project <projectname>
```

where `<filepath>` refers to a single XLIFF file.

You can explicitly add language-specific resource files to your project. For example, you may want to use different sets of image and audio files for different languages and dialects because of cultural differences. At runtime, the app searches the language-specific folder before the base folder to find a resource file, so you can add a resource to the `Base.lproj` folder and then specific language folders as needed.

__To localize a resource__

1. In the project navigator, select a resource you want to localize.
2. If necessary, open the File inspector.
3. In the Localization section, click the Localize button.

   ![../Art/localize_resource_1_2x.png](attachments/Art/localize_resource_1_2x.png)
4. In the dialog that appears, choose a language from the pop-up menu and click the Localize button.

   For example, choose Base if you want to use the resource file for all languages.

   ![../Art/localize_resource_2_2x.png](attachments/Art/localize_resource_2_2x.png)

After localizing a resource, you can add it to additional languages using the File inspector.

__To add localizations to a resource__

1. In the project navigator with the File inspector open, select the resource.
2. In the Localization section, choose the additional languages you want to add.

   Xcode duplicates the file in the corresponding language folder and it appears in the project navigator.

   ![../Art/localize_resource_3_2x.png](attachments/Art/localize_resource_3_2x.png)

If a string contains a noun plural or units of measurement, provide alternate strings for languages that have different plural rules. To specify language plural rules that can’t be represented by key-value pairs in a strings file, use a `.stringsdict` file, an XML property list with a `.stringsdict` file extension. Languages vary in how they handle plurals of nouns or units of measurement. Some languages have a single form, some have two categories, and others have three or more categories to represent quantities. If you display a formatted string containing a variable quantity, you can use one string in your code that is localized using plural rules specified in a `.stringsdict` file.

Similar to how you retrieve localized text from strings files, use `NSLocalizedString` macros in your code to retrieve the format string for different plural forms from a `.stringsdict` file. Next, provide a localized `.stringsdict` file for all the supported languages that have different plural rules. The `NSLocalizedString` macros search an existing `.stringsdict` file before the associated strings file that has the same filename prefix. For example, the macros search the `Localizable.stringsdict` file for the `%d file(s) remaining` key first. If it is not found, the macros search the `Localizable.strings` file for the key. Therefore, only add `.stringsdict` files for languages that have different plural rules.

__To create language plural rules__

1. In your code, use a `NSLocalizedString` macro, passing a formatted string to retrieve a plural phrase.

   For example, to display a variable number of files as text:

```
localizedString = [NSString localizedStringWithFormat:NSLocalizedString(@"%d file(s) remaining", @"Message shown for remaining files"), count];
```

   Pass a format string as the key parameter to the [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring) macro.
2. To create the `Localizable.strings` file for each language, export and import localizations, as described in [Exporting Localizations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk44q) and [Importing Localizations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk42a).

   Xcode generates a `Localizable.strings` file from the [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring) macros in your code. For example, this key-value pair appears in the development language `Localizable.strings` from the previous code fragment:

```
/* Message shown for remaining files */
"%d file(s) remaining" = "%d file(s) remaining";
```

   Alternatively, you can create the development language `Localizable.strings` file yourself, as described in [Creating Strings Files for User-Facing Text in Your Code](Managing%20Strings%20Files%20Yourself.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedcojnknltc).
3. Create a `.stringsdict` property list file and localize it for each language that has different plural rules.

   Add a property list file to the project (choose File > New > File and select Property List from the sheet). In the project navigator, change the filename to `Localizable.stringsdict` and localize it in selected languages, as described in [Adding Additional Resources You Want to Localize](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk4yto).
4. Add the language-specific plural rules to each `.stringsdict` file.

   The `.stringsdict` file contains a collection of plural rules for each phrase. The top-level key is the same key you pass to an `NSLocalizedString` macro in your code. The value for this key is a dictionary that specifies the plural rule details. The dictionary contains the text to use for each number category. The types of categories and meaning vary depending on the language.

   For example, the English `.stringsdict` file for the `%d file(s) remaining` key is:

```xml
<plist version="1.0">
    <dict>
        <key>%d file(s) remaining</key>
        <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@files@</string>
            <key>files</key>
            <dict>
                <key>NSStringFormatSpecTypeKey</key>
                <string>NSStringPluralRuleType</string>
                <key>NSStringFormatValueTypeKey</key>
                <string>d</string>
                <key>one</key>
                <string>%d file remaining</string>
                <key>other</key>
                <string>%d files remaining</string>
            </dict>
        </dict>
    </dict>
</plist>
```

   In English, the `one` category is used for the number 1, and the `other` category is used for all other numbers in English.

   The Russian `.stringsdict` file for the `%d file(s) remaining` key is:

```xml
<plist version="1.0">
    <dict>
       <key>%d file(s) remaining</key>
         <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@files@</string>
            <key>files</key>
            <dict>
                <key>NSStringFormatSpecTypeKey</key>
                <string>NSStringPluralRuleType</string>
                <key>NSStringFormatValueTypeKey</key>
                <string>d</string>
                <key>one</key>
                <string>Остался %d файл</string>
                <key>many</key>
                <string>Осталось %d файлов</string>
                <key>other</key>
                <string>Осталось %d файла</string>
            </dict>
        </dict>
    </dict>
</plist>
```
5. Test the plural rules in multiple languages.

   Follow the steps in [Testing Specific Languages and Regions](Testing%20Your%20Internationalized%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedolktk4za) to run the app in Xcode using different language settings.

   For example, the above English plural rules for the `%d file(s) remaining` key should result in the following localized strings:

| Category | Example numbers | Localized string |
| --- | --- | --- |
| one | 1 | 1 file remaining |
| other | 0, 2, 3, … | 2 files remaining  3 files remaining |

   For Russian, there are three possible categories with different formats:

| Category | Example numbers | Localized string |
| --- | --- | --- |
| one | 1, 21, 31, 41, 51, 61, … | `Остался 1 файл`  `Остался 21 файл` |
| many | 0, 5–20, 25–30, 35–40, … | `Осталось 0 файлов`  `Осталось 20 файлов` |
| other | 2–4, 22–24, 32–34, … | `Осталось 2 файла`  `Осталось 22 файла` |

For a complete description of the `.stringsdict` file properties, read [Stringsdict File Format](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/StringsdictFileFormat/StringsdictFileFormat.html#//apple_ref/doc/uid/10000171i-CH16-SW1). For the plural categories and rules for each language, see [CLDR Language Plural Rules](http://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html).

When you export localizations, Xcode includes an `InfoPlist.strings` file for translation. However, this file contains properties about your app and company, so you may want to verify or translate this file yourself. This strings file allows you to optionally localize some property values in the information property list, such as the app name (bundle display name) and copyright notice.

Xcode automatically adds these keys to the `InfoPlist.strings` file:

- `[CFBundleDisplayName](../../../../General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xugrscovxgi3dfiruxg4dmmf4u4ylnmu)`
- `[CFBundleName](../../../../General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xugrscovxgi3dfjzqw2zi)`
- `[CFBundleShortVersionString](../../../../General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xugrscovxgi3dfknug64tukzsxe43jn5xfg5dsnfxgo)`
- `[NSHumanReadableCopyright](../../../../General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xu4u2iovwwc3ssmvqwiylcnrsug33qpfzgsz3ioq)`

For a complete description of the information property list, read _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

To localize the app name and copyright notice, add values for the `[CFBundleDisplayName](../../../../General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xugrscovxgi3dfiruxg4dmmf4u4ylnmu)` and `[NSHumanReadableCopyright](../../../../General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xu4u2iovwwc3ssmvqwiylcnrsug33qpfzgsz3ioq)` keys to the `InfoPlist.strings` file. For example, add these lines to the `InfoPlist.strings (French)` file in the project navigator:

```
CFBundleDisplayName = "Maisons";
NSHumanReadableCopyright = "Copyright © 2014 My Great Company Tous droits réservés.";
```


If you localize the app name, use it in menu items and elsewhere in the user interface. You can get the localized app name programmatically with the `[CFBundleDisplayName](../../../../General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df5ygy2ltoqxws3tgn4xugrscovxgi3dfiruxg4dmmf4u4ylnmu)` key:

```
NSString *appName = [[[NSBundle mainBundle] localizedInfoDictionary] objectForKey:@"CFBundleDisplayName"];
```

For Mac apps, the user can rename the app in the Finder, so use the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class to get the app name:

```
NSString *bundlePath = [[NSBundle mainBundle] bundlePath];
NSString *appName = [[NSFileManager defaultManager] displayNameAtPath:bundlePath];
```


Add languages to your project if you want to add language-specific resources, as described in [Adding Additional Resources You Want to Localize](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk4yto), before importing localizations. (Xcode automatically adds languages to your project when importing localizations.) For example, add language-specific image and audio files to your project or test language-specific plural rules before you begin localizing all the strings files.

When Xcode adds a language to your project, it creates a separate language folder to store the language-specific resources. Xcode adds a strings file for each `.storyboard` and `.xib` file in the `Base.lproj` folder to the language folder. The strings file has the same name as the `.storyboard` or `.xib` file but with the `strings` extension. For example, if you have a storyboard named `MyStoryboard.storyboard`, the generated strings file is named `MyStoryboard.strings`.

__To add a language to a project__

1. In the project navigator, select the project (not a target) and click Info.
2. In the Localizations section, click the Add button (+) under the Language column and choose the language you want to add from the pop-up menu.

   ![../Art/add_language_1_2x.png](attachments/Art/add_language_1_2x.png)

   The menu items contain the language name followed by the language ID in parentheses, as in German (de), Japanese (ja), and Arabic (ar). Menu items for scripts or dialects contain the region in parentheses, as in German (Switzerland). The language ID for scripts or dialects uses subtags, as in `pt-PT` where `pt` is the code for Portuguese and `PT` is the code for Portugal. For example, use `pt` as the language ID for Portuguese as it is used in Brazil and `pt-PT` as the language ID for Portuguese as it is used in Portugal. The Other submenu (at the bottom of the list) contains more languages and dialects.

   These same language IDs are used in the names of the corresponding `.lproj` language folders, described in [Choosing Languages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedklktk4zq).
3. In the dialog that appears, deselect the resource files you don’t want to localize for this language.

   For the file type Localizable Strings, Xcode creates a strings file for that resource. If you prefer to maintain a separate `.storyboard` or `.xib` file for the language, choose the type of resource file from the File Types pop-up menu instead—for example, choose Interface Builder Cocoa Touch Storyboard for a Mac storyboard file.

   ![../Art/add_language_3_2x.png](attachments/Art/add_language_3_2x.png)
4. Click the Finish button.

[Next](Testing%20Your%20Internationalized%20App.md)[Previous](Supporting%20Right-to-Left%20Languages.md)

