---
title: Audio Components and the Application Sandbox
apple_id: DTS40012567
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2013-03-06'
source_url: https://developer.apple.com/library/archive/technotes/tn2247/_index.html
archived_at: '2026-07-26T19:54:10.273090Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2247

# Audio Components and the Application Sandbox

This Tech Note describes how Audio Components can convey their resource usage requirements to the system, and how the system makes use of this information to resolve the conflict between the resource usage requirements of the Audio Component and the resources a host application's Sandbox allows access to.

[Audio Components vs. the Application Sandbox](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wugsbrfvke4vcbi4yq)[About Audio Components and the Component Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wugsbrfvauet2vkrpucvkejfhv6q2pjvie6tsfjzkfgx2bjzcf6vciivpugt2nkbhu4rkokrpu2qkoifdukuq)[Sandbox Safe Audio Components](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wugsbrfvke4vcbi4za)[Sandbox Safe Audio Components vs. the File System](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wugsbrfvke4vcbi42q)[Audio Components That Are Not Sandbox Safe](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wugsbrfvke4vcbi44a)[Hosting Audio Components in a Sandboxed Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wugsbrfvee6u2ujfheox2bkvcest27inhu2ucpjzcu4vctl5eu4x2bl5juctseijhvqrkel5avaucmjfbucvcjj5ha)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytenjwg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Audio Components vs. the Application Sandbox

The Application Sandbox is a security technology whose job it is to contain the damage that can be done to the system by a compromised application.

This is accomplished by the application voluntarily forgoing access to system resources such as the file system, network, communications with other processes or drivers and so forth. The application indicates what services it requires access to via entitlements that are attached to the application through its code signature. The system reads these entitlements from the code signature and Sandbox enforces the restrictions.

Audio Components are independent bundles of code which can perform tasks such as audio signal processing, encoding/decoding audio data, audio file parsing, and so forth. Applications load Audio Components into their process to take advantage of these abilities. An Audio Component, like any code, may require access to various system resources in order to do its job. This sets up the potential for conflict between the resources an Audio Component needs access to and the resources the host application's Sandbox allows access to.

[Back to Top](#)

## About Audio Components and the Component Manager

In OS X 10.6, the Audio Unit Framework added the `AudioComponent` API for loading and manipulating Audio Components by host applications. The `AudioComponent` API supplants the usage of the Component Manager for these tasks. It is important to note that the `AudioComponent` API provides access to both Audio Component-style plug-ins as well as Component Manager plug-ins. As such, any application targeting 10.6 or later should switch to the `AudioComponent` API. The Component Manager is officially deprecated as of OS X Mountain Lion.

For applications targeting earlier systems, the recommended approach is to use the `AudioComponent` API when running on Mac OS X 10.6 or later and to conditionally fall back to the Component Manager when running on earlier systems.

__Important:__ Using the `AudioComponent` API in the host application is required to take advantage of the support described in this Tech Note.

__Note:__ Audio Components can be built in such a way that the binary can be deployed as an Audio Component Plug-In on OS X 10.7 and later and as a Component Manager component on earlier systems. Please refer to [Tech Note TN2276](https://developer.apple.com/library/mac/#technotes/tn2276/_index.html) for more information.

__Important:__ Only Audio Component Plug-ins can declare themselves safe to open inside a sandboxed process. All Component Manager components are assumed to be unsafe to open in a sandboxed process.

[Back to Top](#)

## Sandbox Safe Audio Components

A "Sandbox Safe Audio Component" is defined to be an Audio Component that can function correctly in a process that has the most severely restricting Sandbox, where access to all system resources such as the file system, network, drivers in the kernel and so on have been curtailed. Such an Audio Component will never cause sandbox violations to be noted in the console logs.

An Audio Component indicates to the system that it is Sandbox Safe by including the "`sandboxSafe`" key in its description dictionary located in the `info.plist` of the containing bundle. This key is reflected in the `componentFlags` field of the `AudioComponentDescription` for the Audio Component with the constant, `kAudioComponentFlag_SandboxSafe`.

Listing 1 shows an example of a description dictionary for a hypothetical AudioUnit called MyExampleAU. This AudioUnit does all of its work without requiring access to any system resources and is completely Sandbox Safe. Note how this is expressed using the "`sandboxSafe`" key.

__Listing 1__  Setting the sandboxSafe key.

```
<dict>
    <key>description</key>
    <string>My Example AudioUnit</string>
    <key>factoryFunction</key>
    <string>MyExampleAUFactory</string>
    <key>manufacturer</key>
    <string>MYCO</string>
    <key>name</key>
    <string>My Company: MyExampleAU</string>
    <key>subtype</key>
    <string>EXAU</string>
    <key>type</key>
    <string>aufx</string>
    <key>version</key>
    <integer>65536</integer>

    <!-- Declare that this AudioComponent is Sandbox Safe -->

    <key>sandboxSafe</key>
    <true/>
</dict>
```

Audio Components can also be registered with the system dynamically with the Audio Component API call, `AudioComponentRegister`(). The caller informs the system that such an Audio Component is Sandbox Safe by setting the flag, `kAudioComponentFlag_SandboxSafe`, in the `AudioComponentDescription` passed to `AudioComponentRegister`(). Listing 2 demonstrates dynamic registration using same information from MyExampleAU above.

__Listing 2__  Registering Dynamically with the sandboxSafe flag.

```c
#include <AudioUnit/AudioComponent.h>
extern AudioComponentPlugInInterface*
                MyExampleAUFactoryFunction(const AudioComponentDescription *inDesc);

AudioComponent RegisterMyExampleAudioUnit()
{
    //	fill out the version number for the AU
    UInt32 theVersion = 0x00010000;

    //	fill out the AudioComponentDescription
    AudioComponentDescription theDescription;
    theDescription.componentType = kAudioUnitType_Effect;
    theDescription.componentSubType = 'EXAU';
    theDescription.componentManufacturer = 'MYCO';
    theDescription.componentFlagsMask = 0;

    //	Use the flag to indicate that this AudioComponent is Sandbox Safe
    theDescription.componentFlags = kAudioComponentFlag_SandboxSafe;

    //	call AudioComponentRegister()
    return AudioComponentRegister(&theDescription, CFSTR("My Company: MyExampleAU"),
                            theVersion, MyExampleAUFactoryFunction);
}
```

[Back to Top](#)

## Sandbox Safe Audio Components vs. the File System

The most common system service whose usage makes an Audio Component not be Sandbox Safe is the file system. As such, an Audio Component should make use of the system provided standard Open & Save dialogs to allow the user to locate necessary files as well as API services such as `NSSearchPathForDirectoriesInDomains`() to locate specific directories.

An Audio Component should also use security-scope bookmarks for dealing with persistent references to a file.

For more information on security-scoped bookmarks, see [Security-Scoped Bookmarks and Persistent Resource Access](https://developer.apple.com/library/mac/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in the [App Sandbox Design Guide](https://developer.apple.com/library/mac/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

An example of creating a securityscope bookmark for persistent storage is demonstrated in Listing 3 and resolving a security-scope bookmark is demonstrated in Listing 4.

__Listing 3__  Creating a Security-Scope Bookmark

```
CFDataRef CreateSecurityScopeBookMarkFromURL(CFURLRef inURL, CFURLRef inRelativeToURL,
                    bool inReadOnly, CFErrorRef* outError)
{
    //	set up the options we want
    CFURLBookmarkCreationOptions theOptions = kCFURLBookmarkCreationWithSecurityScope;
    if(inReadOnly)
    {
        theOptions |= kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess;
    }

    //	create the bookmark data
    return CFURLCreateBookmarkData(NULL, inURL, theOptions, NULL, inRelativeToURL, outError);
}
```

__Listing 4__  Resolving a Security-Scope Bookmark

```
CFURLRef CreateURLFrom SecurityScopeBookMark(CFDataRef inBookmarkData,
                    CFURLRef inRelativeToURL, CFErrorRef* outError)
{
    // Note that if inRelativeToURL is non-NULL, it must be a URL that points to the same
    // location that was used to create the bookmark data.

    return CFURLCreateByResolvingBookmarkData(NULL, inBookmarkData,
          kCFURLBookmarkResolutionWithSecurityScope, inRelativeToURL, NULL, NULL, outError);
}
```

[Back to Top](#)

## Audio Components That Are Not Sandbox Safe

If an Audio Component does not meet the requirements to be Sandbox Safe, it must declare to the system the system resources that it requires access to. This is done using the description dictionary in the Info.plist of the containing bundle with the "`resourceUsage`" key.

The "`resourceUsage`" value is a dictionary that has several defined keys that enumerate the system resources the Audio Component requires access to, these are:

- The "`iokit.user-client`" key. This key describes the IOKit user client objects the Audio Component will open. It is an array of the user clients' class names that the Audio Component needs to open connections to.
- The "`mach-lookup.global-name`" key. This key describes the Mach services the Audio Component needs to connect to. It is an array of the names of the services. Note that these services can be direct mach services found via `bootstrap_look_up`() or XPC services found via `xpc_connection_create_mach_service`().
- The "`network.client`" key. This key indicates that the Audio Component will receive data from the network. Its value is a `boolean`.
- The "`temporary-exception.files.all.read-write`" key. This key is a `boolean` that indicates that the Audio Component needs arbitrary access to the file system. This is for backward compatibility for Audio Components that have not yet adopted the usage of security-scope bookmarks and/or the usage of the standard file dialog for discovering, accessing and storing persistent references to files on the file system. In a future OS release, this key will not be supported.

If none of these keys are appropriate to describe the requirements of the Audio Component, the description dictionary should either not be present or should be empty.

The system will compare the resource usage information provided by the Audio Component with what the host process's sandbox allows. If the Audio Component’s resource usage is completely allowed by the sandbox, the Audio Component is considered Sandbox Safe for that process. Such an Audio Component will automatically have the flag, `kAudioComponentFlag_SandboxSafe` set on it and it will always be allowed to be loaded into that host process.

Listing 5 shows an example dictionary for an AudioUnit that requires all four kinds of resources.

__Listing 5__  Filling out the Resource Usage Dictionary.

```
<dict>
    <key>type</key>
    <string>aufx</string>
    <key>subtype</key>
    <string>XMPL</string>
    <key>manufacturer</key>
    <string>ACME</string>
    <key>name</key>
    <string>AUExample</string>
    <key>version</key>
    <integer>12345</integer>
    <key>factoryFunction</key>
    <string>AUExampleFactory</string>

    <!-- This AU is not sandbox safe so describe it's resource usage -->

    <key>resourceUsage</key>
    <dict>
        <key>iokit.user-client</key>
        <array>
            <string>CustomUserClient1</string>
            <string>CustomUserClient2</string>
        </array>
        <key>mach-lookup.global-name</key>
        <array>
            <string>MachServiceName1</string>
            <string>MachServiceName2</string>
        </array>
        <key>network.client</key>
        <true/>
        <key>temporary-exception.files.all.read-write</key>
        </true>
    </dict>
</dict>
```

__Important:__ A dynamically registered Audio Component __cannot__ declare its resource usage. It is either Sandbox Safe or not as indicated by the presence or absence of the `kAudioComponentFlag_SandboxSafe` component flag in the `AudioComponentDescription` passed to `AudioComponentRegister`().

[Back to Top](#)

## Hosting Audio Components in a Sandboxed Application

There are several approaches a sandboxed application can take regarding loading Audio Components. The simplest method is for the application to only support loading Audio Components that are Sandbox Safe. This can be accomplished by setting the flag, `kAudioComponentFlag_SandboxSafe`, in the `AudioComponentDescription` passed to the `AudioComponent` API call, `AudioComponentFindNext`() when searching for Audio Components to load.

__Listing 6__  Enumerate Sandbox Safe Audio Components.

```c
#include <AudioUnit/AudioComponent.h>
extern void ProcessFoundAudioComponent(AudioComponent inComponent);

void EnumerateSandboxSafeAudioComponents()
{
    //	make a description that includes all wildcards except for the flags and flags
    //	mask so that we traverse all the AudioComponents that are sandbox safe
    AudioComponent theComponent;
    AudioComponentDescription theDescription;
    memset(&theDescription, 0, sizeof(theDescription));

    //	Use the flag to indicate that we want to find Sandbox Safe AudioComponents
    theDescription.componentFlags = kAudioComponentFlag_SandboxSafe;
    theDescription.componentFlagsMask = kAudioComponentFlag_SandboxSafe;

    //	get the first AudioComponent
    theComponent = AudioComponentFindNext(NULL, &theDescription);
    while(theComponent != NULL)
    {
        //	process the AudioComponent
        ProcessFoundAudioComponent(theComponent);

        //	get the next one in the list
        theComponent = AudioComponentFindNext(theComponent, &theDescription);
    }
}
```

If an application wishes to open Audio Components that are not Sandbox Safe, the application must be signed with the entitlement "`com.apple.security.temporary-exception.audio-unit-host`". Any attempt to open an Audio Component that isn't Sandbox Safe by an application that does not have this entitlement will fail.

When an application with the "`com.apple.security.temporary-exception.audio-unit-host`" entitlement tries to open an Audio Component that isn't Sandbox Safe, the system will show the user a dialog indicating that the process is attempting to open an Audio Component that isn't Sandbox Safe.

If the user does not approve of the action, the open attempt will fail and the user will see the dialog again the next time the application tries to open an Audio Component that isn't Sandbox Safe. If the user approves of the action, the system will disable the host application's sandbox, the attempt to open the Audio Component will succeed and any further attempts to open an Audio Component that isn't Sandbox Safe will succeed without the user seeing the dialog. Also, the system will remember the user's response so that if the application tries to open the same Audio Component in the future, it will succeed without showing the dialog to the user.

Many applications build up a list of the various Audio Components and their capabilities. Since querying an Audio Component to find out what it does requires opening the Audio Component, this may cause the application's sandbox to drop even if the application never uses any of the queried Audio Components.

To avoid dropping the application's sandbox while querying components, the new `AudioComponentCopyConfigurationInfo`() API can be used. This call returns a dictionary containing information about the capabilities of the Audio Component. The keys returned in this dictionary depend on the kind of Audio Component. For Audio Codecs and Audio File Components, there are no defined keys. For Audio Units, the keys are defined in <`AudioUnit/AudioUnitProperties.h`> and include such things as whether the Audio Unit has a custom view (`kAudioUnitConfigurationInfo_HasCustomView`) and the channel configurations (`kAudioUnitConfigurationInfo_ChannelConfigurations`) the Audio unit may be configured for and so on.

__Listing 7__  Example ConfigInfo dictionary returned by `AudioComponentCopyConfigurationInfo`.

```
// The contents of this dictionary is different for each Audio Unit.
// Some will have all the defined keys some will have none.
// This is the plist form of the ConfigInfo dictionary for the AUSampler Audio Unit.

<dict>
    <key>ChannelConfigurations</key>
    <array>
        <array>
            <integer>0</integer>
            <integer>-16</integer>
        </array>
    </array>
    <key>HasCustomView</key>
    <true/>
    <key>InitialOutputs</key>
    <array>
        <integer>2</integer>
    </array>
</dict>
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-03-06 | Editorial |
| 2012-07-31 | New document that describes how Audio Components convey their resource usage requirements to the system to work within a host application's Sandbox. |

