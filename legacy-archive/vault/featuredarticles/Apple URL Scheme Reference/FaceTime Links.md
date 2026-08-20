---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/FacetimeLinks/FacetimeLinks.html
archived_at: '2026-07-18T02:29:23.141438Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](SMS%20Links.md)[Previous](Phone%20Links.md)

# FaceTime Links

The `facetime` URL scheme is used to initiate a FaceTime call to a specified user. You can use the phone number or email address of a user to initiate the call. When a user taps a FaceTime link in a webpage, iOS confirms that the user really wants to initiate a FaceTime call before proceeding. When an app opens a URL with the `facetime` scheme, iOS opens the FaceTime app and initiates the call without prompting the user. When opening FaceTime URLs on macOS, the system always prompts the user before initiating a call.

You can specify FaceTime links explicitly in both web and native iOS apps using the `facetime` URL scheme. The following examples show the strings formatted for Safari and for a native app:

- HTML links for FaceTime video calls:

```
<a href="facetime:14085551234">Connect using FaceTime</a>
<a href="facetime:user@example.com">Connect using FaceTime</a>
```
- HTML links for FaceTime audio calls (iOS only):

```
<a href="facetime-audio:14085551234">Connect using FaceTime</a>
<a href="facetime-audio:user@example.com">Connect using FaceTime</a>
```
- Native app URL strings for FaceTime video calls:

```
facetime:// 14085551234
facetime://user@example.com
```
- Native app URL strings for FaceTime audio calls (iOS only):

```
facetime-audio:// 14085551234
facetime-audio://user@example.com
```

To prevent users from maliciously redirecting calls or changing the behavior of a phone or account, the FaceTime app supports most, but not all, of the special characters in the `facetime` schemes. Specifically, if a URL contains the `*` or `#` characters, the app ignores those characters when they are included after the phone number. If your app receives URL strings from the user or from an unknown source, use the [stringByAddingPercentEscapesUsingEncoding:](https://developer.apple.com/documentation/foundation/nsstring/1415058-addingpercentescapes) method of `NSString` to generate a properly escaped version of the original string before opening the URL.

[Next](SMS%20Links.md)[Previous](Phone%20Links.md)

