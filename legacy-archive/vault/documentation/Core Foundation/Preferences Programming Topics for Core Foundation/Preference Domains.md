---
title: Preferences Programming Topics for Core Foundation
apple_id: 10000129i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/Concepts/PreferenceDomains.html
archived_at: '2026-07-15T07:22:43.640406Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preferences Programming Topics for Core Foundation](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Using%20the%20High-Level%20Preferences%20API.md)[Previous](Application%20IDs.md)

# Preference Domains

When creating a new preference or searching for an existing one, Core Foundation uses the notion of “Preference Domains” to specify the scope and location of the preference. A preference domain consists of three pieces of information, an application ID, a host name, and a user name. [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dqlkcineuissbi5ca) shows all of the preference domains, listed in the order that they are searched when attempting to locate a preference value.

__Table 1__  Preference Domains in search order

| 1 | Current User | Current Application | Current Host |
| 2 | Current User | Current Application | Any Host |
| 3 | Current User | Any Application | Current Host |
| 4 | Current User | Any Application | Any Host |
| 5 | Any User | Current Application | Current Host |
| 6 | Any User | Current Application | Any Host |
| 7 | Any User | Any Application | Current Host |
| 8 | Any User | Any Application | Any Host |

When using the high-level preferences functions [CFPreferencesSetAppValue](https://developer.apple.com/documentation/corefoundation/1515528-cfpreferencessetappvalue), and [CFPreferencesCopyAppValue](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue), you need only specify the application ID. The first function, `CFPreferencesSetAppValue`, places the preference value into the “Current User” and “Any Host” domain for the application, meaning that the standard location for application preferences is domain number two as listed in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dqlkcineuissbi5ca). The other function, `CFPreferencesCopyAppValue`, searches through all the domains in order until a value is found. See [Using the High-Level Preferences API](Using%20the%20High-Level%20Preferences%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dslkdjjbekscbifdq) for information on using these functions.

If you need to specify an exact domain for your preference values you can use the low-level preferences functions `CFPreferencesSetValue`, and `CFPreferencesCopyValue`. These functions allow you to specify all three of the domain qualifiers when setting or searching for preferences. When using these functions you cannot pass arbitrary host and user names; you must instead use the appropriate “Any” or “Current” constants given in the list below. For the application domain qualifier, you can either pass the application ID or one of the “Any” or “Current” application constants given in the list below. See [Using the Low-Level Preferences API](Using%20the%20Low-Level%20Preferences%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3talkdjjbekscbifdq) for information on using these functions.

|  |  |
| --- | --- |
| [kCFPreferencesAnyApplication](https://developer.apple.com/documentation/corefoundation/kcfpreferencesanyapplication) |  |
| [kCFPreferencesCurrentApplication](https://developer.apple.com/documentation/corefoundation/kcfpreferencescurrentapplication) |  |
| [kCFPreferencesAnyHost](https://developer.apple.com/documentation/corefoundation/kcfpreferencesanyhost) |  |
| [kCFPreferencesCurrentHost](https://developer.apple.com/documentation/corefoundation/kcfpreferencescurrenthost) |  |
| [kCFPreferencesAnyUser](https://developer.apple.com/documentation/corefoundation/kcfpreferencesanyuser) |  |
| [kCFPreferencesCurrentUser](https://developer.apple.com/documentation/corefoundation/kcfpreferencescurrentuser) |  |

[Next](Using%20the%20High-Level%20Preferences%20API.md)[Previous](Application%20IDs.md)

