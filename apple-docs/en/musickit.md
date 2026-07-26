---
title: MusicKit
framework: MusicKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/musickit
source_url: 'https://developer.apple.com/documentation/musickit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/musickit.json'
content_hash: 'sha256:9a2f5f5ddc8b9522'
translated: false
---

> Navigation: [Technologies](technologies.md)

# MusicKit

<sub>Framework</sub>

Integrate your app with Apple Music.

## Overview

Use MusicKit to integrate your app with [Apple Music API](applemusicapi.md), a web service you use to access information about music items in the Apple Music catalog. Using MusicKit, you can more easily build apps that tie into Apple Music.

The framework provides a model layer for accessing music items in Swift, as well as playback support so you can add music to your app. Additionally, it provides some related user interface elements, such as a view to display images that correspond to artwork for a music item, or a way to present music subscription offers to users who may not have an active Apple Music subscription.

> [!important] Important
> Users must grant permission for your app to access their music data. Add the [NSAppleMusicUsageDescription](bundleresources/information-property-list/nsapplemusicusagedescription.md) key to your app’s `Info.plist` file, and include a description of how you intend to use the user’s media. If this key isn’t present, the system terminates your app when it tries to access the user’s music.

Request permission for your app to use MusicKit with [MusicAuthorization](musickit/musicauthorization.md). Check specific capabilities for the current [MusicSubscription](musickit/musicsubscription.md) to ensure your music-related functionality is available to the user. Find music items using a search term with [MusicCatalogSearchRequest](musickit/musiccatalogsearchrequest.md), or find music items using a filter with [MusicCatalogResourceRequest](musickit/musiccatalogresourcerequest.md). Play music in your app with one of the two music players that MusicKit offers. Allow the user to begin a free trial for Apple Music from within your app by presenting a music subscription offer.

You can load content from an arbitrary Apple Music API endpoint with [MusicDataRequest](musickit/musicdatarequest.md) to take further advantage of additional functionality available in Apple Music API.

## Topics

### Essentials

- [Using Automatic Developer Token Generation for Apple Music API](musickit/using-automatic-token-generation-for-apple-music-api.md) — Enable your app’s integration with the MusicKit App Service in the developer portal.
- [Using MusicKit to integrate with Apple Music](musickit/using-musickit-to-integrate-with-apple-music.md) — Find an album in Apple Music that corresponds to a CD in a user’s collection, and present the information for the album.
- [NSAppleMusicUsageDescription](bundleresources/information-property-list/nsapplemusicusagedescription.md) — A message that tells people why the app is requesting access to their media library.

### Music Items

- [Album](musickit/album.md) — A music item that represents an album.
- [Artist](musickit/artist.md) — A music item that represents an artist.
- [Curator](musickit/curator.md) — A music item that represents a curator.
- [Genre](musickit/genre.md) — A music item that represents a genre.
- [MusicVideo](musickit/musicvideo.md) — A music item that represents a music video.
- [Playlist](musickit/playlist.md) — A music item that represents a playlist.
- [RadioShow](musickit/radioshow.md) — A music item that represents a radio show.
- [RecordLabel](musickit/recordlabel.md) — A music item that represents a record label.
- [Song](musickit/song.md) — A music item that represents a song.
- [Station](musickit/station.md) — A music item that represents a station.
- [Track](musickit/track.md) — A music item that represents a track.

### Music Item Attributes

- [ContentRating](musickit/contentrating.md) — The rating of the content that potentially plays while playing a resource.
- [EditorialNotes](musickit/editorialnotes.md) — An object that represents editorial notes.
- [PreviewAsset](musickit/previewasset.md) — An object that represents a preview for resources.

### Catalog Search

- [MusicCatalogSearchRequest](musickit/musiccatalogsearchrequest.md) — A request that your app uses to fetch items from the Apple Music catalog using a search term.
- [MusicCatalogSearchResponse](musickit/musiccatalogsearchresponse.md) — An object that contains results for a catalog search request.
- [MusicCatalogSearchable](musickit/musiccatalogsearchable.md) — A protocol for music items that your app can fetch by using a catalog search request.

### Resource Loading Using Filters

- [MusicCatalogResourceRequest](musickit/musiccatalogresourcerequest.md) — A request that your app uses to fetch items from the Apple Music catalog using a filter.
- [MusicCatalogResourceResponse](musickit/musiccatalogresourceresponse.md) — An object that contains results for a catalog resource request.
- [AlbumFilter](musickit/albumfilter.md) — Album properties your app uses as a filter for a catalog resource request.
- [ArtistFilter](musickit/artistfilter.md) — Artist properties your app uses as a filter for a catalog resource request.
- [CuratorFilter](musickit/curatorfilter.md) — Curator properties your app uses as a filter for a catalog resource request.
- [GenreFilter](musickit/genrefilter.md) — Genre properties your app uses as a filter for a catalog resource request.
- [MusicVideoFilter](musickit/musicvideofilter.md) — Music video properties your app uses as a filter for a catalog resource request.
- [PlaylistFilter](musickit/playlistfilter.md) — Playlist properties your app uses as a filter for a catalog resource request.
- [RadioShowFilter](musickit/radioshowfilter.md) — Radio Show properties your app uses as a filter for a catalog resource request.
- [RecordLabelFilter](musickit/recordlabelfilter.md) — The set of record label properties your app uses as a filter for a catalog resource request.
- [SongFilter](musickit/songfilter.md) — Song properties your app uses as a filter for a catalog resource request.
- [StationFilter](musickit/stationfilter.md) — The set of station properties your app uses as a filter for a catalog resource request.
- [FilterableMusicItem](musickit/filterablemusicitem.md) — A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.

### General Purpose Data Request

- [MusicDataRequest](musickit/musicdatarequest.md) — A request for loading data from an arbitrary Apple Music API endpoint.
- [MusicDataResponse](musickit/musicdataresponse.md) — An object containing results for a data request.

### Playback

- [ApplicationMusicPlayer](musickit/applicationmusicplayer.md) — An object your app uses to play music in a way that doesn’t affect the Music app’s state.
- [SystemMusicPlayer](musickit/systemmusicplayer.md) — An object your app uses to play music by controlling the Music app’s state.
- [MusicPlayer](musickit/musicplayer.md) — An object your app uses to play music.
- [PlayableMusicItem](musickit/playablemusicitem.md) — A set of properties that a music player uses to initiate playback for a music item.
- [PlayParameters](musickit/playparameters.md) — An opaque object that represents parameters to initiate playback of a playable music item using a music player.

### Artwork

- [Artwork](musickit/artwork.md) — An object that represents artwork for a music item.
- [ArtworkImage](musickit/artworkimage.md) — A view that displays the image for a music item’s artwork.

### Authorization

- [MusicAuthorization](musickit/musicauthorization.md) — A type that allows you to request the user’s informed consent for your app to access their music data.

### Apple Music Subscription

- [MusicSubscription](musickit/musicsubscription.md) — A representation of the current state of the user’s subscription to Apple Music.
- [MusicSubscriptionOffer](musickit/musicsubscriptionoffer.md) — A type for grouping other types for showing subscription offers for Apple Music.

### Token management

- [MusicTokenProvider](musickit/musictokenprovider.md) — An object that music requests use to access Apple Music API.
- [MusicDeveloperTokenProvider](musickit/musicdevelopertokenprovider.md) — A set of methods that music requests use to access Apple Music API.
- [MusicUserTokenProvider](musickit/musicusertokenprovider.md) — A class that music requests use to fetch user tokens your app requires to access Apple Music API.
- [MusicTokenRequestOptions](musickit/musictokenrequestoptions.md) — Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.
- [MusicTokenRequestError](musickit/musictokenrequesterror.md) — An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
- [DefaultMusicTokenProvider](musickit/defaultmusictokenprovider.md) — The default token provider that music requests use to access Apple Music API.

### Utility

- [MusicItem](musickit/musicitem.md) — A protocol with basic requirements for music items.
- [MusicItemID](musickit/musicitemid.md) — An object that represents a unique identifier for a music item.
- [MusicItemCollection](musickit/musicitemcollection.md) — A collection of music items.
- [MusicPropertyContainer](musickit/musicpropertycontainer.md) — A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- [MusicRelationshipProperty](musickit/musicrelationshipproperty.md) — An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- [MusicExtendedAttributeProperty](musickit/musicextendedattributeproperty.md) — An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- [MusicAttributeProperty](musickit/musicattributeproperty.md) — An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- [PartialMusicAsyncProperty](musickit/partialmusicasyncproperty.md) — A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- [PartialMusicProperty](musickit/partialmusicproperty.md) — A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- [AnyMusicProperty](musickit/anymusicproperty.md) — A type-erased identifier for a music item property, from any root type to any resulting value type.

### Articles

- [Explore more content with MusicKit](musickit/explore-more-content-with-musickit.md) — Track your outdoor runs with access to the Apple Music catalog, personal recommendations, and your own personal music library.
- [Integrating MusicKit into your app](musickit/integrating-musickit-into-your-app.md) — Enhance your workouts with Apple Music playback.

### Classes

- [MusicLibrary](musickit/musiclibrary.md) — An object your app uses to access the user’s music library.

### Protocols

- [LibraryAlbumFilter](musickit/libraryalbumfilter.md) — Album properties your app uses as a filter for a library request.
- [LibraryAlbumSortProperties](musickit/libraryalbumsortproperties.md) — Album properties your app uses to sort results for a library request.
- [LibraryArtistFilter](musickit/libraryartistfilter.md) — Artist properties your app uses as a filter for a library request.
- [LibraryArtistSortProperties](musickit/libraryartistsortproperties.md) — Artist properties your app uses to sort results for a library request.
- [LibraryGenreFilter](musickit/librarygenrefilter.md) — Genre properties your app uses as a filter for a library request.
- [LibraryGenreSortProperties](musickit/librarygenresortproperties.md) — Genre properties your app uses to sort results for a library request.
- [LibraryMusicVideoFilter](musickit/librarymusicvideofilter.md) — Music video properties your app uses as a filter for a library request.
- [LibraryMusicVideoSortProperties](musickit/librarymusicvideosortproperties.md) — Music video properties your app uses to sort results for a library request.
- [LibraryPlaylistEntryFilter](musickit/libraryplaylistentryfilter.md) — Playlist entry properties your app uses as a filter for a library request.
- [LibraryPlaylistEntrySortProperties](musickit/libraryplaylistentrysortproperties.md) — Playlist entry properties your app uses to sort results for a library request.
- [LibraryPlaylistFilter](musickit/libraryplaylistfilter.md) — Playlist properties your app uses as a filter for a library request.
- [LibraryPlaylistSortProperties](musickit/libraryplaylistsortproperties.md) — Playlist properties your app uses to sort results for a library request.
- [LibrarySongFilter](musickit/librarysongfilter.md) — Song properties your app uses as a filter for a library request.
- [LibrarySongSortProperties](musickit/librarysongsortproperties.md) — Song properties your app uses to sort results for a library request.
- [LibraryTrackFilter](musickit/librarytrackfilter.md) — Track properties your app uses as a filter for a library request.
- [LibraryTrackSortProperties](musickit/librarytracksortproperties.md) — Track properties your app uses to sort results for a library request.
- [MusicCatalogChartRequestable](musickit/musiccatalogchartrequestable.md) — A protocol for music items that your app can fetch by using a catalog charts request.
- [MusicCatalogTopLevelResourceRequesting](musickit/musiccatalogtoplevelresourcerequesting.md) — A protocol for music items that your app can fetch by using a catalog resource request without any filter.
- [MusicLibraryAddable](musickit/musiclibraryaddable.md) — A protocol for music items that your app can add to the music library.
- [MusicLibraryRequestFilterValueEquatable](musickit/musiclibraryrequestfiltervalueequatable.md) — A protocol for types of values your app can use with equality filters when fetching items using a music library request.
- [MusicLibraryRequestFilterValueMembershipComparable](musickit/musiclibraryrequestfiltervaluemembershipcomparable.md) — A protocol for types of values your app can use with membership filters when fetching items using a music library request.
- [MusicLibraryRequestable](musickit/musiclibraryrequestable.md) — A protocol for music items that your app can fetch by using a library request.
- [MusicLibrarySearchable](musickit/musiclibrarysearchable.md) — A protocol for music items that your app can fetch by using a library search request.
- [MusicLibrarySectionRequestable](musickit/musiclibrarysectionrequestable.md) — A protocol for types your app uses as sections when fetching items using a library sectioned request.
- [MusicPersonalRecommendationItem](musickit/musicpersonalrecommendationitem.md) — A protocol for music items that your app can fetch by using a personal recommendations request.
- [MusicPlaylistAddable](musickit/musicplaylistaddable.md) — A protocol for music items that your app can add to a playlist.
- [MusicRecentlyPlayedRequestable](musickit/musicrecentlyplayedrequestable.md) — A protocol for music items that your app can fetch by using a recently played request.
- [PickableMusicItem](musickit/pickablemusicitem.md) — A protocol for the MusicKit item type that can be selected in the music picker. _(beta)_

### Structures

- [MusicCatalogChart](musickit/musiccatalogchart.md) — An object that contains popular items in the Apple Music catalog.
- [MusicCatalogChartsRequest](musickit/musiccatalogchartsrequest.md) — A request that your app uses to fetch the most popular items in the Apple Music catalog.
- [MusicCatalogChartsResponse](musickit/musiccatalogchartsresponse.md) — An object that contains results for a catalog charts request.
- [MusicCatalogResourceRequestOption](musickit/musiccatalogresourcerequestoption.md) — An option to use when requesting a resource from the Apple Music catalog.
- [MusicCatalogSearchSuggestionsRequest](musickit/musiccatalogsearchsuggestionsrequest.md) — A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.
- [MusicCatalogSearchSuggestionsResponse](musickit/musiccatalogsearchsuggestionsresponse.md) — An object that contains results for a catalog search suggestions request.
- [MusicLibraryRequest](musickit/musiclibraryrequest.md) — A request that your app uses to fetch items from the user’s music library.
- [MusicLibraryResponse](musickit/musiclibraryresponse.md) — An object that contains results for a library request.
- [MusicLibrarySearchRequest](musickit/musiclibrarysearchrequest.md) — A request that your app uses to fetch items from user’s library using a search term.
- [MusicLibrarySearchResponse](musickit/musiclibrarysearchresponse.md) — An object that contains results for a library search request.
- [MusicLibrarySection](musickit/musiclibrarysection.md) — A section for a library sectioned response.
- [MusicLibrarySectionedRequest](musickit/musiclibrarysectionedrequest.md) — A request that your app uses to fetch items grouped by sections from the user’s music library.
- [MusicLibrarySectionedResponse](musickit/musiclibrarysectionedresponse.md) — An object that contains results for a library sectioned request.
- [MusicPersonalRecommendation](musickit/musicpersonalrecommendation.md) — An object that contains recommended items based on the user’s library and listening history.
- [MusicPersonalRecommendationsRequest](musickit/musicpersonalrecommendationsrequest.md) — A request that your app uses to fetch music recommendations based on the user’s library and listening history.
- [MusicPersonalRecommendationsResponse](musickit/musicpersonalrecommendationsresponse.md) — An object that contains results for a personal recommendations request.
- [MusicRecentlyPlayedRequest](musickit/musicrecentlyplayedrequest.md) — A request that your app uses to fetch items the user has recently played.
- [MusicRecentlyPlayedResponse](musickit/musicrecentlyplayedresponse.md) — An object that contains items the user has recently played.
- [TitledSection](musickit/titledsection.md) — A section you can use to request items from the library grouped by title.

### Type Aliases

- [MusicRecentlyPlayedContainerRequest](musickit/musicrecentlyplayedcontainerrequest.md) — A request that your app uses to fetch albums, playlists or stations that the user has recently played.
- [MusicRecentlyPlayedContainerResponse](musickit/musicrecentlyplayedcontainerresponse.md) — An object that contains albums, playlists or stations that the user has recently played.

### Enumerations

- [AudioVariant](musickit/audiovariant.md) — Variants that indicate the quality of audio available for an item.
- [MusicCatalogChartKind](musickit/musiccatalogchartkind.md) — The available kinds of catalog charts.
- [MusicPropertySource](musickit/musicpropertysource.md) — An enumeration that specifies which source to use when requesting properties and relationships.
- [RecentlyPlayedMusicItem](musickit/recentlyplayedmusicitem.md) — An item that represents an album, a playlist, or a station that the user has recently played.

## See Also

### Related Documentation

- [Media Player](mediaplayer.md) — Find and play songs, audio podcasts, audio books, and more from within your app.
- [Apple Music API](applemusicapi.md) — Integrate streaming music with catalog and personal content.
