---
title: iOS 6.0 Release Notes
apple_id: TP40012166
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2013-01-15'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-6_0/index.html
archived_at: '2026-07-18T02:54:41.926260Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 6

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcnrwfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcnrwfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcnrwfvbuqmjnknlti)

### Introduction

iOS 6 SDK provides support for developing iOS apps, and it includes the complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 6. You can also test your apps using the included iOS Simulator, which supports iOS 6. iOS 6 SDK requires a Mac computer running OS X 10.7.4 or higher (Lion).

This version of iOS is intended for installation only on devices registered with Apple’s Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

To report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcnrwfvbuqmjnknlti) section, please use the Apple Bug Reporter on the Apple Developer website ([http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS 6 SDK in the Apple Developer Forums ([http://devforums.apple.com](http://devforums.apple.com/)). You can get more information about iCloud for Developers at [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS 6 SDK to develop code.

### Accounts Framework

- When requesting access to Facebook accounts, the only key required in your options dictionary is [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey). `ACFacebookPermissionGroupKey` and `ACFacebookAppVersionKey` are now obsolete.

  If you request a write permission under [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey), such as `publish_stream`, you must provide a value for [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey), which can be one of [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone), [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends), or [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme).

### Address Book

- Requesting access to contacts:

  - Users are able to grant or deny access to contact data on a per-app basis. To request access to contact data, call the [ABAddressBookRequestAccessWithCompletion](https://developer.apple.com/documentation/addressbook/1622001-abaddressbookrequestaccesswithco) function after calling the [ABAddressBookCreateWithOptions](https://developer.apple.com/documentation/addressbook/1621991-abaddressbookcreatewithoptions) function. The [ABAddressBookRequestAccessWithCompletion](https://developer.apple.com/documentation/addressbook/1622001-abaddressbookrequestaccesswithco) function does not block the app while the user is being asked to grant or deny access. Until access has been granted, the [ABAddressBookRef](https://developer.apple.com/documentation/addressbook/abaddressbook-kkq) object will not contain any contacts, and any attempt to modify contacts fails with a [kABOperationNotPermittedByUserError](https://developer.apple.com/documentation/addressbook/kaboperationnotpermittedbyusererror) error. The user is prompted only the first time access is requested; any subsequent calls to `ABAddressBookCreateWithOptions` will use the existing permissions. The completion handler is called on an arbitrary queue. If the `ABAddressBookRef` object is used throughout the app, then all usage must be dispatched to the same queue to use `ABAddressBookRef` in a thread-safe manner.
- Checking access authorization status:

  - An app can use the authorization status API to check if it can access contacts, calendars, reminders, or the photo library. This API is independent from the request access API and will not prompt the user to grant or deny access. With this API an app can adjust the display of its UI elements that would access the data class. For example, if access to contacts is authorized or not determined, then a UI button to pick a contact can be displayed.
  - For Address Book, call the [ABAddressBookGetAuthorizationStatus](https://developer.apple.com/documentation/addressbook/1622002-abaddressbookgetauthorizationsta) function. For Event Kit, call the [authorizationStatusForEntityType:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507239-authorizationstatus) class method of [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore). For Assets Library, call the [authorizationStatus](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423523-authorizationstatus) class method of [ALAssetsLibrary](https://developer.apple.com/documentation/assetslibrary/alassetslibrary). The meaning of the status values that are returned is as follows:

    - __Authorization Status Not Determined__—The user has not yet made a choice regarding whether this app can access the data class.
    - __Authorization Status Restricted__—This app is not authorized to access the data class. The user cannot change this app’s status, possibly due to active restrictions such as parental controls being in place.
    - __Authorization Status Denied__—The user explicitly denied access to the data class for this app.
    - __Authorization Status Authorized__—This app is authorized to access the data class.

### Audio

- Beginning in iOS 6, apps need to have the audio key in their `UIBackgroundModes` in order to use CoreMIDI’s [MIDISourceCreate](https://developer.apple.com/documentation/coremidi/1495212-midisourcecreate) and [MIDIDestinationCreate](https://developer.apple.com/documentation/coremidi/1495347-mididestinationcreate) functions. Without the key set, these functions will return `kMIDINotPermitted` (-10844).

### Bonjour

- The [NSNetService](https://developer.apple.com/documentation/foundation/netservice) class and CFNetService APIs do not include P2P interfaces by default. To browse, register, or resolve services over P2P interfaces, an app needs to use the Bonjour `DNSService*()` APIs noted below.
- Setting the _interfaceIndex_ parameter to [kDNSServiceInterfaceIndexAny](https://developer.apple.com/documentation/dnssd/kdnsserviceinterfaceindexany) in the following APIs will not include P2P interfaces by default. To include P2P interfaces, you must now set the [kDNSServiceFlagsIncludeP2P](https://developer.apple.com/documentation/dnssd/1823436-anonymous/kdnsserviceflagsincludep2p) flag when using `kDNSServiceInterfaceIndexAny`, or set `interfaceIndex` to [kDNSServiceInterfaceIndexP2P](https://developer.apple.com/documentation/dnssd/kdnsserviceinterfaceindexp2p). The affected APIs are:

  - [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse)
  - [DNSServiceRegister](https://developer.apple.com/documentation/dnssd/1804733-dnsserviceregister)
  - [DNSServiceResolve](https://developer.apple.com/documentation/dnssd/1804744-dnsserviceresolve)
  - [DNSServiceRegisterRecord](https://developer.apple.com/documentation/dnssd/1804727-dnsserviceregisterrecord)
  - [DNSServiceQueryRecord](https://developer.apple.com/documentation/dnssd/1804747-dnsservicequeryrecord)

### Core Image

- In iOS 6, Core Image adds the following filters to the set provided in iOS 5:

  `[CIAffineClamp](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqlgmzuw4zkdnrqw24a)`, `[CIAffineTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqlgmzuw4zkunfwgk)`, `[CIBarsSwipeTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqtbojzvg53jobsvi4tbnzzws5djn5xa)`, `[CIBlendWithMask](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqtmmvxgiv3jorue2yltnm)`, `[CIBloom](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqtmn5xw2)`, `[CIBumpDistortion](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqtvnvyei2ltorxxe5djn5xa)`, `[CIBumpDistortionLinear](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busqtvnvyei2ltorxxe5djn5xey2lomvqxe)`, `CICircleSplashDistortion,CICircularScreen`, `[CIColorMap](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busq3pnrxxetlboa)`, `[CIColorPosterize](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busq3pnrxxeudpon2gk4tjpjsq)`, `[CICopyMachineTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busq3pob4u2yldnbuw4zkuojqw443joruw63q)`, `[CIDisintegrateWithMaskTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrdjonuw45dfm5zgc5dfk5uxi2cnmfzwwvdsmfxhg2lunfxw4)`, `[CIDissolveTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrdjonzw63dwmvkheyloonuxi2lpny)`, `[CIDotScreen](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrdporjwg4tfmvxa)`, `[CIEightfoldReflectedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrljm5uhiztpnrsfezlgnrswg5dfmrkgs3df)`, `[CIFlashTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrtmmfzwqvdsmfxhg2lunfxw4)`, `[CIFourfoldReflectedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrtpovzgm33mmrjgkztmmvrxizlekruwyzi)`, `[CIFourfoldRotatedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrtpovzgm33mmrjg65dborswivdjnrsq)`, `[CIFourfoldTranslatedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busrtpovzgm33mmrkheyloonwgc5dfmrkgs3df)`, `[CIGaussianBlur](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busr3bovzxg2lbnzbgy5ls)`, `[CIGlideReflectedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busr3mnfsgkutfmzwgky3umvsfi2lmmu)`, `[CIGloom](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busr3mn5xw2)`, `[CIHatchedScreen](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bussdborrwqzleknrxezlfny)`, `[CIHoleDistortion](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bussdpnrsui2ltorxxe5djn5xa)`, `[CILanczosScaleTransform](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bustdbnzrxu33tknrwc3dfkrzgc3ttmzxxe3i)`, `[CILineScreen](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bustdjnzsvgy3smvsw4)`, `[CIMaskToAlpha](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bustlbonvvi32bnrygqyi)`, `[CIMaximumComponent](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bustlbpbuw25lninxw24dpnzsw45a)`, `[CIMinimumComponent](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bustljnzuw25lninxw24dpnzsw45a)`, `[CIModTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5bustlpmrkheyloonuxi2lpny)`, `[CIPerspectiveTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busudfojzxazldoruxmzkunfwgk)`, `[CIPerspectiveTransform](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busudfojzxazldoruxmzkuojqw443gn5zg2)`, `[CIPinchDistortion](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busudjnzrwqrdjon2g64tunfxw4)`, `[CIPixellate](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busudjpbswy3dborsq)`, `[CIRandomGenerator](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busutbnzsg63khmvxgk4tborxxe)`, `[CISharpenLuminance](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busu3imfzhazlojr2w22lomfxggzi)`, `[CISixfoldReflectedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busu3jpbtg63dekjswm3dfmn2gkzcunfwgk)`, `[CISixfoldRotatedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busu3jpbtg63dekjxxiylumvsfi2lmmu)`, `[CISmoothLinearGradient](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busu3nn5xxi2cmnfxgkylsi5zgczdjmvxhi)`, `[CIStarShineGenerator](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busu3umfzfg2djnzsuozlomvzgc5dpoi)`, `[CISwipeTransition](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busu3xnfygkvdsmfxhg2lunfxw4)`, `[CITriangleKaleidoscope](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busvdsnfqw4z3mmvfwc3dfnfsg643dn5ygk)`, `[CITwelvefoldReflectedTile](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busvdxmvwhmzlgn5wgiutfmzwgky3umvsfi2lmmu)`, `[CIUnsharpMask](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busvloonugc4tqjvqxg2y)`, `[CIVortexDistortion](../../../documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df5tgs3dumvzc6y3jf5busvtpoj2gk6cenfzxi33soruw63q)`

  Also in iOS 6, Core Image allows the creation of `CIImage` objects that reference Open GL texture objects via the [imageWithTexture:size:flipped:colorSpace:](https://developer.apple.com/documentation/coreimage/ciimage/1547006-imagewithtexture) method of the `CIImage` class.

### Event Kit

- When requesting access to calendars or reminders:

  - Users are able to grant or deny access to event and reminder data on a per-app basis. To request access to event and/or reminder data, call the [requestAccessToEntityType:completion:](https://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess): method of [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore). This will not block the app while the user is being asked to grant or deny access. Until access has been granted for an entity type, the event store will not contain any calendars for that entity type and any attempt to save data will fail.
  - The user will be prompted only the first time access is requested; any subsequent instantiations of `EKEventStore` will use the existing permissions. The completion handler is called on an arbitrary queue.

### Game Center

- Landscape-only apps that invoke a portrait-only view controller (such as the Game Center login screen) will cause the app to crash.

  Workaround:

  1. Apps should provide the delegate method `application:supportedIntefaceOrientationsForWindow` and ensure that portrait is one of the returned mask values.
  2. When a `UIBNavigationController` is involved, subclass the [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) and overriding [supportedInterfaceOrientations](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations).

### iCloud

- When creating an iCloud account, you can use any email-based Apple ID or your existing iCloud account. If you had a MobileMe account that you did not move to iCloud, you can use that Apple ID to sign up for a new iCloud account (none of your previous MobileMe data will be present).

  - `icloud.com` email cannot be sent from [www.icloud.com](http://www.icloud.com/). At this time, users should go to [http://beta.icloud.com](http://beta.icloud.com/) if they wish to use a web browser to send email from their `icloud.com` address.
- Provisioning profiles must be enabled for iCloud in the iOS Provisioning Portal. To enable a provisioning profile for iCloud, navigate to the App ID section of the iOS Provisioning Portal and configure your App ID for iCloud. After enabling the App ID for iCloud, regenerate your provisioning profiles to enable them for iCloud.
- The `setSortDescriptors:` method of `NSMetadataQuery` is not supported.
- In iOS 6, files that are protected via Data Protection cannot be used with iCloud Storage APIs.
- Filenames are case-insensitive in OS X but case-sensitive in iOS. This can lead to problems when using iCloud to share files between the two platforms. On iOS, you should avoid creating files with names that differ only by case.
- The behavior of coordinated read operations on iCloud Documents has changed:

  - In previous iOS releases, when your app performed a coordinated read operation on a file or package and the iCloud daemon noticed that there was a newer version of the item available, the coordinated read operation blocked until the newer version of the item was downloaded and written to the disk.
  - As of iOS 6, when you start a coordinated read operation on a file or package for which you already have a local version, the coordinated read will be granted as soon as possible, and the new version, if any, will download in the background. This call will block for downloading reasons only if you do not have a version of the file available locally.

    Additionally, when the file is conflicted, the iCloud daemon will not wait until it has all the conflict losers of the file available to make the file available to your app. It will make the different versions of the conflicted file available as soon as it can. Your app can use the existing file coordination and the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) callbacks to be notified when the conflict losers have been downloaded and are available.

### iTunes

- iTunes 10.6.3 is required for iOS 6 SDK.
- Previous public betas of iOS can no longer download iTunes Match songs.

### Location

- In iOS 6 beta 4, modifications were introduced to the new enum [CLActivityType](https://developer.apple.com/documentation/corelocation/clactivitytype) in Core Location:

  - Replace `CLActivityTypeVehicularNavigation` with [CLActivityTypeAutomotiveNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypeautomotivenavigation).
  - Add [CLActivityTypeOtherNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/othernavigation) for other vehicular navigation—e.g., boats, trains, or planes.

### Maps

- In iOS 6 and later, Map Kit is built on a new infrastructure hosted by Apple. Earlier iOS releases will continue to use Google’s service.

  - API compatibility will be maintained (see known issues below).
  - Maps are now supported in Simulator.
  - Map data will continue to evolve—only a limited amount of high-resolution satellite imagery is currently available.
- Routing apps that do not specify a coverage file during development will always be displayed in the Maps routing search results.
- Testing and debugging of coverage files for routing apps is only supported during development through the Xcode Run workflow. (You can specify the coverage file for a given Run scheme using the Options pane of the Run section of the scheme editor.) Apps that are archived and distributed (outside of the App Store) onto devices will not have access to the app’s coverage files.
- Developers should review their code for calls to `renderInContext` on the layer backing an [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview); failure to do so can cause their apps to crash. If these calls are made off the main thread, they should be eliminated or moved to the main thread.

### Media Player

- As of iOS 6, if you play video or audio within a [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview), you must configure the audio session correctly so that the audio is not silenced by the ringer switch. This behavior matches video and audio when played using native classes.

### Passbook

- Passes will no longer fall back to `background.png` if `strip.png` is not included in your pass bundle.
- The contents of the `userInfo` dictionary for [PKPassLibraryDidChangeNotification](https://developer.apple.com/documentation/passkit/pkpasslibrarydidchangenotification) have changed in the case of removed passes. Please consult the latest documentation for the new `userInfo` dictionary.
- Passes must include the WWDR Intermediate Certificate in their signature. Passes that omit this certificate are invalid and cannot be added to Passbook. This restriction was not enforced in previous beta releases.
- Images included in passes that use RGB need to include an alpha channel.

### Security

- In iOS 5, signing a certificate with an MD5 signature is not supported. Please ensure that certificates use signature algorithms based on SHA1 or SHA2.
- In iOS 6, there are improved privacy controls for Calendar, Reminders, Contacts, and Photos.

  - Users will see access dialogs when an app tries to access any of those data types. The user can switch access on and off in Settings > Privacy.
  - Developers can set a “purpose” string for each class of isolated data. iOS displays this string to users to help them understand why their data is being requested. These strings can be added using Xcode’s Project editor, which is in the Info tab. The relevant key names begin with the string “Privacy -”.
  - There are changes to the Event Kit and Address Book frameworks to help developers with this feature.

### Shared Photo Stream

- The Shared Photo Stream feature is set to OFF when updating from iOS 6 beta 1 to a later release. The default setting should be ON.

### Simulator

- No privacy alerts are displayed in iOS Simulator for apps that access Photos, Contacts, Calendar, and Reminders.
- For this release, iOS Simulator does not support testing In-App Purchase. Please use a device to test your apps that use this feature.
- When attempting to play an MP3 sound in Simulator, you will hear a popping sound instead.

### Social

- Weibo shows up in the Settings app only if a Chinese keyboard is enabled.
- The `requestAccessToAccountsWithType:withCompletionHandler:` method of [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore) is now deprecated. To access user accounts, please use the [requestAccessToAccountsWithType:options:completion:](https://developer.apple.com/documentation/accounts/acaccountstore/1493964-requestaccesstoaccounts) method.

  In the _options_ parameter of this new method, pass `nil` to access Twitter and Weibo accounts. To access Facebook accounts, pass a dictionary with the following keys (which are documented in `ACAccountStore.h`):

  - [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)
  - [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)

  You should no longer add this dictionary to your app’s `Info.plist` file, as was required in beta 1.
- When requesting access to Facebook accounts, the only key required in your options dictionary is [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey). `ACFacebookPermissionGroupKey` and `ACFacebookAppVersionKey` are now obsolete.

  If you request a write permission under [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)—such as `publish_stream`—you must provide a value for [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey), which can be one of [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone), [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends), or [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme).

### Status Bar

- It is now possible to set status bar tint parameters in your app’s `Info.plist` file. You might do this to ensure that the status bar color matches your app’s navigation bar color during startup. To set the status bar tint, add the `UIStatusBarTintParameters` key to your `Info.plist` file. The value of this key is a dictionary with the appropriate values describing the navigation bar your app has at startup. Inside the dictionary should be the `UINavigationBar` key, which has a value that is also a dictionary. That dictionary contains the initial navigation bar’s style (with the `Style` key) and indicates whether it is translucent (with the `Translucent` key). You can also specify your navigation bar’s tint color (with the `TintColor` key) or the name of its custom background image (with the `BackgroundImage` key).

### UIKit

- In iOS 5.1, the [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) class adopts the sliding presentation style when presenting the left view (previously seen only in Mail). This style is used when presentation is initiated either by the existing bar button item provided by the delegate methods or by a swipe gesture within the right view. No additional API adoption is required to obtain this behavior, and all existing APIs—including that of the `UIPopoverController` instance provided by the delegate—will continue to work as before. If the gesture would be insupportable in your app, setting the [presentsWithGesture](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/1623171-presentswithgesture) property of your split view controller to `NO` disables the gesture. However, disabling the gesture is discouraged because its use preserves a consistent user experience across all apps.
- In iOS 6, changes have been introduced so that you no longer need to set a delegate and implement a method for single-finger and single-tap gesture recognizers. This makes them work well with the [UIControl](https://developer.apple.com/documentation/uikit/uicontrol) objects.
- In iOS 6 and later, the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class paints its contents asynchronously.
- Autorotation is changing in iOS 6. In iOS 6, the `shouldAutorotateToInterfaceOrientation:` method of [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) is deprecated. In its place, you should use the [supportedInterfaceOrientationsForWindow:](https://developer.apple.com/documentation/uikit/uiapplication/1623091-supportedinterfaceorientations) and [shouldAutorotate](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621419-shouldautorotate) methods.

  - More responsibility is moving to the app and the app delegate. Now, iOS containers (such as [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller)) do not consult their children to determine whether they should autorotate. By default, an app and a view controller’s supported interface orientations are set to [UIInterfaceOrientationMaskAll](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/uiinterfaceorientationmaskall) for the iPad idiom and [UIInterfaceOrientationMaskAllButUpsideDown](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask/1622957-allbutupsidedown) for the iPhone idiom.
  - A view controller’s supported interface orientations can change over time—even an app’s supported interface orientations can change over time. The system asks the top-most full-screen view controller (typically the root view controller) for its supported interface orientations whenever the device rotates or whenever a view controller is presented with the full-screen modal presentation style. Moreover, the supported orientations are retrieved only if this view controller returns `YES` from its [shouldAutorotate](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621419-shouldautorotate) method. The system intersects the view controller’s supported orientations with the app’s supported orientations (as determined by the `Info.plist` file or the app delegate’s [application:supportedInterfaceOrientationsForWindow:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623107-application) method) to determine whether to rotate.
  - The system determines whether an orientation is supported by intersecting the value returned by the app’s [supportedInterfaceOrientationsForWindow:](https://developer.apple.com/documentation/uikit/uiapplication/1623091-supportedinterfaceorientations) method with the value returned by the [supportedInterfaceOrientations](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations) method of the top-most full-screen controller.
  - The [setStatusBarOrientation:animated:](https://developer.apple.com/documentation/uikit/uiapplication/1622939-setstatusbarorientation) method is not deprecated outright. It now works only if the [supportedInterfaceOrientations](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations) method of the top-most full-screen view controller returns `0`. This makes the caller responsible for ensuring that the status bar orientation is consistent.
- The [willRotateToInterfaceOrientation:duration:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621376-willrotate), [willAnimateRotationToInterfaceOrientation:duration:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621458-willanimaterotation), and [didRotateFromInterfaceOrientation:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621492-didrotatefrominterfaceorientatio) methods are no longer called on any view controller that makes a full-screen presentation over itself—for example, [presentViewController:animated:completion:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621380-presentviewcontroller).

  - You should make sure that your apps are not using these methods to manage the layout of any subviews. Instead, they should use the view controller’s [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews) method and adjust the layout using the view’s bounds rectangle.
- In iOS 6, the `viewWillUnload` and `viewDidUnload` methods of [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) are now deprecated. If you were using these methods to release data, use the [didReceiveMemoryWarning](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621409-didreceivememorywarning) method instead. You can also use this method to release references to the view controller’s view if it is not being used. You would need to test that the view is not in a window before doing this.
- It is not supported to set values for the [shadowOffset](https://developer.apple.com/documentation/uikit/uilabel/1620528-shadowoffset) or [shadowColor](https://developer.apple.com/documentation/uikit/uilabel/1620536-shadowcolor) properties of a `UILabel` object if its [attributedText](https://developer.apple.com/documentation/uikit/uilabel/1620542-attributedtext) property contains a valid attributed string. Instead, use the [NSShadowAttributeName](https://developer.apple.com/documentation/uikit/nsshadowattributename) attribute of the attributed string to set the shadow.
- Due to compatibility concerns, the `NSBaselineOffsetAttributeName` attribute is no longer supported in iOS 6.
- The `NSTextAlignmentNatural` value is not supported. It will throw an exception when it is used with the [textAlignment](https://developer.apple.com/documentation/uikit/uilabel/1620541-textalignment) property of `UILabel` or is supplied as the _alignment_ parameter to the [drawInRect:withFont:lineBreakMode:alignment:](https://developer.apple.com/documentation/foundation/nsstring/1619912-drawinrect) method of `NSString`.
- The `setContentStretch:` method of [UIView](https://developer.apple.com/documentation/uikit/uiview) has been deprecated. To achieve the same effect, use the [resizableImageWithCapInsets:](https://developer.apple.com/documentation/uikit/uiimage/1624102-resizableimagewithcapinsets) method of `UIImage` and display the image with a [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview).
- The [resizableImageWithCapInsets:](https://developer.apple.com/documentation/uikit/uiimage/1624102-resizableimagewithcapinsets) method of `UIImage` effectively resizes images by tiling. As a performance optimization, it uses stretching rather than tiling when the user would not be able to tell the difference, such as when a single column or row is being stretched. But in certain circumstances, the user might want to actually stretch some region of an image. In iOS 6, the [resizableImageWithCapInsets:resizingMode:](https://developer.apple.com/documentation/uikit/uiimage/1624127-resizableimagewithcapinsets) method allows the caller to specify a tiling or stretching resizing mode.
- The [UICollectionViewLayout](https://developer.apple.com/documentation/uikit/uicollectionviewlayout) class has changed:

  - The class now supports the customization of the animations created during rotation. The names of methods for customizing insert and delete animations have also changed, so the same hooks can be used for rotations as well as for insertions and deletions.
  - The class has changed some method names. Specifically, decoration views are no longer referred to by “reuse identifier” but rather by “element kind.” Apps that are using decoration views will need to modify their code and be rebuilt to accommodate this.
- The bottom edge of a [UILabel](https://developer.apple.com/documentation/uikit/uilabel) view is now different from its baseline.

  Previously, Auto Layout was interpreting the bottom of a `UILabel` to be the same as its baseline. While convenient in many cases, it caused problems if you wanted to place the top edge of one label against the bottom edge of another. In such a scenario, the bottom label would overlap the top one, and descenders from the top label could crash into ascenders from the bottom label. Now, Auto Layout interprets `UILayoutAttributeBottom` as the bottom of the text box (presuming the label is not bigger than its intrinsic content size) and `UILayoutAttributeBaseline` as the baseline of the text. If you have already created code for laying out labels according to the bottom or center point, your text will move around a little and you will need to adjust your constraints.
- Apps with table views in their nib or storyboard files, and that were built using previous versions of iOS 6 beta, will require a clean build with beta 3 and newer.
- Here are some notes regarding Auto Layout support for [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview):

  - In general, Auto Layout considers the top, left, bottom, and right edges of a view to be the _visible_ edges. That is, if you pin a view to the left edge of its superview, you’re really pinning it to the minimum x-value of the superview’s bounds. Changing the bounds origin of the superview does _not_ change the position of the view.
  - The `UIScrollView` class scrolls its content by changing the origin of its bounds. To make this work with Auto Layout, the top, left, bottom, and right edges _within_ a scroll view now mean the edges of its content view.
  - The constraints on the subviews of the scroll view must result in a size to fill, which is then interpreted as the content size of the scroll view. (This should not be confused with the [intrinsicContentSize](https://developer.apple.com/documentation/uikit/uiview/1622600-intrinsiccontentsize) method used for Auto Layout.) To size the scroll view’s `frame` with Auto Layout, constraints must either be explicit regarding the width and height of the scroll view, or the edges of the scroll view must be tied to views _outside_ of its subtree.
  - Note that you can make a subview of the scroll view appear to float (not scroll) over the other scrolling content by creating constraints between the view and a view outside the scroll view’s subtree, such as the scroll view’s superview.
  - Here are some examples of how to configure the scroll view:

    - Mixed approach:

      1. Position and size your scroll view with constraints external to the scroll view—that is, the [translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco) property is set to `NO`.
      2. Create a plain [UIView](https://developer.apple.com/documentation/uikit/uiview) content view for your scroll view that will be the size you want your content to have. Make it a subview of the scroll view but let it continue to translate the autoresizing mask into constraints:

```
UIView *contentView = [[UIView alloc]
    initWithFrame:CGRectMake(0,0,contentWidth,contentHeight)];
[scrollView addSubview:contentView];
// DON'T change contentView's translatesAutoresizingMaskIntoConstraints,
// which defaults to YES;
```
      3. Set the content size of the scroll view to match the size of the content view:

```
[scrollView setContentSize:CGMakeSize(contentWidth,contentHeight)];
```
      4. Create the views you want to put inside the content view and configure their constraints so as to position them within the content view.

         Alternatively, you can create a view subtree to go in the scroll view, set up your constraints, and call the [systemLayoutSizeFittingSize:](https://developer.apple.com/documentation/uikit/uiview/1622624-systemlayoutsizefittingsize) method (with the [UILayoutFittingCompressedSize](https://developer.apple.com/documentation/uikit/uiview/1622568-layoutfittingcompressedsize) option) to find the size you want to use for your content view and the [contentSize](https://developer.apple.com/documentation/uikit/uiscrollview/1619399-contentsize) property of the scroll view.
    - Pure Auto Layout approach:

      1. Set [translatesAutoresizingMaskIntoConstraints](https://developer.apple.com/documentation/uikit/uiview/1622572-translatesautoresizingmaskintoco) to `NO` on all views involved.
      2. Position and size your scroll view with constraints external to the scroll view.
      3. Use constraints to lay out the subviews within the scroll view, being sure that the constraints tie to all four edges of the scroll view and do not rely on the scroll view to get their size.

         A simple example would be a large image view, which has an intrinsic content size derived from the size of the image. In the [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) method of your view controller, you would include code like the following:

```
UIScrollView *scrollView = [[UIScrollView alloc] init];
UIImageView *imageView = [[UIImageView alloc] init];
[imageView setImage:[UIImage imageNamed:"MyReallyBigImage"]];
[self.view addSubview:scrollView];
[scrollView addSubview:imageView];

scrollView.translatesAutoresizingMaskIntoConstraints = NO;
imageView.translatesAutoresizingMaskIntoConstraints = NO;

NSDictionary *viewsDictionary = NSDictionaryOfVariableBindings(scrollView,imageView);
[self.view addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"H:|[scrollView]|" options:0 metrics: 0 viewsDictionary:viewsDictionary]];
[self.view addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:|[scrollView]|" options:0 metrics: 0 viewsDictionary:viewsDictionary]];
[scrollView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"H:|[imageView]|" options:0 metrics: 0 viewsDictionary:viewsDictionary]];
[scrollView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"V:|[imageView]|" options:0 metrics: 0 viewsDictionary:viewsDictionary]];
```

         This would give you a scroll view that resized as the view controller’s view resized (such as on device rotation), and the image view would be a scrolling subview. You don’t have to set the content size of the scroll view.
- Landscape-only apps that invoke a portrait-only view controller (such as the Game Center login screen) will cause the app to crash.

  Workaround:

  1. Apps should provide the delegate method `application:supportedIntefaceOrientationsForWindow` and ensure that portrait is one of the returned mask values.
  2. When a `UIBNavigationController` is involved, subclass the [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) and overriding [supportedInterfaceOrientations](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621435-supportedinterfaceorientations).

### WebKit and Safari

- WebKit on iOS now supports the `requestAnimationFrame` and `cancelAnimationFrame` methods in JavaScript, as described here: [http://www.w3.org/TR/animation-timing/](http://www.w3.org/TR/animation-timing/).

  - Note that because the specification is still at the Working Draft state, these methods have the `webkit` prefix, so they are `window.webkitRequestAnimationFrame` and `window.webkitCancelAnimationFrame`.
- The default app cache quota has increased from 5 MB to 25 MB.
- The JPEG subsampling threshold has increased from 2 MP (megapixels) to 5 MP on all supported hardware except iPhone 3GS and iPod touch (4th generation).
- Support has been added for `<input type="file">` tags in web forms. Users can upload existing photos and videos from their photo library or take a picture or video using the camera. Previously, this form control was always disabled.
- With Safari 6.0 on OS X, developers can now use the Web Inspector (web development tool) with attached iOS devices and iOS Simulator. Developers can use the Web Inspector to debug Safari and the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class in their own apps built and run from Xcode. This replaces the Debug Console banner in Safari.
- In iOS 6 and later, web data (SQL Web Storage and LocalStorage) from a [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) object can be stored in a directory that will be backed up. To enable backing up this data, set the `WebKitStoreWebDataForBackup` key to `YES` in your app’s user defaults. This should be done only if your app relies on web content data that cannot be reloaded. If your `UIWebView` object opens links to arbitrary web content, this key should be set to `NO`. Toggling the value of this key will not preserve existing web view data.
- In iOS 6 and later, Safari no longer registers for the common `feed:` RSS/ATOM scheme. Apps that can view those types of feeds are encouraged to register for that URL scheme.
- WebKit no longer always creates hardware-accelerated layers for elements with the `-webkit-transform: preserve-3d` option. Authors should stop using this option as a way to get hardware acceleration.
- As of iOS 6, embedded YouTube URLs in the form of `http://www.youtube.com/watch?v=oHg5SJYRHA0` will no longer work. These URLs are for viewing the video on the YouTube site, not for embedding in web pages. Instead, the format that should be used is described here: [https://developers.google.com/youtube/player_parameters](https://developers.google.com/youtube/player_parameters).
- In iOS 6, the [keyboardDisplayRequiresUserAction](https://developer.apple.com/documentation/uikit/uiwebview/1617967-keyboarddisplayrequiresuseractio) property was added to the `UIWebView` class. The property defaults to `YES`, which means that calling `focus()` on a form element will not bring up the keyboard. By changing the property to `NO`, a JavaScript call to `focus()` on a form element will focus the element and bring up the keyboard automatically.
- As of iOS 6, calling `focus()` on a form element in a web app will focus the element.
