---
title: Resolving the Privacy-Sensitive Data App Rejection
apple_id: DTS40017549
resource_type: QA
platform: watchOS|tvOS|iOS
topic: Security
technology: null
published: '2016-10-07'
source_url: https://developer.apple.com/library/archive/qa/qa1937/_index.html
archived_at: '2026-07-18T02:37:24.968950Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1937

# Resolving the Privacy-Sensitive Data App Rejection

## Q:  How do I resolve the privacy-sensitive data app rejection?

A: Maintaining user privacy is an important consideration when designing your app. Most iOS, watchOS, and tvOS devices contain data that users might not want to expose to apps or external entities. Access user data only with the user’s informed consent, and be transparent about how you use it.

Your app is responsible for all usage of privacy-sensitive data, including access to this data by all third party libraries used in your app. If your app attempts to access privacy-sensitive data without a usage description, your app will exit. Additionally, App Review checks for use of privacy-sensitive data, and rejects apps that request access to this data without a usage description. Listing 1 shows an example of such a rejection.

__Listing 1__  Example privacy-sensitive data rejection email for an app accessing the user's contacts

```
This app attempts to access privacy-sensitive data without a usage description. The app's Info.plist must contain an NSContactsUsageDescription key with a string value explaining to the user how the app uses this data.
```


Table 1 lists the different classes of privacy-sensitive data, and the APIs your app uses to access the data class. Using any of these data classes requires [Providing A Usage Description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjuhewugsbrfvifet2wjfcekx2eivjugusjkbkest2o). For examples of requesting user consent to access any of these data classes, consult the [Additional Documentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjuhewugsbrfvhviscfkjpuit2dkm) section.

If you receive a rejection email from App Review, such as the example email in Listing 1, and you don't believe your app accesses the data class named in the email, look for any use of the listed APIs in your code, including in all of your third party libraries. If a third party library requires the privacy-sensitive data, you should work with the library vendor to understand how this data is used by their library and provide a transparent and meaningful usage description.

__Table 1__  APIs requiring usage descriptions

| Data Class | Xcode Key | Raw Info.plist Key | API Requiring Usage Description |
| Apple Music | Privacy - Media Library Usage Description | NSAppleMusicUsageDescription | SKCloudServiceController requestCapabilitiesWithCompletionHandler: SKCloudServiceController requestCapabilitiesWithCompletionHandler: SKCloudServiceController requestStorefrontIdentifierWithCompletionHandler: MPMediaQuery MPMediaLibrary requestAuthorization: |
| Bluetooth | Privacy - Bluetooth Peripheral Usage Description | NSBluetoothPeripheralUsageDescription | CBCentralManager CBPeripheralManager |
| Calendar | Privacy - Calendars Usage Description | NSCalendarsUsageDescription | EKEventStore requestAccessToEntityType: |
| Camera | Privacy - Camera Usage Description | NSCameraUsageDescription | AVCaptureDeviceInput |
| Contacts | Privacy - Contacts Usage Description | NSContactsUsageDescription | CNContactStore requestAccessForEntityType: |
| Health | Privacy - Health Share Usage Description Privacy - Health Update Usage Description | NSHealthShareUsageDescription NSHealthUpdateUsageDescription | com.apple.developer.healthkit entitlement HKHealthStore |
| Home | Privacy - HomeKit Usage Description | NSHomeKitUsageDescription | HMHomeManager |
| Location | Privacy - Location Always Usage Description Privacy - Location When In Use Usage Description | NSLocationAlwaysUsageDescription NSLocationWhenInUseUsageDescription | CLLocationManager requestAlwaysAuthorization: CLLocationManager requestWhenInUseAuthorization: |
| Microphone | Privacy - Microphone Usage Description | NSMicrophoneUsageDescription | AVAudioSession requestRecordPermission: |
| Motion | Privacy - Motion Usage Description | NSMotionUsageDescription | CMMotionActivityManager |
| Photos | Privacy - Photo Library Usage Description | NSPhotoLibraryUsageDescription | UIImagePickerController or PHPhotoLibrary requestAuthorization: used in conjunction with any of the following classes: PHAsset PHAssetCollection PHCollection PHCollectionList |
| Reminders | Privacy - Reminders Usage Description | NSRemindersUsageDescription | EKEventStore requestAccessToEntityType: |
| Siri | Privacy - Siri Usage Description | NSSiriUsageDescription | INPreferences requestSiriAuthorization: |
| Speech Recognition | Privacy - Speech Recognition Usage Description | NSSpeechRecognitionUsageDescription | SFSpeechRecognizer requestAuthorization: |
| TV Provider Account | Privacy - TV Provider Usage Description | NSVideoSubscriberAccountUsageDescription | VSAccountManager |

All usage descriptions, including for privacy-sensitive data access from a framework, are declared in your app's `Info.plist` file, [which can be edited in Xcode](http://help.apple.com/xcode/mac/8.0/#/dev3f399a2a6). Add a new row to the `Info.plist` file, and set the key for the appropriate data class, defined in Table 1. Set your usage description string as the value.

If your app supports multiple locales, localize the usage description and place the localized string in  `InfoPlist.strings` for each locale, in addition to providing a usage description in the `Info.plist` file. See [Localizing Property List Values](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html#//apple_ref/doc/uid/TP40009254-102276) for more information about localizing property lists.

For additional information on using privacy-sensitive data, consult the following resources:

- App Programming Guide: [Supporting User Privacy](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/ExpectedAppBehaviors/ExpectedAppBehaviors.html#//apple_ref/doc/uid/TP40007072-CH3-SW6)
- Sample Code: [Checking and Requesting Access to Data Classes in Privacy Settings](https://developer.apple.com/library/prerelease/content/samplecode/PrivacyPrompts/Introduction/Intro.html)
- WWDC 2016 video: [Engineering Privacy for Your Users](https://developer.apple.com/videos/play/wwdc2016/709/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-10-07 | Clarified where to declare usage descriptions for frameworks and localizations |
| 2016-09-21 | New document that describes how to resolve the privacy-sensitive data app rejection |

