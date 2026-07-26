---
title: 'The new HTTP QUERY method explained | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/new-http-query-method-explained/'
original_language: en
published: 2026-06-17
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dd7d02939ac1f8aa'
translated: false
---

> 原文：[The new HTTP QUERY method explained | Kreya](https://kreya.app/blog/new-http-query-method-explained/)　·　Kreya Blog

In the world of RESTful APIs, we have long lived by a strict set of (self-imposed) rules. Whether you are fetching data with GET, creating an entity with POST, or updating a resource with PUT, the HTTP method tells the server what your intention is.

Quite recently, [RFC 10008](https://www.rfc-editor.org/info/rfc10008/) got published, which defines the new QUERY method for HTTP. Why is this needed when we already have other HTTP methods? Let's find out.

From a purely technical point of view, the HTTP method is just a string. Instead of sending

```text
GET /api/v1/users
```

you could also use

```text
FETCH /api/v1/users
```

in theory. In practice, there are lots of RFCs and implicit, undocumented behaviour around the well-known HTTP methods, such as GET and POST.

As an example, browsers send a GET request when you enter an address or click on a bookmark. Standard HTTP forms only allow GET and POST as methods. Most proxies, firewalls and webservers only allow the "standard" HTTP methods.

So why introduce a new HTTP method when we already have a set of existing ones that worked well for decades?

## Queries using GET

Traditionally, if you wanted to filter a resource, you used query parameters in a GET request (e.g., `/api/v1/users?role=admin&status=active&sort=desc`). This works well for simple filters. However, when you need to perform complex relational queries, deep nesting, or advanced logic, the URL becomes massive, hard to read, and sometimes hits browser or server character limits.

Other potential problems include:

- Sending non-ASCII or special characters as parameters requires encoding them, increasing the request size
- Servers and other middlewares probably log the request parameters, which may be problematic in certain circumstances
- Expressing some data structures, such as arrays, is not well-defined and implementation specific (e.g. `?roles[0]=admin&roles[1]=reporter` vs `?roles=admin&roles=reporter` vs `?roles[]=admin&roles[]=reporter`)
- Same for expressing deeply nested structures

Since these are all drawbacks of sending the data as query parameters, why not simply send a GET request with a JSON request body? Again, from a theoretical point of view, this should work. None of the HTTP RFCs explicitly forbid the usage of a request body when performing a HTTP GET request, but indicate that it should not be done. As a result, various client, proxy and webserver implementation handle GET requests with a body differently. Some reject them outright, some simply drop the body while others interpret it.

Due to this, using HTTP GET with a request body is a bad idea, as for example users behind a corporate firewall or a different browser may be unable to use your website. This is also the reason why there is no new RFC which specifies that GET requests should now support request bodies, as that would break lots of existing implementations.

## The workaround: Querying using POST

Since sending request bodies using GET could introduce problems, the workaround is to use POST.

While POST allows for a request body, it introduces significant semantic issues. POST is defined as non-idempotent and is intended for resource creation or processing.

While this may not sound like a huge problem, it can be annoying when implementing e.g. automatic retries on failures. As the GET method is defined as safe and idempotent, as long as the server implementation is correct, we can retry failed requests without worrying about side effects. It also makes it impossible for proxies or other middleware to automatically understand that the operation is read-only. For example, a middleware may automatically cache GET requests for some time, which does not work with POST requests.

## The QUERY method

All of the above reasons resulted in the QUERY method being specified, after many years of discussion. The QUERY method is nothing special, the RFC roughly states that it is similar to the GET method, but with a request body. It is meant to be safe and idempotent.

QUERY request can be cached, but implementation must be careful to incorporate the request content into the cache key. All in all, it finally offers a fitting HTTP method for complicated search queries.

![Kreya screenshot of sending a QUERY request](https://kreya.app/blogposts/new-http-query-method/query-example.png)

## QUERY gotchas

It may be tempting to immediately switch all search related endpoints to use QUERY. Before doing that, there are a few things that you need to consider.

- Support for HTTP QUERY is still very limited and may be for some time. It may take years for it to be fully supported everywhere. As an example, [Kreya](https://kreya.app) has added out-of-the-box support for HTTP QUERY with the recent 1.20 release (though it was possible to send custom HTTP methods before already). Other clients, proxies and webservers may still reject it.
- Standard GET queries with data in the URL parameters are still perfectly fine. If there is no immediate need to change those to the QUERY method, leave them be.
- If your users should be able to share or bookmark links of the filtered data, continue using GET requests. Sharing links as QUERY requests does not work.
- Implementing custom caching for QUERY requests is more difficult than for GET requests, since you need to consider the request body.

## Conclusion

In short, HTTP QUERY replaces POST for read-only requests. It may take some time until it is fully supported everywhere, but you should still consider (and test!) it should normal GET requests not suffice for your use case.
