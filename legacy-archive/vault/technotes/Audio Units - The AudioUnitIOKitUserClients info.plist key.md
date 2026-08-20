---
title: Audio Units - The AudioUnit_IOKitUserClients info.plist key
apple_id: DTS40011955
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-03-06'
source_url: https://developer.apple.com/library/archive/technotes/tn2296/_index.html
archived_at: '2026-07-26T19:54:10.204769Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2296

# Audio Units - The AudioUnit_IOKitUserClients info.plist key

This Technical Note discusses the `AudioUnit_IOKitUserClients` info.plist key necessary for allowing audio unit plugins to talk to custom drivers in a fully sandboxed process.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvguwugsbrfvke4vcbi4yq)[Using the AudioUnit_IOKitUserClients key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvguwugsbrfvke4vcbi4za)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The purpose of the `AudioUnit_IOKitUserClients` key in an audio unit plugins info.plist file is to have the audio unit inform the system of its entitlement requirements in a fully sandboxed process. When an audio unit needs to communicate with a custom driver, setting this key applies the appropriate entitlements to the process loading the audio unit plugin thereby allowing the audio unit access to a custom driver.

[Back to Top](#)

## Using the AudioUnit_IOKitUserClients key

An audio unit plugin may create user-clients by calling `IOServiceOpen` for standard IOKit objects without restriction. However, if an audio unit plugin needs to create a custom user-client, it must explicity list the class name(s) of the user-client(s) in its bundles info.plist specified by the `AudioUnit_IOKitUserClients` key. The value of this key is an array of user-client class names.

__Listing 1__  Adding the `AudioUnit_IOKitUserClients` key to an audio unit plugins info.plist.

```
<key>AudioUnit_IOKitUserClients</key>
    <array>
        <string>com_mycompany_driver_UserClient1</string>
        <string>com_mycompany_driver_UserClient2</string>
    </array>
```

__Note:__ In the above listing, "`com_mycompany_driver_UserClient1`" and "`com_mycompany_driver_UserClient2`" are the full names of the subclasses of IOKit's `IOUserClient` class, or a subclass of one of the Apple supplied user-client classes (e.g. `IOAudioEngineUserClient`) that the audio unit wants to create with calls to `IOServiceOpen`.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-03-06 | New document that discusses the AudioUnit_IOKitUserClients key required by Audio Units that need to talk to custom drivers in a fully sandboxed process. |

