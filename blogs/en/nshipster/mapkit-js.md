---
title: MapKit JS
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/mapkit-js/'
original_language: en
published: 2019-03-11
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:098a956619e4736a'
translated: false
---

> 原文：[MapKit JS](https://nshipster.com/mapkit-js/)　·　NSHipster (Mattt)

# [Map​Kit JS](https://nshipster.com/mapkit-js/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  March 11^th, 2019

Announced in 2018, [MapKit JS](https://developer.apple.com/documentation/mapkitjs) takes the convenient cartographic capabilities of the MapKit framework on iOS and macOS, and brings them to the web.

MapKit JS — along with [MusicKit JS](https://developer.apple.com/documentation/musickitjs) — usher in a new generation of web APIs from Apple, that’s defined by a brand new authentication flow based on [JSON Web Tokens (JWT)](https://jwt.io). These APIs also come at a time when Swift on the Server is just starting to hit its stride, making the browser-based offering all the more exciting.

This week on NSHipster, we’ll zoom out and give turn-by-turn directions of how to start your journey with MapKit JS. (Once we figure out where we lost our keys) on our way to a working integration.

---

## Setting Up MapKit JS

To use MapKit JS on the web, you’ll need an Apple Developer account. Using that account, you may obtain credentials for issuing tokens that can be used to request map tiles, directions, and other mapping APIs.

You create and manage MapKit JS keys from your [Apple Developer Account Dashboard](https://developer.apple.com/account). (The process should be familiar to anyone who’s set up push notifications for their iOS app before.)

### Step 1: Register a Maps ID

On the “Certificates, Identifiers & Profiles” page, navigate to the [Maps IDs section](https://developer.apple.com/account/ios/identifier/mapsId), which is listed in the sidebar under the “Identifiers” heading. Click the + button and fill out the form, providing a Maps ID description and a unique, reverse-domain identifier (such as `maps.com.nshipster`).

![Register a Maps ID](https://nshipster.com/assets/mapkit-js-register-maps-id-66732f2a06610f9cf7f02eb45e81a74b712cd1406e914583f564cc9b3b4cb0c518ecea859215198ac30c64b7543ce9baa3b4976f49d5eed0fae491804712635a.png)

### Step 2: Create a New MapKit JS Key

Next, go to the [all keys page](https://developer.apple.com/account/ios/authkey/) found in the sidebar under the “Keys” heading. Again, click the + button and proceed to fill out the form, selecting the checkbox that enable MapKit JS key services and configuring it to use the Maps ID created in the previous step.

![Create a New MapKit JS Key](https://nshipster.com/assets/mapkit-js-create-a-new-key-67b3d792d6213282444eb20898b00b874a29a85128ea396113462e1605d06bf2d9b3e024739aa054d806c07885f9bf162fc450056a6950abed340a22d71a5eb6.png)

### Step 3: Download the Key

Finally, go back to the [all keys page](https://developer.apple.com/account/ios/authkey/), click on the key you just created, and click the Download button.

![Download Key](https://nshipster.com/assets/mapkit-js-download-key-199cac4bee0bd4d542557b88085b67ab550fdc9800db280649403f4577b464f557ff58bd6b58c75070713e02d0e9022ac543c0c1bf0d6f875a0abfa56b19a832.png)

At this point, you should now have a file named something like `AuthKey_Key ID.p8` sitting in your Downloads folder.

_“But what is a `.p8` file_?”, you might ask. Well, the truth is…

## P8, PEM, ASN.1

`.p8` is a made-up file extension; the `AuthKey_Key ID.p8` file you downloaded is a text file like any other. If you open it up, you can see that it is, indeed, text:

```
-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQg84Z+p4rGieL6YiCO
DxAeH0BcSZprk99Dl1UWMOODbHagCgYIKoZIzj0DAQehRANCAARDijSXDV6xjH0N
CbPelVcWUfWG80nadLsuaGOcsrixyPaKlEdzsBeypOZfxbLM3glKoZCCLUjF/WGd
Ho0RMbco
-----END PRIVATE KEY-----
```

The convention of delimiting text-encoded binary data with `-----BEGIN THING-----` and `-----END THING-----` is known as PEM format, which is named after [Privacy-Enhanced Mail](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail). The text sandwiched between those delimiters is the [Base64-encoding](https://en.wikipedia.org/wiki/Base64) of the private key, represented in [ASN.1](https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One).

---

At this point, you may feel like you took a wrong turn and drove right into an ocean of acronyms. This wouldn’t be surprising, as drowning in alphabet soup is an occupational hazard of the software development profession — especially when it comes to matters cryptographic.

But worry not! You can make it back to shore just by treading water. All you need to know at this point is that you’ll use the private key in the `.p8` file to let Apple know that our requests for map data are coming from us.

---

## JSON Web Tokens

[JSON Web Tokens (JWT)](https://jwt.io) are a way for claims to be securely communicated between two parties They’re an open standard, codified by [RFC 7519](https://tools.ietf.org/html/rfc7519).

A JSON Web Token has three distinct parts consisting of Base64-encoded segments joined by a period (`.`).

- The first segment represents the header, which distinguishes the token type, and information needed to verify the identity of the signer.
- The second segment is the payload, which contains one of more claims to be transmitted between two parties.
- The third segment is the signature, which can be cryptographically verified using the contents of the message and one or more keys.

JSON web tokens can be daunting when seen up close, but the structure makes more sense when you see it visually:

### Encoded Form Base-64 Encoded JSON

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjRUOTJZWlNXR00ifQ.eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjRUOTJZWlNXR00ifQ.eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjRUOTJZWlNXR00ifQ
```

### Header Algorithm and Token Type

```
{
  "typ": "JWT",
  "alg": "ES256",
  "kid": "4T92YZSWGM"
}
```

### Payload Data

```
{
  "iss": "9JWVADR3RQ",
  "exp": 1552393165.925637,
  "iat": 1552306765.925637
}
```

### Signature Verification of Identity

```
ECDSASHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  fs.readSync("key.pub"),
  fs.readSync("key.p8")
);
```

Apple Maps JS requires claims for the issuer (`iss`), the date of issuing (`iat`), and the expiration date (`exp`); you may optionally specify an `origin` to restrict which hosts are allowed to make requests. To verify that claims are made by who they claim to be, tokens are signed and encrypted using the [ES256 algorithm](https://tools.ietf.org/html/rfc7518).

## Signing MapKit JS Tokens

To sign a JWT token for MapKit JS, we’ll need the following 3 pieces of information:

- A **private key** provided by Apple
- The **ID** of the private key
- The **ID** of the team that owns the private key

Once you have all of that, it’s simply a matter of creating a JWT Header), creating a JWT claims object, and signing it using the ES256 algorithm.

```
import Foundation
import SwiftJWT

let header = Header(typ: "JWT", kid: "KEY ID")
let claims = ClaimsStandardJWT(
                iss: "TEAM ID",
                exp: Date(timeIntervalSinceNow: 86400),
                iat: Date()
             )
var jwt = JWT(header: header, claims: claims)

let p8 = """
-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQg84Z+p4rGieL6YiCO
DxAeH0BcSZprk99Dl1UWMOODbHagCgYIKoZIzj0DAQehRANCAARDijSXDV6xjH0N
CbPelVcWUfWG80nadLsuaGOcsrixyPaKlEdzsBeypOZfxbLM3glKoZCCLUjF/WGd
Ho0RMbco
-----END PRIVATE KEY-----
""".data(using: .utf8)!

let signedToken = try jwt.sign(using: .es256(privateKey: p8))
/* "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjRUOTJZWlNXR00ifQ.\
    eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjRUOTJZWlNXR00ifQ.\
    eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjRUOTJZWlNXR00ifQ"  */
```

Although you could generate a single API key that doesn’t expire, that opens your account to abuse from those who might take advantage of these generous terms. Here, a “principle of least privilege” is generally preferred; instead of issuing one immortal token, issue tokens that expire after a short period of time, and require clients to request new ones as necessary.

Of course, in order for this to work, we need to keep the private key secret from the client. To do that, we’ll store it on a server and mediate access by way of responses to token requests.

## Serving Tokens with a Web Application

Here’s a simple web application using the [Vapor framework](https://vapor.codes). When a `GET` request is made to the host root (`/`), a static HTML page is served that displays a map. The code that generates the map, in turn, sends a `GET` request to the `/token` endpoint to get a JWT in plaintext that it can use to initialize MapKit JS.

Below, the implementation of the `generateSignedJWTToken()` function is essentially what we had in the previous code listing.

```
import Vapor
import SwiftJWT

public func routes(_ router: Router) throws {
    router.get { req in
        return try req.view().render("map")
    }

    router.get("token") { req -> String in
        return try generateSignedJWTToken()
    }
}
```

## Initializing MapKit in JavaScript

Finally, let’s complete _le grand tour_ with a peek at what’s going on in our client-side JavaScript file:

```
mapkit.init({
  authorizationCallback: done => {
    fetch("/token")
      .then(res => res.text())
      .then(token => done(token))
      .catch(error => {
        console.error(error);
      });
  }
});
```

Before we can request map tiles, we need to have Apple’s servers give us the OK. We do this by calling the `init` method, which takes an `authorizationCallback`; the function takes a single closure parameter, which is called asynchronously when the token is received by the `fetch` request.

Alternatively, if what you’re making is unlikely to leak outside of your `localhost`, you could certainly take a short cut and hard-code a long-lived token. Instead of waiting for a `fetch` to finish, you simply call the `done` function straight away:

```
const token = "...";

mapkit.init({
  authorizationCallback: done => {
    done(token);
  }
});
```

## At Last, a Map!

Now that we’ve gone through all of that trouble to get map tiles hooked up for our website, let’s do a quick drive-by of the actual MapKit API:

MapKit JS should be familiar to anyone familiar with the original MapKit framework on iOS and macOS. For example, when you initialize a map, you can configure its initial view by constructing a region from a fixed distance around center point.

```
const center = new mapkit.Coordinate(37.3327, -122.0053),
  span = new mapkit.CoordinateSpan(0.0125, 0.0125),
  region = new mapkit.CoordinateRegion(center, span);

let map = new mapkit.Map("map", {
  region: region,
  showsCompass: mapkit.FeatureVisibility.Hidden,
  showsZoomControl: false,
  showsMapTypeControl: false
});
```

Annotations work much the same, except with arguably nicer affordances out of the box. For example, `mapkit.MarkerAnnotation` offers the same, familiar pushpin shape that we iOS developers have always wanted — with simple, power knobs for customization.

```
const annotation = new mapkit.MarkerAnnotation(center, {
  title: "Apple Park Visitor Center",
  subtitle: "10600 North Tantau Avenue, Cupertino, CA 95014",
  glyphText: "",
  color: "#8e8e93",
  displayPriority: 1000
});
map.addAnnotation(annotation);
```

```
<div id="map"></div>
<script src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"></script>
<script async="async" integrity="sha512-dde+psGeD6+2w9Fq+EBqAr9EeND1NO9c1E7gnr3do8OlfNJwP7QhOiGxouhqGW0tN5mjRBAOYsj/04rmtIVhQQ==" crossorigin="anonymous" type="text/javascript" src="/assets/articles/mapkit-js-75d7bea6c19e0fafb6c3d16af8406a02bf4478d0f534ef5cd44ee09ebddda3c3a57cd2703fb4213a21b1a2e86a196d2d3799a344100e62c8ffd38ae6b4856141.js"></script>
```

With only a few lines of JavaScript and HTML, we can embed a beautiful little map into our webpages using MapKit JS.

---

MapKit JS joins a robust ecosystem of mapping providers. Currently in beta, it offers 250,000 map initializations and 25,000 service requests for free _per day_ (!), which is quite generous — especially when compared to similar offerings from [Google](https://cloud.google.com/maps-platform/pricing/) and [MapBox](https://www.mapbox.com/pricing/).

So if you’ve been kicking around an idea for a map widget to add to your site or a directions feature for your web app, you might want to give MapKit JS a look!
