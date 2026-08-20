---
title: Passbook FAQ
apple_id: DTS40013009
resource_type: Technical Note
platform: watchOS|iOS
topic: null
technology: PassKit
published: '2013-01-10'
source_url: https://developer.apple.com/library/archive/technotes/tn2302/_index.html
archived_at: '2026-07-26T19:54:10.444413Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2302

# Passbook FAQ

Answers to some of the most common issues you might encounter while integrating Passbook into your app.

[Adding Passes to Passbook](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvauircjjzdv6ucbknjukuy)[Why do my passes display fine in the PKAddPassesViewController but when I tap Add they don't get added to Passbook?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvauircjjzdv6ucbknjukuznk5efsx2ej5pu2wk7kbavgu2fknpuisktkbgecwk7izeu4rk7jfhf6vciivpvas2bircfaqktkncvgvsjivlugt2okrje6tcmivjf6qsvkrpvoscfjzpusx2uifif6qkeirpviscflfpuit2ol5kf6r2fkrpucrceivcf6vcpl5iecu2tijhu6s27)[Why is my app able to add passes but it is not able to access them using the PKPassLibrary class?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvauircjjzdv6ucbknjukuznk5efsx2jknpu2wk7ififax2bijgekx2uj5pucrcel5iecu2tivjv6qsvkrpusvc7jfjv6tspkrpucqsmivpvit27ifbugrktknpviscfjvpvku2jjzdv6vciivpvas2qifjvgtcjijjecuszl5buyqktknpq)[What is the best way to enable adding passes to Passbook in my app?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvauircjjzdv6ucbknjukuznk5eecvc7jfjv6vciivpuerktkrpvoqkzl5ke6x2fjzauetcfl5auircjjzdv6ucbknjuku27krhv6ucbknjuet2pjnpusts7jvmv6qkqkbpq)[Can users add passes to their library from OS X?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvauircjjzdv6ucbknjukuzninau4x2vkncveu27ifceix2qifjvgrktl5ke6x2ujbcusus7jreueusbkjmv6rssj5gv6t2tl5mf6)[Building Passes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvbfkskmireu4r27kbavgu2fkm)[Do passes support 1D barcodes?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvbfkskmireu4r27kbavgu2fkmwuit27kbavgu2fknpvgvkqkbhvevc7gfcf6qsbkjbu6rcfknpq)[How can I include links on the back of my pass?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvbfkskmireu4r27kbavgu2fkmwuqt2xl5bucts7jfpustsdjrkuirk7jreu4s2tl5hu4x2ujbcv6qsbinfv6t2gl5gvsx2qifjvgxy)[Distributing Passes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvcesu2ukjeuevkujfheox2qifjvgrkt)[Is the only way to get a pass into Passbook through an app?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvcesu2ukjeuevkujfheox2qifjvgrktfvevgx2ujbcv6t2ojrmv6v2blfpvit27i5cvix2bl5iecu2tl5eu4vcpl5iecu2tijhu6s27krefet2vi5ef6qkol5avauc7)[I'm using a UIWebView in my app and it does not automatically support adding passes to Passbook. What should I do?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvcesu2ukjeuevkujfheox2qifjvgrktfvev6tk7kvjustshl5av6vkjk5cuevsjivlv6skol5gvsx2bkbif6qkoirpusvc7irhuku27jzhvix2bkvke6tkbkreugqkmjrmv6u2vkbie6usul5auircjjzdv6ucbknjuku27krhv6ucbknjuet2pjnpv6x2xjbavix2tjbhvktcel5ev6rcpl4)[Updating Passes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvkvarcbkreu4r27kbavgu2fkm)[Can I change anything in my pass.json file when updating a pass?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvkvarcbkreu4r27kbavgu2fkmwugqkol5ev6q2iifheork7ifhfsvcijfheox2jjzpu2wk7kbavgu27jjju6ts7izeuyrk7k5eekts7kvieiqkujfheox2bl5iecu2tl4)[If a pass has expired or been redeemed, how can I remove a pass from the Passbook library?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvkvarcbkreu4r27kbavgu2fkmwusrs7ifpvaqktknpuqqktl5cvqucjkjcuix2pkjpuerkfjzpverkeivcu2rkel5puqt2xl5bucts7jfpverknj5lekx2bl5iecu2tl5dfet2nl5keqrk7kbavgu2cj5huwx2mjfbfeqkslfpq)[Sending Push Notifications to Passes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvifku2il5he6vcjizeugqkujfhu4uy)[If I send a push to a device that no longer has my pass, will that token show up in the APNs feedback service?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvifku2il5he6vcjizeugqkujfhu4uznjfdf6sk7kncu4rc7ifpvavktjbpvit27ifpuirkwjfbukx2ujbavix2oj5puyt2oi5cvex2iifjv6tkzl5iecu2tl5pvoskmjrpviscbkrpvit2livhf6u2ij5lv6vkql5eu4x2ujbcv6qkqjzjv6rsfivceeqkdjnpvgrkskzeugrk7)[My push notifications do not seem to be working, what should I do?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewugsbrfvifku2il5he6vcjizeugqkujfhu4uznjvmv6ucvknef6tspkreumskdifkest2oknpuit27jzhvix2tivcu2x2uj5puerk7k5hves2jjzdv6x2xjbavix2tjbhvktcel5ev6rcpl4)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgmbqhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Adding Passes to Passbook

### Why do my passes display fine in the PKAddPassesViewController but when I tap Add they don't get added to Passbook?

If a pass fails to get added to the Passbook library, there are logs in the console to explain why it could not be added. This is the first thing to look at in order to diagnose failures adding passes. The most common cause is an incorrect signature in the pass caused by one of the following:

- The WWDR Intermediate Certificate was not included when signing. This cert can be downloaded from here: [Apple WWDR Intermediate Certificate](https://developer.apple.com/certificationauthority/AppleWWDRCA.cer).
- The team identifier in the pass.json file does not match the team identifier in the cert used to sign the pass. Your team identifier can be found in [your profile on the Member Center](https://developer.apple.com/membercenter/index.action#profile).
- The contents of the manifest.json file don't actually match the contents of the pass directory. Do not change the contents of the pass bundle or any file in the pass after signing it. Any discrepancies between what the manifest file specifies and the contents of the pass bundle will be logged to the console. When building the manifest.json file, do not include entries for the manifest.json or signature files.

Use the `signpass` tool to verify that your passes are signed correctly. The source code for the `signpass` tool can be found in the [Passbook Support Materials](https://developer.apple.com/downloads/index.action?name=passbook) disk image.

### Why is my app able to add passes but it is not able to access them using the PKPassLibrary class?

Adding a pass to Passbook requires explicit user action (i.e. the user must tap the Add button), so this operation does not require any special setup or entitlement. To access a pass, however, an app must have the appropriate entitlement. An app may only access passes in the Passbook library that were signed using a cert from the same development team that signed the app. For this reason, if you already have a companion app, or potentially may have one in the future, it is crucial that you plan ahead and register passes in the same development team. To configure entitlements for your app use the Entitlements section of the Summary tab in Xcode. Select the 'Use Entitlements File' checkbox to enable entitlements, then choose the appropriate option in the Passes section depending on whether you want to allow access to specific pass type identifiers or any pass belonging to the development team specified in the provisioning profile used for the app.

### What is the best way to enable adding passes to Passbook in my app?

The best way to allow users to add passes to their Passbook library is to use the "Add to Passbook" badge provided by Apple. This badge is available in numerous languages and provides a consistent visual cue to your users that they can easily add a pass to their Passbook Library. Show the Add to Passbook badge in an obvious place to make it obvious to users how to add your pass. For example, if you provide a ticket to an event you might put the Add to Passbook badge directly in the purchase confirmation shown to the user. To streamline the experience, reduce the number of taps required to add a pass. When the user taps on this badge the next thing they should see is the PKAddPassesViewController.

The localized badges and usage guidelines can be found on the [Passbook for Developers](https://developer.apple.com/passbook/) page.

### Can users add passes to their library from OS X?

Yes, passes can be added to Passbook using Safari or Mail in OS X Mountain Lion (10.8.2 or later). If you have a website where it makes sense for a user to add a pass to Passbook, allow them to do so in both iOS and OS X. If you detect the browser as Safari running on OS X 10.8.2 or later, show the Add to Passbook badge and link to your pass. Be sure to use the correct MIME type for your pass, application/vnd.apple.pkpass. Passes added to Passbook on OS X will be stored in iCloud and automatically sent to all iPhone and iPod touch devices configured with the same iCloud account.

[Back to Top](#)

## Building Passes

### Do passes support 1D barcodes?

No, passes support 2D barcodes only including Aztec, PDF417 and QR codes.

### How can I include links on the back of my pass?

Passbook uses Data Detectors to automatically add links to the text in the fields on the back of a pass. Website URLs, street addresses and phone numbers will automatically be detected and turned into tappable hyperlinks.

[Back to Top](#)

## Distributing Passes

### Is the only way to get a pass into Passbook through an app?

No. Passes can be distributed in three ways: as an attachment to an email message, downloaded from a website, or through an app. Passes distributed via email and websites can be added using iOS (on iPhone and iPod touch) or OS X Mountain Lion (10.8.2 or later). Distribute your pass using as many of these three ways that make sense for your situation. It's recommended that you use the Add to Passbook badge in each way you choose to distribute your pass to provide a consistent visual cue to your users.

### I'm using a UIWebView in my app and it does not automatically support adding passes to Passbook. What should I do?

UIWebViews do not automatically support adding passes to Passbook. To add passes using a UIWebView, implement the appropriate UIWebViewDelegate methods to identify when the view loads data with a MIME type of application/vnd.apple.pkpass. Download the data for the request and instantiate a PKPass object with that data. Use the PKAddPassesViewController class to present the pass to the user, or if the pass is already in the user's Passbook Library, use the `-[PKPassLibrary replacePassWithPass:]` method to update it.

[Back to Top](#)

## Updating Passes

### Can I change anything in my pass.json file when updating a pass?

Almost everything in a pass can be changed when you update a pass. The only fields in the pass.json file that cannot be changed are the pass type identifier and the serial number. It is not recommended to change the authenticationToken field of a pass.

### If a pass has expired or been redeemed, how can I remove a pass from the Passbook library?

Because passes are explicitly added by users to their Passbook library, you should not silently remove a pass behind the user's back. Users should be in control and decide when to remove something from their library. For passes that an app has access to, the `-[PKPassLibrary removePass:]` method can remove a pass, but only do this in response to a user action or confirmation from the user to remove the pass.

[Back to Top](#)

## Sending Push Notifications to Passes

### If I send a push to a device that no longer has my pass, will that token show up in the APNs feedback service?

When a user deletes a pass from their device your web server's endpoint for unsubscribing that pass is called. It is important to handle this call by removing the pass from your list of passes that the device has subscribed to. Sending a push notification for a pass that the device isn't subscribed to is incorrect behavior.

The push token is determined by the pass type identifier and the device, not by the individual pass. This means if you incorrectly send a push notification for a pass that a device isn't subscribed to, the result depends on whether other passes with the same pass type identifier exist in that device's Passbook library:

- If the device doesn't have any passes with the same pass type identifier (or isn't subscribed to updates for them), then the push token is invalid. In this case, the push token __DOES__ appear in the APNs feedback service.
- If the device is subscribed to other passes with the same pass type identifier, then the push token is still valid, and it __DOES NOT__ appear in the APNs feedback service. In this case, when Passbook receives the push, it queries your web service to look for updated passes. If there are no changes (for example, because this device is not subscribed to the pass that was updated) Passbook calls the logging endpoint on your server to warn that your server has sent an unnecessary push notification. Review your logs periodically to catch and correct this kind of error.

### My push notifications do not seem to be working, what should I do?

Please consult [this document for helpful information on troubleshooting push notifications](https://developer.apple.com/library/ios/#technotes/tn2265/_index.html).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-01-10 | New document that provides answers to frequently asked questions about Passbook development. |

