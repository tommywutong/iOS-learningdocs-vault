---
title: NSURLComponents
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents.json'
content_hash: 'sha256:210a0acbdfbbca09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLComponents

<sub>Class</sub>

An object that parses URLs into and constructs URLs from their constituent parts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSURLComponents
```

## Overview

In Swift, this object bridges to [URLComponents](urlcomponents.md); use [NSURLComponents](nsurlcomponents.md) when you need reference semantics or other Foundation-specific behavior.

The [NSURLComponents](nsurlcomponents.md) class is a class that is designed to parse URLs based on [RFC 3986](http://www.ietf.org/rfc/rfc3986.txt) and to construct URLs from their constituent parts. Its behavior differs subtly from the [NSURL](nsurl.md) class, which conforms to older RFCs. However, you can easily obtain an [NSURL](nsurl.md) object based on the contents of a URL components object or vice versa.

You create a URL components object in one of three ways: from an [NSString](nsstring.md) object that contains a URL, from an [NSURL](nsurl.md) object, or from scratch by using the default initializer. From there, you can modify the URL’s individual components and subcomponents by modifying various properties, either in unencoded form or in URL-encoded form. If you set the unencoded property, you can then obtain the encoded equivalent by reading the encoded property value and vice versa.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [URLComponents](urlcomponents.md) structure, which bridges to the [NSURLComponents](nsurlcomponents.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating URL components

- [- init](<nsurlcomponents/init().md>) — Creates a URL components object with all components left undefined.
- [- initWithString:](<nsurlcomponents/init(string_).md>) — Creates a URL components object by parsing a URL in string form.
- [- initWithString:encodingInvalidCharacters:](<nsurlcomponents/init(string_encodinginvalidcharacters_).md>) — Creates a URL components instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [- initWithURL:resolvingAgainstBaseURL:](<nsurlcomponents/init(url_resolvingagainstbaseurl_)-3bbte.md>) — Creates a URL components object by parsing the URL from an `NSURL` object.

### Getting the URL

- [string](nsurlcomponents/string.md) — A URL derived from the components object, in string form.
- [URL](nsurlcomponents/url.md) — A URL object derived from the components object.
- [- URLRelativeToURL:](<nsurlcomponents/url(relativeto_).md>) — Returns a URL object derived from the components object.

### Accessing components in native format

- [fragment](nsurlcomponents/fragment.md) — The fragment URL component (the part after a `#` symbol), or nil if not present.
- [host](nsurlcomponents/host.md) — The host URL subcomponent, or nil if not present.
- [encodedHost](nsurlcomponents/encodedhost.md) — The host subcomponent, percent-encoded.
- [password](nsurlcomponents/password.md) — The password URL subcomponent, or nil if not present.
- [path](nsurlcomponents/path.md) — The path URL component, or nil if not present.
- [port](nsurlcomponents/port.md) — The port number URL component, or nil if not present.
- [query](nsurlcomponents/query.md) — The query URL component as a string, or nil if not present.
- [queryItems](nsurlcomponents/queryitems.md) — The query URL component as an array of name/value pairs.
- [scheme](nsurlcomponents/scheme.md) — The scheme URL component, or nil if not present.
- [user](nsurlcomponents/user.md) — The username URL subcomponent, or nil if not present.

### Accessing components in URL-encoded format

- [percentEncodedFragment](nsurlcomponents/percentencodedfragment.md) — The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedHost](nsurlcomponents/percentencodedhost.md) — The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present. _(deprecated)_
- [percentEncodedPassword](nsurlcomponents/percentencodedpassword.md) — The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedPath](nsurlcomponents/percentencodedpath.md) — The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedQuery](nsurlcomponents/percentencodedquery.md) — The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedUser](nsurlcomponents/percentencodeduser.md) — The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.

### Locating components in the URL string representation

- [percentEncodedQueryItems](nsurlcomponents/percentencodedqueryitems.md)
- [rangeOfFragment](nsurlcomponents/rangeoffragment.md) — Returns the character range of the fragment in the string returned by the string property.
- [rangeOfHost](nsurlcomponents/rangeofhost.md) — Returns the character range of the host in the string returned by the string property.
- [rangeOfPassword](nsurlcomponents/rangeofpassword.md) — Returns the character range of the password in the string returned by the string property.
- [rangeOfPath](nsurlcomponents/rangeofpath.md) — Returns the character range of the path in the string returned by the string property.
- [rangeOfPort](nsurlcomponents/rangeofport.md) — Returns the character range of the port in the string returned by the string property.
- [rangeOfQuery](nsurlcomponents/rangeofquery.md) — Returns the character range of the query in the string returned by the string property.
- [rangeOfScheme](nsurlcomponents/rangeofscheme.md) — Returns the character range of the scheme in the string returned by the string property.
- [rangeOfUser](nsurlcomponents/rangeofuser.md) — Returns the character range of the user in the string returned by the string property.

### Initializers

- [init(URL:resolvingAgainstBaseURL:)](<nsurlcomponents/init(url_resolvingagainstbaseurl_)-5k5ld.md>)
- [init(URL:resolvingAgainstBaseURL:)](<nsurlcomponents/init(url_resolvingagainstbaseurl_)-6mpr5.md>)
