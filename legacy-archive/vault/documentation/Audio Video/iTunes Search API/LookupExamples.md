---
title: iTunes Search API
apple_id: TP40017632
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: MediaLibrary
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/LookupExamples.html
archived_at: '2026-07-15T05:21:34.474141Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Search API](index.md)



## Lookup Examples

You can also create a lookup request to search for content in the stores based on iTunes IDs, UPCs/ EANs, and All Music Guide (AMG) IDs. ID-based lookups are faster and contain fewer false-positive results.

The following are examples of fully-qualified URLs for specific lookup requests:

- Look up Jack Johnson by iTunes artist ID: [https://itunes.apple.com/lookup?id=909253](https://itunes.apple.com/lookup?id=909253)
- Look up Yelp Software application by iTunes ID: [https://itunes.apple.com/lookup?id=284910350](https://itunes.apple.com/lookup?id=284910350)
- Look up Jack Johnson by AMG artist ID: [https://itunes.apple.com/lookup?amgArtistId=468749](https://itunes.apple.com/lookup?amgArtistId=468749).
- Look up multiple artists by their AMG artist IDs: [https://itunes.apple.com/lookup?amgArtistId=468749,5723](https://itunes.apple.com/lookup?amgArtistId=468749,5723).
- Look up all albums for Jack Johnson: [https://itunes.apple.com/lookup?id=909253&entity=album](https://itunes.apple.com/lookup?id=909253&entity=album).
- Look up multiple artists by their AMG artist IDs and get each artist’s top 5 albums: [https://itunes.apple.com/lookup?amgArtistId=468749,5723&entity=album&limit=5](https://itunes.apple.com/lookup?amgArtistId=468749,5723&entity=album&limit=5).
- Look up multiple artists by their AMG artist IDs and get each artist’s 5 most recent songs: [https://itunes.apple.com/lookup?amgArtistId=468749,5723&entity=song&limit=5&sort=recent](https://itunes.apple.com/lookup?amgArtistId=468749,5723&entity=song&limit=5&sort=recent).
- Look up an album or video by its UPC: [https://itunes.apple.com/lookup?upc=720642462928](https://itunes.apple.com/lookup?upc=720642462928).
- Look up an album by its UPC, including the tracks on that album: [https://itunes.apple.com/lookup?upc=720642462928&entity=song](https://itunes.apple.com/lookup?upc=720642462928&entity=song).
- Look up an album by its AMG Album ID: [https://itunes.apple.com/lookup?amgAlbumId=15175,15176,15177,15178,15183,15184,15187,1519,15191,15195,15197,15198](https://itunes.apple.com/lookup?amgAlbumId=15175,15176,15177,15178,15183,15184,15187,1519,15191,15195,15197,15198).
- Look up a Movie by AMG Video ID: [https://itunes.apple.com/lookup?amgVideoId=17120](https://itunes.apple.com/lookup?amgVideoId=17120).
- Look up a book by its 13 digit ISBN: [https://itunes.apple.com/lookup?isbn=9780316069359](https://itunes.apple.com/lookup?isbn=9780316069359).

[Search Examples](SearchExamples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmzsfvbuqnrnknltc)

[Understanding Search Results](UnderstandingSearchResults.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmzsfvbuqobnknltc)
