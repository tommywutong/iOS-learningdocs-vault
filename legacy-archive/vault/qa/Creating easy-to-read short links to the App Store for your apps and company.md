---
title: Creating easy-to-read short links to the App Store for your apps and company
apple_id: DTS40009414
resource_type: QA
platform: iOS|macOS
topic: General
technology: null
published: '2013-04-24'
source_url: https://developer.apple.com/library/archive/qa/qa1633/_index.html
archived_at: '2026-07-18T02:33:02.643922Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1633

# Creating easy-to-read short links to the App Store for your apps and company

## Q:  How can I create easy-to-read short links to the App Store for my apps and company?

A: The iTunes and App Store apps generate URLs for all apps and companies available in the App Store and Mac App Store by clicking the disclosure triangle next to the app's price (or by right-clicking/control-clicking the app icon) and selecting "Copy link", or by using [iTunes Link Maker](http://itunes.apple.com/linkmaker/). These URLs look similar to Listing 1.

__Listing 1__  Standard App Store Links.

```
https://itunes.apple.com/us/app/keynote/id361285480?mt=8
```

These URLs are great for linking to your app or company page in the App Store or Mac App Store from your website or inside your app, or anywhere you don't need to type or speak the URL. As a rule, always use these standard links when driving users to your app from your digital marketing communications.

You can also create easy-to-read links to your app using App Store Short Links, which use the AppStore.com base URL plus a specific form of your app or company name. These short links are ideal for use in offline communications materials like print ads, TV spots, app trailers, radio ads and billboards where you need a memorable URL.

There are three types of App Store Short Links, in two forms, one for iOS apps, another for Mac Apps:

__Company Name__

- iOS: http://appstore.com/<companyname> for example, http://appstore.com/apple
- Mac: http://appstore.com/mac/<companyname> for example, http://appstore.com/mac/apple

__App Name__

- iOS: http://appstore.com/<appname> for example, http://appstore.com/keynote
- Mac: http://appstore.com/mac/<appname> for example, http://appstore.com/mac/keynote

__App by Company__

- iOS: http://appstore.com/<companyname>/<appname> for example, http://appstore.com/apple/keynote
- Mac: http://appstore.com/mac/<companyname>/<appname> for example, http://appstore.com/mac/apple/keynote

Most companies and apps have a canonical App Store Short Link. This canonical URL is created by changing or removing certain characters (many of which are illegal or have special meaning in a URL (for example, "&")).

To create an App Store Short Link, apply the following rules to your company or app name:

- Remove all whitespace
- Convert all characters to lower-case
- Remove all copyright (©), trademark (™) and registered mark (®) symbols
- Replace ampersands ("&") with "and"
- Remove most punctuation (See Listing 2 for the set)
- Replace accented and other "decorated" characters (ü, å, etc.) with their elemental character (u, a, etc.)
- Leave all other characters as-is.

__Listing 2__  Punctuation characters that must be removed.

```
!¡"#$%'()*+,\-./:;<=>¿?@[\]^_`{|}~
```

Below are some examples to demonstrate the conversion that takes place.

__App Store__

__Company Name examples__

- Gameloft => http://appstore.com/gameloft
- Activision Publishing, Inc. => http://appstore.com/activisionpublishinginc
- Chen's Photography & Software => http://appstore.com/chensphotographyandsoftware

__App Name examples__

- Ocarina => http://appstore.com/ocarina
- Where’s My Perry? => http://appstore.com/wheresmyperry
- Brain Challenge™ => http://appstore.com/brainchallenge

__Mac App Store__

__Company Name examples__

- PopCap => http://appstore.com/mac/popcap
- Autodesk Inc. => http://appstore.com/mac/autodeskinc
- Chen's Photography & Software => http://appstore.com/chensphotographyandsoftware

__App Name examples__

- Pixelmator => http://appstore.com/mac/pixelmator
- Human Japanese => http://appstore.com/mac/humanjapanese
- F1 2012™ => http://appstore.com/mac/f12012

All URLs are accessible worldwide and will direct the customer to their respective country's App Store. Because of the possibility of name conflicts or other errors, URLs which have multiple results, for example <http://appstore.com/airhockey>, will return a search page. Using unique names for your apps will help prevent this.

If you experience incorrect results (for example, a URL which doesn't go where you expect it would) or if there are characters you would like to see removed or changed, please file a bug report via <http://developer.apple.com/bugreporter> with the following information:

- Full current or desired URL, for example, http://appstore.com/mysuperapp
- Applicable countries
- The iTunes-generated URL to the desired landing page, which you get by clicking the disclosure triangle next to the app's price (or by right-clicking/control-clicking the app icon) and selecting "Copy link" (for example, http://itunes.apple.com/us/app...)

These App Store Short Links are provided as a convenience and are not guaranteed to link to a particular app or company. Be sure to test your URLs before using them in any marketing or other public materials. If there are naming conflicts, continue using the standard itunes.apple.com URLs, which contain a unique numerical identifier within the URL.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-04-24 | Added reference to iTunes Link Maker; removed reference to r. 7414684 (itunes.apple.com links to your company's page give an error) as issue is fixed. Minor editorial changes. |
| 2013-02-21 | Minor changes to URLs |
| 2013-01-31 | Updated to reflect App Store Short Links (appstore.com) and Mac App Store options. |
| 2010-01-25 | Corrected link to QA1629; fixed a company name misspelling. |
| 2009-12-10 | New document that describes how to create appstore.com short URLs to the App Store. |

