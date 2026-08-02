---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/PhoneLinks/PhoneLinks.html
archived_at: '2026-07-18T02:29:23.353366Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](FaceTime%20Links.md)[Previous](Mail%20Links.md)

# Phone Links

The `tel` URL scheme is used to launch the Phone app on iOS devices and initiate dialing of the specified phone number. When a user taps a telephone link in a webpage, iOS displays an alert asking if the user really wants to dial the phone number and initiates dialing if the user accepts. When a user opens a URL with the `tel` scheme in a native app, iOS 10.3 and later displays an alert and requires user confirmation before dialing. (When this scenario occurs in versions of iOS prior to 10.3, iOS initiates dialing without further prompting the user and does not display an alert, although a native app can be configured to display its own alert.)

FaceTime in macOS 10.10 and later can also use the `tel` URL scheme to launch the Phone app on an iOS device by using Handoff. This scenario works when FaceTime is configured to dial phone numbers (the default configuration) and the iOS device is connected to the same iCloud account as the Mac.

You can specify phone links explicitly in both web and native iOS apps using the `tel` URL scheme. The following examples show the strings formatted for Safari and for a native app:

- HTML link:

```
<a href="tel:1-408-555-5555">1-408-555-5555</a>
```
- Native app URL string:

```
tel:1-408-555-5555
```

To prevent users from maliciously redirecting phone calls or changing the behavior of a phone or account, the Phone app supports most, but not all, of the special characters in the `tel` scheme. Specifically, if a URL contains the `*` or `#` characters, the Phone app does not attempt to dial the corresponding phone number. If your app receives URL strings from the user or an unknown source, you should also make sure that any special characters that might not be appropriate in a URL are escaped properly. For native apps, use the [stringByAddingPercentEscapesUsingEncoding:](https://developer.apple.com/documentation/foundation/nsstring/1415058-addingpercentescapes) method of `NSString` to escape characters, which returns a properly escaped version of your original string.

In Safari on iOS, telephone number detection is on by default. However, if your webpage contains numbers that can be interpreted as phone numbers, but are not phone numbers, you can turn off telephone number detection. You might also turn off telephone number detection to prevent the DOM document from being modified when parsed by the browser. To turn off telephone number detection in Safari on iOS, use the `format-detection` meta tag as follows:

```
<meta name = "format-detection" content = "telephone=no">
```

Listing 2-1 shows a simple webpage in which automatic telephone number detection is off. When displayed in Safari on iOS, the `408-555-5555` telephone number does not appear as a link. However, the `1-408-555-5555` number does appear as a link because it is in a phone link.

__Listing 2-1__  Turning telephone number detection off

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" >
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Telephone Number Detection</title>
    <meta name = "viewport" content = "width=device-width">
     <!-- Turn off telephone number detection. -->
    <meta name = "format-detection" content = "telephone=no">
</head>
<body>
     <!-- Then use phone links to explicitly create a link. -->
     <p>A phone number: <a href="tel:1-408-555-5555">1-408-555-5555</a></p>
     <!-- Otherwise, numbers that look like phone numbers are not links. -->
     <p>Not a phone number: 408-555-5555</p>
</body>
</html>
```

For more information about the `tel` URL scheme, see [RFC 2806](http://www.ietf.org/rfc/rfc2806.txt) and [RFC 2396](http://www.ietf.org/rfc/rfc2396.txt).

[Next](FaceTime%20Links.md)[Previous](Mail%20Links.md)

