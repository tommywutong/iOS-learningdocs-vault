---
title: Audio Unit - Testing your custom Audio Unit in a sandboxed environment
apple_id: DTS40012796
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2012-09-10'
source_url: https://developer.apple.com/library/archive/qa/qa1483/_index.html
archived_at: '2026-07-18T02:31:23.106285Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1483

# Audio Unit - Testing your custom Audio Unit in a sandboxed environment

## Q:  I want to test my custom Audio Unit in a host that is sandboxed to check its behavior. Where can I get a sandboxed host like AU Lab to test with?

A: You can sandbox AU Lab (or any other other application) yourself from the command line using the [codesign](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/codesign.1.html#//apple_ref/doc/man/1/codesign) tool.

There are a few steps you need to perform prior to signing the application:

__1)__ Create an entitlements Property List file to specify the entitlements.

The following set of suggested entitlements for AU Lab will place the application in the most restrictive sandbox while still allowing it to function. You may add or remove entitlements as needed to test your Audio Unit in a variety of sandbox conditions.


```
<dict>
<key>com.apple.security.app-sandbox</key>
<true/>
<key>com.apple.security.device.microphone</key>
<true/>
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
<array>
<string>com.apple.midiserver</string>
<string>com.apple.midiserver.io</string>
</array>
<key>com.apple.security.temporary-exception.audio-unit-host</key>
<true/>
</dict>
```

- `com.apple.security.app-sandbox` :- this key turns on the application sandbox.
- `com.apple.security.device.microphone` :- this key allows the application to use audio input devices.
- `com.apple.security.files.user-selected.read-write` :- this key allows the application to read and write files selected by the user via an Open/Save dialog.
- `com.apple.security.temporary-exception.mach-lookup.global-name` :- in this case, this key/array value pair is used to enable communication with the MIDI server.
- `com.apple.security.temporary-exception.audio-unit-host` :- this key allows the application to open Audio Components that are __NOT__ sandbox safe thereby dropping the host application's sandbox, provided the user approves this action.

__2)__ Obtain a code signing identity by using the Certificate Assistant in the Keychain Access application.

You can also create a self-signed signing identity for testing purposes, or use the single character "-" (hyphen) for the identity for adhoc-signing. See the [Code Signing Tasks](https://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/Procedures/Procedures.html#//apple_ref/doc/uid/TP40005929-CH4-SW2) section of the Code Signing Guide for more information.

With the above tasks completed, you may now sign the application by using the command-line [codesign](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/codesign.1.html#//apple_ref/doc/man/1/codesign) tool:


```
codesign --entitlements /path/to/Foo.entitlements -f -s <identity> /path/to/AU\ Lab.app
```

For more information, see the [Code Signing Guide](https://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929-CH1-SW1) and [Audio Components and the Application Sandbox](https://developer.apple.com/library/mac/#technotes/tn2247/_index.html#//apple_ref/doc/uid/DTS40012567).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-09-10 | New document that discusses how to sandbox AULab so Audio Unit developers can test AU functionality in a fully sandboxed environment. |

