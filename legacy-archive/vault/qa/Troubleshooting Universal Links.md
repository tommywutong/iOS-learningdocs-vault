---
title: Troubleshooting Universal Links
apple_id: DTS40017117
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: UIKit
published: '2016-05-16'
source_url: https://developer.apple.com/library/archive/qa/qa1916/_index.html
archived_at: '2026-07-18T02:36:50.200702Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1916

# Troubleshooting Universal Links

## Q:  Why do Universal Links not work for my iOS app?

A: This Q&A assumes that you have an implementation of the Universal Links technology, described at [Support Universal Links](https://developer.apple.com/library/ios/documentation/General/Conceptual/AppSearch/UniversalLinks.html#//apple_ref/doc/uid/TP40016308-CH12-SW1) in the [iOS Developer Library](https://developer.apple.com/library/ios/navigation/), but when you tap on a link in the Mail or Notes app on your device, the link opens in Safari, and not in your app.

This is caused either by an issue in your web server configuration, where you host your `apple-app-site-association` (AASA) file, or by an issue in your app.

The below procedure will help diagnose the issue:

1. Use the [App Search API Validation Tool](https://search.developer.apple.com/appsearch-validation-tool) to test your website. The Universal Links section should show "Passed" status.
2. Make sure your app is not installed on your test device. Delete it from the device if necessary.
3. Install your app from Xcode or from TestFlight.
4. Confirm in your web server’s HTTPS logs that the AASA file was downloaded when the app was installed.
5. Email yourself the link that you are interested in testing.
6. On the device, after receiving the email, long press on the link in the email. Pick "Open in <your app>".
7. Observe if your app opens.
8. Observe if your app displays the expected information.

If the procedure was completed successfully, then Universal Links is working as expected.

If one of the steps did not give the expected result, do not continue with the procedure, but proceed to the [Troubleshooting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomjrg4wugsbrfviucvcbi4za) section.

If the Diagnostic Procedure produced a failure in one of the steps, then something was not set up correctly. Please correct the issues as described below, and re-try the [Diagnostic Procedure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomjrg4wugsbrfviucvcbi4yq).

The App Search API Validation Tool should give you a reason for the failure. Here are some of the common causes:

- The JSON schema does not match the one in the [documentation](https://developer.apple.com/library/ios/documentation/General/Conceptual/AppSearch/UniversalLinks.html#//apple_ref/doc/uid/TP40016308-CH12-SW1). Correct the schema in the AASA file.
- The AASA file is served through a 3xx redirect. Make sure this file is served without any redirects.

The web server's HTTPS logs indicate that the AASA file was not requested by the device. This can happen if the associated domains entitlement contains the incorrect `applinks` domain. Make sure the `applinks` domain is the same one where the AASA file resides.

If the logs indicate that the AASA file was requested, but not returned by your web server, then the file is either in the wrong location, or is not named `apple-app-site-association`.

When you long-pressed on the link that you emailed, the "Open in <your app>" option was not presented. There are multiple reasons why this might happen:

- It is possible that Universal Links has become disabled for your link on your device. To see if this is the case, let iOS open Safari when you tap on the link, and observe if pulling down on the webpage reveals a small Smart App Banner. If this is the case, then Universal Links were indeed disabled on this device for this link. To re-enable, tap on OPEN in the Smart App Banner, and start the [Diagnostic Procedure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomjrg4wugsbrfviucvcbi4yq) again.
- If your AASA file is signed, the signing certificate or the intermediate certificate may have expired. The App Search API Validation Tool may give a "Passed" status when the AASA file is signed, even if there is an issue with the certificates used to sign the file. Please check on the certificates embedded in the signed AASA file. If necessary, upload a newly signed file to the root of your web server. The signing procedure is detailed in Listing 2 of the [Shared Web Credentials Reference](https://developer.apple.com/library/ios/documentation/Security/Reference/SharedWebCredentialsRef/index.html#//apple_ref/doc/uid/TP40014989)
- The `appID` given in the AASA file does not match the App ID of your app. The correct `appID` string is the same as the `application-identifier` entitlement in your exported app archive. The App ID might be different than what you expect if you are not using team-based code signing, or if the app was transferred between developer accounts.
- None of the paths listed in the AASA file, for the `appID` that corresponds to your app, match the path component of the link you long-pressed on. You can fix this by specifying a link with a path that matches one of those in the AASA file.
- Your app returned `false` from one of the following `UIApplicationDelegate` protocol methods: `application(_:continueUserActivity:restorationHandler:)`, `application(_:willFinishLaunchingWithOptions:)`, `application(_:didFInishLaunchingWithOptions:)`.

  This can happen if you parsed the URL that is passed into these methods, and you implemented logic to determine that your app can not use this URL.

Your app returned `true` from the `UIApplicationDelegate` methods mentioned above, but was not able to fetch the expected information from your backend, or it misinterpreted the URL that the link represented. These are issues that you need to debug yourself, since they are specific to your code.

If you have completed the troubleshooting procedure, and verified that your app responds as described in the [documentation](https://developer.apple.com/library/ios/documentation/General/Conceptual/AppSearch/UniversalLinks.html#//apple_ref/doc/uid/TP40016308-CH12-SW1), but would like a different behavior, please submit an enhancement request, accompanied by a compelling use-case, via Apple's [bug reporting tool](https://developer.apple.com/bug-reporting/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-05-16 | New document that gives a diagnostic procedure and troubleshooting steps to discover and fix issues in implementing Universal Links. |

