---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/ShowUI.html
archived_at: '2026-07-27T06:57:07.328126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Requesting%20Payment.md)[Previous](Designing%20Your%20App%E2%80%99s%20Products.md)

# Retrieving Product Information

In the first part of the purchase process, your app retrieves information about its products from the App Store, presents its store UI to the user, and then lets the user select a product, as shown in Figure 2-1.

__Figure 2-1__  Stages of the purchase process—displaying store UI

（原归档配图未能恢复：`retrieving_product_info_2x.png`）

## Getting a List of Product Identifiers

Every product you sell in your app has a unique _product identifier_. Your app uses these product identifiers to fetch information about products from the App Store, such as pricing, and to submit payment requests when users purchase those products. Your app can either read its list of product identifiers from a file in its app bundle or fetch them from your server. Table 2-1 summarizes the differences between the two approaches.

__Table 2-1__  Comparison of approaches for obtaining product identifiers

|  | Embedded in the app bundle | Fetched from your server |
| Used for purchases that | Unlock functionality | Deliver content |
| List of products can change | When the app is updated | At any time |
| Requires a server | No | Yes |

If your app has a fixed list of products, such as an in-app purchase to remove ads or enable functionality, embed the list in the app bundle. If the list of product identifiers can change without your app needing to be updated, such as a game that supports additional levels or characters, have your app fetch the list from your server.

There’s no runtime mechanism to fetch a list of all products configured in App Store Connect for a particular app. You’re responsible for managing your app’s list of products and providing that information to your app. If you need to manage a large number of products, consider using the bulk XML upload/download feature in App Store Connect.

### Embedding Product IDs in the App Bundle

Include a property list file in your app bundle containing an array of product identifiers, such as the following:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <string>com.example.level1</string>
    <string>com.example.level2</string>
    <string>com.example.rocket_car</string>
</array>
</plist>
```

To get product identifiers from the property list, locate the file in the app bundle and read it.

```
NSURL *url = [[NSBundle mainBundle] URLForResource:@"product_ids"
                                     withExtension:@"plist"];
NSArray *productIdentifiers = [NSArray arrayWithContentsOfURL:url];
```

### Fetching Product IDs from Your Server

Host a JSON file on your server with the product identifiers. For example:

```
[
    "com.example.level1",
    "com.example.level2",
    "com.example.rocket_car"
]
```

To get product identifiers from your server, fetch and read the JSON file as shown in Listing 2-1. Consider versioning the JSON file so that future versions of your app can change its structure without breaking older versions of your app. For example, you could name the file that uses the old structure `products_v1.json` and the file that uses a new structure `products_v2.json`. This is especially useful if your JSON file is more complex than the simple array in the example.

__Listing 2-1__  Fetching product identifiers from your server

```objc
- (void)fetchProductIdentifiersFromURL:(NSURL *)url delegate:(id)delegate
{
    dispatch_queue_t global_queue =
           dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    dispatch_async(global_queue, ^{
        NSError *err;
        NSData *jsonData = [NSData dataWithContentsOfURL:url
                                                  options:NULL
                                                    error:&err];
        if (!jsonData) { /* Handle the error */ }

        NSArray *productIdentifiers = [NSJSONSerialization
            JSONObjectWithData:jsonData options:NULL error:&err];
        if (!productIdentifiers) { /* Handle the error */ }

        dispatch_queue_t main_queue = dispatch_get_main_queue();
        dispatch_async(main_queue, ^{
           [delegate displayProducts:productIdentifiers]; // Custom method
        });
    });
}
```

For information about downloading files using [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection), see Using NSURLConnection in _URL Loading System Programming Guide_.

To ensure that your app remains responsive, use a background thread to download the JSON file and extract the list of product identifiers. To minimize the data transferred, use standard HTTP caching mechanisms, such as the `Last-Modified` and `If-Modified-Since` headers.

## Retrieving Product Information

To make sure your users see only products that are actually available for purchase, query the App Store before displaying your app’s store UI.

Use a products request object to query the App Store. First, create an instance of [SKProductsRequest](https://developer.apple.com/documentation/storekit/skproductsrequest) and initialize it with a list of product identifiers. Be sure to keep a strong reference to the request object; otherwise, the system might deallocate the request before it can complete.

The products request retrieves information about valid products, along with a list of the invalid product identifiers, and then calls its delegate to process the result. The delegate must implement the [SKProductsRequestDelegate](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate) protocol to handle the response from the App Store. Listing 2-2 shows a simple implementation of both pieces of code.

__Listing 2-2__  Retrieving product information

```objc
// Custom method
- (void)validateProductIdentifiers:(NSArray *)productIdentifiers
{
    SKProductsRequest *productsRequest = [[SKProductsRequest alloc]
                    initWithProductIdentifiers:[NSSet setWithArray:productIdentifiers]];

    // Keep a strong reference to the request.
    self.request = productsRequest;
    productsRequest.delegate = self;
    [productsRequest start];
}

// SKProductsRequestDelegate protocol method
- (void)productsRequest:(SKProductsRequest *)request
     didReceiveResponse:(SKProductsResponse *)response
{
    self.products = response.products;

    for (NSString *invalidIdentifier in response.invalidProductIdentifiers) {
        // Handle any invalid product identifiers.
    }

    [self displayStoreUI]; // Custom method
}
```

When the user purchases a product, you need the corresponding product object to create a payment request, so keep a reference to the array of product objects that’s returned to the delegate. If the list of products your app sells can change, you may want to create a custom class that encapsulates a reference to the product object as well as other information—for example, pictures or description text that you fetch from your server. Payment requests are discussed in [Requesting Payment](Requesting%20Payment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnbnknlte).

Product identifiers being returned as invalid usually indicates an error in your app’s list of product identifiers, although it could mean the product hasn’t been properly configured in App Store Connect. Good logging and a good UI help you resolve this type of issue more easily. In production builds, your app needs to fail gracefully—typically, this means displaying the rest of your app’s store UI and omitting the invalid product. In development builds, display an error to call attention to the issue. In both production and development builds, use [NSLog](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSLog) to write a message to the console so you have a record of the invalid identifier. If your app fetched the list from your server, you could also define a logging mechanism to let your app send the list of invalid identifiers back to your server.

## Presenting Your App’s Store UI

Because the design of your app’s store has an important impact on your in-app sales, it’s worth investing the time and effort to get it right. Design the user interface for your store UI so it integrates with the rest of your app. StoreKit can’t provide a store UI for you. Only you know your app and its content well enough to design your store UI in a way that showcases your products in their best light and fits seamlessly with the rest of your app.

Consider the following guidelines as you design and implement your app’s store UI.

__Display a store only if the user can make payments.__ To determine whether the user can make payments, call the [canMakePayments](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506139-canmakepayments) class method of the [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue) class. If the user can’t make payments (for example, because of parental restrictions), either display UI indicating that that the store isn’t available or omit the store portion of your UI entirely.

__Present products naturally in the flow of your app.__ Find the best place in your UI to show your app’s store UI. Present products in context at the time when the user can use them—for example, let users unlock functionality when they try to use that premium feature. Pay special attention to the experience a user has when exploring your app for the first time.

__Organize products so that exploration is easy and enjoyable.__ If your app has a small enough number of products, you can display everything on one screen; otherwise, group or categorize products to make them easy to navigate. Apps with a large number of products, such as comic book readers or magazines with many issues, benefit especially from an interface that makes it easy for users to discover new items they want to purchase. Make the differences between your products clear by giving them distinct names and visuals—if necessary, include explicit comparisons.

__Communicate the value of your products to your users.__ Users want to know exactly what they’re going to buy. Combine information from the App Store, such as product prices and descriptions, with additional data from your server or the app bundle, such as images or demos of your products. Let users interact with a product in a limited way before buying it. For example, a game that gives the user the option to buy new race cars can allow users to run a test lap with the new car. Likewise, a drawing app that lets the user buy additional brushes can give users the chance to draw with the new brush on a small scratch pad and see the difference between brushes. This kind of design provides users an opportunity to experience the product and be convinced they want to purchase it.

__Display prices clearly, using the locale and currency returned by the App Store.__ Ensure that the price of a product is easy to find and easy to read. Don’t try to convert the price to a different currency in your UI, even if the user’s locale and the price’s locale differ. Consider, for example, a user in the United States who prefers the United Kingdom locale for its units and date formatting. Your app displays its UI according to the United Kingdom locale, but it still needs to display product information in the locale specified by the App Store. Converting prices to British pounds sterling, in an attempt to match the United Kingdom locale of the rest of the interface, would be incorrect. The user has an App Store account in the United States and pays in U.S. dollars, so prices would be provided to your app in U.S. dollars. Likewise, your app would display its prices in U.S. dollars. Listing 2-3 shows how to correctly format a price by using the product’s locale information.

__Listing 2-3__  Formatting a product’s price

```
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setFormatterBehavior:NSNumberFormatterBehavior10_4];
[numberFormatter setNumberStyle:NSNumberFormatterCurrencyStyle];
[numberFormatter setLocale:product.priceLocale];
NSString *formattedPrice = [numberFormatter stringFromNumber:product.price];
```

After a user selects a product to buy, your app connects to the App Store to request payment for the product.

## Suggested Testing Steps

Test each part of your code to verify that you’ve implemented it correctly.

### Sign In to the App Store with Your Test Account

Create a test user account in App Store Connect.

On a development iOS device, sign out of the App Store in Settings. Then build and run your app from Xcode.

On a development macOS device, sign out of the Mac App Store. Then build your app in Xcode and launch it from the Finder.

Use your app to make an in-app purchase. When prompted to sign in to the App Store, use your test account. Note that the text “[Environment: Sandbox]” appears as part of the prompt, indicating that you’re connected to the test environment.

If the text “[Environment: Sandbox]” doesn’t appear, you’re using the production environment. Make sure you’re running a development-signed build of your app. Production-signed builds use the production environment.

__Important:__ Don’t use your test user account to sign in to the production environment. If you do, the test user account becomes invalid and can no longer be used.

### Test Fetching the List of Product Identifiers

If your product identifiers are embedded in your app, set a breakpoint in your code after they’re loaded and verify that the instance of `NSArray` contains the expected list of product identifiers.

If your product identifiers are fetched from a server, manually fetch the JSON file—using a web browser such as Safari or a command-line utility such as `curl`—and verify that the data returned from your server contains the expected list of product identifiers. Also verify that your server correctly implements standard HTTP caching mechanisms.

### Test Handling of Invalid Product Identifiers

Intentionally include an invalid identifier in your app’s list of product identifiers. (Make sure you remove it after testing.)

In a production build, verify that the app displays the rest of its store UI and users can purchase other products. In a development build, verify that the app brings the issue to your attention.

Check the console log and verify that you can correctly identify the invalid product identifier.

### Test a Products Request

Using the list of product identifiers that you tested, create and submit an instance of [SKProductsRequest](https://developer.apple.com/documentation/storekit/skproductsrequest). Set a breakpoint in your code, and inspect the lists of valid and invalid product identifiers. If there are invalid product identifiers, review your products in App Store Connect and correct your JSON file or property list.

[Next](Requesting%20Payment.md)[Previous](Designing%20Your%20App%E2%80%99s%20Products.md)
