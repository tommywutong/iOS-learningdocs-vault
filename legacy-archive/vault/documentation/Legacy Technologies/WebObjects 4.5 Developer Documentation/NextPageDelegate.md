---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/DirectToWeb.framework/Java/Protocols/NextPageDelegate.html
archived_at: '2026-07-15T08:11:31.308144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Direct to Web

[[Table of Contents]](../DirectToWebTOC.md)

# NextPageDelegate

> **__Package:__**
> : com.apple.yellow.directtoweb

---

## Interface Description

---

This interface defines the `nextPage` method that a Direct to Web template can invoke in its next page delegate. See the "Customizing a Direct to Web Application" chapter of _Developing WebObjects Applications With Direct to Web_ for more information about using the next page delegate.

## Method Types

---

> ****
> : [nextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6ttfpb2faylhmvcgk3dfm5qxizjpnzsxq5cqmftwkl2xj5bw63lqn5xgk3tuf4ufot2dn5wxa33omvxhiki)

## Methods

---

### nextPage

abstract public WOComponent nextPage(WOComponent sender)

This action method is invoked when the user leaves a Direct to Web page. It returns the next page (a WOComponent object) to display. The `sender` argument contains the Direct to Web template instance that invokes the method. If this method is not implemented, the `sender` is redisplayed.

---

[[Table of Contents]](../DirectToWebTOC.md)
