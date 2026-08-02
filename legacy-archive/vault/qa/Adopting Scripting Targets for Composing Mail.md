---
title: Adopting Scripting Targets for Composing Mail
apple_id: DTS40013831
resource_type: QA
platform: macOS
topic: Interapplication Communication
technology: null
published: '2013-10-10'
source_url: https://developer.apple.com/library/archive/qa/qa1802/_index.html
archived_at: '2026-07-18T02:34:53.072033Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1802

# Adopting Scripting Targets for Composing Mail

## Q:  How do I use Scripting Targets to replace the temporary sandbox entitlement for composing a message in Apple Mail?

A: Temporary sandboxing entitlements are granted on a short-term basis and will be phased out over time. One such temporary entitlement is the ability to script the Apple Mail app to compose messages.

OS X 10.8 (Mountain Lion) introduced the concept of Scripting Targets. This gives the developers of a target app the ability to expose the functionality they want to be scriptable, and provides a mechanism for scripting that target app without the need for temporary entitlements.

Apple Mail adopts [Scripting Targets](https://developer.apple.com/library/mac/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW25) for composing mail. If your app uses a temporary entitlement to script Apple Mail for the purposes of composing messages, you will need to migrate to Scripting Targets.

Specifically, if your app composes messages in Apple Mail using AppleScript, and

- has a minimum OS of 10.8, and
- uses the `com.apple.security.temporary-exception.apple-events` entitlement with a value of `com.apple.mail`

replace it with the

- `com.apple.security.scripting-targets` entitlement
- with a key of `com.apple.mail`
- and an array with a string value of `com.apple.mail.compose`.

See Listing 1 for an example plist entry.

__Listing 1__  Using Scripting Targets to compose messages in Apple Mail.

```
<key>com.apple.security.scripting-targets</key>
<dict>
    <key>com.apple.mail</key>
    <array>
        <string>com.apple.mail.compose</string>
    </array>
</dict>
```

You will not need to change your AppleScript code.

If your app scripts Mail to do more than compose messages, you can continue using the temporary entitlement. Please file bugs indicating what you're scripting Mail to do, so engineering can investigate potential replacements using Scripting Targets. (You should also include the Scripting Targets entitlement if your app composes messages.)

If your app has a minimum OS earlier than 10.8, you will also need to continue using the temporary entitlement, but will need to modify it to include `:before:10.8`. You will also need to add the Scripting Targets entitlement for 10.8 and later compatibility. See Listing 2 for the modified temporary entitlement.

__Listing 2__  Modifying the Apple Events temporary exception for use prior to 10.8.

```
<key>com.apple.security.temporary-exception.apple-events:before:10.8</key>
    <string>com.apple.mail</string>
```

For more information, watch [Secure Automation Techniques in OS X](https://developer.apple.com/videos/wwdc/2012/?id=206).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-10-10 | New document that shows how to use Scripting Targets for composing Apple Mail messages instead of using temporary sandboxing entitlements. |

