---
title: 'isEqual:'
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl-isequal
source_url: 'https://developer.apple.com/documentation/foundation/nsurl-isequal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl-isequal.json'
content_hash: 'sha256:2e6bd59bfc6c68c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md) · [NSURL](nsurl.md)

# isEqual:

<sub>Article</sub>

Returns a Boolean value that indicates whether the receiver and a given object have identical URL strings and base URLs.

## Overview

This method defines what it means for instances to be equal. Two NSURLs are considered equal if and only if they return identical values for both [baseURL](nsurl/baseurl.md) and [relativeString](nsurl/relativestring.md).
