---
title: Hey Siri, How Can I Improve the Recognition of My App's Name?
apple_id: DTS40017627
resource_type: QA
platform: iOS
topic: null
technology: Intents
published: '2017-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1950/_index.html
archived_at: '2026-07-18T02:37:30.051433Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1950

# Hey Siri, How Can I Improve the Recognition of My App's Name?

## Q:  How can I improve Siri's recognition of my app's name?

A: Siri uses multiple sources of information within an app to determine if a user's request to Siri refers to your app. This document provides guidance to developers to help Siri recognize when a user request refers to your app.

All apps, even those not specifically using SiriKit, should provide a [CFBundleDisplayName](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-110725) key in their `Info.plist`. The string value for this key is displayed to the user throughout the system, such as below the app icon on the home screen. The presence of this key will help Siri to identify your app, even if your app does not use SiriKit.

All apps, even those not specifically using SiriKit, can provide a [CFBundleSpokenName](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-SW3) key in their `Info.plist`. The string value of this key represents the expected pronunciation of your app's name, such as "My app one two three" for an app with a bundle display name "MyApp123." This key is also used by VoiceOver to speak the app name.

Apps adopting SiriKit and linking to the iOS 11 SDK can provide a small number of alternate app names that users may use when interacting with Siri by specifying the [INAlternativeAppNames key](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW26) in the `Info.plist` for the app. As an example, if a banking app is named "Unicorn Bank" but users frequently refer to the app as "Unicorn Pay" or "Unicorn", it is helpful to specify both of these alternate app names so users can use them in their request to Siri.

Additionally, `INAlternativeAppNames` contains a pronunciation hint to help Siri understand how users pronounce your app's name.

__Listing 1__  Sample of `INAlternativeAppNames`

```
<key>INAlternativeAppNames</key>
<array>
    <dict>
        <key>INAlternativeAppName</key>
        <string>Unicorn Pay</string>
        <key>INAlternativeAppNamePronunciationHint</key>
        <string>you nee corn pay</string>
    </dict>
    <dict>
        <key>INAlternativeAppName</key>
        <string>Unicorn</string>
        <key>INAlternativeAppNamePronunciationHint</key>
        <string>you nee corn</string>
    </dict>
</array>
```


All apps adopting SiriKit, regardless of the specific SiriKit domain, should provide Siri with example phrases that demonstrate the different ways your users will use your app through Siri. This is done using the `IntentPhrases` key of the global vocabulary file, named `AppIntentVocabulary.plist`.

Example phrases for using an app named Cuddly Creatures that shows pet photos and implements the SiriKit photo domain might include the following:

- Look for silly cat photos with Cuddly Creatures.
- Can you show my album of dog photos in Cuddly Creatures?
- Start a photo slide show in Cuddly Creatures.

The `AppIntentVocabulary.plist` file for Cuddly Creatures with these example phrases is shown in Listing 2.

__Listing 2__  Sample `AppIntentVocabulary.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>IntentPhrases</key>
    <array>
        <dict>
            <key>IntentExamples</key>
            <array>
                <string>Look for silly cat photos with Cuddly Creatures.</string>
                <string>Can you show my album of dog photos in Cuddly Creatures?</string>
            </array>
            <key>IntentName</key>
            <string>INSearchForPhotosIntent</string>
        </dict>
        <dict>
            <key>IntentExamples</key>
            <array>
                <string>Start a photo slide show in Cuddly Creatures.</string>
            </array>
            <key>IntentName</key>
            <string>INStartPhotoPlaybackIntent</string>
        </dict>
    </array>
</dict>
</plist>
```

Example phrases are needed for every intent declared by the `IntentsSupported` key in the Intents extension `Info.plist`. Further, a complete `AppIntentVocabulary.plist`, with example phrases for each supported intent, needs to be present for every locale the app supports. Submitting an app with a missing example phrase will result in warnings from the App Store, such as the example in Listing 3.

__Listing 3__  Sample warning from the App Store if an example phrase is missing

```
Invalid Siri Support - No example phrase was provided for INSearchForPhotosIntent in the "de" language
```

See the [SiriKit Programming Guide](https://developer.apple.com/library/content/documentation/Intents/Conceptual/SiriIntegrationGuide/SpecifyingCustomVocabulary.html#//apple_ref/doc/uid/TP40016875-CH6-SW1) for instructions on creating the global vocabulary file and documentation for the specific keys.

It is important to provide Siri with an `AppIntentVocabulary.plist` file in every language your app supports. Additionally, if your app's name (including alternative app names) is localized, a [localized InfoPlist.strings file](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html#//apple_ref/doc/uid/TP40009254-102276) should be provided with the localized version of CFBundleDisplayName in each language.

As an example, imagine that the app Cuddly Creatures supports English, German, Japanese, and Korean, with the app's name localized in each language. The app uses base localization, with the development language set to English. A complete set of localized files used by Siri for this app is shown in Figure 1.

__Figure 1__  Example of a fully localized SiriKit app

!!

In Figure 1, none of the localized files are provided for the English locale. Instead, the English files are associated with the [Base locale](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPInternational/InternationalizingYourUserInterface/InternationalizingYourUserInterface.html#//apple_ref/doc/uid/10000171i-CH3-SW2), because the Base locale is the localization used for the app's development language. Providing an additional `AppIntentVocabulary.plist` and `InfoPlist.strings` specifically in the development language's locale is unnecessary.

For additional information on SiriKit, consult the following resources:

- [SiriKit Programming Guide](https://developer.apple.com/library/content/documentation/Intents/Conceptual/SiriIntegrationGuide/index.html#//apple_ref/doc/uid/TP40016875)
- Sample Code with sample phrases in `AppIntentVocabulary.plist`: [Searching for Photos](https://developer.apple.com/documentation/sirikit/photos/searching_for_photos)
- Sample Code with custom app vocabulary and sample phrases in `AppIntentVocabulary.plist`: [IntentHandling: Using the Intents framework to handle custom Siri request](https://developer.apple.com/library/content/samplecode/IntentHandling/Introduction/Intro.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-10-27 | Added information about CFBundleSpokenName and INAlternativeAppNames |
| 2017-04-05 | New document that describes how apps can improve Siri's recognition of the app's name |

