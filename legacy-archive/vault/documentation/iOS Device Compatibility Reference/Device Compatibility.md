---
title: iOS Device Compatibility Reference
apple_id: TP40013599
resource_type: Guide
platform: iOS
topic: Data Management
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/DeviceCompatibilityMatrix/DeviceCompatibilityMatrix.html
archived_at: '2026-07-15T07:31:54.485656Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [iOS Device Compatibility Reference](Introduction.md)


[Next](Displays.md)[Previous](Introduction.md)

# Device Compatibility

The [information property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/InfoPlist.html#//apple_ref/doc/uid/TP40008195-CH61) (`Info.plist`) file contains critical information about your app’s configuration and must be included in your app bundle. Every new project you create in Xcode has a default `Info.plist` file configured with some basic information about your project. You can modify this file to specify additional configuration details for your app.

The `UIRequiredDeviceCapabilities` key lets you declare the hardware or specific capabilities that your app needs in order to run. All apps are required to have this key in their `Info.plist` file. The App Store uses the contents of this key to prevent users from downloading your app onto a device that cannot possibly run it. The tables in this chapter show all iOS devices and their capabilities.

The value of the `UIRequiredDeviceCapabilities` key is either an [array or a dictionary](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) that contains additional keys identifying features your app requires (or specifically prohibits). If you specify the value of the key using an array, the presence of a key indicates that the feature is required; the absence of a key indicates that the feature is not required and that the app can run without it. If you specify a dictionary instead, each key in the dictionary must have a Boolean value that indicates whether the feature is required or prohibited. A value of `true` indicates the feature is required and a value of `false` indicates that the feature must _not_ be present on the device. If a given capability is optional for your app, do not include the corresponding key in the dictionary.

For the list of possible `UIRequiredDeviceCapabilities` keys, see [UIRequiredDeviceCapabilities](../General/Information%20Property%20List%20Key%20Reference/iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomy) in _[Information Property List Key Reference](../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_. Be sure to include keys only for the features that your app absolutely requires. If your app can run without a specific feature, do not include the corresponding key. For detailed information on how to create and edit property lists, see _[Information Property List Key Reference](../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

The sections that follow detail the compatibility of each iOS device model with all `UIRequiredDeviceCapabilities` keys.

[Table 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjxfvjvooi), [Table 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjxfvjvomjt), and [Table 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjxfvjvomy) list the capabilities for iPhone devices.

__Table 1-1__  iPhone 6, iPhone 7, iPhone 8, iPhone X, and iPhone SE device compatibility

| Compatibility | iPhone 8  iPhone 8 Plus  iPhone X | iPhone 7  iPhone 7 Plus | iPhone 6s  iPhone 6s Plus | iPhone SE | iPhone 6  iPhone 6 Plus |
| accelerometer | X | X | X | X | X |
| arkit | X | X | X | X |  |
| armv6 | X | X | X | X | X |
| armv7 | X | X | X | X | X |
| arm64 | X | X | X | X | X |
| __auto-focus-camera__ | X | X | X | X | X |
| __bluetooth-le__ | X | X | X | X | X |
| __camera-flash__ | X | X | X | X | X |
| __front-facing-camera__ | X | X | X | X | X |
| gamekit | X | X | X | X | X |
| gps | X | X | X | X | X |
| __gyroscope__ | X | X | X | X | X |
| __healthkit__ | X | X | X | X | X |
| location-services | X | X | X | X | X |
| __magnetometer__ | X | X | X | X | X |
| __metal__ | X | X | X | X | X |
| microphone | X | X | X | X | X |
| nfc | X | X |  |  |  |
| opengles-1 | X | X | X | X | X |
| __opengles-2__ | X | X | X | X | X |
| __opengles-3__ | X | X | X | X | X |
| peer-peer | X | X | X | X | X |
| sms | X | X | X | X | X |
| still-camera | X | X | X | X | X |
| telephony | X | X | X | X | X |
| __video-camera__ | X | X | X | X | X |
| wifi | X | X | X | X | X |

__Table 1-2__  iPhone 4 and iPhone 5 device compatibility

| Compatibility | iPhone 4 | iPhone 4s | iPhone 5 | iPhone 5c | iPhone 5s |
| accelerometer | X | X | X | X | X |
| arkit |  |  |  |  |  |
| armv6 | X | X | X | X | X |
| armv7 | X | X | X | X | X |
| arm64 |  |  |  |  | X |
| __auto-focus-camera__ | X | X | X | X | X |
| __bluetooth-le__ |  | X | X | X | X |
| __camera-flash__ | X | X | X | X | X |
| __front-facing-camera__ | X | X | X | X | X |
| gamekit | X | X | X | X | X |
| gps | X | X | X | X | X |
| __gyroscope__ | X | X | X | X | X |
| __healthkit__ |  | X | X | X | X |
| location-services | X | X | X | X | X |
| __magnetometer__ | X | X | X | X | X |
| __metal__ |  |  |  |  | X |
| microphone | X | X | X | X | X |
| nfc |  |  |  |  |  |
| opengles-1 | X | X | X | X | X |
| __opengles-2__ | X | X | X | X | X |
| __opengles-3__ |  |  |  |  | X |
| peer-peer | X | X | X | X | X |
| sms | X | X | X | X | X |
| still-camera | X | X | X | X | X |
| telephony | X | X | X | X | X |
| __video-camera__ | X | X | X | X | X |
| wifi | X | X | X | X | X |

__Table 1-3__  iPhone and iPhone 3G device compatibility

| Compatibility | iPhone | iPhone 3G | iPhone 3GS | iPhone 3GS (China) |
| accelerometer | X | X | X | X |
| arkit |  |  |  |  |
| armv6 | X | X | X | X |
| armv7 |  |  | X | X |
| arm64 |  |  |  |  |
| __auto-focus-camera__ |  |  | X | X |
| __bluetooth-le__ |  |  |  |  |
| __camera-flash__ |  |  |  |  |
| __front-facing-camera__ |  |  |  |  |
| gamekit |  |  | X | X |
| gps |  | X | X | X |
| __gyroscope__ |  |  |  |  |
| __healthkit__ |  |  |  |  |
| location-services | X | X | X | X |
| __magnetometer__ |  |  | X | X |
| __metal__ |  |  |  |  |
| microphone | X | X | X | X |
| nfc |  |  |  |  |
| opengles-1 | X | X | X | X |
| __opengles-2__ |  |  | X | X |
| __opengles-3__ |  |  |  |  |
| peer-peer |  | X | X | X |
| sms | X | X | X | X |
| still-camera | X | X | X | X |
| telephony | X | X | X | X |
| __video-camera__ |  |  | X | X |
| wifi | X | X | X |  |

Table 1-4, [Table 1-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjxfvjvona), [Table 1-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjxfvjvomjr), and [Table 1-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjxfvjvoni) list the capabilities for iPad devices.

__Table 1-4__  iPad Pro device compatibility

| Compatibility | iPad Pro (12.9-inch)  Wi-Fi | iPad Pro (12.9-inch)  Wi-Fi + Cellular | iPad Pro (9.7-inch)  Wi-Fi | iPad Pro (9.7-inch)  Wi-Fi + Cellular | iPad Pro 12.9-inch (2nd generation)  Wi-Fi | iPad Pro 12.9-inch (2nd generation)  Wi-Fi + Cellular | iPad Pro (10.5-inch)  Wi-Fi | iPad Pro (10.5-inch)  Wi-Fi + Cellular |
| accelerometer | X | X | X | X | X | X | X | X |
| arkit | X | X | X | X | X | X | X | X |
| armv6 | X | X | X | X | X | X | X | X |
| armv7 | X | X | X | X | X | X | X | X |
| arm64 | X | X | X | X | X | X | X | X |
| __auto-focus-camera__ | X | X | X | X | X | X | X | X |
| __bluetooth-le__ | X | X | X | X | X | X | X | X |
| __camera-flash__ |  |  | X | X | X | X | X | X |
| __front-facing-camera__ | X | X | X | X | X | X | X | X |
| gamekit | X | X | X | X | X | X | X | X |
| gps |  | X |  | X |  | X |  | X |
| __gyroscope__ | X | X | X | X | X | X | X | X |
| __healthkit__ |  |  |  |  |  |  |  |  |
| location-services | X | X | X | X | X | X | X | X |
| __magnetometer__ | X | X | X | X | X | X | X | X |
| __metal__ | X | X | X | X | X | X | X | X |
| microphone | X | X | X | X | X | X | X | X |
| nfc |  |  |  |  |  |  |  |  |
| opengles-1 | X | X | X | X | X | X | X | X |
| __opengles-2__ | X | X | X | X | X | X | X | X |
| __opengles-3__ | X | X | X | X | X | X | X | X |
| peer-peer | X | X | X | X | X | X | X | X |
| sms |  |  |  |  |  |  |  |  |
| still-camera | X | X | X | X | X | X | X | X |
| telephony |  |  |  |  |  |  |  |  |
| __video-camera__ | X | X | X | X | X | X | X | X |
| wifi | X | X | X | X | X | X | X | X |

__Table 1-5__  iPad (4th generation), iPad Air, and iPad (5th generation) device compatibility

| Compatibility | iPad  Wi-Fi  (4th gen) | iPad  Wi-Fi + Cellular  (4th gen) | iPad Air  Wi-Fi | iPad Air  Wi-Fi + Cellular | iPad Air 2  Wi-Fi | iPad Air 2  Wi-Fi + Cellular | iPad (5th generation)  Wi-Fi | iPad (5th generation)  Wi-Fi + Cellular |
| accelerometer | X | X | X | X | X | X | X | X |
| arkit |  |  |  |  |  |  | X | X |
| armv6 | X | X | X | X | X | X | X | X |
| armv7 | X | X | X | X | X | X | X | X |
| arm64 |  |  | X | X | X | X | X | X |
| __auto-focus-camera__ | X | X | X | X | X | X | X | X |
| __bluetooth-le__ | X | X | X | X | X | X | X | X |
| __camera-flash__ |  |  |  |  |  |  |  |  |
| __front-facing-camera__ | X | X | X | X | X | X | X | X |
| gamekit | X | X | X | X | X | X | X | X |
| gps |  | X |  | X |  | X |  | X |
| __gyroscope__ | X | X | X | X | X | X | X | X |
| __healthkit__ |  |  |  |  |  |  |  |  |
| location-services | X | X | X | X | X | X | X | X |
| __magnetometer__ | X | X | X | X | X | X | X | X |
| __metal__ |  |  | X | X | X | X | X | X |
| microphone | X | X | X | X | X | X | X | X |
| nfc |  |  |  |  |  |  |  |  |
| opengles-1 | X | X | X | X | X | X | X | X |
| __opengles-2__ | X | X | X | X | X | X | X | X |
| __opengles-3__ |  |  | X | X | X | X | X | X |
| peer-peer | X | X | X | X | X | X | X | X |
| sms |  |  |  |  |  |  |  |  |
| still-camera | X | X | X | X | X | X | X | X |
| telephony |  |  |  |  |  |  |  |  |
| __video-camera__ | X | X | X | X | X | X | X | X |
| wifi | X | X | X | X | X | X | X | X |

__Table 1-6__  iPad mini device compatibility

| Compatibility | iPad mini  Wi-Fi | iPad mini  Wi-Fi + Cellular | iPad mini 2  Wi-Fi | iPad mini 2  Wi-Fi + Cellular | iPad mini 3  Wi-Fi | iPad mini 3  Wi-Fi + Cellular | iPad mini 4  Wi-Fi | iPad mini 4  Wi-Fi + Cellular |
| accelerometer | X | X | X | X | X | X | X | X |
| arkit |  |  |  |  |  |  |  |  |
| armv6 | X | X | X | X | X | X | X | X |
| armv7 | X | X | X | X | X | X | X | X |
| arm64 |  |  | X | X | X | X | X | X |
| __auto-focus-camera__ | X | X | X | X | X | X | X | X |
| __bluetooth-le__ | X | X | X | X | X | X | X | X |
| __camera-flash__ |  |  |  |  |  |  |  |  |
| __front-facing-camera__ | X | X | X | X | X | X | X | X |
| gamekit | X | X | X | X | X | X | X | X |
| gps |  | X |  | X |  | X |  | X |
| __gyroscope__ | X | X | X | X | X | X | X | X |
| __healthkit__ |  |  |  |  |  |  |  |  |
| location-services | X | X | X | X | X | X | X | X |
| __magnetometer__ | X | X | X | X | X | X | X | X |
| __metal__ |  |  | X | X | X | X | X | X |
| microphone | X | X | X | X | X | X | X | X |
| nfc |  |  |  |  |  |  |  |  |
| opengles-1 | X | X | X | X | X | X | X | X |
| __opengles-2__ | X | X | X | X | X | X | X | X |
| __opengles-3__ |  |  | X | X | X | X | X | X |
| peer-peer | X | X | X | X | X | X | X | X |
| sms |  |  |  |  |  |  |  |  |
| still-camera | X | X | X | X | X | X | X | X |
| telephony |  |  |  |  |  |  |  |  |
| __video-camera__ | X | X | X | X | X | X | X | X |
| wifi | X | X | X | X | X | X | X | X |

__Table 1-7__  iPad 1, iPad 2, and iPad (3rd generation) device compatibility

| Compatibility | iPad  Wi-Fi | iPad  Wi-Fi + 3G | iPad 2  Wi-Fi | iPad 2  Wi-Fi + 3G | iPad  Wi-Fi  (3rd gen) | iPad  Wi-Fi + Cellular  (3rd gen) |
| accelerometer | X | X | X | X | X | X |
| arkit |  |  |  |  |  |  |
| armv6 | X | X | X | X | X | X |
| armv7 | X | X | X | X | X | X |
| arm64 |  |  |  |  |  |  |
| __auto-focus-camera__ |  |  |  |  | X | X |
| __bluetooth-le__ |  |  |  |  | X | X |
| __camera-flash__ |  |  |  |  |  |  |
| __front-facing-camera__ |  |  | X | X | X | X |
| gamekit | X | X | X | X | X | X |
| gps |  | X |  | X |  | X |
| __gyroscope__ |  |  | X | X | X | X |
| __healthkit__ |  |  |  |  |  |  |
| location-services | X | X | X | X | X | X |
| __magnetometer__ | X | X | X | X | X | X |
| __metal__ |  |  |  |  |  |  |
| microphone | X | X | X | X | X | X |
| nfc |  |  |  |  |  |  |
| opengles-1 | X | X | X | X | X | X |
| __opengles-2__ | X | X | X | X | X | X |
| __opengles-3__ |  |  |  |  |  |  |
| peer-peer | X | X | X | X | X | X |
| sms |  |  |  |  |  |  |
| still-camera |  |  | X | X | X | X |
| telephony |  |  |  |  |  |  |
| __video-camera__ |  |  | X | X | X | X |
| wifi | X | X | X | X | X | X |

Table 1-8 list the capabilities for iPod touch devices.

__Table 1-8__  iPod touch device compatibility

| Compatibility | iPod touch | iPod touch  2nd gen | iPod touch  3rd gen | iPod touch  4th gen | iPod touch  5th gen | iPod touch  5th gen 16GB (no rear-facing camera) | iPod touch  6th gen |
| accelerometer | X | X | X | X | X | X | X |
| arkit |  |  |  |  |  |  |  |
| armv6 | X | X | X | X | X | X | X |
| armv7 |  |  | X | X | X | X | X |
| arm64 |  |  |  |  |  |  | X |
| __auto-focus-camera__ |  |  |  |  | X |  | X |
| __bluetooth-le__ |  |  |  |  | X | X | X |
| __camera-flash__ |  |  |  |  | X |  | X |
| __front-facing-camera__ |  |  |  | X | X | X | X |
| gamekit |  | X | X | X | X | X | X |
| gps |  |  |  |  |  |  |  |
| __gyroscope__ |  |  |  | X | X | X | X |
| __healthkit__ |  |  |  |  | X | X | X |
| location-services | X | X | X | X | X | X | X |
| __magnetometer__ |  |  |  |  |  |  |  |
| __metal__ |  |  |  |  |  |  | X |
| microphone |  | X | X | X | X | X | X |
| nfc |  |  |  |  |  |  |  |
| opengles-1 | X | X | X | X | X | X | X |
| __opengles-2__ |  |  | X | X | X | X | X |
| __opengles-3__ |  |  |  |  |  |  | X |
| peer-peer |  | X | X | X | X | X | X |
| sms |  |  |  |  |  |  |  |
| still-camera |  |  |  | X | X |  | X |
| telephony |  |  |  |  |  |  |  |
| __video-camera__ |  |  |  | X | X |  | X |
| wifi | X | X | X | X | X | X | X |

[Next](Displays.md)[Previous](Introduction.md)

