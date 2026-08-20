---
title: Entitlement Key Reference
apple_id: TP40011195
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/AppSandboxTemporaryExceptionEntitlements.html
archived_at: '2026-07-15T08:17:10.403183Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Entitlement Key Reference](About%20Entitlements.md)


[Next](Document%20Revision%20History.md)[Previous](Enabling%20App%20Sandbox.md)

# App Sandbox Temporary Exception Entitlements

A temporary exception entitlement permits your macOS app to perform certain operations otherwise disallowed by App Sandbox.

If you need to request a temporary exception entitlement, use Apple’s [bug reporting system](https://bugreport.apple.com/) to let Apple know what’s not working for you. Apple considers feature requests as it develops the macOS platform.

To request a temporary exception entitlement for a target in an macOS Xcode project, add it to the target’s `.entitlements` property list file using the Xcode property list editor.

The value to provide for any temporary exception entitlement is a string or an array of one or more strings. For more information on using temporary exceptions in macOS, refer to [Designing for App Sandbox](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/DesigningYourSandbox/DesigningYourSandbox.html#//apple_ref/doc/uid/TP40011183-CH4) in _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

When you adopt App Sandbox, your app retains the ability to:

- Receive Apple events
- Send Apple events to itself
- Respond to Apple events it receives

However, with App Sandbox you cannot send Apple events to other apps unless you configure a `scripting-targets` entitlement or an `apple-events` temporary exception entitlement.

The `scripting-targets` entitlement is the preferred way to request the ability to send Apple events to apps that provide scripting access groups, as described in [App Sandbox Entitlement Keys](Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltk).

When an app you are scripting does not provide scripting access groups, use the `apple-events` temporary exception entitlement instead. This entitlement contains an array of strings, each of which should contain the bundle identifier of an app to which you want to send Apple events. For example, to enable sending Apple events to iPhoto from your app, you can pass an array containing a single string whose value is `com.apple.iphoto`.

The `scripting-targets` and `apple-events` entitlements are not mutually exclusive, even for a single target app. For example, if your app has a minimum OS version earlier than 10.8, when `scripting-targets` was introduced, and your app scripts the Apple Mail app to compose messages, you continue using the temporary entitlement (modified to include the suffix `:before:10.8`), while also including the `scripting-targets` entitlement for 10.8 and later compatibility, as show below:

```
<key>com.apple.security.temporary-exception.apple-events:before:10.8</key>
    <string>com.apple.mail</string>

<key>com.apple.security.scripting-targets</key>
<dict>
    <key>com.apple.mail</key>
    <array>
        <string>com.apple.mail.compose</string>
    </array>
</dict>
```

Entitlement keyCapability

com.apple.security.temporary-exception.apple-events

Enables sending of Apple events to one or more destination apps.

By default, sandboxed apps load only audio unit plugins that declare themselves to be safe for use in a sandbox. With this temporary exception, the user is instead asked for permission when the app attempts to load an unsafe (or undeclared) plugin.

Entitlement keyCapability

com.apple.security.temporary-exception.audio-unit-host

Enables hosting of audio components that are not designated as sandbox-safe. See _[Audio Components and the Application Sandbox](https://developer.apple.com/library/archive/technotes/tn2247/_index.html#//apple_ref/doc/uid/DTS40012567)_ for details.

With App Sandbox, lookup of global Mach services fails unless you configure the `mach-lookup.global.name` temporary exception entitlement. For each service that you want to enable, add the service as a string value for this entitlement key’s value array.

Entitlement keyCapability

com.apple.security.temporary-exception.mach-lookup.global-name

Enables lookup of one or more global Mach services.

With App Sandbox, dynamic registration of global Mach services fails unless you configure the `mach-register.global-name` temporary exception entitlement. For each service that you want to enable, add the service as a string value for this entitlement key’s value array.

Entitlement keyCapability

com.apple.security.temporary-exception.mach-register.global-name

Enables dynamic registration of one or more global Mach services.

With App Sandbox, your app has access only to its container, to its application group containers, to locations that are POSIX world-readable, and to locations in the file system that the user indicates direct intent to use, such as by interacting with an Open or Save dialog. If your app needs permanent access to other locations, you can bring additional locations into your sandbox by enabling the temporary exception entitlement keys described here.

For each path that you want to enable access to, specify the path as a string value for the appropriate entitlement key’s value array. Each string must start with a slash (`/`) character—whether it represents an absolute path or a path relative to the user’s home directory. If a path you provide specifies a directory rather a file, you must end the path with a slash character.

- For a `home-relative-path` temporary exception, provide a path relative to the user’s home directory; that is, relative to `~`
- For an `absolute-path` temporary exception, provide an absolute path; that is, relative to `/`

Do not use a read/write entitlement when a read-only entitlement will do.

Entitlement keyCapability

com.apple.security.temporary-exception.files.home-relative-path.read-only

Enables read-only access to the specified files or subdirectories in the user’s home directory.

com.apple.security.temporary-exception.files.home-relative-path.read-write

Enables read/write access to the specified files or subdirectories in the user’s home directory.

com.apple.security.temporary-exception.files.absolute-path.read-only

Enables read-only access to the specified files or directories at specified absolute paths.

com.apple.security.temporary-exception.files.absolute-path.read-write

Enables read/write access to the specified files or directories at specified absolute paths.

If you need to grant the ability to interact with other subclasses of [IOUserClient](https://developer.apple.com/documentation/kernel/iouserclient), use the following entitlement.

Entitlement keyCapability

com.apple.security.temporary-exception.iokit-user-client-class

Ability to specify additional [IOUserClient](https://developer.apple.com/documentation/kernel/iouserclient) subclasses to open or to set properties on.

If your app needs read-only or read/write access to a shared preference domain, use the following entitlements. Do not use a read/write entitlement when a read-only entitlement will do.

Entitlement keyCapability

com.apple.security.temporary-exception.shared-preference.read-only

Enables read-only access to the contents of the specified preference domain or domains in the user’s home directory.

com.apple.security.temporary-exception.shared-preference.read-write

Enables read/write access to the contents of the specified preference domain or domains in the user’s home directory.

[Next](Document%20Revision%20History.md)[Previous](Enabling%20App%20Sandbox.md)

