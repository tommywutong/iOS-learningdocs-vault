---
title: In-App Purchase FAQ
apple_id: DTS40016228
resource_type: Technical Note
platform: iOS|macOS
topic: null
technology: StoreKit
published: '2018-05-01'
source_url: https://developer.apple.com/library/archive/technotes/tn2413/_index.html
archived_at: '2026-07-26T19:54:14.967412Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2413

# In-App Purchase FAQ

This document provides answers to frequently asked questions about in-app purchase.

[Configuration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvke4vcbi4yq)[Must I upload a binary to test In-App Purchase?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvke4vcbi4ys2tkvknkf6sk7kvieyt2birpucx2cjfhecuszl5ke6x2uivjvix2jjzpucucql5ifkusdjbavgrk7)[What can I do to help combat fraud during purchase transactions?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvke4vcbi4ys2v2iifkf6q2bjzpusx2ej5pvit27jbcuyuc7inhu2qsbkrpumusbkvcf6rcvkjeu4r27kbkveq2iifjukx2ukjau4u2binkest2oknpq)[What is the minimum version for supporting auto-renewable subscriptions?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvke4vcbi4yte)[When should I use the restoreCompletedTransactions method of SKPaymentQueue?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvke4vcbi4ys2v2iivhf6u2ij5kuyrc7jfpvku2fl5keqrk7kjcvgvcpkjcugt2nkbgekvcfirkfeqkoknaugvcjj5hfgx2nivkeqt2el5humx2tjniecwknivhfiukvivkukxy)[How many In-App Purchase product IDs can we create per application in iTunes Connect?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvke4vcbi4ytc)[Error Messages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorkt)[Your account info has changed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvaugq2ujfhemty)[Cannot connect to iTunes Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvbuctsoj5kf6q2pjzhekq2ul5ke6x2jkrku4rktl5jvit2siu)[This Apple ID has not yet been used in this iTunes Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvkeqsktl5avaucmivpusrc7jbavgx2oj5kf6wkfkrpuerkfjzpvku2firpusts7kreesu27jfkfktsfknpvgvcpkjcq)[You've already purchased this. Tap OK to download it again for free](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvmu6vk7kzcv6qkmkjcucrczl5ifkusdjbavgrkel5keqsktl5pviqkql5huwx2uj5puit2xjzge6qkel5evix2bi5austs7izhvex2gkjcuk)[You've already purchased this. Would you like to get it again for free?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvmu6vk7kzcv6qkmkjcucrczl5ifkusdjbavgrkel5keqsktl5pvot2vjrcf6wkpkvpuysklivpvit27i5cvix2jkrpucr2bjfhf6rspkjpumusfivpq)[This In-App Purchase has already been bought. It will be restored for free.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvkeqsktl5eu4x2bkbif6ucvkjbuqqktivpuqqktl5auyusfifcfsx2civcu4x2cj5kuoscul5pusvc7k5euytc7ijcv6usfknke6usfirpumt2sl5dferkfl4)[You've already purchased this In-App Purchase but it hasn't been downloaded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvmu6vk7kzcv6qkmkjcucrczl5ifkusdjbavgrkel5keqsktl5eu4x2bkbif6ucvkjbuqqktivpuevkul5evix2iifju4x2ul5bekrkol5ce6v2ojrhucrcfiq)[This is not a test user account. Please create a new account in the Sandbox environment](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvcveuspkjpu2rktknauorktfvkeqsktl5evgx2oj5kf6qk7krcvgvc7kvjukus7ifbugt2vjzkf6x2qjrcucu2fl5bverkbkrcv6qk7jzcvox2binbu6vkokrpusts7kreekx2tifheiqsplbpuktswjfje6tsnivhfi)[Localization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvge6q2bjrevuqkujfhu4)[My In-App Purchase has localized information for various languages on iTunes Connect. However, the localizedDescription and localizedTitle properties always return information in English even though my test device language is not set to English](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvge6q2bjrevuqkujfhu4lknlfpusts7ififax2qkvjegscbkncv6scbknpuyt2difgeswsfirpustsgj5je2qkujfhu4x2gj5jf6vsbkjeu6vktl5gectshkvauorktl5hu4x2jkrku4rktl5bu6tsoivbvix27jbhvorkwivjf6x2ujbcv6tcpinauysk2ivceirktinjesucujfhu4x2bjzcf6tcpinauysk2ivcfiskujrcv6ucsj5iekusujfcvgx2bjrlucwktl5jekvcvkjhf6skoizhvetkbkreu6ts7jfhf6rkoi5gesu2il5cvmrkol5keqt2vi5ef6tkzl5keku2ul5cekvsjincv6tcbjzdvkqkhivpusu27jzhvix2tivkf6vcpl5cu4r2mjfjuq)[Receipt](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifi)[How do I use the cancellation_date field?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifilkij5lv6rcpl5ev6vktivpviscfl5buctsdivgeyqkujfhu4x2eifkekx2gjfcuyrc7)[What url should I use to verify my receipt?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifivksjq)[Current receipt invalid or mismatched ds person id](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifilkdkvjferkokrpverkdivevavc7jfhfmqkmjfcf6t2sl5gusu2nifkegscfirpuiu27kbcveu2pjzpusra)[Verifying my receipt fails with a status of <string of numbers>](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifilkwivjesrszjfheox2nlfpverkdivevavc7izaustctl5lusvcil5av6u2uifkfku27j5df6x2tkrjestshl5humx2okvguerksknpq)[App Review cannot see my content despite a successful purchase.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifilkbkbif6usfkzeukv27inau4tspkrpvgrkfl5gvsx2dj5hfirkokrpuirktkbevirk7ifpvgvkdincvgu2gkvgf6ucvkjbuqqktivpq)[My app validates its receipt with the App Store via paymentQueue:updatedTransactions: after a successful purchase. However, the returned receipt contains an empty in_app array rather than the expected products.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifilknlfpucucql5lectcjiravirktl5eviu27kjcugrkjkbkf6v2jkref6vciivpucucql5jvit2sivpvmskbl5iecwknivhfiukvivkukx2vkbcecvcfirkfeqkoknaugvcjj5hfgx27ifdfirksl5av6u2vinbuku2tizkuyx2qkvjegscbkncv6x2ij5lukvsfkjpv6vciivpverkukvje4rkel5jekq2fjfifix2dj5hfiqkjjzjv6qkol5cu2uculfpusts7ififax2bkjjecwk7kjaviscfkjpviscbjzpviscfl5cvqucfinkekrc7kbje6rcvinkfgxy)[After I install the development app with Xcode, the appStoreReceiptURL is nil. What is the proper way to handle this situation?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifilkbizkekus7jfpuststkrauytc7kreekx2eivlektcpkbguktsul5avauc7k5evisc7lbbu6rcfl5pviscfl5avauctkrhverksivbukskqkrkvetc7jfjv6tsjjrpv6v2iifkf6sktl5keqrk7kbje6ucfkjpvoqkzl5ke6x2iifheitcfl5keqsktl5jusvcvifkest2ol4)[Subscriptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjvkqstinjesucujfhu4uy)[How do I create and upload a hosted non-consumable product?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjvkqstinjesucujfhu4uznjbhvox2ej5pusx2dkjcucvcfl5au4rc7kvieyt2birpucx2ij5jvirkel5he6ts7inhu4u2vjvauetcfl5ifet2ekvbvixy)[How do I handle auto-renewable subscriptions of multiple lengths for the same product?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjvkqstinjesucujfhu4uznjbhvox2ej5pusx2iifheitcfl5avkvcpl5jektsfk5auetcfl5jvkqstinjesucujfhu4u27j5df6tkvjrkesucmivpuyrkoi5kequ27izhvex2ujbcv6u2bjvcv6ucsj5cfkq2ul4)[How do I migrate from an auto-renewable subscription to another In-App Purchase product?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjvkqstinjesucujfhu4uznjbhvox2ej5pusx2njfdveqkuivpumuspjvpucts7ifkvit27kjcu4rkxifbeyrk7knkueu2dkjevavcjj5hf6vcpl5au4t2ujbcvex2jjzpucucql5ifkusdjbavgrk7kbje6rcvinkf6)[My app does not receive any renewal notices even though it is running in the foreground.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjvkqstinjesucujfhu4uznjvmv6qkqkbpuit2fknpu4t2ul5jekq2fjflekx2bjzmv6usfjzcvoqkml5he6vcjincvgx2fkzcu4x2ujbhvkr2il5evix2jknpvevkojzeu4r27jfhf6vciivpumt2sivdvet2vjzcf6)[My server process rarely receives RENEWAL notices when the auto-renewing subscription renews.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjvkqstinjesucujfhu4uznjvmv6u2fkjlekus7kbje6q2fknjv6usbkjcuywk7kjcugrkjkzcvgx2sivhekv2bjrpu4t2ujfbuku27k5eekts7kreekx2bkvke6x2sivhekv2jjzdv6u2vijjugusjkbkest2ol5jektsfk5jv6)[Troubleshooting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvkfet2vijgeku2ij5hviskoi4)[Why are my product identifiers being returned in the invalidProductIdentifiers array?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvkfet2vijgeku2ij5hviskoi4wvosczl5averk7jvmv6ucsj5cfkq2ul5euirkokreumskfkjjv6qsfjfheox2sivkfkusoivcf6skol5keqrk7jfhfmqkmjfcfauspirkugvcjircu4vcjizeukustl5aveusblfpq)[App Review has recently approved my application, but my In-App Purchase identifiers in the production version of the application are being returned in the invalidProductIdentifiers array.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvkfet2vijgeku2ij5hviskoi4wucucql5jekvsjivlv6scbknpverkdivhfitczl5avaucsj5lekrc7jvmv6qkqkbgesq2bkreu6ts7l5bfkvc7jvmv6skol5avauc7kbkveq2iifjukx2jircu4vcjizeukustl5eu4x2ujbcv6ucsj5cfkq2ujfhu4x2wivjfgskpjzpu6rs7kreekx2bkbieyskdifkest2ol5averk7ijcustshl5jekvcvkjhekrc7jfhf6vciivpustswifgesrcqkjhuivkdkreuirkokreumskfkjjv6qkskjavsxy)[Calling the payment queue’s restoreCompletedTransactions method does not restore any products in my application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvkfet2vijgeku2ij5hviskoi4wugqkmjreu4r27kreekx2qifmu2rkokrpvcvkfkvcv6x27knpverktkrhverkdj5gvatcfkrcuivcsifhfgqkdkreu6tstl5gukvcij5cf6rcpivjv6tspkrpverktkrhverk7ifhfsx2qkjhuivkdkrjv6skol5gvsx2bkbieyskdifkest2o)[My app does nothing or crashes when App Review attempts to purchase an In-App Purchase product](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvkfet2vijgeku2ij5hviskoi4wu2wk7ififax2ej5cvgx2oj5keqskoi5pu6us7injecu2iivjv6x2xjbcu4x2bkbif6usfkzeukv27ifkfirknkbkfgx2uj5pvavksineecu2fl5au4x2jjzpucucql5ifkusdjbavgrk7kbje6rcvinkf6)[Additional Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvauircjkreu6tsbjrpverktj5kveq2fkm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Configuration

### Must I upload a binary to test In-App Purchase?

No. Testing in-app purchase does not require uploading a binary.

__Important:__ DO NOT upload the development binary to iTunes Connect until the application is ready for App Review approval. If the binary is present in iTunes Connect and it is not fully functional, App Review will review the binary and likely reject the development binary. Testing in-app purchase will fail if you or App Review reject your most recent binary in iTunes Connect. The workaround in this case is to upload a binary without in-app purchase features that can get approved by App Review. Once the binary is approved, resume testing the binary with in-app purchase features.

### What can I do to help combat fraud during purchase transactions?

[SKPayment](https://developer.apple.com/reference/storekit/skpayment) provides the [applicationUsername](https://developer.apple.com/reference/storekit/skpayment/1506116-applicationusername) property, which allows you to help Apple detect irregular activity when requesting payment. it is an opaque identifier whose recommended value is a one-way hash of the user’s account name on your server. To help Apple combat fraud during purchase transactions, create a payment object, then set its `applicationUsername` property to an opaque identifier associated with the user’s account name on your server before making a purchase.

__Important:__ Do not populate `applicationUsername` with the Apple ID for your developer account, the user’s Apple ID, or the user’s unhashed account name on your server.

See [Detecting Irregular Activity](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/RequestPayment.html#//apple_ref/doc/uid/TP40008267-CH4-SW6), which provides a `hashedValueForAccountName:` method that demonstrates how to create a one-way hash of the user's account. `hashedValueForAccountName:` assumes that the current user is associated with a username on your server. It takes the username as a parameter and returns its hash value as shown in Listing 1.

__Listing 1__  Providing an application username.

```objc
// Custom method to calculate the SHA-256 hash using Common Crypto.
-(NSString *)hashedValueForAccountName:(NSString *)userAccountName
{
    const int HASH_SIZE = 32;
    unsigned char hashedChars[HASH_SIZE];
    const char *accountName = [userAccountName UTF8String];
    size_t accountNameLen = strlen(accountName);

    // Confirm that the length of the user name is small enough
    // to be recast when calling the hash function.
    if (accountNameLen > UINT32_MAX) {
        NSLog(@"Account name too long to hash: %@", userAccountName);
        return nil;
    }
    CC_SHA256(accountName, (CC_LONG)accountNameLen, hashedChars);

    // Convert the array of bytes into a string showing its hex representation.
    NSMutableString *userAccountHash = [[NSMutableString alloc] init];
    for (int i = 0; i < HASH_SIZE; i++) {
        // Add a dash every four bytes, for readability.
        if (i != 0 && i%4 == 0) {
            [userAccountHash appendString:@"-"];
        }
        [userAccountHash appendFormat:@"%02x", hashedChars[i]];
    }
    return userAccountHash;
}
```

Use the above returned hash value of your user's account to populate the [applicationUsername](https://developer.apple.com/documentation/storekit/skpayment/1506116-applicationusername) property of your payment object before calling `addPayment:` as shown in Listing 2.

__Listing 2__  Populate the applicationUsername property of an SKMutablePayment object.

```
// product is an SKProduct object.
SKMutablePayment *payment = [SKMutablePayment paymentWithProduct:product];

//Populate applicationUsername with your customer's username on your server.
payment.applicationUsername = [self hashedValueForAccountName:@"userNameOnYourServer"];

// Submit payment request.
[[SKPaymentQueue defaultQueue] addPayment:payment];
```

### What is the minimum version for supporting auto-renewable subscriptions?

- iOS 4.2 is the minimum iOS version for supporting auto-renewable subscriptions.
- macOS 10.9 is the minimum macOS version for supporting auto-renewable subscriptions.

### When should I use the restoreCompletedTransactions method of SKPaymentQueue?

You should only use [restoreCompletedTransactions](https://developer.apple.com/reference/storekit/skpaymentqueue/1506123-restorecompletedtransactions?language=objc) to restore your auto-renewable subscription or non-consumable products in both of these cases:

- To install them on additional devices owned by your customers.
- To reinstall them on devices where their associated application was deleted.

### How many In-App Purchase product IDs can we create per application in iTunes Connect?

Read [Workflow for configuring in-app purchases](https://help.apple.com/itunes-connect/developer/#/devb57be10e7) to find out how many in-app purchase product IDs you can create across all apps in the account.

[Back to Top](#)

## Error Messages

### Your account info has changed

The "Your account info has changed" message indicates that you are signed in the App Store with your test user account on your device. Sandbox test user accounts become unusable once you use them to log in to a production environment. To resolve this error, sign out of iTunes & App Stores in the Settings application on your device, create a new test user account in iTunes Connect, and use it when prompted by StoreKit to confirm a purchase from within your app.

### Cannot connect to iTunes Store

The "Cannot connect to iTunes Store" issue may be due to one or more of the following reasons:

- The sandbox may be unreachable. Check the [System Status](https://developer.apple.com/system-status/) for the status of the iTunes Sandbox.
- Your app does not have a bundle version ([CFBundleVersion](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102364)). See [Setting the Version Number and Build String](https://help.apple.com/xcode/mac/current/#/devba7f53ad4) for more information.
- Your app is running in the Simulator, which does not support in-app purchase.
- You are attempting to purchase a product that is unavailable for sale. See [Query the App Store for product information before presenting your app’s store UI](https://developer.apple.com/library/ios/technotes/tn2387/_index.html#//apple_ref/doc/uid/DTS40014795-CH1-BEST_PRACTICES-QUERY_THE_APP_STORE_FOR_PRODUCT_INFORMATION_BEFORE_PRESENTING_YOUR_APP___S_STORE_UI) for more information.

### This Apple ID has not yet been used in this iTunes Store

The "This Apple ID has not yet been used in this iTunes Store" message indicates that you are signed in the iTunes Store with your test user account on your device. See [Your account info has changed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvaugq2ujfhemty) for more information on how to resolve this issue.

### You've already purchased this. Tap OK to download it again for free

The "You've already purchased this. Tap OK to download it again for free." message is a notification rather than an error. It indicates that you are attempting to purchase a non-consumable product that you have already bought. You are not charged when purchasing an already bought non-consumable product.

### You've already purchased this. Would you like to get it again for free?

The "You've already purchased this. Would you like to get it again for free?" message indicates that you are attempting to purchase a non-consumable product that you have already bought. You are not charged when purchasing an already bought non-consumable product.

### This In-App Purchase has already been bought. It will be restored for free.

The "This In-App Purchase has already been bought. It will be restored for free." message indicates that you did not call `SKPaymentQueue`'s `finishTransaction:` in your application. Calling `finishTransaction:` allows you to remove a transaction from the payment queue. It notifies the App Store that the application acknowledges the transaction so that the App Store can mark it as completed.

### You've already purchased this In-App Purchase but it hasn't been downloaded

You are getting the "You've already purchased this In-App Purchase but it hasn't been downloaded." message because you did not call `SKPaymentQueue`'s `finishTransaction:` in your application. Calling `finishTransaction:` allows you to remove a transaction from the payment queue. It notifies the App Store that the application acknowledges the transaction so that the App Store can mark it as completed.

### This is not a test user account. Please create a new account in the Sandbox environment

You are getting the "This is not a test user account. Please create a new account in the Sandbox environment." message because you signed in with your iTunes user account when prompted by StoreKit to confirm a purchase. To resolve this error, sign out of iTunes & App Stores in the Settings application on your device and use your sandbox test user account when prompted by StoreKit to confirm a purchase.

[Back to Top](#)

## Localization

### My In-App Purchase has localized information for various languages on iTunes Connect. However, the localizedDescription and localizedTitle properties always return information in English even though my test device language is not set to English

`localizedDescription` and `localizedTitle` return localized information whose language is based on the current iTunes Store rather than the current device language setting. For instance, if your in-app purchase is localized for German in iTunes Connect and you are logged with an English test user account, then `localizedDescription` and `localizedTitle` will return information localized in English. To have `localizedDescription` and `localizedTitle` return information localized in German, login with a German test user account on your test device.

[Back to Top](#)

## Receipt

### How do I use the cancellation_date field?

The [Cancellation Date](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW19) (`cancellation_date`) field is designed for use with auto-renewable subscription, non-consumable and non-renewing subscription products. This field is set when a customer contacts Apple customer support for a refund and the transaction is canceled. The utility of the `cancellation_date` field is most useful with auto-renewing subscription products. After the refund is issued and the `cancellation_date` field is added to the iTunes Server records for the user, there is no automatic update process for the application copy of the appStoreReceipt to be automatically updated. In the case of a receipt with an auto-renewing subscription product, validating the appStoreReceipt results in the iTunes Store verifyReceipt server providing the most current information about the auto-renewing subscription product in the latest_receipt_info field of the validated receipt.

At present this support does not exist for validating appStoreReceipts which have non-consumable and non-renewing subscription products. After the refund event, validating the appStoreReceipt in the app will not reflect a refund for non-consumable and non-renewing subscription purchases. The iTunes Server can update the appStoreReceipt to show the `cancellation_date`, but an update event must occur. The appStoreReceipt is refreshed only in the following cases after the refund has occurred - when there is a successful purchase of an in-app purchase item, when the `SKReceiptRefreshRequest` call is used and when the `restoreCompletedTransactions` is used to restore previously purchased products.

__Important:__ `cancellation_date` is not currently added for consumable products.

### What url should I use to verify my receipt?

- Use the sandbox URL `https://sandbox.itunes.apple.com/verifyReceipt` while testing your application in the sandbox and while your application is in review.
- Use the production URL `https://buy.itunes.apple.com/verifyReceipt` once your application is live in the App Store.

  __Important:__ The App Review team reviews apps in the sandbox.

  Always verify your receipt first with the production URL; proceed to verify with the sandbox URL if you receive a 21007 status code. Following this approach ensures that you do not have to switch between URLs while your application is being tested or reviewed in the sandbox or is live in the App Store.

  The 21007 status code indicates that this receipt is a sandbox receipt, but it was sent to the production service for verification. A status of 0 indicates that the receipt was properly verified. See for [WWDC 2012: Managing Subscriptions with In-App Purchase](https://developer.apple.com/videos/wwdc/2012/?id=308) more information.

### Current receipt invalid or mismatched ds person id

You are getting this message because your application does not contain a macOS App Store receipt. See [Receipt Validation Programming Guide](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Introduction.html) for more infomation on how to obtain a receipt for your application.

### Verifying my receipt fails with a status of <string of numbers>

Verifying your receipt may fail with a status of <string of numbers> for one or more of the following reasons:

- You did not encode your receipt data using base64 encoding in your iOS application.
- Your receipt contains characters that were not properly encoded or covered by your base-64 algorithm. See [Send the Receipt Data to the App Store](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Chapters/ValidateRemotely.html#//apple_ref/doc/uid/TP40010573-CH104-SW3) for an example that shows how to properly encode a receipt using base-64.
- The object being posted to the App Store is not formatted as JSON. See Listing 3 for a proper JSON object for an auto-renewable subscription.

  __Listing 3__  Valid sample receipt for verifying an auto-renewable subscription.

  ```
  {
      "exclude-old-transactions": true/false,
      "receipt-data" : "...",
          "password" : "..."
  }
  ```

__Note:__ If the key `exclude-old-transactions` is not included, the default value is `true`.

### App Review cannot see my content despite a successful purchase.

If your app validates its receipt with the App Store after a successful purchase, check that your app is using the correct App Store URL to validate the receipt. See [What url should I use to verify my receipt?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifivksjq) for more information.

### My app validates its receipt with the App Store via paymentQueue:updatedTransactions: after a successful purchase. However, the returned receipt contains an empty in_app array rather than the expected products.

An empty `in_app` array indicates that the App Store has not recorded any transactions for the user yet. It may be that the application receipt has not yet been updated. When this happens, your app can inform the user that the receipt does not appear current and ask whether to refresh it. Upon user agreement, your app should use the [SKReceiptRefreshRequest](https://developer.apple.com/library/ios/documentation/StoreKit/Reference/SKReceiptRefreshRequest_ClassRef/) class to update the receipt. At this point, if the App Store has recorded a purchase for the user, your app receipt will show it in `in_app`. See [Refreshing the App Receipt](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Restoring.html#//apple_ref/doc/uid/TP40008267-CH8-SW2) for more information on how to update a receipt.

__Important:__ Information about auto-renewable subscriptions, non-consumable products, and non-renewing subscriptions is added to the receipt when they are paid for and remains in the receipt indefinitely.

Information about consumable products is added to the receipt when they are paid for and remains in the receipt until you finish the transaction. After you finish the transaction, this information is removed the next time the receipt is updated. Thus resulting into an empty `in_app` array if your app only sells consumable products.

### After I install the development app with Xcode, the appStoreReceiptURL is nil. What is the proper way to handle this situation?

When an application checks `appStoreReceiptURL` and finds that it is nil, start with the assumption that the current user has no access to premium content. The application can advise the user that the appStoreReceipt appears to be outdated and may require refreshing. If the user agrees that that appStoreReceipt requires refreshing, then the application can make the `SKReceiptRefreshRequest` call. Using `SKReceiptRefreshRequest` will have iOS present the iTunes User Authentication dialog. Once the user enters their password, the App Store will attempt to refresh the appStoreReceipt and the application will be called via `requestDidFinish` or `didFailWithError`. The application must allow the user to cancel the authentication dialog presented by `SKReceiptRefreshRequest` and continue on with the assumption that the user has no access to premium content.

The absence of the appStoreReceipt is typical when the application is installed using Xcode or TestFlight. When the application is installed from the App Store or restored from iCloud, the appStoreReceipt will always be present. However there are some unusual production cases where the appStoreReceipt may be missing from the application.

[Back to Top](#)

## Subscriptions

### How do I create and upload a hosted non-consumable product?

See [Upload in-app purchase content](https://help.apple.com/xcode/mac/current/#/dev285fb60ce) for more information on how to create and upload a hosted non-consumable product in Xcode and iTunes Connect.

### How do I handle auto-renewable subscriptions of multiple lengths for the same product?

You should let your customers manage auto-renewable subscriptions via the Manage Subscription page on their device. Use the following URL to open this page from within your app:

```
https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/manageSubscriptions
```

### How do I migrate from an auto-renewable subscription to another In-App Purchase product?

Follow these steps to migrate from an auto-renewable subscription to another type of in-app purchase product:

1. Remove your current auto-renewable subscription from sale in iTunes Connect by turning off their Clear for Sale flag, then remove it from your code. As a result, auto-renewal will be disabled for your product and an email will be sent to your customer. Note that you must still provide your customer with the paid product until the end of the subscription. Furthermore, all previously auto-renewable subscriptions are still restorable.

   For instance, if your customer has purchased a monthly subscription on April 1st and this subscription was removed from sale on April 19th, then you must provide the purchased provide content until May 1st.
2. Create a new in-app purchase product of a type of your choosing, then update your binary to use it. See [Create an in-app purchase](https://help.apple.com/itunes-connect/developer/#/devae49fb316) for more information.

   __Note:__ This step is required because you cannot change the type of an in-app purchase once it has been created.
3. Validate your app's receipt with the App Store, then parse its response to determine whether to provide its associated functionality to your customer. See [Receipt Validation Programming Guide](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573) for more information.

### My app does not receive any renewal notices even though it is running in the foreground.

If your app has a persistent transaction observer, then it will receive all its renewal notices when launching or resuming from the background. See [Add a transaction queue observer at application launch](https://developer.apple.com/library/ios/technotes/tn2387/_index.html#//apple_ref/doc/uid/DTS40014795-CH1-BEST_PRACTICES-ADD_A_TRANSACTION_QUEUE_OBSERVER_AT_APPLICATION_LAUNCH) for more information.

### My server process rarely receives RENEWAL notices when the auto-renewing subscription renews.

Your application process implements support for the server-to-server notification service for auto-renewing subscriptions and expects to receive the RENEWAL status update notification when a renewal occurs. The description for the [RENEWAL notification type in Table 6-4 Status Update Notification Types](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Subscriptions.html#//apple_ref/doc/uid/TP40008267-CH7-SW13) needs clarification. The description states "Automatic renewal was successful for an expired subscription. Check `Subscription Expiration Date` to determine the next renewal date and time.

The App Store attempts to charge the user account 24 hours before an auto-renewing subscription expires. If the renewal is successful, there is no server-to server notification because the auto-renewing subscription did not enter into the expired state. However, in the few cases that iTunes is unable to renew the subscription (generally there was a connection problem with the credit card server) and the auto-renewing subscription is not renewed before the expiration_date passes, the auto-renewing subscription is technically considered __expired__. iTunes may continue to attempt to renew the subscription. If iTunes is successful, then the RENEWAL event is sent. For this reason, the advice is presented - Check Subscription Expiration Date to determine the next renewal date and time.

For a normal renewal where the user account is successfully charged before the subscription expires, validate the appStoreReceipt. Check the contents of the latest_receipt_info field to verify that there is an auto-renewing subscription in-app purchase item where the `expires-date` is later than the current date.

[Back to Top](#)

## Troubleshooting

### Why are my product identifiers being returned in the invalidProductIdentifiers array?

Your product identifiers may be returned in the `invalidProductIdentifiers` array for one or more of the following reasons:

- You did not use an explicit App ID.
- If you or App Review rejected your most recent binary in iTunes Connect.
- You did not clear your in-app purchase products for sale in iTunes Connect.
- You did not sign your app with the Provisioning Profile associated with your explicit App ID.
- You might have modified your products, but these changes are not yet available to all the App Store servers.
- You did not complete all the financial requirements. See [Agreements, Tax, and Banking Information](https://developer.apple.com/library/ios/technotes/tn2259/_index.html#//apple_ref/doc/uid/DTS40009578-CH1-CONTRACTS__TAX__AND_BANKING_INFORMATION) for more information.

  __Note:__ If you recently renewed your developer membership, check whether you need to update the financial agreements. If your developer membership expired, the financial agreement will also have expired.
- Your product is marked as Apple-hosted whose content has not yet been uploaded to iTunes Connect. See [Upload in-app purchase content](https://help.apple.com/xcode/mac/current/#/dev285fb60ce) for more information on how to upload hosted content.

  __Note:__ Your product identifier will be invalid until its content is uploaded to iTunes Connect. However, if your content is not ready, select the `Turn off Content Hosting`  feature for your product in iTunes Connect to resolve this issue. Select the `Turn on Content Hosting`  feature for your product once your content has been uploaded.
- Your product identifier specified in iTunes Connect does not match the identifier used by the `SKProductsRequest` object in your app. See [QA1329: In-App Purchase Product Identifiers](https://developer.apple.com/library/content/qa/qa1329) for more information about product identifiers.

### App Review has recently approved my application, but my In-App Purchase identifiers in the production version of the application are being returned in the invalidProductIdentifiers array.

When an application is approved, the developer must also approve the application for release to the App Store. On approval, the application ID is activated to the App Store. The same activation is required for the in-app purchase identifiers and can only take place once the application is activated. In some cases, the activation of the In-App Purchase identifiers may lag up to 48 hours following the activation of the application.

If the developer does not approve the release of the production application to the App Store, then any new in-app purchase identifiers will not be activated. This is an issue when a developer wants to verify the application prior to activating it on the App Store. If the desire is to test the in-app purchase process for the new items, the application must be activated to the App Store. This is only an issue for new in-app purchase identifiers in a corresponding application submission. Once these in-app purchase identifiers have been activated, application updates to the submission will find that these in-app purchase identifiers are validated, even if the update is not activated.

### Calling the payment queue’s restoreCompletedTransactions method does not restore any products in my application

Calling the payment queue’s `restoreCompletedTransactions` method may not restore any products in your application for one or more of the following reasons:

- Your products have unfinished transactions. The restore process does not return a product if it has an unfinished transaction in the payment queue. See [Finish the transaction](https://developer.apple.com/library/ios/technotes/tn2387/_index.html#//apple_ref/doc/uid/DTS40014795-CH1-BEST_PRACTICES-TEST_YOUR_IMPLEMENTATION_OF_IN_APP_PURCHASE) for more information on how to finish transactions.
- You did not have any previously bought non-consumable, auto-renewable subscriptions, or free subscriptions.
- You were trying to restore non-renewing subscription or consumable products, which are not restorable. The `restoreCompletedTransactions` method only restores non-consumable, auto-renewable subscriptions, and free subscriptions.

  __Note:__ StoreKit does not call the  `paymentQueue:updatedTransactions:` method when there are no restorable products.
- Your app's build version number (`CFBundleVersion`) does not follow guidelines for build version numbers. `CFBundleVersion` is a string made of three unsigned integers separated by a period. See [Set the version and build](https://help.apple.com/xcode/mac/current/#/devba7f53ad4) for more information.

### My app does nothing or crashes when App Review attempts to purchase an In-App Purchase product

- Your app called SKPaymentQueue's[addPayment:](https://developer.apple.com/reference/storekit/skpaymentqueue/1506036-addpayment?language=objc) with an `SKPayment` object that is either nil or is associated with an invalid product identifier.

  Consider the case where tapping the "Buy" button results in the serial call sequence in an app: The app first sends a product request to the App Store to validate an in-app purchase product identifier, then calls `addPayment:` to make a purchase. If for some reasons (such as a network failure), the product request fails and the app does not verify that the `response.product` array contains the SKProduct object associated with the product identifier, then the app should not call `addPayment:`. If however, the app makes the `addPayment:` call with an `SKPayment` object thats uses an invalid product identifier as seen in Listing 4, at best, nothing happens. At worst, the app crashes for using a nil identifier. To App Review, the issue was triggered by tapping the "Buy" button and nothing happened (or the app crashed).

  __Listing 4__  App implements the serial call sequence. Does not follow best practices for presenting in-app purchase products.

  ```objc
  @property SKProductsRequest *request;
  @property SKProduct *product;

  - (IBAction)purchase:(id)sender
  {
      NSSet *productID = [NSSet setWithObject:@"product_identifier"];
      // Create a product request.
      self.request = [[SKProductsRequest alloc] initWithProductIdentifiers:productID];
      self.request.delegate = self;

      // Send the product request to the App Store.
      [self.request start];
  }

  - (void)productsRequest:(SKProductsRequest *)request didReceiveResponse:(SKProductsResponse *)response
  {
      // product is an instance of SKProduct. The app assumes that response.products is
      // not empty by getting its first element without any checks.
      self.product = [response.products firstObject];

      NSLog(@"Name: %@", self.product.localizedTitle);

      // The app creates a payment request for a product whose value could be nil.
      SKMutablePayment *payment = [SKMutablePayment paymentWithProduct:self.product];

     // If the product was nil, the app will crash when executing addPayment:.
      [[SKPaymentQueue defaultQueue] addPayment:payment];
  }
  ```

  As such, be sure to follow the [Query the App Store for product information before presenting your app’s store UI](https://developer.apple.com/library/ios/technotes/tn2387/_index.html#//apple_ref/doc/uid/DTS40014795-CH1-BEST_PRACTICES-QUERY_THE_APP_STORE_FOR_PRODUCT_INFORMATION_BEFORE_PRESENTING_YOUR_APP___S_STORE_UI) best practice, to check that `response.product` contains the desired in-app purchase identifiers before using them, and call `addPayment:` only with payment requests associated with valid products as seen in Listing 5.

  __Listing 5__  Follows best practices for presenting and purchasing in-app purchase products.

  ```objc
  @property SKProduct *product;
  @property SKProductsRequest *request;

  -(void)fetchProductInformation
  {
       NSSet *productID = [NSSet setWithObject:@"product_identifier"];
       // Create a product request.
       self.request = [[SKProductsRequest alloc] initWithProductIdentifiers:productID];
       self.request.delegate = self;

      // Send the product request to the App Store.
      [self.request start];
  }

  - (void)productsRequest:(SKProductsRequest *)request didReceiveResponse:(SKProductsResponse *)response
  {
      // Be sure that the products array is not empty before fetching its content.
      if ([response.products count] > 0)
      {
         // product is an instance of SKProduct.
         self.product = [response.products firstObject];
         NSLog(@"Name: %@", self.product.localizedTitle);
      }
  }

  - (IBAction)purchase:(id)sender
   {
      if (self.product != nil)
      {
          SKMutablePayment *payment = [SKMutablePayment paymentWithProduct:self.product];
          [[SKPaymentQueue defaultQueue] addPayment:payment];
      }
  }
  ```
- If your app uses receipt validation to determine whether to provide its features, then it may be sending its receipt to the wrong verification environment.

  App Review reviews apps in the sandbox. If you assume that submitting your app for review means that your app must be set to work in the production environment, then your app will be sending a Sandbox receipt to the production environment for verification. This will result in validation failure, which prevents your app from delivering content.To App Review, your app does nothing when making a purchase. See [What url should I use to verify my receipt?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrshawugsbrfvjekq2fjfifivksjq) for more information about receipt URLs.
[Back to Top](#)

## Additional Resources

- [In-App Purchase](https://developer.apple.com/in-app-purchase/)
- [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/Introduction/Introduction.html)
- [iTunes Connect Developer Help](http://help.apple.com/itunes-connect/developer/)
- [In-App Purchase Programming Guide](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html)
- [Receipt Validation Programming Guide](https://developer.apple.com/library/mac/releasenotes/General/ValidateAppStoreReceipt/Introduction.html)
- [TN2387: In-App Purchase Best Practices](https://developer.apple.com/library/ios/technotes/tn2387/_index.html)
- [QA1329: In-App Purchase Product Identifiers](https://developer.apple.com/library/content/qa/qa1329/_index.html)
- [TN2259: Adding In-App Purchase to Your Applications](https://developer.apple.com/library/ios/technotes/tn2259/_index.html)
- [WWDC 2012: Managing Subscriptions with In-App Purchase](https://developer.apple.com/videos/wwdc/2012/?id=308)
- [WWDC 2013: Using Store Kit for In-App Purchases](https://developer.apple.com/videos/play/wwdc2013/305)
- [WWDC 2013: Using Receipts to Protect Your Digital Sales](https://developer.apple.com/videos/play/wwdc2013/308)
- [WWDC 2014: Designing a Great In-App Purchase Experience](https://developer.apple.com/videos/play/wwdc2014/218)
- [WWDC 2014: Optimizing In-App Purchases](https://developer.apple.com/videos/play/wwdc2014/303)
- [WWDC 2016: Using Store Kit for In-App Purchases with Swift 3](https://developer.apple.com/videos/play/wwdc2016/702)
- [WWDC 2017: What's New in StoreKit](https://developer.apple.com/videos/play/wwdc2017/303)
- [WWDC 2017: Advanced StoreKit](https://developer.apple.com/videos/play/wwdc2017/305)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-05-01 | Updated SKProductsRequest reason for failure to validate In-App Purchase identifiers. Added QA about missing appStoreReceipt in sandbox environment. Added clarification on the RENEWAL server-to-server Status Update Notification type. Added QA about testing a production app with new In-App Purchase items and the failure to validate the new In-App Purchase identifiers. Removed ref to status 21009 - now outdated. Fixed outdated URL references. Clarified the use of the "cancellation_date" field in the appStoreReceipt. Removed outdated QA on customer sharing of information. |
| 2017-06-28 | Fixed typos. |
| 2017-02-09 | Added the "How do I create a hosted non-consumable product?" and "When validating my receipt, the App Store returns a status code of 21009" questions. |
| 2015-12-07 | Updated the "What url should I use to verify my receipt?" faq and Additional Reading section. Added the "How do I use the cancellation_date field?", "My app does nothing or crashes when App Review attempts to purchase an In-App Purchase product", "You've already purchased this. Would you like to get it again for free?", "This In-App Purchase has already been bought. it will be restored for free.", and "Are there any guidelines I need to follow to help protect against potential fraudulent activities?" faqs. |
| 2015-08-18 | Added the "How do I handle auto-renewable subscriptions of multiple lengths for the same product?" question. Updated the "Verifying my receipt fails with a status of <string of numbers>" question. |
| 2015-05-29 | New document that provides answers to frequently asked questions about in-app purchase. |

