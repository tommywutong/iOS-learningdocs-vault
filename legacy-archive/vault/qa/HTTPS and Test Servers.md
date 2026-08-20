---
title: HTTPS and Test Servers
apple_id: DTS40017603
resource_type: QA
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-11-02'
source_url: https://developer.apple.com/library/archive/qa/qa1948/_index.html
archived_at: '2026-07-18T02:37:30.003915Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1948

# HTTPS and Test Servers

## Q:  My app talks to a server over HTTPS. The production server uses a certificate issued by a trusted certificate authority, so everything works just fine. However, when my app talks to my test server, which uses a self-signed certificate, things fail. How can I test my app against my test server?

A: There are two approaches you can take here, discussed in the sections below.

Our recommended approach is that you do this by setting up a test certificate authority (CA). The basic idea is:

1. Create your own CA for testing
2. Use that CA to create a digital identity for your server
3. Install that CA’s root certificate on your test devices

This approach has some important benefits:

- It works with all OS subsystems, whereas the alternative, [customising HTTPS server trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrqgmwugsbrfvjukq2dkvjvit2njfjustshjbkfiuctkncvevsfkjkfevktkrcvmqkmkvaviskpjy), relies on specific hooks that aren’t supported by all subsystems
- It does not require you to write any code
- Because there’s no test code in your app, there’s no chance of you accidentally shipping an app to customers with that test code enabled
- Your testing is more realistic because it uses exactly the same code path as your production app

With regards step 1, if you don’t have experience running a CA you can take advantage of the facilities built in to macOS; see _[Creating Certificates for TLS Testing](https://developer.apple.com/library/archive/technotes/tn2326/_index.html#//apple_ref/doc/uid/DTS40014136)_ for the details.

With regards step 3, there are various ways to install your test CA’s root certificate on your test device. For detailed instructions on how to do this, see [Installing a CA’s Root Certificate on Your Test Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrqgmwugsbrfvjukq2jjzjviqkmjreu4ry), below.

If you’re unable to use a test CA, your only alternative is to customise HTTPS server trust evaluation to ignore the fact that you’re connecting to an insecure server. There are two basic steps here:

1. You must override the default HTTPS server trust evaluation. Techniques for doing this are described in _[HTTPS Server Trust Evaluation](https://developer.apple.com/library/archive/technotes/tn2232/_index.html#//apple_ref/doc/uid/DTS40012884)_.
2. If your app uses a high-level HTTPS API — NSURLSession, NSURLConnection, or anything layered on top of those — you must disable App Transport Security (ATS) for your server. See the “NSAppTransportSecurity” section of the [Information Property List Key Reference](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) for details.

The process for installing a CA’s root certificate on your test device varies by device type. The following sections cover the most common cases.

To install a CA’s root certificate on macOS, use the Keychain Access utility to add the root certificate to the System keychain and then explicitly mark it as trusted.

There are three common ways to install a CA’s root certificate on an iOS device for testing purposes:

- Put the `.cer` file on a web server and navigate to it in Safari. iOS will then ask you whether you want to install and trust that root certificate.
- Attach the root certificate to an email and then email it to yourself; when you open the attachment, iOS will ask you whether you want to install and trust that root certificate.
- Use [Apple Configurator](https://itunes.apple.com/us/app/apple-configurator-2/id1037126344?mt=12) to create a configuration profile that includes the root certificate and then drag that configuration profile to the device in the main Apple Configurator window. In most cases you’ll need to complete the install process on the iOS device itself.

The quickest way to install a CA’s root certificate on the simulator is to drag the root certificate to the main simulator window. This will kick off the same install process that you see on the device.

Alternatively, you can put the root certificate on a web server and then navigate to it in Safari, as you would on a real device.

watchOS can run network requests via the paired iPhone or directly on the Apple Watch. For your CA’s root certificate to be effective in all circumstances it must be installed on both devices.

When you install a root certificate on your iPhone (using one of the processes [described above](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrqgmwugsbrfvjukq2jj5juirkwjfbuk)), iOS will ask you whether you want to install it on iPhone or Apple Watch. You must run through this process twice, once to install the certificate on your iPhone and again to install it on your Apple Watch.

The watchOS simulator always runs network requests via the paired iPhone simulator, so installing a CA’s root certificate on that paired simulator is sufficient to support watchOS testing.

To install a CA’s root certificate on a tvOS device or simulator, do the following:

1. Put the `.cer` file containing the root certificate on a web server
2. Navigate to Settings > General > Privacy and select Share Apple TV Analytics
3. Press the Play/Pause button on the remote; this brings up a screen that lists the installed profiles along with an Add Profile option at the top
4. Choose Add Profile
5. Enter the URL of the profile and follow the on-screen instructions to complete the install process

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-11-02 | Updated for iOS 11, mac OS 10.13, tvOS 11, and watchOS 4. Added a reference to Apple Configurator. |
| 2017-01-25 | New document that describes how to work with HTTPS test servers. |

