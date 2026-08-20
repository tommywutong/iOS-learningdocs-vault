---
title: App Search Programming Guide
apple_id: TP40016308
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-15'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/FindingImages.html
archived_at: '2026-07-15T07:32:54.569604Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Search Programming Guide](index.md)



## Help Users Find Your Images

The #images app in Messages shows people popular images from public websites. Your publicly accessible images may be included in #images search results after Apple's web crawler, known as Applebot, has scanned your website.

> [!IMPORTANT]
> 

To make your publicly accessible images available for #images search results, follow these steps:

- Implement an iMessage app. To learn more, see _[Messages Framework Reference](https://developer.apple.com/documentation/messages)_ and the sample code project _[Ice Cream Builder: A simple Messages app extension](https://developer.apple.com/library/archive/samplecode/IceCreamBuilder/Introduction/Intro.html#//apple_ref/doc/uid/TP40017329)_.
- Update your `apple-app-site-association` file to include a dictionary that specifies the paths and patterns that should be indexed by #images (to learn how to do this, see [Update Your Association File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjufvjvona)).
- Update your `com.apple.developer.associated-domains` entitlement to include a list of web domains that host your publicly available images.
- Allow crawling by Applebot. To learn more, see [About Applebot](https://support.apple.com/en-us/HT204683).

To be considered for inclusion in #images search results, your publicly accessible images must meet the following specifications:

- No smaller than 180 x 180 pixels
- GIF format (preferred) or static image
- No larger than 2 MB per image file

### Update Your Association File

Add a dictionary for the `spotlight-image-search` service to your `apple-app-site-association` file (if you need to create this file, see [Creating and Uploading the Association File](UniversalLinks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjsfvjvona) to learn how). The `spotlight-image-search` dictionary should include your app ID (which is the team ID or app ID prefix, followed by the bundle ID) and a `search` key that contains the root path for your images. You can specify up to 500 paths and patterns that can be included for indexing by #images.

The `spotlight-image-search` dictionary can also include the `trending` and `keywords` keys, each of which points to an area of your server that contains resources that Applebot can fetch. Listing 7-1 shows part of an `apple-app-site-association` file that includes a dictionary for the `spotlight-image-search` service.

__Listing 7-1__Adding a `spotlight-image-search` service to an `apple-app-site-association` file

1. `{`
2. `"spotlight-image-search": {`
3. `"details": [{`
4. `"appId": "....",`
5. `"trending": [ { "url": "/trending?secret=abcdefgh&lc=en_US",`
6. `"locale": "en_US" },... ],`
7. `"keywords": [ "/keywords?secret=abcdefgh&page=1",`
8. `"/keywords?secret=abcdefgh&page=2" ... ]`
9. `}`
10. `]}`
11. `}`

One URL on your server can contain multiple keywords, but you should return no more than 20 MB of keywords per fetch. If you want to return keywords in excess of 20 MB, split the resources into multiple server pages and list the pages separately, as shown in Listing 7-1.

Each `/keywords` item should map a keyword to a URL that contains no more than 1000 associated images. List the most important keywords first. Each `trending` URL should point to a server resource that returns a list of `ImageObject` types.

As shown in [Listing 7-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjufvjvoni), you can mix different locales in the same list. You can also map a keyword in one locale to relevant results associated with a different locale, if the results related to the first locale are sparse.

__Listing 7-2__Associating keywords with relevant images

1. `[`
2. `{`
3. `"keyword": "facepalm",`
4. `"locale": "en_US",`
5. `"url": "/search?q=facepalm&format=jsonld"`
6. `},`
7. `{`
8. `"keyword": "télévision drôle",`
9. `"locale": "fr_FR",`
10. `"url": "/search?q=television+funny&format=jsonld"`
11. `},`
12. `...`
13. `]`

> [!NOTE]
> 

To specify images that are trending or associated with keywords, you use the JSON-LD format for the `ImageObject` type to describe each image (for a full list of properties, see [ImageObject](https://schema.org/ImageObject)). The format includes the following keys and values:

|  |  |
| --- | --- |
| **`contentUrl`** | : The URL of the image in the best possible resolution |
| **`mainEntityOfPage`** | : The URL of the webpage that is hosting the content given by `contentUrl` |

|  |  |
| --- | --- |
| **`sameAs`** | : The original source of the asset (raw content bytes) |

|  |  |
| --- | --- |
| **`description`** | : A general description of the image (optional) |
| **`interactionStatistic`** | : A user interaction statistic on a per query level, used for ranking |
| **`aggregateRating`** | : Overall rating based on reviews |
| **`keywords`** | : A list of keywords, each of which is combined with the rating of the keyword with regard to the corresponding image (the rating is required only when `/trending` is used) |
| **`contentRating`** | : MPAA US rating (that is, G, PG, PG-13, R, or NC-17) |
| **`datePublished`** | : The date on which the image was published |

Listing 7-3 shows an example of an image specified in the JSON-LD format for image objects.

__Listing 7-3__Specifying an image using the JSON-LD format

1. `[{`
2. `"@context": "http://schema.org",`
3. `"@type": "ImageObject",`
4. `"contentUrl": "https://www.example.com/media/face-palm-1.gif",`
5. `"mainEntityOfPage": "https://www.example.com/funny",`
6. `"sameAs": "https://www.original-site.com/face-palm-1.gif",`
7. `"description": "rock-n-roll",`
8. `"encodingFormat": "gif",`
9. `"interactionStatistic": {`
10. `"@type": "InteractionCounter",`
11. `"interactionType": "http://schema.org/WatchAction",`
12. `"userInteractionCount": 14300`
13. `},`
14. `"aggregateRating": {`
15. `"@type": "AggregateRating",`
16. `"bestRating": 100,`
17. `"ratingCount": 24,`
18. `"ratingValue": 87`
19. `},`
20. `"contentRating": "PG-13",`
21. `"datePublished": "2016-09-16",`
22. `"keywords": "no, facepalm, smh, smdh, shaking head"`
23. `},`
24. `...`
25. `]`

> [!NOTE]
> 

### Update Your Associated Domains Entitlement

Add to your `com.apple.developer.associated-domains` entitlement a list of the web domains that host the images you want to make searchable. For each domain, specify the `spotlight-image-search` service in an entry such as `spotlight-image-search:yourdomain.com`. To learn more about the associated domains entitlement, see [Preparing Your App to Handle Universal Links](UniversalLinks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjsfvjvomq).

### Specifying a Frequency for Pulling Images

The #images app periodically pulls content from the resources you specify in your `apple-app-site-association` file. You can use HTTP headers to specify frequencies that are appropriate for your content, such as:

- Expiration
- Last modified
- ETag

[Support Universal Links](UniversalLinks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjsfvjvomi)

[Combine APIs to Increase Coverage](CombiningAPIs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjqfvjvomi)
