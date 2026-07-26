---
title: Apple Maps Server API
framework: Apple Maps Server API
symbol_kind: module
role: collection
role_heading: Web Service
platforms: [Apple Maps Server API 1.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/applemapsserverapi
source_url: 'https://developer.apple.com/documentation/applemapsserverapi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/applemapsserverapi.json'
content_hash: 'sha256:969c2e67dab6b358'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Apple Maps Server API

<sub>Web Service</sub>

Reduce API calls and conserve device power by streamlining your app’s georelated searches.

## Overview

Use this web-based service to streamline your app’s API by moving georelated searches for places, points of interest, geocoding, directions, possible autocompletions for searches, and estimated time of arrival (ETA) calculations from inside your app to your server.

To try the Maps Server API, generate a temporary token as described in [Creating a Maps token](mapkitjs/creating-a-maps-token.md). Use these credentials to access the API from your app, or use them on [Try Maps Server API](https://developer.apple.com/maps/try-maps-server-api/).

The Apple Maps Server API is a web-based API similar to the [MapKit JS](mapkitjs.md) API, and uses the same authorization infrastructure. It requires authorization using a JSON Web Token (JWT) for API calls. You obtain a key for creating the token when you complete the setup in your Apple Developer account.

To start using the API, you first need to generate an identifier and a private key, and authenticate with the service, following the steps below:

- To create an identifier and private key, follow the steps in [Creating a Maps identifier and a private key](applemapsserverapi/creating-a-maps-identifier-and-a-private-key.md).
- To create tokens from your identifier and private key with the Apple Maps Server API, follow the steps in [Creating and using tokens with Maps Server API](applemapsserverapi/creating-and-using-tokens-with-maps-server-api.md).
- Use the Token API to [Generate a Maps token](applemapsserverapi/-v1-token.md) for API access.

The service provides up to 25,000 service calls per day per team between Apple Maps Server API and MapKit JS. If your app exceeds this quota, the service returns an HTTP 429 error (Too Many Requests) and your app needs to retry later. If your app requires a larger daily quota, submit a [quota increase request form](https://developer.apple.com/contact/request/mapkitjs/).

## Topics

### Essentials

- [Creating and using tokens with Maps Server API](applemapsserverapi/creating-and-using-tokens-with-maps-server-api.md) — Sign JSON Web Tokens to use Maps Server API and debug common signing errors.
- [Creating a Maps identifier and a private key](applemapsserverapi/creating-a-maps-identifier-and-a-private-key.md) — Create a Maps identifier and a private key before generating tokens for MapKit JS.
- [Generate a Maps token](applemapsserverapi/-v1-token.md) — Returns a JWT maps access token that you use to call the service API.
- [Debugging an Invalid token](applemapsserverapi/debugging-an-invalid-token.md) — Inspect the JavaScript console logs, the token, and events to determine why a token is invalid.
- [Common objects](applemapsserverapi/common-objects.md) — Understand the common JSON objects that API responses contain.
- [Integrating the Apple Maps Server API into Java server applications](applemapsserverapi/integrating-the-apple-maps-server-api-into-java-server-applications.md) — Streamline your app’s API by moving georelated searches from inside your app to your server.

### Geocoding

- [Geocode an address](applemapsserverapi/-v1-geocode.md) — Returns the latitude and longitude of the address you specify.
- [Reverse geocode a location](applemapsserverapi/-v1-reversegeocode.md) — Returns an array of addresses present at the coordinates you provide.

### Searching

- [AddressCategory](applemapsserverapi/addresscategory.md) — Search categories related to political geographical boundaries.
- [SearchACResultType](applemapsserverapi/searchacresulttype.md) — An enumerated string that indicates the result type for the search request.
- [SearchResultType](applemapsserverapi/searchresulttype.md) — An enumerated string that indicates the result type for the search autocomplete request.
- [AlternateIdsResponse](applemapsserverapi/alternateidsresponse.md) — A list of alternate Place IDs and associated errors.
- [AlternateIdsResponse.AlternateIds](applemapsserverapi/alternateidsresponse/alternateids.md) — Contains a list of alternate Place IDs for a given Place ID.
- [PlacesResponse](applemapsserverapi/placesresponse.md) — A list of Place IDs and errors.
- [PlacesResponse.PlaceLookupError](applemapsserverapi/placesresponse/placelookuperror.md) — An error associated with a lookup call.
- [Search for places that match specific criteria](applemapsserverapi/-v1-search.md) — Find places by name or by specific search criteria.
- [Search for places that meet specific criteria to autocomplete a place search](applemapsserverapi/-v1-searchautocomplete.md) — Find results that you can use to autocomplete searches.
- [Search for a place using an identifier](applemapsserverapi/-v1-place-_id.md) — Obtain a Place object for a given Place ID.
- [Search for places using mulitple identifiers](applemapsserverapi/-v1-place.md) — Obtain a set of Place objects for a given set of Place IDs.
- [Obtain a list of alternate place identifiers](applemapsserverapi/-v1-place-alternateids.md) — Get a list of alternate Place IDs given one or more Place IDs.

### Directions

- [Search for directions and estimated travel time between locations](applemapsserverapi/-v1-directions.md) — Find directions by specific criteria.
- [Determine estimated arrival times and distances to one or more destinations](applemapsserverapi/-v1-etas.md) — Returns the estimated time of arrival (ETA) and distance between starting and ending locations.
