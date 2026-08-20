---
title: Understanding the UIRequiredDeviceCapabilities key
apple_id: DTS40009877
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2013-08-15'
source_url: https://developer.apple.com/library/archive/qa/qa1397/_index.html
archived_at: '2026-07-18T02:30:31.492946Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1397

# Understanding the UIRequiredDeviceCapabilities key

## Q:  What is UIRequiredDeviceCapabilities?

A: `UIRequiredDeviceCapabilities` is a property list key that indicates the specific hardware features your application requires in order to run on a device. Read the [UIRequiredDeviceCapabilities](../documentation/General/Information%20Property%20List%20Key%20Reference/iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomy) section of the Information Property List Key Reference to get a complete list of these keys.

You should only include a key if you absolutely need to limit your application's target devices. Setting a key to `false` is not the same as leaving out the key. Therefore, each key effectively has three states:

- `true`: Devices __must have__ the associated feature in order to run your application.
- `false`: Devices __must not have__ the associated feature in order to run your application.
- `non-existent`: Devices __may__ or __may not have__ the associated feature in order to run your application (in other words, you don't care either way).

For instance:

- Setting the `telephony` key to `true` will prevent your application from installing for iPod touch users (because the device "must have" telephony capabilities).
- Setting the `telephony` key to `false` will prevent it from installing for iPhone users (because the device "must not have" telephony capabilities).
- Leaving out the `telephony` key will allow it to install regardless of the presence of telephony capabilities (because you "do not care" if the device has telephony capabilities).

Do not add a `UIRequiredDeviceCapabilities` key unless you actively need to restrict installation of your application based on the availability or lack of availability of a device feature.

See the [Adding Keys to an Information Property List File](../documentation/General/Information%20Property%20List%20Key%20Reference/About%20Information%20Property%20List%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjufvjvomy) section of the Information Property List Key Reference to learn how to add keys to your `Info.plist`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-15 | Updated documentation link. |
| 2010-06-30 | Updated documentation link. |
| 2010-05-07 | Updated documentation link. |
| 2010-03-30 | New document that describes how to add required device-related features for your application. |

