---
title: iTunes Search API
apple_id: TP40017632
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: MediaLibrary
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/UnderstandingSearchResults.html
archived_at: '2026-07-15T05:21:36.474624Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Search API](index.md)



## Understanding Search Results

The Search API returns your search results in JavaScript Object Notation (JSON) format. JSON is built on two structures:

- A collection of name/value pairs, also known as an object; this concept is similar to a Java Map object, a Javascript Dictionary, or a Pearl/Ruby hash. An object is an unordered set of name/value pairs, beginning with a left brace ( { ) and ending with a right brace ( } ). Each name is surrounded by double-quotes and followed by a colon ( : ); the name/value pairs are separated by commas ( , ).
- An ordered list of values, also known as an array. An array is an ordered collection of values, beginning with a left bracket ( [ ) and ending with a right bracket ( ] ). Values are separated by commas ( , ).

All JSON results are encoded as UTF-8. For more information on JSON, see [http://www.json.org](http://www.json.org/).

The following example displays the JSON results for a song in the iTunes Store:

1. `{"wrapperType":"track",
   "kind":"song",
   "artistId":909253,
   "collectionId":120954021,
   "trackId":120954025,
   "artistName":"Jack Johnson",
   "collectionName":"Sing-a-Longs and Lullabies for the Film Curious George",
   "trackName":"Upside Down",
   "collectionCensoredName":"Sing-a-Longs and Lullabies for the Film Curious George",
   "trackCensoredName":"Upside Down",
   "artistViewUrl":"https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewArtist?id=909253",
   "collectionViewUrl":"https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewAlbum?i=120954025&id=120954021&s=143441",
   "trackViewUrl":"https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewAlbum?i=120954025&id=120954021&s=143441",
   "previewUrl":"http://a1099.itunes.apple.com/r10/Music/f9/54/43/mzi.gqvqlvcq.aac.p.m4p",
   "artworkUrl60":"http://a1.itunes.apple.com/r10/Music/3b/6a/33/mzi.qzdqwsel.60x60-50.jpg",
   "artworkUrl100":"http://a1.itunes.apple.com/r10/Music/3b/6a/33/mzi.qzdqwsel.100x100-75.jpg",
   "collectionPrice":10.99,
   "trackPrice":0.99,
   "collectionExplicitness":"notExplicit",
   "trackExplicitness":"notExplicit",
   "discCount":1,
   "discNumber":1,
   "trackCount":14,
   "trackNumber":1,
   "trackTimeMillis":210743,
   "country":"USA",
   "currency":"USD",
   "primaryGenreName":"Rock"}`

The following table defines the JSON result keys and values:

| Result Key | Description | Returned | Retun Values and Examples |
| --- | --- | --- | --- |
| wrapperType | The name of the object returned by the search request. | Y | track, collection, artist  For example: track. |
| \*explicitness | The Recording Industry Association of America (RIAA) parental advisory for the content returned by the search request. For more information, see [http://itunes.apple.com/WebObjects/MZStore.woa/wa/parentalAdvisory](http://itunes.apple.com/WebObjects/MZStore.woa/wa/parentalAdvisory). | Y | explicit (explicit lyrics, possibly explicit album cover), cleaned (explicit lyrics “bleeped out”), notExplicit (no explicit lyrics)  For example: “trackExplicitness”:”notExplicit”. |
| kind | The kind of content returned by the search request. | Y | book, album, coached-audio, feature-movie, interactive- booklet, music-video, pdf podcast, podcast-episode, software-package, song, tv- episode, artist  For example: song. |
| trackName | The name of the track, song, video, TV episode, and so on returned by the search request. | Y | For example: “Banana Pancakes”. |
| artistName | The name of the artist returned by the search request. | Y | For example: “Jack Johnson”. |
| collectionName | The name of the album, TV season, audiobook, and so on returned by the search request. | Y | For example: “In Between Dreams”. |
| \*censoredName | The name of the album, TV season, audiobook, and so on returned by the search request, with objectionable words \*’d out.  __Note:__ Artist names are never censored. | Y | For example: “S\*\*t Happens”. |
| artworkUrl100, artworkUrl60 | A URL for the artwork associated with the returned media type, sized to 100×100 pixels or 60×60 pixels. | Only when artwork is available | For example: “http:// a1.itunes.apple.com/jp/r10/Music/ y2005/m06/d03/h05/ s05.oazjtxkw.100×100-75.jpg”. |
| \*viewURL | A URL for the content associated with the returned media type. You can click the URL to view the content in the iTunes Store. | Y | For example: “http:// itunes.apple.com/WebObjects/ MZStore.woa/wa/viewAlbum? i=68615807&id=68615813&s=1434 62”. |
| previewURL | A URL referencing the 30-second preview file for the content associated with the returned media type. . | Only when media type is track | For example: “http:// a392.itunes.apple.com/jp/r10/ Music/y2005/m06/d03/h05/s05.zdzqlufu.p.m4p”. |
| trackTimeMillis | The returned track’s time in milliseconds. | Only when media type is track |  |

[Lookup Examples](LookupExamples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmzsfvbuqnznknltc)
