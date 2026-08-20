---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Introduction.html
archived_at: '2026-07-15T08:11:47.243346Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](WebObjectsTOC.md)

# WebObjects

> __Package:__
> com.apple.yellow.webobjects

---

## Introduction

The WebObjects class hierarchy is rooted in the Foundation
Framework's NSObject class. The bulk of the WebObjects framework
consists of several related groups of classes as well as a few individual classes.

The more commonly-used classes within the WebObjects framework
can be grouped as follows:

- Server and Application Level Classes. [WOAdaptor](WOAdaptor.md#apple-k5huczdbob2g64q) defines the interface for
  objects mediating the exchange of data between an HTTP server and
  a WebObjects application. [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4) receives requests from
  the adaptor and initiates and coordinates the request-handling process,
  after which it returns a response to the adaptor.
- Session Level Classes. [WOSession](WOSession.md#apple-k5hvgzltonuw63q) encapsulates the state of
  a session; WOSession objects persiste between the cycles of the
  request-response loop. [WOSessionStore](WOSessionStore.md#apple-k5hvgzltonuw63storxxezi) provides the strategy
  or mechanism through which WOSession objects are made persistent.
- Request Level Classes. [WORequest](WORequest.md#apple-k5hvezlrovsxg5a) and [WOResponse](WOResponse.md#apple-k5hvezltobxw443f), along with their parent
  class [WOMessage](WOMessage.md#apple-k5hvezltobxw443f), store essential data about
  HTTP requests and responses, such as header information, form values, HTTP
  version, host and page name, and session, context, and sender IDs. [WOContext](WOContext.md#apple-k5hug33oorsxq5a) provides access to the objects
  involved in the current cycle, such as the current request, response,
  session, and application objects.
- Page Level Classes. [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) represents an integral,
  reusable page (or portion of a page) for display in a web browser. [WOElement](WOElement.md#apple-k5huk3dfnvsw45a) declares the three request-handling
  methods: [takeValuesFromRequest](WOElement.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a), [invokeActionForRequest](WOElement.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c62loozxwwzkbmn2gs33oizxxeutfof2wk43u),
  and [appendToResponse](WOElement.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pivwgk3lfnz2c6ylqobsw4zcun5jgk43qn5xhgzi). [WODynamicElement](WODynamicElement.md#apple-k5hui6lomfwwsy2fnrsw2zlooq) is an abstract class
  for subclasses that generate particular dynamic elements. [WOAssociation](WOAssociation.md#apple-k5huc43tn5rwsylunfxw4) knows how to find and
  set a value by reference to a key.
- Database Integration Level Classes. [WODisplayGroup](WODisplayGroup.md#apple-ijauoq2ijjceu) performs fetches, queries,
  creations, and deletions of records from one table in the database.

[![Table of Contents](attachments/images/up.gif)](WebObjectsTOC.md)
