---
title: iTunes Search API
apple_id: TP40017632
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: MediaLibrary
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html
archived_at: '2026-07-15T05:21:35.971551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iTunes Search API](index.md)



## Constructing Searches

To search for content from a field in your website and display the results in your website, you must create a search field that passes a fully-qualified URL content request to the iTunes Store, parse the JavaScript Object Notation (JSON) format returned from the search, and display the results in your website.

The fully-qualified URL must have the following format: `https://itunes.apple.com/search?parameterkeyvalue`. Where `parameterkeyvalue` can be one or more parameter key and value pairs indicating the details of your query.

To construct a parameter key and value pair, you must concatenate each parameter key with an equal sign (=) and a value string. For example: `key1=value1`. To create a string of parameter key and value pairs, you must concatenate each pair using an ampersand (&). For example: `key1=value1&key2=value2&key3=value3`.

> [!NOTE]
> 

The following table defines the parameter keys and values you can specify to search for content within the iTunes Store, App Store, iBooks Store and Mac App Store:

| Parameter Key | Description | Required | Values |
| --- | --- | --- | --- |
| term | The URL-encoded text string you want to search for. For example: jack+johnson. | Y | Any URL-encoded text string.  __Note__: URL encoding replaces spaces with the plus (+) character and all characters except the following are encoded: letters, numbers, periods (.), dashes (-), underscores (_), and asterisks (\*). |
| country | The two-letter country code for the store you want to search. The search uses the default store front for the specified country. For example: US. The default is US. | Y | See [http://en.wikipedia.org/wiki/ ISO_3166-1_alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) for a list of ISO Country Codes. |
| media | The media type you want to search for. For example: movie. The default is all. | N | movie, podcast, music, musicVideo, audiobook, shortFilm, tvShow, software, ebook, all |
| entity | The type of results you want returned, relative to the specified media type. For example: movieArtist for a movie media type search. The default is the track entity associated with the specified media type. | N | For a list of available entitites, see [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmzsfvbuqnjnknlte). |
| callback | The name of the Javascript callback function you want to use when returning search results to your website. | Y, for cross-site searches | wsSearchCB |
| limit | The number of search results you want the iTunes Store to return. For example: 25. The default is 50. | N | 1 to 200 |
| lang | The language, English or Japanese, you want to use when returning search results. Specify the language using the five-letter codename. For example: en_us. The default is en_us (English). | N | en_us, ja_jp |
| version | The search result key version you want to receive back from your search. The default is 2. | N | 1,2 |
| explicit | A flag indicating whether or not you want to include explicit content in your search results. The default is Yes. | N | Yes, No |

The following table describes the available entities for each media type:

__Table 2-1__Media type entities

| Media Type | Entities |
| --- | --- |
| movie | movieArtist, movie |
| podcast | podcastAuthor, podcast |
| music | musicArtist, musicTrack, album, musicVideo, mix, song.  Please note that “musicTrack” can include both songs and music videos in the results. |
| musicVideo | musicArtist, musicVideo |
| audiobook | audiobookAuthor, audiobook |
| shortFilm | shortFilmArtist, shortFilm |
| tvShow | tvEpisode, tvSeason |
| software | software, iPadSoftware, macSoftware |
| ebook | ebook |
| all | movie, album, allArtist, podcast, musicVideo, mix, audiobook, tvSeason, allTrack |

Use the following techniques to improve search response times:

- It is critical to encode your URLs correctly in order to be commissioned for affiliate links. Notes on affiliate encoding raw links can be found in the [Advanced Affiliate Linking](https://affiliate.itunes.apple.com/resources/documentation/linking-to-the-itunes-music-store/) document.
- To improve response times, minimize the number of search results the Search API returns by specifying an appropriate value for the limit parameter key.
- The Search API is limited to approximately 20 calls per minute (subject to change). If you require heavier usage, we suggest you consider using our Enterprise Partner Feed (EPF). If you wish to access content on our EPF, please review [iTunes Affliate Resources](https://affiliate.itunes.apple.com/resources/documentation/itunes-enterprise-partner-feed/) for more information.
- Large websites should set up caching logic for the search and lookup requests sent to the Search API.

[Overview](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmzsfvbuqmznknltc)

[Search Examples](SearchExamples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmzsfvbuqnrnknltc)
